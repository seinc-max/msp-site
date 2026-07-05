import re

files_changes = {
    "/data/msp-site/blog/20-southern-ontario-shadow-ai-audits-2026.html": [
        ("we offer a free 15-minute IT Health Score assessment .", "we offer a free 15-minute AI Exposure Assessment .")
    ],
    "/data/msp-site/blog/is-your-ontario-business-pipeda-compliant.html": [
        ("Book your free 15-minute Trueline IT Health Score.", "Book your free 15-minute Trueline AI Exposure Score.")
    ],
    "/data/msp-site/ai-exposure-score.html": [
        ("AI Exposure Health Score & Readiness Audit | Trueline IT", "AI Exposure Risk Score & Readiness Audit | Trueline IT"),
        ("Health Score Questions", "AI Exposure Score Questions"),
        ("What do I do after I get my health score?", "What do I do after I get my AI exposure score?")
    ]
}

def apply_fixes():
    for file_path, changes in files_changes.items():
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            original_content = content
            
            for find_str, replace_str in changes:
                if find_str in content:
                    content = content.replace(find_str, replace_str)
                    print(f"[{file_path.split('/')[-1]}] Replaced string successfully")
                else:
                    print(f"[{file_path.split('/')[-1]}] WARNING: String not found: {find_str[:50]}...")

            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"--> Updated {file_path}")
            else:
                print(f"--> No changes made to {file_path}")
        except Exception as e:
            print(f"Error processing {file_path}: {e}")

apply_fixes()
print("Done.")
