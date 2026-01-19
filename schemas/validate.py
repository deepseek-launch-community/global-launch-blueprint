#!/usr/bin/env python3
"""
SRCP JSON基础验证工具
"""
import json
import sys

def main():
    if len(sys.argv) < 2:
        print("用法: python validate.py 你的文件.json")
        return
    
    try:
        with open(sys.argv[1], 'r') as f:
            data = json.load(f)
        
        # 基础检查
        if "ResponsibilityView" not in data:
            print("❌ 缺少 ResponsibilityView")
        else:
            print("✅ ResponsibilityView: 存在")
            
        if "ReasoningPath" not in data:
            print("❌ 缺少 ReasoningPath")
        else:
            print("✅ ReasoningPath: 存在")
            
        print("\n📋 基础验证完成")
        
    except Exception as e:
        print(f"❌ 错误: {e}")

if __name__ == "__main__":
    main()
