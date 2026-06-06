import glob
import re
import os

files = glob.glob("/data/msp-site/*.html")

for filename in files:
    with open(filename, "r") as f:
        content = f.read()

    original = content
    
    # "category": "Managed Service Provider" -> "category": "AI Automation Agency"
    content = content.replace('"category": "Managed Service Provider"', '"category": "AI Automation Agency"')
    
    # In index.html specifically
    if "index.html" in filename:
        content = re.sub(r'content="Trueline IT \| Managed IT Services for Small Business in Canada"', 'content="Trueline IT | AI Governance & Automation for Professional Services Businesses in Ontario"', content)
        content = re.sub(r'"description": "Flat-rate managed IT services for small businesses across Canada\.', '"description": "Flat-rate AI governance and automation for professional services in Ontario.', content)
        content = re.sub(r'"name": "Managed IT Support"', '"name": "AI Governance & Automation"', content)
        content = re.sub(r'24/7 helpdesk, security monitoring, backups, and M365', 'Shadow AI audits, Copilot compliance, and secure workflow automation', content)
        content = re.sub(r'"description": "Unlimited helpdesk, proactive monitoring, backups, and cyber', '"description": "Flat-rate AI governance, Copilot compliance, and secure automation for', content)

    if content != original:
        with open(filename, "w") as f:
            f.write(content)
        print(f"Updated {os.path.basename(filename)}")
