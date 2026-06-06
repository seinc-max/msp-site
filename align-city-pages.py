import os
import re

# We will use Burlington as the master template for the 5 main pages, 
# and explicitly structure Guelph to match that layout + FAQ injection.
# Actually, the simplest approach to guarantee 100% uniformity is to literally 
# copy the structure from Burlington and inject the specific city name.

source_file = '/data/msp-site/managed-it-services-burlington.html'

with open(source_file, 'r') as f:
    master_content = f.read()

cities = {
    'hamilton': 'Hamilton',
    'waterloo': 'Waterloo',
    'cambridge': 'Cambridge',
    'kitchener-waterloo': 'Kitchener-Waterloo'
    # We will handle Guelph separately due to the FAQ block
}

for city_slug, city_name in cities.items():
    new_content = master_content.replace('Burlington', city_name).replace('burlington', city_slug)
    
    filepath = f'/data/msp-site/managed-it-services-{city_slug}.html'
    with open(filepath, 'w') as f:
        f.write(new_content)
    
    print(f"[+] Aligned {city_name} with master layout")

print("Done standardizing the 4 basic city pages.")
