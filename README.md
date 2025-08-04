# 认知型 AI 思维挑战助手

这是一个基于 Streamlit 和 LangChain 的认知型 AI 助手应用，旨在帮助用户提升批判性思维能力。

## 功能特点

- 🤖 支持多种 AI 模型：OpenAI GPT、Anthropic Claude、DeepSeek
- 🧠 认知型思维分析：拆解、挑战、反驳用户观点
- 🔄 智能重试机制：自动处理网络超时和 API 错误
- 🎯 结构化分析：五步思维分析流程
- 💡 用户友好界面：清晰的使用提示和错误处理

## 支持的 API 提供商

### 1. OpenAI (GPT)
- **API 密钥格式**: `sk-...`
- **可用模型**: GPT-3.5 Turbo, GPT-4, GPT-4 Turbo
- **特点**: 响应速度快，分析质量高

### 2. Anthropic (Claude)
- **API 密钥格式**: `sk-proj-...`
- **可用模型**: Claude 3.5 Sonnet, Claude 3 Haiku, Claude 3 Opus
- **特点**: 分析深入，逻辑性强

### 3. DeepSeek
- **API 密钥格式**: `sk-...` (通常更长)
- **可用模型**: DeepSeek Chat, DeepSeek Coder, DeepSeek Chat Pro
- **特点**: 中文理解能力强，分析准确

## 安装和设置

### 1. 安装依赖
```bash
pip install streamlit langchain langchain-community python-dotenv openai anthropic deepseek-ai
```

### 2. 配置 API 密钥
在 `openkey.env` 文件中设置你的 API 密钥：
```
OPENAI_API_KEY=你的API密钥
```

### 3. 运行应用
```bash
streamlit run app.py
```

## 使用方法

1. **选择 API 提供商**: 在界面中选择 OpenAI、Anthropic 或 DeepSeek
2. **选择模型**: 根据你的需求选择合适的 AI 模型
3. **输入观点**: 在文本框中输入你想要分析的观点
4. **获取分析**: 点击"分析我的观点"按钮，AI 将进行五步思维分析

## 思维分析流程

AI 助手会对每个观点执行以下五步分析：

1. **拆解基本前提**: 分析观点的核心假设和逻辑结构
2. **反事实设想**: 提出至少三个"如果前提不成立"的假设
3. **逻辑漏洞分析**: 识别可能存在的偏见、假设错误或证据缺失
4. **反方构建**: 模拟对立立场如何系统性地反驳该观点
5. **结构化总结**: 输出关键前提、反方观点和观点成立的条件边界

## 错误处理

应用包含完善的错误处理机制：

- 🔄 **自动重试**: 网络超时时自动重试最多3次
- ⚠️ **API 错误**: 针对不同 API 提供商的特定错误处理
- 💡 **用户提示**: 提供具体的故障排除建议
- 🕐 **超时处理**: 增加请求超时时间，支持指数退避

## 文件结构

```
cognitive_ai_assistant/
├── app.py              # 主应用文件
├── test_api.py         # API 测试脚本
├── test_deepseek.py    # DeepSeek 测试脚本
├── openkey.env         # API 密钥配置文件
├── README.md           # 说明文档
└── venv/               # 虚拟环境
```

## 注意事项

- 确保网络连接稳定
- API 密钥格式必须正确
- 不同模型的分析质量和速度可能不同
- 建议输入简洁明了的观点以获得更好的分析效果

## 版本信息

- **版本**: 1.0.0
- **作者**: AI Assistant
- **更新日期**: 2024年 