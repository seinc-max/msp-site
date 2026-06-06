import os

fixes = [
    ("/data/msp-site/about.html", '<link rel="canonical" href="https://truelineit.com/about.html" />', '<link rel="canonical" href="https://truelineit.com/about" />'),
    ("/data/msp-site/privacy.html", '<link rel="canonical" href="https://truelineit.com/privacy.html" />', '<link rel="canonical" href="https://truelineit.com/privacy" />'),
    ("/data/msp-site/terms.html", '<link rel="canonical" href="https://truelineit.com/terms.html" />', '<link rel="canonical" href="https://truelineit.com/terms" />')
]

for filepath, old_str, new_str in fixes:
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        
        if old_str in content:
            content = content.replace(old_str, new_str)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Updated {filepath}")
        else:
            print(f"String not found in {filepath}:\n{old_str}")
    else:
        print(f"File not found: {filepath}")
