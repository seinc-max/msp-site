import os
import re

def update_schema(file_path):
    if not os.path.exists(file_path):
        return
        
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Step 1: Add "knowsAbout" to LocalBusiness JSON-LD
    if '"category": "AI Automation Agency",' in content and '"knowsAbout"' not in content:
        content = content.replace(
            '"category": "AI Automation Agency",',
            '"category": "AI Automation Agency",\n  "knowsAbout": ["AI Governance", "Shadow AI Prevention", "PIPEDA Compliance", "Microsoft 365 Copilot", "AI Acceptable Use Policy"],'
        )

    # Step 2: Write back
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

# Update Schema on all HTML files
for root, dirs, files in os.walk("/data/msp-site"):
    for file in files:
        if file.endswith(".html"):
            update_schema(os.path.join(root, file))

