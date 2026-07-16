import os
import re

post_dir = r"f:\project\go\hugo_extended_withdeploy_0.163.2_windows-amd64\dev4\content\post"

byte_replacements = [
    (b'\xe6\xa0\x91\xef\xbf\xbd?', b'\xe6\xa0\x91'),
    (b'\xe4\xba\xa7\xef\xbf\xbd?', b'\xe4\xba\xa7'),
    (b'\xe8\xae\xa2\xef\xbf\xbd?', b'\xe8\xae\xa2'),
    (b'\xe6\xb3\x95\xef\xbf\xbd?', b'\xe6\xb3\x95'),
    (b'\xe6\xa8\xa1\xef\xbf\xbd?', b'\xe6\xa8\xa1'),
    (b'\xe5\x88\x86\xef\xbf\xbd?', b'\xe5\x88\x86'),
    (b'\xe6\x8e\xa5\xef\xbf\xbd?', b'\xe6\x8e\xa5'),
    (b'\xe6\xb5\x81\xef\xbf\xbd?', b'\xe6\xb5\x81'),
    (b'\xe6\x8e\xa7\xef\xbf\xbd?', b'\xe6\x8e\xa7'),
    (b'\xe9\x80\x9a\xef\xbf\xbd?', b'\xe9\x80\x9a'),
    (b'\xe5\x8e\x9f\xef\xbf\xbd?', b'\xe5\x8e\x9f'),
    (b'\xe8\xb4\xa3\xef\xbf\xbd?', b'\xe8\xb4\xa3'),
    (b'\xe6\x83\x85\xef\xbf\xbd?', b'\xe6\x83\x85'),
    (b'\xe5\x88\x9b\xef\xbf\xbd?', b'\xe5\x88\x9b'),
    (b'\xe8\xae\xbe\xef\xbf\xbd?', b'\xe8\xae\xbe'),
    (b'\xe6\x96\xbd\xef\xbf\xbd?', b'\xe6\x96\xbd'),
    (b'\xe7\xae\x97\xef\xbf\xbd?', b'\xe7\xae\x97'),
    (b'\xe9\x97\xae\xef\xbf\xbd?', b'\xe9\x97\xae'),
    (b'\xe8\xb7\xaf\xef\xbf\xbd?', b'\xe8\xb7\xaf'),
    (b'\xe5\xae\x9e\xef\xbf\xbd?', b'\xe5\xae\x9e'),
    (b'\xef\xbf\xbd?M', b'M'),
    (b'\xef\xbf\xbd?S', b'S'),
    (b'\xef\xbf\xbd?T', b'T'),
]

char_replacements = {
    '\ufffd?': '',
    '\ufffd': '',
    '???---': '---',
}

fixed_count = 0

for root, dirs, files in os.walk(post_dir):
    dirs[:] = [d for d in dirs if d != 'llm']
    
    for file in files:
        if file.endswith('.zh-CN.md'):
            filepath = os.path.join(root, file)
            
            try:
                with open(filepath, 'rb') as f:
                    raw = f.read()
                
                modified = False
                
                for old, new in byte_replacements:
                    if old in raw:
                        raw = raw.replace(old, new)
                        modified = True
                
                if modified:
                    try:
                        content = raw.decode('utf-8')
                        for old, new in char_replacements.items():
                            content = content.replace(old, new)
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(content)
                        print(f"Fixed: {file}")
                        fixed_count += 1
                    except:
                        print(f"Failed to decode after fix: {file}")
                        
            except Exception as e:
                print(f"Error processing {file}: {e}")

print(f"\nDone! Total fixed: {fixed_count}")
