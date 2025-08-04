"""
Streamlit Cloud 真实 API 应用
使用真实的 AI API 进行分析
"""

import os
import streamlit as st
from dotenv import load_dotenv

# 尝试加载环境变量
try:
    load_dotenv('openkey.env')
except:
    pass

# 设置页面配置
st.set_page_config(
    page_title="认知型 AI 思维挑战助手",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

def get_api_key():
    """获取 API 密钥"""
    # 首先尝试从 Streamlit secrets 获取
    if hasattr(st, 'secrets') and 'OPENAI_API_KEY' in st.secrets:
        return st.secrets['OPENAI_API_KEY']
    
    # 然后尝试从环境变量获取
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key:
        return api_key
    
    return None

def analyze_viewpoint_with_real_api(viewpoint, api_key):
    """使用真实 API 分析观点"""
    try:
        # 导入必要的库
        from langchain_community.chat_models import ChatOpenAI
        from langchain.prompts import ChatPromptTemplate
        from langchain.chains import LLMChain
        
        # 创建 LLM
        llm = ChatOpenAI(
            model_name="gpt-3.5-turbo",
            temperature=0.3,
            openai_api_key=api_key
        )
        
        # 创建提示模板
        template = """
        你是一个认知型思维分析专家。请对用户的观点进行五步分析：

        用户观点：{viewpoint}

        请按照以下格式进行分析：

        ### 🧾 分析结果：

        **1. 观点拆解：**
        - 核心主张：[提取观点的核心主张]
        - 隐含假设：[识别隐含的假设]
        - 逻辑推理：[分析论证逻辑]

        **2. 反事实设想：**
        - [提出3-4个反事实场景]
        - [如果条件改变会怎样？]

        **3. 逻辑漏洞：**
        - [指出可能的逻辑错误]
        - [分析论证的薄弱环节]

        **4. 反方观点：**
        [提供有力的反方论证]

        **5. 条件边界：**
        [说明观点成立需要满足的条件]

        请用中文回答，保持客观、理性、批判性的分析态度。
        """
        
        prompt = ChatPromptTemplate.from_template(template)
        chain = LLMChain(llm=llm, prompt=prompt)
        
        # 执行分析
        result = chain.run(viewpoint=viewpoint)
        return result
        
    except Exception as e:
        return f"❌ API 调用失败：{str(e)}\n\n💡 请检查 API 密钥是否正确配置"

def main():
    """主函数 - 真实 API 版本"""
    st.title("🧠 认知型 AI 思维挑战助手")
    st.markdown("输入你的观点，让 AI 来 **拆解、挑战、反驳** 你")
    
    # 显示部署信息
    st.info("🚀 部署在 Streamlit Cloud 上")
    
    # 检查 API 密钥
    api_key = get_api_key()
    if api_key:
        st.success("✅ API 密钥已配置，使用真实 AI 分析")
    else:
        st.warning("⚠️ 未检测到 API 密钥，将使用演示模式")
        st.info("💡 请在 Streamlit Cloud 的 Settings → Secrets 中配置 OPENAI_API_KEY")
    
    # 用户输入
    user_input = st.text_area(
        "💬 请输入你的观点或主张：", 
        height=150,
        placeholder="例如：我认为人工智能会完全取代人类工作..."
    )
    
    if st.button("分析我的观点", type="primary"):
        if not user_input.strip():
            st.warning("请输入一个非空观点。")
        else:
            st.success("✅ 观点已提交！")
            
            # 显示分析进度
            with st.spinner("🤖 AI 正在分析你的观点..."):
                if api_key:
                    # 使用真实 API
                    analysis_result = analyze_viewpoint_with_real_api(user_input, api_key)
                else:
                    # 使用演示模式
                    analysis_result = f"""
### 🧾 分析结果（演示模式）：

**1. 观点拆解：**
- 核心主张：{user_input}
- 隐含假设：这个观点基于特定的假设和背景
- 逻辑推理：需要进一步分析其论证过程

**2. 反事实设想：**
- 如果条件发生变化会怎样？
- 如果历史发展路径不同会怎样？
- 如果外部环境改变会怎样？

**3. 逻辑漏洞：**
- 可能存在论证不充分的问题
- 可能忽视了复杂性因素
- 需要更多证据支持

**4. 反方观点：**
这个观点需要更多论证和证据支持。现实情况往往比表面看起来更复杂。

**5. 条件边界：**
这个观点成立需要：充分的证据、合理的逻辑、对复杂性的考虑等多个条件。

💡 **提示**：配置 API 密钥后可获得更深入的分析
                    """
                
                # 显示结果
                st.markdown(analysis_result)
    
    # 添加使用说明
    with st.expander("ℹ️ 使用说明"):
        st.markdown("""
        - 这是一个认知型思维分析工具
        - 输入你的观点，AI 会进行五步分析
        - 包括拆解、反事实、漏洞分析、反方观点和条件边界
        - 帮助提升批判性思维能力
        """)
        
        if api_key:
            st.success("✅ 已配置 API 密钥，使用真实 AI 分析功能")
        else:
            st.info("💡 如需完整功能，请在 Streamlit Cloud 中配置 API 密钥")

if __name__ == "__main__":
    main() 
