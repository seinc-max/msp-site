import os

files_to_update = [
    "managed-it-services-burlington.html",
    "managed-it-services-hamilton.html",
    "managed-it-services-guelph.html",
    "managed-it-services-waterloo.html",
    "managed-it-services-cambridge.html",
    "managed-it-services-kitchener-waterloo.html"
]

cwd = '/data/msp-site'

for filename in files_to_update:
    filepath = os.path.join(cwd, filename)
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, 'r') as f:
        content = f.read()

    # The meta description string replacement was failing to catch "Managed IT services" due to casing/placement. Let's force rewrite it.
    import re
    
    city_match = re.search(r'managed-it-services-(\w+)', filename)
    if city_match:
        city_raw = city_match.group(1)
        city = city_raw.capitalize()
        if city_raw == "kitchener-waterloo":
            city = "Kitchener-Waterloo"
            
        old_meta = f'<meta name="description" content="Managed IT services for {city} businesses. Shadow AI audits, AI acceptable use policies, safe Microsoft Copilot deployment, and flat-rate monthly AI compliance for professional services." />'
        new_meta = f'<meta name="description" content="AI Governance and Automation for {city} businesses. Shadow AI audits, AI acceptable use policies, safe Microsoft Copilot deployment, and flat-rate monthly AI compliance for professional services." />'
        
        content = content.replace(old_meta, new_meta)

    with open(filepath, 'w') as f:
        f.write(content)

    print(f"[+] Fixed meta desc in: {filename}")

