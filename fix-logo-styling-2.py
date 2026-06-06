import os
import re

files_to_update = [
    "index.html",
    "managed-it-services-burlington.html",
    "managed-it-services-hamilton.html",
    "managed-it-services-guelph.html",
    "managed-it-services-waterloo.html",
    "managed-it-services-cambridge.html",
    "managed-it-services-kitchener-waterloo.html"
]

cwd = '/data/msp-site'

old_anthropic_logo = """    <!-- Anthropic -->
    <div class="partner-item" title="Anthropic" style="opacity: 0.8; margin-top: -2px;">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 541.36 512" width="46" height="46">
        <path d="M129.21,123.63L234.33,306H109.91L4.79,123.63H129.21ZM308.28,306l105.12-182.37h124.42L367.6,423.86l-59.31-117.86ZM235.34,307.74l96.79,167.64V123.63h-96.79v184.11Z" fill="#D3A581"/>
      </svg>
    </div>"""

# Ensure the SVG itself doesn't cause clipping due to padding/borders by adjusting the viewBox and giving it standard dimensions for that specific SVG container.
new_anthropic_logo = """    <!-- Anthropic -->
    <div class="partner-item" title="Anthropic">
      <svg role="img" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" width="38" height="38">
        <path d="M17.3041 3.541h-3.6718l6.696 16.918H24Zm-10.6082 0L0 20.459h3.7442l1.3693-3.5527h7.0052l1.3693 3.5528h3.7442L10.5363 3.5409Zm-.3712 10.2232 2.2914-5.9456 2.2914 5.9456Z" fill="#D3A581"/>
      </svg>
    </div>"""


for filename in files_to_update:
    filepath = os.path.join(cwd, filename)
    if not os.path.exists(filepath):
        print(f"[!] File not found: {filename}")
        continue
        
    with open(filepath, 'r') as f:
        content = f.read()

    if old_anthropic_logo in content:
        content = content.replace(old_anthropic_logo, new_anthropic_logo)
        print(f"[+] Replaced Anthropic logo in: {filename}")
        
    with open(filepath, 'w') as f:
        f.write(content)

