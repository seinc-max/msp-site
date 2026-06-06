import re

filepath = "/data/msp-site/sitemap.xml"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# Replace all occurrences of .html inside <loc> tags
content = re.sub(r'(<loc>.*?)(\.html)(</loc>)', r'\1\3', content)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)
print("Updated sitemap.xml")
