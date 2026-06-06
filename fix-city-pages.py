import os
import glob
import re

files_to_update = [
    "managed-it-services-burlington.html",
    "managed-it-services-hamilton.html",
    "managed-it-services-guelph.html",
    "managed-it-services-waterloo.html",
    "managed-it-services-cambridge.html",
    "managed-it-services-kitchener-waterloo.html"
]

keywords_map = {
    "managed-it-services-burlington.html": '<meta name="keywords" content="AI governance Burlington Ontario, AI acceptable use policy Burlington, shadow AI audit Burlington, AI automation Burlington professional services" />',
    "managed-it-services-hamilton.html": '<meta name="keywords" content="AI governance Hamilton Ontario, AI acceptable use policy Hamilton, shadow AI audit Hamilton, AI automation Hamilton professional services" />',
    "managed-it-services-guelph.html": '<meta name="keywords" content="AI governance Guelph Ontario, AI acceptable use policy Guelph, shadow AI audit Guelph, AI automation Guelph professional services" />',
    "managed-it-services-waterloo.html": '<meta name="keywords" content="AI governance Waterloo Ontario, AI acceptable use policy Waterloo, shadow AI audit Waterloo, AI automation Waterloo professional services" />',
    "managed-it-services-cambridge.html": '<meta name="keywords" content="AI governance Cambridge Ontario, AI acceptable use policy Cambridge, shadow AI audit Cambridge, AI automation Cambridge professional services" />',
    "managed-it-services-kitchener-waterloo.html": '<meta name="keywords" content="AI governance Kitchener Waterloo Ontario, AI acceptable use policy Kitchener Waterloo, shadow AI audit KW, AI automation Kitchener Waterloo professional services" />'
}

titles_map = {
    "managed-it-services-burlington.html": "<title>AI Governance & Automation Burlington | Protect Client Data | Trueline IT</title>",
    "managed-it-services-hamilton.html": "<title>AI Governance & Automation Hamilton | Protect Client Data | Trueline IT</title>",
    "managed-it-services-guelph.html": "<title>AI Governance & Automation Guelph | Protect Client Data | Trueline IT</title>",
    "managed-it-services-waterloo.html": "<title>AI Governance & Automation Waterloo | Protect Client Data | Trueline IT</title>",
    "managed-it-services-cambridge.html": "<title>AI Governance & Automation Cambridge | Protect Client Data | Trueline IT</title>",
    "managed-it-services-kitchener-waterloo.html": "<title>AI Governance & Automation Kitchener-Waterloo | Protect Client Data | Trueline IT</title>"
}

og_title_map = {
    "managed-it-services-burlington.html": '<meta property="og:title" content="AI Governance & Automation Burlington | Protect Client Data | Trueline IT" />',
    "managed-it-services-hamilton.html": '<meta property="og:title" content="AI Governance & Automation Hamilton | Protect Client Data | Trueline IT" />',
    "managed-it-services-guelph.html": '<meta property="og:title" content="AI Governance & Automation Guelph | Protect Client Data | Trueline IT" />',
    "managed-it-services-waterloo.html": '<meta property="og:title" content="AI Governance & Automation Waterloo | Protect Client Data | Trueline IT" />',
    "managed-it-services-cambridge.html": '<meta property="og:title" content="AI Governance & Automation Cambridge | Protect Client Data | Trueline IT" />',
    "managed-it-services-kitchener-waterloo.html": '<meta property="og:title" content="AI Governance & Automation Kitchener-Waterloo | Protect Client Data | Trueline IT" />'
}

cwd = '/data/msp-site'

for filename in files_to_update:
    filepath = os.path.join(cwd, filename)
    if not os.path.exists(filepath):
        print(f"[!] File not found: {filename}")
        continue
        
    with open(filepath, 'r') as f:
        content = f.read()

    # Meta keywords
    content = content.replace(
        '<meta name="keywords" content="managed IT services Canada, IT support small business, MSP Canada, flat rate IT support, outsourced IT Toronto" />',
        keywords_map[filename]
    )

    # Twitter title
    content = content.replace(
        '<meta name="twitter:title" content="Trueline IT | Managed IT Services for Small Business in Canada" />',
        '<meta name="twitter:title" content="Trueline IT | AI Governance & Automation for Professional Services" />'
    )

    # Search for exactly `<title>Managed IT Services [City] | Flat-Rate Support | Trueline IT</title>` or variant
    content = re.sub(
        r'<title>Managed IT Services [^<]+<\/title>', 
        titles_map[filename], 
        content
    )

    # Try to grab the OG title
    content = re.sub(
        r'<meta property="og:title" content="Managed IT Services [^"]+" \/>',
        og_title_map[filename],
        content
    )

    # Schema Replacements
    content = content.replace('"serviceType": "Managed IT Services"', '"serviceType": "AI Governance and Automation"')
    content = content.replace('"name": "Managed IT Services"', '"name": "AI Governance and Automation"')
    content = content.replace('"name": "Managed IT Support"', '"name": "AI Governance"')
    content = content.replace('"unitText": "per user per month"', '"unitText": "per business per month"') # Used per business due to previous rule changing firm to business
    content = content.replace('"unitText": "per firm per month"', '"unitText": "per business per month"')

    # Pricing in FAQ
    content = re.sub(
        r'>Basic \$99\/user\/month, Professional \$149\/user\/month, Enterprise \$199\/user\/month[^<]+<',
        '>Foundation $1,500/month, Growth $2,500/month, Transform $4,500/month — flat fee per business, not per user.<',
        content
    )
    content = re.sub(
        r'>\$99\/user\/month.*?\$199\/user\/month.*?<',
        '>Foundation $1,500/month, Growth $2,500/month, Transform $4,500/month — flat fee per business, not per user.<',
        content
    )

    # Body Content Replacements
    content = content.replace(
        '<p>You\'ve heard the horror stories — ransomware, phishing, stolen data. You don\'t know if it could happen to you, and honestly, you don\'t know who to ask.</p>',
        '<p>Your team is using AI tools with client data right now. In May 2026, Canada\'s Privacy Commissioner ruled that ChatGPT violated PIPEDA. The Law Society of Ontario has warned lawyers about disciplinary action. Most businesses have no policy in place and no idea what data has already left the building.</p>'
    )
    
    content = content.replace('<li>Unlimited helpdesk support — call, email, or chat</li>', '<li>AI Acceptable Use Policy — created, maintained, and updated</li>')
    content = content.replace('<li>Automated backups &amp; disaster recovery</li>', '<li>Shadow AI audit — full visibility into what tools your team is using</li>')
    content = content.replace('<li>Unlimited helpdesk support</li>', '<li>AI Acceptable Use Policy maintained</li>')
    content = content.replace('<li>Automated backups</li>', '<li>Quarterly shadow AI audit</li>')
    
    content = content.replace('$99<span> / user / mo</span>', '$1,500<span> / mo</span>')
    content = content.replace('$149<span> / user / mo</span>', '$2,500<span> / mo</span>')
    content = content.replace('$199<span> / user / mo</span>', '$4,500<span> / mo</span>')
    
    content = content.replace('<p class="offer-price-note">Everything included. No hidden fees.</p>', '<p class="offer-price-note">For businesses with 15–30 employees.</p>')
    content = content.replace('<p class="offer-price-note">Everything in Basic, plus:</p>', '<p class="offer-price-note">For businesses with 30–75 employees.</p>')
    content = content.replace('<p class="offer-price-note">Everything in Professional, plus:</p>', '<p class="offer-price-note">For businesses with 75–150 employees.</p>')

    with open(filepath, 'w') as f:
        f.write(content)
        
    print(f"[+] Processed: {filename}")

