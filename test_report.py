#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from undoom_uninstaller_mcp.program_manager import ProgramManager
from undoom_uninstaller_mcp.report_generator import ReportGenerator

def test_all_functions():
    """测试所有功能"""
    print("=" * 60)
    print("🚀 开始测试 undoom-uninstaller-mcp 所有功能")
    print("=" * 60)
    
    # 初始化
    print("\n1️⃣ 正在初始化ProgramManager...")
    program_manager = ProgramManager()
    report_generator = ReportGenerator()
    
    print("2️⃣ 正在加载已安装程序列表...")
    program_manager.load_installed_programs()
    
    total_programs = len(program_manager.programs)
    print(f"✅ 找到 {total_programs} 个已安装程序")
    
    if total_programs == 0:
        print("❌ 没有找到已安装程序，无法继续测试")
        return
    
    # 测试基本功能
    print("\n3️⃣ 测试基本功能...")
    
    # 显示前5个程序
    print("\n📋 前5个程序列表:")
    for i, program in enumerate(program_manager.programs[:5], 1):
        print(f"  {i}. {program.name} - {program.publisher} ({program.version})")
    
    # 测试搜索功能
    print("\n🔍 测试搜索功能 (搜索'Microsoft'):")
    search_results = program_manager.search_programs('Microsoft')
    print(f"  找到 {len(search_results)} 个相关程序")
    
    # 测试Markdown表格生成
    print("\n4️⃣ 测试Markdown表格生成...")
    test_programs = program_manager.programs[:3]  # 取前3个程序测试
    markdown_table = report_generator.generate_markdown_table(test_programs, "测试程序列表")
    
    print("✅ Markdown表格生成成功")
    print("📄 表格预览 (前200字符):")
    print(markdown_table[:200] + "..." if len(markdown_table) > 200 else markdown_table)
    
    # 测试增强版Markdown报告生成
    print("\n5️⃣ 测试增强版Markdown报告生成...")
    test_programs = program_manager.programs[:15]  # 取前15个程序测试
    
    success, message = report_generator.generate_enhanced_markdown_report(
        test_programs, 
        filename="complete_test_report", 
        include_stats=True
    )
    
    if success:
        print(f"✅ {message}")
    else:
        print(f"❌ 报告生成失败: {message}")
    
    # 统计信息
    print("\n6️⃣ 系统统计信息:")
    stats = program_manager.get_statistics()
    
    print("📊 按盘符分布:")
    for drive, count in sorted(stats["drive_distribution"].items()):
        percentage = (count / total_programs) * 100
        print(f"  - {drive}: {count} 个程序 ({percentage:.1f}%)")
    
    # 按发布商统计（前5名）
    top_publishers = sorted(stats["publisher_distribution"].items(), key=lambda x: x[1], reverse=True)[:5]
    if top_publishers:
        print("\n🏢 主要软件发布商（前5名）:")
        for publisher, count in top_publishers:
            print(f"  - {publisher}: {count} 个程序")
    
    print("\n" + "=" * 60)
    print("🎉 所有功能测试完成！")
    print("=" * 60)

if __name__ == "__main__":
    test_all_functions()