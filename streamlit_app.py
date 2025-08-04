"""
Streamlit Cloud 专用应用文件
适配 Streamlit Cloud 环境
"""

import os
import streamlit as st
from dotenv import load_dotenv

# 加载环境变量
load_dotenv('openkey.env')

# 设置页面配置
st.set_page_config(
    page_title="认知型 AI 思维挑战助手",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

def main():
    """主函数 - Streamlit Cloud 版本"""
    st.title("🧠 认知型 AI 思维挑战助手")
    st.markdown("输入你的观点，让 AI 来 **拆解、挑战、反驳** 你")
    
    # 显示部署信息
    st.info("🚀 部署在 Streamlit Cloud 上")
    
    # 简化的界面
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
            st.info("💡 这是一个演示版本，实际分析功能需要配置 API 密钥")
            
            # 模拟分析结果
            st.markdown("### 🧾 分析结果：")
            st.markdown("""
            **1. 观点拆解：**
            - 核心主张：AI 将完全取代人类工作
            - 隐含假设：AI 能力将超过人类
            - 逻辑推理：技术进步 → 能力提升 → 完全替代
            
            **2. 反事实设想：**
            - 如果 AI 发展遇到瓶颈怎么办？
            - 如果人类创造新的工作类型怎么办？
            - 如果社会选择限制 AI 应用怎么办？
            
            **3. 逻辑漏洞：**
            - 忽视了人类独特的情感创造力
            - 假设了线性的技术进步路径
            - 忽略了社会和文化因素
            
            **4. 反方观点：**
            AI 将与人类协作，而非替代。人类专注于创造性、情感性和战略性工作，AI 处理重复性任务。
            
            **5. 条件边界：**
            观点成立需要：AI 技术突破、社会接受度、经济可行性等多个条件同时满足。
            """)
    
    # 添加使用说明
    with st.expander("ℹ️ 使用说明"):
        st.markdown("""
        - 这是一个认知型思维分析工具
        - 输入你的观点，AI 会进行五步分析
        - 包括拆解、反事实、漏洞分析、反方观点和条件边界
        - 帮助提升批判性思维能力
        """)

if __name__ == "__main__":
    main() 