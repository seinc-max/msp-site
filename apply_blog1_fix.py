import re

file_path = "/data/msp-site/blog/20-southern-ontario-shadow-ai-audits-2026.html"

try:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    
    # Text in Schema
    find_str_1 = "free 15-minute IT Health Score assessment."
    replace_str_1 = "free 15-minute AI Exposure Assessment."
    
    # Text in HTML
    find_str_2 = "free 15-minute IT Health Score assessment</strong>."
    replace_str_2 = "free 15-minute AI Exposure Assessment</strong>."
    
    if find_str_1 in content:
        content = content.replace(find_str_1, replace_str_1)
        print(f"[{file_path.split('/')[-1]}] Replaced string 1 successfully")
        
    if find_str_2 in content:
        content = content.replace(find_str_2, replace_str_2)
        print(f"[{file_path.split('/')[-1]}] Replaced string 2 successfully")

    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"--> Updated {file_path}")
    else:
        print(f"--> No changes made to {file_path}")
except Exception as e:
    print(f"Error processing {file_path}: {e}")

print("Done.")
