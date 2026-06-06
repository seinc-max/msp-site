import sys

file_path = "/data/msp-site/it-cost-guide-ontario.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Fix h1
content = content.replace("<h1>What Does IT Really Cost?<br>A Budget Guide for Business Owners.</h1>", "<h1>Stop Ignoring the Hidden Cost<br>of Shadow AI.</h1>")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

