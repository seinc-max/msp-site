filepath = '/data/msp-site/managed-it-services-kitchener-waterloo.html'
with open(filepath, 'r') as f:
    content = f.read()

content = content.replace(
    '<meta name="description" content="Managed IT services for Kitchener-Waterloo businesses. Shadow AI audits, AI acceptable use policies, safe Microsoft Copilot deployment, and flat-rate monthly AI compliance for professional services." />',
    '<meta name="description" content="AI Governance and Automation for Kitchener-Waterloo businesses. Shadow AI audits, AI acceptable use policies, safe Microsoft Copilot deployment, and flat-rate monthly AI compliance for professional services." />'
)

with open(filepath, 'w') as f:
    f.write(content)
