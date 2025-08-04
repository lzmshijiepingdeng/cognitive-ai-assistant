"""
认知型 AI 思维挑战助手

这是一个基于 Streamlit 和 LangChain 的认知型 AI 助手应用，
旨在帮助用户提升批判性思维能力。

作者: AI Assistant
版本: 1.0.0
"""

import os
import time
from typing import Optional

import streamlit as st
from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain_community.chat_models import ChatOpenAI, ChatAnthropic
from langchain.prompts import ChatPromptTemplate
from openai import APITimeoutError, APIError

# DeepSeek 集成
try:
    from langchain_deepseek import ChatDeepSeek
except ImportError:
    # 如果 langchain-deepseek 不可用，使用 OpenAI 兼容的方式
    ChatDeepSeek = None


def load_environment() -> tuple[Optional[str], str]:
    """
    加载环境变量并获取 API 密钥
    
    Returns:
        tuple[Optional[str], str]: (API 密钥, API 类型)
    """
    # 尝试加载 .env 文件，如果不存在则加载 openkey.env
    if os.path.exists('.env'):
        load_dotenv('.env')
    else:
        load_dotenv('openkey.env')
    
    api_key = os.getenv("OPENAI_API_KEY")
    
    if not api_key:
        st.error("请先在 .env 或 openkey.env 文件中设置你的 API 密钥")
        st.stop()
    
    # 检查 API 密钥格式并确定 API 类型
    if api_key.startswith("sk-proj-"):
        return api_key, "anthropic"
    elif api_key.startswith("sk-"):
        return api_key, "openai"
    elif api_key.startswith("sk-") and len(api_key) > 50:  # DeepSeek 密钥通常更长
        return api_key, "deepseek"
    else:
        st.warning("⚠️ API 密钥格式可能不正确")
        st.info("💡 支持的格式：\n- OpenAI: sk-...\n- Anthropic: sk-proj-...\n- DeepSeek: sk-...")
        return api_key, "unknown"


def initialize_llm() -> ChatOpenAI:
    """
    初始化大语言模型
    
    Returns:
        ChatOpenAI: 配置好的语言模型实例
    """
    return ChatOpenAI(
        model_name="gpt-3.5-turbo",  # 使用更通用的模型
        temperature=0.3,
        request_timeout=60,  # 增加超时时间到60秒
        max_retries=3  # 添加重试机制
    )


def get_system_prompt() -> str:
    """
    获取系统角色提示词
    
    Returns:
        str: 系统角色提示词
    """
    return """
你是一个认知型AI助手，职责是帮助用户提升批判性思维能力，而不是安慰或迎合他们。

当用户提出任何一个观点时，你需执行以下五步：
1. 拆解该观点的基本前提和逻辑推理结构；
2. 提出至少三个"反事实"设想：如果前提不成立，可能会怎样？
3. 分析该观点可能存在的逻辑漏洞、偏见、假设错误或证据缺失；
4. 构建一个立场对立的反方人物，模拟其如何系统性地反驳该观点；
5. 输出一个结构化总结，包括关键前提、反方观点、观点成立的条件边界。

注意事项：
- 你不提供情绪安慰，不默认用户是对的；
- 你不做模糊判断，每一步都要具体清晰；
- 在逻辑分析时必须遵循因果链，避免跳跃或空泛。
"""


def create_cognitive_chain(llm: ChatOpenAI) -> LLMChain:
    """
    创建认知分析链
    
    Args:
        llm (ChatOpenAI): 语言模型实例
        
    Returns:
        LLMChain: 配置好的认知分析链
    """
    template = ChatPromptTemplate.from_messages([
        ("system", get_system_prompt()),
        ("user", "{user_input}")
    ])
    
    return LLMChain(
        llm=llm,
        prompt=template,
        verbose=True
    )


def setup_streamlit_interface(api_type: str) -> tuple[str, str, str]:
    """
    设置 Streamlit 用户界面
    
    Args:
        api_type (str): API 类型 ("openai", "anthropic", 或 "deepseek")
    
    Returns:
        tuple[str, str, str]: (用户输入的观点, 选择的模型, 选择的 API 类型)
    """
    st.title("🧠 认知型 AI 思维挑战助手")
    st.markdown("输入你的观点，让 AI 来 **拆解、挑战、反驳** 你")
    
    # API 类型选择
    api_options = {
        "OpenAI (GPT)": "openai",
        "Anthropic (Claude)": "anthropic"
    }
    
    # 如果 DeepSeek 可用，添加该选项
    if ChatDeepSeek is not None:
        api_options["DeepSeek"] = "deepseek"
    
    # 根据检测到的 API 类型设置默认选择
    default_index = 0
    if api_type == "anthropic":
        default_index = 1
    elif api_type == "deepseek" and ChatDeepSeek is not None:
        default_index = 2
    
    selected_api = st.selectbox(
        "🔗 选择 API 提供商：",
        options=list(api_options.keys()),
        index=default_index,
        help="选择不同的 API 提供商"
    )
    
    # 根据选择的 API 类型显示模型选项
    if api_options[selected_api] == "anthropic":
        model_options = {
            "Claude 3.5 Sonnet": "claude-3-5-sonnet-20241022",
            "Claude 3 Haiku": "claude-3-haiku-20240307",
            "Claude 3 Opus": "claude-3-opus-20240229"
        }
    elif api_options[selected_api] == "deepseek":
        model_options = {
            "DeepSeek Chat": "deepseek-chat",
            "DeepSeek Coder": "deepseek-coder",
            "DeepSeek Chat (Pro)": "deepseek-chat-pro"
        }
    else:  # openai
        model_options = {
            "GPT-3.5 Turbo": "gpt-3.5-turbo",
            "GPT-4": "gpt-4",
            "GPT-4 Turbo": "gpt-4-turbo-preview"
        }
    
    selected_model = st.selectbox(
        "🤖 选择 AI 模型：",
        options=list(model_options.keys()),
        index=0,
        help="选择不同的模型可能影响分析质量和速度"
    )
    
    # 显示 API 类型信息
    st.info(f"🔗 当前使用: {api_options[selected_api].upper()} API")
    
    # 添加网络状态提示
    with st.expander("ℹ️ 使用提示"):
        st.markdown("""
        - 确保网络连接稳定
        - 如果遇到超时，请稍后重试
        - 建议输入简洁明了的观点
        - 分析可能需要 10-30 秒，请耐心等待
        - DeepSeek 模型分析更深入但可能较慢
        """)
    
    user_input = st.text_area("💬 请输入你的观点或主张：", height=150)
    
    return user_input, model_options[selected_model], api_options[selected_api]


def process_user_input(user_input: str, cognitive_chain: LLMChain) -> None:
    """
    处理用户输入并生成分析结果
    
    Args:
        user_input (str): 用户输入的观点
        cognitive_chain (LLMChain): 认知分析链
    """
    if not user_input.strip():
        st.warning("请输入一个非空观点。")
        return
    
    max_retries = 3
    retry_delay = 2
    
    for attempt in range(max_retries):
        try:
            with st.spinner(f"🧠 思维分析中... (尝试 {attempt + 1}/{max_retries})"):
                result = cognitive_chain.run(user_input=user_input)
                st.markdown("### 🧾 分析结果：")
                st.write(result)
                break  # 成功则跳出循环
                
        except APITimeoutError:
            if attempt < max_retries - 1:
                st.warning(f"请求超时，正在重试... ({attempt + 1}/{max_retries})")
                time.sleep(retry_delay)
                retry_delay *= 2  # 指数退避
            else:
                st.error("❌ 请求超时，请检查网络连接或稍后重试。")
                st.info("💡 建议：\n- 检查网络连接\n- 稍后重试\n- 尝试使用更短的输入")
                
        except APIError as e:
            error_msg = str(e)
            st.error(f"❌ API 错误：{error_msg}")
            
            if "model_not_found" in error_msg.lower():
                st.info("💡 模型不存在或没有访问权限，请尝试选择其他模型")
            elif "invalid_api_key" in error_msg.lower() or "authentication" in error_msg.lower():
                st.info("💡 API 密钥无效，请检查密钥是否正确")
            elif "quota" in error_msg.lower() or "billing" in error_msg.lower():
                st.info("💡 API 配额已用完或账户余额不足")
            else:
                st.info("💡 请检查 API 密钥和网络连接")
            break
            
        except Exception as e:
            error_msg = str(e)
            st.error(f"❌ 发生错误：{error_msg}")
            
            # 处理特定 API 错误
            if "anthropic" in error_msg.lower():
                if "invalid_api_key" in error_msg.lower():
                    st.info("💡 Anthropic API 密钥无效，请检查密钥是否正确")
                elif "quota" in error_msg.lower() or "balance" in error_msg.lower():
                    st.info("💡 Anthropic API 配额已用完或余额不足")
                else:
                    st.info("💡 请检查 Anthropic API 密钥和网络连接")
            elif "deepseek" in error_msg.lower():
                if "invalid_api_key" in error_msg.lower():
                    st.info("💡 DeepSeek API 密钥无效，请检查密钥是否正确")
                elif "quota" in error_msg.lower() or "balance" in error_msg.lower():
                    st.info("💡 DeepSeek API 配额已用完或余额不足")
                else:
                    st.info("💡 请检查 DeepSeek API 密钥和网络连接")
            else:
                st.info("💡 请检查 API 密钥和网络连接")
            break
            
        except Exception as e:
            st.error(f"❌ 发生未知错误：{str(e)}")
            break


def main():
    """
    主函数：应用程序入口点
    """
    # 加载环境变量
    api_key, api_type = load_environment()
    
    # 设置用户界面
    user_input, selected_model, selected_api = setup_streamlit_interface(api_type)
    
    # 根据选择的 API 类型初始化语言模型
    if selected_api == "anthropic":
        llm = ChatAnthropic(
            model=selected_model,
            temperature=0.3,
            max_tokens=4000,
            anthropic_api_key=api_key
        )
    elif selected_api == "deepseek":
        if ChatDeepSeek is None:
            st.error("❌ DeepSeek 集成不可用，请安装 langchain-deepseek 包")
            st.info("💡 运行命令: pip install langchain-deepseek")
            st.stop()
        
        llm = ChatDeepSeek(
            model=selected_model,
            temperature=0.3,
            max_tokens=4000,
            api_key=api_key
        )
    else:  # openai
        llm = ChatOpenAI(
            model_name=selected_model,
            temperature=0.3,
            request_timeout=60,
            max_retries=3
        )
    
    # 创建认知分析链
    cognitive_chain = create_cognitive_chain(llm)
    
    # 处理用户输入
    if st.button("分析我的观点"):
        process_user_input(user_input, cognitive_chain)


if __name__ == "__main__":
    main()