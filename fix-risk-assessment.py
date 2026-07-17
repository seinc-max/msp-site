import re

with open('/opt/data/msp-site/index.html', 'r') as f:
    master_html = f.read()

# Extract exactly what is in index.html to inject into risk-assessment.html
# 1. <style> block
style_match = re.search(r'(<style>.*?</style>)', master_html, re.DOTALL)
master_style = style_match.group(1) if style_match else ""

# 2. Font link
font_match = re.search(r'(<link href="https://fonts\.googleapis\.com/css2[^"]*".*?>)', master_html)
font_link = font_match.group(1) if font_match else ""

# 3. <nav> block
nav_match = re.search(r'(<nav>.*?</nav>)', master_html, re.DOTALL)
master_nav = nav_match.group(1) if nav_match else ""

# 4. <footer> block
footer_match = re.search(r'(<footer>.*?</footer>)', master_html, re.DOTALL)
master_footer = footer_match.group(1) if footer_match else ""


with open('/opt/data/msp-site/risk-assessment.html', 'r') as f:
    risk_html = f.read()

# Replace the mismatched blocks in risk-assessment.html with exactly what was found in index.html
risk_html = re.sub(r'<style>.*?</style>', master_style, risk_html, flags=re.DOTALL)
risk_html = re.sub(r'<link href="https://fonts\.googleapis\.com/css2.*?>', font_link, risk_html, flags=re.DOTALL)
risk_html = re.sub(r'<nav>.*?</nav>', master_nav, risk_html, flags=re.DOTALL)
risk_html = re.sub(r'<footer>.*?</footer>', master_footer, risk_html, flags=re.DOTALL)

with open('/opt/data/msp-site/risk-assessment.html', 'w') as f:
    f.write(risk_html)

print("Injected exact index.html parity blocks.")
