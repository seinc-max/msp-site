import os
import re

files_to_update = [
    "managed-it-services-burlington.html",
    "managed-it-services-hamilton.html",
    "managed-it-services-guelph.html",
    "managed-it-services-waterloo.html",
    "managed-it-services-cambridge.html",
    "managed-it-services-kitchener-waterloo.html",
    "managed-it-services-southern-ontario.html"
]

cwd = '/data/msp-site'

for filename in files_to_update:
    filepath = os.path.join(cwd, filename)
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, 'r') as f:
        content = f.read()

    # The breadcrumb schema still had "Managed IT Services" specifically defined in it
    content = content.replace(
        '"name":"Managed IT Services"',
        '"name":"AI Governance"'
    )

    with open(filepath, 'w') as f:
        f.write(content)

    print(f"[+] Fixed breadcrumb names in: {filename}")

