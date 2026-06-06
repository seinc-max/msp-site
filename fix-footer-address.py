import os

files_to_update = [
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

    # I made a mistake using Burlington as the direct base — it changed the footer address physically
    # I'll revert just that exact string 
    
    # Extract the city to revert correctly from the file name
    import re
    city_match = re.search(r'managed-it-services-(.+)\.html', filename)
    if city_match:
        city_raw = city_match.group(1)
        city = city_raw.capitalize()
        if city_raw == "kitchener-waterloo":
            city = "Kitchener-Waterloo"
            
        old_footer = f'1250 Brant Street, Suite 400, {city}, ON L7P 1X8'
        new_footer = '1250 Brant Street, Suite 400, Burlington, ON L7P 1X8'
        
        content = content.replace(old_footer, new_footer)

    with open(filepath, 'w') as f:
        f.write(content)

    print(f"[+] Reverted footer address in: {filename}")

