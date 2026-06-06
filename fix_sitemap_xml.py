import re

filename = "/data/msp-site/sitemap.xml"

# Replace strings inside sitemap.xml
with open(filename, "r") as f:
    content = f.read()

content = content.replace("managed-it-services-southern-ontario.html", "ai-governance-southern-ontario.html")
content = content.replace("managed-it-services-burlington.html", "ai-governance-burlington.html")
content = content.replace("managed-it-services-hamilton.html", "ai-governance-hamilton.html")
content = content.replace("managed-it-services-guelph.html", "ai-governance-guelph.html")
content = content.replace("managed-it-services-waterloo.html", "ai-governance-waterloo.html")
content = content.replace("managed-it-services-cambridge.html", "ai-governance-cambridge.html")
content = content.replace("managed-it-services-kitchener-waterloo.html", "ai-governance-kitchener-waterloo.html")

with open(filename, "w") as f:
    f.write(content)
