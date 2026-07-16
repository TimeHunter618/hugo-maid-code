import os
import re

post_dir = r"f:\project\go\hugo_extended_withdeploy_0.163.2_windows-amd64\dev4\content\post"

replacements = {
    '线段?': '线段树',
    '技术分?': '技术分享',
    '适配器模式详?': '适配器模式详解',
    '责任链模式详?': '责任链模式详解',
    '观察者模式详?': '观察者模式详解',
    '装饰器模式详?': '装饰器模式详解',
    '策略模式详?': '策略模式详解',
    '模板方法模式详?': '模板方法模式详解',
    '单例模式详?': '单例模式详解',
    '代理模式详?': '代理模式详解',
    '工厂方法与抽象工厂模?': '工厂方法与抽象工厂模式',
    '建造者模式详?': '建造者模式详解',
    '结构型模?': '结构型模式',
    '行为型模?': '行为型模式',
    '创建型模?': '创建型模式',
    '排序算法详?': '排序算法详解',
    '哈希表HashM?': '哈希表HashMap',
    'TCP三次握手与四次挥?': 'TCP三次握手与四次挥手',
    'TCP流量控制与拥塞控?': 'TCP流量控制与拥塞控制',
    'WebSocket与实时通?': 'WebSocket与实时通信',
    'HTTP协议详解与HTTPS原?': 'HTTP协议详解与HTTPS原理',
    '网络分层模型与数据封?': '网络分层模型与数据封装',
    '从输入URL到页面渲染全过?': '从输入URL到页面渲染全过程',
    '动态规划经典问?': '动态规划经典问题',
    '图算法与最短路径详?': '图算法与最短路径详解',
    '二叉树与遍历实?': '二叉树与遍历实战',
    '位图BitMap详?': '位图BitMap详解',
}

fixed_count = 0

for root, dirs, files in os.walk(post_dir):
    dirs[:] = [d for d in dirs if d != 'llm']
    
    for file in files:
        if file.endswith('.zh-CN.md'):
            filepath = os.path.join(root, file)
            
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                has_garbage = '?' in content
                
                if has_garbage:
                    new_content = content
                    for old, new in replacements.items():
                        new_content = re.sub(old, new, new_content)
                    
                    if new_content != content:
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        print(f"Fixed: {file}")
                        fixed_count += 1
            except Exception as e:
                print(f"Error processing {file}: {e}")

print(f"\nDone! Total fixed: {fixed_count}")
