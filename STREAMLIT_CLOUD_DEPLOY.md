# 🚀 Streamlit Cloud 部署指南

## 快速部署步骤

### 1. 准备 GitHub 仓库
确保你的代码已经推送到 GitHub 仓库，包含以下文件：
- `streamlit_app.py` - 主应用文件
- `requirements.txt` - 依赖包列表
- `openkey.env` - 环境变量文件

### 2. 部署到 Streamlit Cloud
1. 访问 [share.streamlit.io](https://share.streamlit.io)
2. 使用 GitHub 账号登录
3. 点击 "New app"
4. 配置部署参数：
   - **Repository**: 选择你的 GitHub 仓库
   - **Branch**: main
   - **Main file path**: `streamlit_app.py`
   - **Python version**: 3.9
5. 点击 "Deploy!"

### 3. 配置环境变量
在 Streamlit Cloud 中设置环境变量：
1. 进入你的应用页面
2. 点击 "Settings" → "Secrets"
3. 添加以下配置：
```toml
[secrets]
OPENAI_API_KEY = "你的 API 密钥"
```

## 文件说明

### 📁 项目文件
- `streamlit_app.py` - Streamlit Cloud 专用应用文件
- `requirements.txt` - Python 依赖包
- `openkey.env` - 本地环境变量（可选）

### 🔧 配置说明

#### requirements.txt
```
streamlit>=1.28.0
langchain>=0.1.0
langchain-community>=0.0.10
langchain-deepseek>=0.1.4
python-dotenv>=1.0.0
openai>=1.0.0
anthropic>=0.7.0
deepseek-ai>=0.0.1
```

## 部署优势

### ✅ Streamlit Cloud 优势
- **零配置**: 无需安装任何工具
- **自动部署**: 连接 GitHub 后自动部署
- **免费使用**: 有免费额度
- **全球访问**: 全球用户都能访问
- **自动 HTTPS**: 自动配置 SSL 证书
- **版本控制**: 与 Git 集成

### 🎯 适用场景
- 快速原型开发
- 演示项目
- 个人项目
- 小型应用

## 部署后配置

### 1. 获取应用 URL
部署完成后，你会得到类似这样的 URL：
```
https://your-app-name.streamlit.app
```

### 2. 自定义域名（可选）
- 购买域名
- 在 Streamlit Cloud 中配置
- 设置 DNS 解析

### 3. 环境变量管理
- 在 Streamlit Cloud 控制台设置
- 支持多环境配置
- 安全存储敏感信息

## 故障排除

### 常见问题

#### 1. 部署失败
- 检查 `streamlit_app.py` 文件是否存在
- 确认 `requirements.txt` 包含所有依赖
- 查看部署日志

#### 2. 环境变量问题
- 确保在 Streamlit Cloud 中设置了正确的环境变量
- 检查变量名是否正确（区分大小写）
- 重新部署应用

#### 3. 依赖包问题
- 更新 `requirements.txt` 文件
- 检查包版本兼容性
- 查看错误日志

### 调试命令
```bash
# 本地测试
streamlit run streamlit_app.py

# 检查依赖
pip install -r requirements.txt

# 验证环境变量
python -c "import os; print(os.getenv('OPENAI_API_KEY'))"
```

## 性能优化

### 1. 应用优化
- 减少不必要的依赖
- 优化代码结构
- 使用缓存策略

### 2. 用户体验
- 添加加载提示
- 优化界面响应
- 提供错误处理

## 安全注意事项

### 1. API 密钥保护
- 使用 Streamlit Cloud 的 secrets 功能
- 不要在代码中硬编码密钥
- 定期轮换密钥

### 2. 访问控制
- 考虑添加用户认证
- 限制 API 调用频率
- 监控使用情况

## 更新部署

### 自动更新
```bash
# 推送代码到 GitHub
git add .
git commit -m "Update app"
git push origin main
```

### 手动更新
- 在 Streamlit Cloud 控制台点击 "Redeploy"

## 监控和分析

### 1. Streamlit Analytics
- 访问量统计
- 用户行为分析
- 性能监控

### 2. 自定义监控
- 添加日志记录
- 设置告警
- 错误追踪

## 支持资源

- [Streamlit 文档](https://docs.streamlit.io)
- [Streamlit Cloud](https://share.streamlit.io)
- [部署指南](https://docs.streamlit.io/streamlit-community-cloud)
- [故障排除](https://docs.streamlit.io/streamlit-community-cloud/troubleshooting)

## 下一步

部署完成后，你可以：
1. 分享应用链接给其他人
2. 收集用户反馈
3. 持续改进应用功能
4. 考虑升级到付费版本 