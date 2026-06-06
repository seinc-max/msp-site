import os

files = [
    "/data/msp-site/blog/20-southern-ontario-shadow-ai-audits-2026.html",
    "/data/msp-site/blog/is-your-ontario-business-pipeda-compliant.html"
]

tags = '<meta property="og:image" content="https://truelineit.com/assets/og-image.png" />\n<meta name="twitter:image" content="https://truelineit.com/assets/og-image.png" />\n'

for filepath in files:
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        
        if '<meta property="og:image"' not in content:
            parts = content.rsplit("</head>", 1)
            if len(parts) == 2:
                new_content = parts[0] + tags + "</head>" + parts[1]
                
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(new_content)
                print(f"Updated {filepath}")
