import os

filepath = '/data/msp-site/managed-it-services-southern-ontario.html'

with open(filepath, 'r') as f:
    content = f.read()

content = content.replace(
    '"description": "Flat-rate managed IT services for small businesses across Canada. 24/7 helpdesk, security monitoring, backups, and M365 support.",',
    '"description": "Flat-rate AI governance and shadow AI audits for professional services firms in Southern Ontario. Protect your firm from data leaks and liability with rapid 30-day rollouts.",'
)

content = content.replace(
    '"serviceType": "Managed IT Services",',
    '"serviceType": "AI Governance",'
)

content = content.replace(
    '"name": "Managed IT Services",',
    '"name": "AI Governance",'
)

content = content.replace(
    '"name": "Managed IT Support",',
    '"name": "Monthly AI Governance",'
)

content = content.replace(
    '"description": "Unlimited helpdesk, proactive monitoring, backups, and cybersecurity — flat rate per user per month."',
    '"description": "Unlimited active automations, shadow AI audits, acceptable use policies, and compliance reporting at a flat monthly rate."'
)

content = content.replace(
    '"description": "Proactive, flat-rate managed IT services for Southern Ontario businesses — 24/7 monitoring, security, backups, and compliance.",',
    '"description": "Flat-rate AI Governance for Southern Ontario businesses — shadow AI audits, AUP compliance, and intelligent automations.",'
)

with open(filepath, 'w') as f:
    f.write(content)
print("[+] Fixed scheme tags on Southern Ontario parent page")
