import re

file_path = "/data/msp-site/about.html"
find_str = "Your outsourced AI department — without the overhead."
replace_str = "Your Sovereign Automation & Governance Partners — without the overhead."

try:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    
    if find_str in content:
        content = content.replace(find_str, replace_str)
        print(f"[{file_path.split('/')[-1]}] Replaced string successfully")

    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"--> Updated {file_path}")
    else:
        print(f"--> No changes made to {file_path}")
except Exception as e:
    print(f"Error processing {file_path}: {e}")

print("Done.")
