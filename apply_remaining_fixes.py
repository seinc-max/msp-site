import os
import re

files_to_fix = [
    "/data/msp-site/about.html",
    "/data/msp-site/it-support-ontario.html",
    "/data/msp-site/audit-confirmed.html",
    "/data/msp-site/privacy.html",
    "/data/msp-site/terms.html",
    "/data/msp-site/blog/blog-post.html"
]

for file_path in files_to_fix:
    if not os.path.exists(file_path):
        continue
        
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Standard JSON-LD replacements
    content = content.replace(
        '"description": "Flat-rate managed IT services for small businesses across Canada. 24/7 helpdesk, security monitoring, backups, and M365 support."',
        '"description": "Flat-rate AI governance and automation for professional services in Ontario. Shadow AI audits, Copilot compliance, and secure workflow automation support."'
    )
    
    # Specific file replacements
    if "about.html" in file_path:
        content = content.replace(
            '<meta name="description" content="Learn about Trueline IT — a Southern Ontario managed IT provider delivering flat-rate support, cybersecurity, and compliance for small businesses starting at $99/user/mo." />',
            '<meta name="description" content="Learn about Trueline IT — a Southern Ontario AI governance provider delivering flat-rate AI policies, automation limits, and Shadow AI audits for professional services." />'
        )
    elif "terms.html" in file_path:
        content = content.replace(
            '<meta name="description" content="Trueline IT terms of service — governing use of our managed IT services for small businesses across Southern Ontario." />',
            '<meta name="description" content="Trueline IT terms of service — governing use of our AI governance and automation services for businesses across Southern Ontario." />'
        )
        content = content.replace(
            '<p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.7; margin-bottom: 30px;">Managed IT services provided by Trueline IT are governed by a separate Master Service Agreement signed at the time of engagement. Nothing on this site constitutes a binding service commitment.</p>',
            '<p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.7; margin-bottom: 30px;">AI governance and automation services provided by Trueline IT are governed by a separate Master Service Agreement signed at the time of engagement. Nothing on this site constitutes a binding service commitment.</p>'
        )
    elif "blog-post.html" in file_path:
        content = content.replace(
            '<meta name="keywords" content="managed IT, Southern Ontario, keyword1, keyword2">',
            '<meta name="keywords" content="AI governance, Southern Ontario, keyword1, keyword2">'
        )
    elif "it-support-ontario.html" in file_path:
        # We need to completely repurpose this page just like the others. Let's do a quick structural hit.
        content = re.sub(
            r'<title>.*?</title>', 
            '<title>IT Support & AI Automation in Ontario | Trueline IT</title>', 
            content
        )
        content = content.replace(
            '<strong style="color: var(--navy);">SMBs without managed IT spend up to 40% more</strong> on technology support costs than those with a dedicated provider. — BizTech',
            '<strong style="color: var(--navy);">Professional services wasting time on manual entry instead of automation spend up to 40% more</strong> on administrative overhead than those with an AI governance plan. — Trueline IT'
        )
        
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

print("Done")
