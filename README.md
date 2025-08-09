# 🗑️ Undoom Uninstaller MCP

一个基于MCP (Model Context Protocol) 的Windows程序卸载器服务，提供程序管理、卸载、强制删除和残留清理功能。

[![PyPI version](https://badge.fury.io/py/undoom-uninstaller-mcp.svg)](https://badge.fury.io/py/undoom-uninstaller-mcp)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## ✨ 功能特性

- 📋 **程序列表管理**: 从Windows注册表获取已安装程序列表
- 🔍 **智能搜索**: 支持按名称和发布商搜索程序
- 📊 **详细信息**: 查看程序的详细信息（版本、大小、安装位置等）
- 🗑️ **标准卸载**: 使用程序自带的卸载程序进行卸载
- ⚡ **强制删除**: 强制删除程序文件和注册表项
- 🧹 **残留清理**: 清理程序卸载后的残留文件和文件夹
- 🔄 **列表刷新**: 重新扫描系统中的已安装程序
- 📈 **美化报告**: 生成详细的Markdown格式程序报告

## 🚀 快速开始

### 安装方式

#### 方式一：通过PyPI安装（推荐）
```bash
# 使用uv安装
uvx --index-url https://pypi.tuna.tsinghua.edu.cn/simple undoom-uninstaller-mcp

# 或使用pip安装
pip install undoom-uninstaller-mcp
```

#### 方式二：从源码安装
```bash
git clone https://github.com/kk520879/undoom_Uninstaller_mcp.git
cd undoom_Uninstaller_mcp
uv sync
```

### MCP配置

在您的MCP客户端配置文件中添加以下配置：

```json
{
  "mcpServers": {
    "undoom-uninstaller-mcp": {
      "command": "uvx",
      "args": [
        "--index-url",
        "https://pypi.tuna.tsinghua.edu.cn/simple",
        "undoom-uninstaller-mcp"
      ]
    }
  }
}
```

#### 常见MCP客户端配置位置：

- **Claude Desktop**: `%APPDATA%\Claude\claude_desktop_config.json`
- **CodeBuddy**: 在设置中的MCP服务器配置
- **其他客户端**: 请参考相应客户端的文档

## 📖 使用方法

### 启动MCP服务器

配置完成后，MCP服务器会自动启动。您可以通过MCP客户端调用以下工具：

### 🛠️ 可用工具

以下是所有可用的MCP工具及其详细说明：

#### 1. list_programs
列出所有已安装的程序（包含安装时间和盘符信息）

**参数:**
- `search` (可选): 搜索关键词

**返回信息:**
- 程序名称、发布商、版本、大小、安装位置
- **新增**: 安装时间、所在盘符

**示例:**
```json
{
  "search": "chrome"
}
```

#### 2. get_program_details
获取指定程序的详细信息（包含安装时间和盘符信息）

**参数:**
- `program_name` (必需): 程序名称

**返回信息:**
- 程序名称、发布商、版本、大小、安装位置、卸载字符串、注册表键
- **新增**: 安装时间、所在盘符

**示例:**
```json
{
  "program_name": "Google Chrome"
}
```

#### 3. uninstall_program
卸载指定程序（使用程序自带的卸载程序）

**参数:**
- `program_name` (必需): 要卸载的程序名称

**示例:**
```json
{
  "program_name": "Google Chrome"
}
```

#### 4. force_remove_program
强制删除程序（删除文件和注册表项）

**警告**: 此操作不可逆，请谨慎使用

**参数:**
- `program_name` (必需): 要强制删除的程序名称

**示例:**
```json
{
  "program_name": "Broken Software"
}
```

#### 5. clean_residues
清理程序残留文件

**参数:**
- `program_name` (必需): 要清理残留的程序名称

**示例:**
```json
{
  "program_name": "Old Program"
}
```

#### 6. refresh_programs
刷新程序列表

**参数:** 无

#### 7. show_all_programs_detailed
显示所有程序的详细信息，包括名称、安装时间和盘符

**参数:**
- `limit` (可选): 限制返回的程序数量，默认为100
- `sort_by` (可选): 排序字段，可选值：
  - `name`: 按程序名称排序（默认）
  - `install_date`: 按安装时间排序
  - `drive_letter`: 按盘符排序

**返回信息:**
- 程序名称、安装时间、所在盘符
- 发布商、版本、大小、安装位置

**示例:**
```json
{
  "limit": 50,
  "sort_by": "install_date"
}
```

#### 8. generate_markdown_report
生成系统程序信息的美化Markdown报告文件

**参数:**
- `filename` (可选): 输出文件名（不包含扩展名），默认为'system_programs_report'
- `limit` (可选): 限制返回的程序数量，默认为200
- `sort_by` (可选): 排序字段，可选值：
  - `name`: 按程序名称排序（默认）
  - `install_date`: 按安装时间排序
  - `drive_letter`: 按盘符排序
- `include_stats` (可选): 是否包含详细统计信息，默认为true

**返回信息:**
- 生成包含所有程序信息的美化Markdown报告文件
- 包含统计概览、分类显示、程序详细列表等
- 支持按类别分组显示（开发工具、浏览器、游戏等）

**示例:**
```json
{
  "filename": "my_programs_report",
  "limit": 100,
  "sort_by": "name",
  "include_stats": true
}
```

## 🎯 使用示例

### 基本操作示例

1. **获取程序列表**
```json
// 获取所有程序
{
  "tool": "list_programs"
}

// 搜索特定程序
{
  "tool": "list_programs",
  "arguments": {
    "search": "chrome"
  }
}
```

2. **查看程序详情**
```json
{
  "tool": "get_program_details",
  "arguments": {
    "program_name": "Google Chrome"
  }
}
```

3. **生成美化报告**
```json
{
  "tool": "generate_markdown_report",
  "arguments": {
    "filename": "system_analysis",
    "limit": 50,
    "sort_by": "install_date",
    "include_stats": true
  }
}
```

### 高级管理操作

4. **卸载程序**
```json
{
  "tool": "uninstall_program",
  "arguments": {
    "program_name": "Unwanted Software"
  }
}
```

5. **强制删除程序**
```json
{
  "tool": "force_remove_program",
  "arguments": {
    "program_name": "Broken Software"
  }
}
```

6. **清理残留文件**
```json
{
  "tool": "clean_residues",
  "arguments": {
    "program_name": "Old Program"
  }
}
```

## 🔧 技术实现

### 数据来源
程序信息从以下Windows注册表位置获取：
- `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall`
- `HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall`
- `HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall`

### 程序信息字段
| 字段 | 描述 | 示例 |
|------|------|------|
| **name** | 程序名称 | `Google Chrome` |
| **publisher** | 发布商 | `Google LLC` |
| **version** | 版本号 | `139.0.7258.66` |
| **size** | 安装大小 | `342.3 MB` |
| **install_location** | 安装位置 | `C:\Program Files\Google\Chrome` |
| **install_date** | 安装时间 | `2025-08-07` |
| **drive_letter** | 所在盘符 | `C:`, `D:`, `网络路径` |
| **uninstall_string** | 卸载命令 | 程序的卸载命令行 |
| **reg_key** | 注册表键路径 | 注册表中的完整路径 |

### 残留清理位置
系统会自动检查以下常见残留位置：
- 📁 程序安装目录
- 📁 `%APPDATA%\[程序名]`
- 📁 `%LOCALAPPDATA%\[程序名]`
- 📁 `%PROGRAMDATA%\[程序名]`
- 📁 `%USERPROFILE%\AppData\Local\[程序名]`
- 📁 `%USERPROFILE%\AppData\Roaming\[程序名]`

### 美化报告特性
- 📊 **智能分类**: 自动将程序按类型分组（开发工具、浏览器、游戏等）
- 📈 **可视化统计**: 盘符分布图表、发布商统计等
- 🎨 **美观界面**: 使用图标和颜色增强可读性
- 📋 **详细信息**: 包含完整的程序信息和系统统计

## ⚠️ 注意事项

| ⚠️ 重要提醒 | 说明 |
|-------------|------|
| **管理员权限** | 某些操作可能需要管理员权限才能执行 |
| **数据安全** | 强制删除和残留清理操作不可逆，请谨慎使用 |
| **系统兼容性** | 仅支持Windows系统（Windows 10/11推荐） |
| **程序限制** | 某些系统程序可能无法卸载或删除 |
| **备份建议** | 执行删除操作前建议备份重要数据 |

## 🤝 贡献指南

我们欢迎各种形式的贡献！

### 如何贡献
1. Fork 本项目
2. 创建您的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交您的更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开一个 Pull Request

### 报告问题
如果您发现了bug或有功能建议，请在 [Issues](https://github.com/kk520879/undoom_Uninstaller_mcp/issues) 页面提交。

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 🙏 致谢

- 感谢 [MCP](https://modelcontextprotocol.io/) 提供的优秀协议框架
- 感谢所有贡献者和用户的支持

---

<div align="center">

**如果这个项目对您有帮助，请给它一个 ⭐**

[报告问题](https://github.com/kk520879/undoom_Uninstaller_mcp/issues) • [功能请求](https://github.com/kk520879/undoom_Uninstaller_mcp/issues) • [贡献代码](https://github.com/kk520879/undoom_Uninstaller_mcp/pulls)

</div>
