import os

post_dir = r"f:\project\go\hugo_extended_withdeploy_0.163.2_windows-amd64\dev4\content\post"

duplicates = [
    ('详解解', '详解'),
    ('模式式', '模式'),
    ('分享享', '分享'),
    ('问题题', '问题'),
    ('实战战', '实战'),
    ('原理理', '原理'),
    ('封装装', '封装'),
    ('过程程', '过程'),
    ('通信信', '通信'),
    ('控制制', '控制'),
    ('挥手手', '挥手'),
    ('HashMapap', 'HashMap'),
    ('???---', '---'),
]

fixed_count = 0

for root, dirs, files in os.walk(post_dir):
    dirs[:] = [d for d in dirs if d != 'llm']
    
    for file in files:
        if file.endswith('.zh-CN.md'):
            filepath = os.path.join(root, file)
            
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                modified = False
                for old, new in duplicates:
                    if old in content:
                        content = content.replace(old, new)
                        modified = True
                
                if modified:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"Fixed: {file}")
                    fixed_count += 1
                        
            except Exception as e:
                print(f"Error processing {file}: {e}")

print(f"\nDone! Total fixed: {fixed_count}")
