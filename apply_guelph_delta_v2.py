import sys
import re

file_path = "/data/msp-site/ai-governance-guelph.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Try exact substring matching for the structured data
pattern = r'\{\s*"@type":\s*"Question",\s*"name":\s*"What does Trueline IT cost\?",\s*"acceptedAnswer":\s*\{\s*"@type":\s*"Answer",\s*"text":\s*"Essentials: \$99/user/month\. Professional: \$149/user/month \(most popular\)\. Complete: \$199/user/month\. Minimum 10 users\. Month-to-month, no long-term contract\."\s*\}\s*\},?'

content = re.sub(pattern, '', content)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

