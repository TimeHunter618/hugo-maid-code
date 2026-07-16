import os
import re

post_dir = r"f:\project\go\hugo_extended_withdeploy_0.163.2_windows-amd64\dev4\content\post"

fixed_count = 0

for root, dirs, files in os.walk(post_dir):
    dirs[:] = [d for d in dirs if d != 'llm']
    
    for file in files:
        if file.endswith('.zh-CN.md'):
            filepath = os.path.join(root, file)
            
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                original = content
                
                content = content.replace('\ufffd', '')
                content = content.replace('\ufffd?', '')
                content = content.replace('???---', '---')
                
                content = re.sub(r'(\w)\1{2,}', r'\1', content)
                
                if content != original:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"Fixed: {file}")
                    fixed_count += 1
                        
            except Exception as e:
                print(f"Error processing {file}: {e}")

print(f"\nDone! Total fixed: {fixed_count}")
