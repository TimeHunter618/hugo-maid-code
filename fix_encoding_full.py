import os

post_dir = r"f:\project\go\hugo_extended_withdeploy_0.163.2_windows-amd64\dev4\content\post"

fixed_count = 0

for root, dirs, files in os.walk(post_dir):
    dirs[:] = [d for d in dirs if d != 'llm']
    
    for file in files:
        if file.endswith('.zh-CN.md'):
            filepath = os.path.join(root, file)
            
            try:
                with open(filepath, 'rb') as f:
                    raw = f.read()
                
                try:
                    content = raw.decode('utf-8')
                    has_question = '\ufffd' in content
                    if has_question:
                        gbk_content = raw.decode('gbk')
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(gbk_content)
                        print(f"Fixed (GBK->UTF8): {file}")
                        fixed_count += 1
                except UnicodeDecodeError:
                    try:
                        gbk_content = raw.decode('gbk')
                        fixed_content = gbk_content.replace('???---', '---')
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(fixed_content)
                        print(f"Fixed (GBK->UTF8): {file}")
                        fixed_count += 1
                    except:
                        print(f"Failed: {file}")
                        
            except Exception as e:
                print(f"Error processing {file}: {e}")

print(f"\nDone! Total fixed: {fixed_count}")
