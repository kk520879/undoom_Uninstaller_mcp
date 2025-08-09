#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MCP服务器诊断工具
用于检查undoom-uninstaller-mcp服务器的运行状态和配置
"""

import sys
import os
import json
import subprocess
from pathlib import Path

def check_python_environment():
    """检查Python环境"""
    print("🔍 检查Python环境...")
    print(f"  Python版本: {sys.version}")
    print(f"  Python路径: {sys.executable}")
    
    # 检查虚拟环境
    venv_python = Path("D:/undoom_Uninstaller_mcp/.venv/Scripts/python.exe")
    if venv_python.exists():
        print(f"  ✅ 虚拟环境Python存在: {venv_python}")
    else:
        print(f"  ❌ 虚拟环境Python不存在: {venv_python}")
        return False
    
    return True

def check_dependencies():
    """检查依赖包"""
    print("\n📦 检查依赖包...")
    
    try:
        import mcp
        print(f"  ✅ mcp包已安装: {mcp.__file__}")
    except ImportError as e:
        print(f"  ❌ mcp包未安装: {e}")
        return False
    
    try:
        import winreg
        print("  ✅ winreg模块可用")
    except ImportError as e:
        print(f"  ❌ winreg模块不可用: {e}")
        return False
    
    return True

def check_main_script():
    """检查主脚本"""
    print("\n📄 检查主脚本...")
    
    main_script = Path("D:/undoom_Uninstaller_mcp/main.py")
    if main_script.exists():
        print(f"  ✅ 主脚本存在: {main_script}")
    else:
        print(f"  ❌ 主脚本不存在: {main_script}")
        return False
    
    # 检查语法
    try:
        result = subprocess.run(
            ["D:/undoom_Uninstaller_mcp/.venv/Scripts/python.exe", "-m", "py_compile", "main.py"],
            cwd="D:/undoom_Uninstaller_mcp",
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode == 0:
            print("  ✅ 脚本语法检查通过")
        else:
            print(f"  ❌ 脚本语法错误: {result.stderr}")
            return False
    except Exception as e:
        print(f"  ⚠️ 无法检查脚本语法: {e}")
    
    return True

def test_mcp_server():
    """测试MCP服务器启动"""
    print("\n🚀 测试MCP服务器启动...")
    
    try:
        # 尝试启动服务器（短时间测试）
        process = subprocess.Popen(
            ["D:/undoom_Uninstaller_mcp/.venv/Scripts/python.exe", "main.py"],
            cwd="D:/undoom_Uninstaller_mcp",
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        # 等待2秒看是否有错误
        try:
            stdout, stderr = process.communicate(timeout=2)
            if process.returncode is not None and process.returncode != 0:
                print(f"  ❌ 服务器启动失败: {stderr}")
                return False
        except subprocess.TimeoutExpired:
            # 超时说明服务器正在运行
            process.terminate()
            print("  ✅ 服务器启动成功（正在运行中）")
            return True
            
    except Exception as e:
        print(f"  ❌ 启动测试失败: {e}")
        return False
    
    return True

def generate_config_suggestions():
    """生成配置建议"""
    print("\n⚙️ MCP配置建议:")
    
    # 标准配置
    config1 = {
        "mcpServers": {
            "undoom-uninstaller-mcp": {
                "command": "D:/undoom_Uninstaller_mcp/.venv/Scripts/python.exe",
                "args": ["D:/undoom_Uninstaller_mcp/main.py"]
            }
        }
    }
    
    # 带工作目录的配置
    config2 = {
        "mcpServers": {
            "undoom-uninstaller-mcp": {
                "command": ".venv/Scripts/python.exe",
                "args": ["main.py"],
                "cwd": "D:/undoom_Uninstaller_mcp"
            }
        }
    }
    
    print("\n  配置方案1（绝对路径）:")
    print(json.dumps(config1, indent=2, ensure_ascii=False))
    
    print("\n  配置方案2（相对路径+工作目录）:")
    print(json.dumps(config2, indent=2, ensure_ascii=False))
    
    print("\n  📝 配置步骤:")
    print("  1. 将上述配置复制到Trae IDE的MCP配置文件中")
    print("  2. 确保JSON格式正确（无语法错误）")
    print("  3. 重启Trae IDE")
    print("  4. 检查MCP服务器状态")

def main():
    """主诊断流程"""
    print("=" * 60)
    print("🔧 undoom-uninstaller-mcp 诊断工具")
    print("=" * 60)
    
    all_checks_passed = True
    
    # 执行各项检查
    if not check_python_environment():
        all_checks_passed = False
    
    if not check_dependencies():
        all_checks_passed = False
    
    if not check_main_script():
        all_checks_passed = False
    
    if not test_mcp_server():
        all_checks_passed = False
    
    # 生成配置建议
    generate_config_suggestions()
    
    print("\n" + "=" * 60)
    if all_checks_passed:
        print("✅ 所有检查通过！MCP服务器应该可以正常运行。")
        print("如果仍然无法连接，请检查Trae IDE的MCP配置。")
    else:
        print("❌ 发现问题，请根据上述提示进行修复。")
    print("=" * 60)

if __name__ == "__main__":
    main()