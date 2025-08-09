# MCP服务器连接问题解决方案

## 问题描述
MCP服务器 `mcp.config.usrlocalmcp.undoom-uninstaller-mcp` 无法正常运行或连接。

## 诊断结果
✅ **所有系统检查都已通过**：
- Python环境正常
- 依赖包已正确安装
- 主脚本语法正确
- MCP服务器可以正常启动

## 解决方案

### 1. 检查配置文件格式
确保你的MCP配置文件使用正确的JSON格式，**不要包含注释**：

```json
{
  "mcpServers": {
    "undoom-uninstaller-mcp": {
      "command": "D:/undoom_Uninstaller_mcp/.venv/Scripts/python.exe",
      "args": [
        "D:/undoom_Uninstaller_mcp/main.py"
      ]
    }
  }
}
```

### 2. 替代配置方案
如果上述配置不工作，尝试使用相对路径配置：

```json
{
  "mcpServers": {
    "undoom-uninstaller-mcp": {
      "command": ".venv/Scripts/python.exe",
      "args": ["main.py"],
      "cwd": "D:/undoom_Uninstaller_mcp"
    }
  }
}
```

### 3. 配置步骤
1. **找到Trae IDE的MCP配置文件**
   - 通常位于用户配置目录
   - 文件名可能是 `mcp.json` 或类似名称

2. **更新配置文件**
   - 复制上述配置到文件中
   - 确保JSON格式正确（使用JSON验证器检查）
   - 保存文件

3. **重启Trae IDE**
   - 完全关闭Trae IDE
   - 重新启动IDE
   - 等待MCP服务器初始化

### 4. 验证连接
重启后，检查MCP面板中是否显示 `undoom-uninstaller-mcp` 服务器为运行状态。

### 5. 常见问题排查

#### 问题1：路径错误
- 确保所有路径使用正斜杠 `/` 而不是反斜杠 `\`
- 验证Python可执行文件路径正确
- 确认main.py文件路径正确

#### 问题2：权限问题
- 确保Trae IDE有权限访问指定目录
- 检查防火墙设置

#### 问题3：端口冲突
- MCP使用stdio通信，通常不会有端口冲突
- 如果有其他MCP服务器运行，确保名称不冲突

### 6. 手动测试
如果仍然有问题，可以手动测试服务器：

```bash
# 在命令行中运行
cd D:/undoom_Uninstaller_mcp
.venv/Scripts/python.exe main.py
```

服务器应该启动并等待MCP协议输入。

### 7. 可用工具
成功连接后，你将可以使用以下工具：

- `list_programs` - 列出已安装程序
- `search_programs` - 搜索程序
- `uninstall_program` - 卸载程序
- `show_program_details` - 显示程序详情
- `show_all_programs_detailed` - 显示所有程序详情
- `generate_markdown_report` - 生成Markdown报告

## 技术支持
如果按照上述步骤仍然无法解决问题，请：

1. 检查Trae IDE的日志输出
2. 确认IDE版本是否支持MCP协议
3. 尝试重新安装依赖包：
   ```bash
   cd D:/undoom_Uninstaller_mcp
   .venv/Scripts/pip install -r requirements.txt
   ```

---

**注意**：本文档基于当前系统诊断结果生成。所有系统组件都正常工作，问题很可能出现在IDE配置层面。