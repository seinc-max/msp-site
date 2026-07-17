import re

with open('/opt/data/msp-site/risk-assessment.html', 'r') as f:
    html = f.read()

# Apply the same mobile fixes to the main Risk Assessment page since it uses the same core form logic
html = html.replace('<div id="form-container" class="p-8 sm:p-12">', '<div id="form-container" class="px-5 py-8 sm:p-12 relative" style="min-height: 400px;">')
html = html.replace('text-[0.95rem] font-medium', 'text-[0.9rem] sm:text-[0.95rem] font-medium leading-snug')
html = html.replace('text-[0.95rem] rounded-xl', 'text-[16px] rounded-xl') # Prevent iOS Zoom on Inputs

with open('/opt/data/msp-site/risk-assessment.html', 'w') as f:
    f.write(html)

print("Applied secondary fixes to main risk page.")
