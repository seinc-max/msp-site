import os
import re

files_to_update = [
    "managed-it-services-burlington.html",
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

    # FIX 0: Hero h1
    content = re.sub(
        r'<h1>.*?</h1>',
        '<h1>Your team is using AI with client data.<br>One mistake can cost you <em>everything.</em></h1>',
        content, count=1, flags=re.DOTALL
    )

    # FIX 1: Nav CTA
    content = content.replace(
        '<a href="#contact" class="nav-cta">Book a Discovery Call</a>',
        '<a href="#contact" class="nav-cta">Book My Free Discovery Call</a>'
    )
    
    # FIX 2: Hero sub pricing reference
    content = content.replace(
        ' — starting at $1,500/mo.</p>',
        ' — for a flat monthly fee.</p>'
    )
    
    # FIX 3: Stat bar
    # Find any strong tag inside the hero-proof div and replace the paragraph
    content = re.sub(
        r'<div class="hero-proof">.*?<p>.*?</p>.*?</div>',
        '<div class="hero-proof">\n      <p><strong>76% of employees admit to using unauthorized AI tools at work.</strong> Most of their managers don\'t know. — IBM Institute for Business Value, 2025</p>\n    </div>',
        content, flags=re.DOTALL
    )

    # FIX 4: Pain section label
    content = re.sub(
        r'<div class="section-label">The.*?Reality</div>',
        '<div class="section-label">Sound familiar?</div>',
        content
    )
    # Generic catch-all for pain section label if it was different
    content = re.sub(
        r'(<section[^>]*id="pain"[^>]*>.*?<div class="container">.*?<div class="section-label">)(.*?)(</div>)',
        r'\1Sound familiar?\3',
        content, count=1, flags=re.DOTALL
    )

    # FIX 5: Pain section title
    content = re.sub(
        r'(<section[^>]*id="pain"[^>]*>.*?<h2 class="section-title">)(.*?)(</h2>)',
        r'\1The call you\'re dreading has already happened at another business.\3',
        content, count=1, flags=re.DOTALL
    )

    # FIX 6: Pain section sub
    content = re.sub(
        r'(<section[^>]*id="pain"[^>]*>.*?<p class="section-sub">)(.*?)(</p>)',
        r'\1Most professional services businesses have no AI policy, no visibility into what tools their team is using, and no idea how much client data has already left the building. Here\'s what managing partners tell us every week.\3',
        content, count=1, flags=re.DOTALL
    )

    # FIX 7: Pain card icons
    content = content.replace('<span class="pain-icon">🔥</span>', '<span class="pain-icon">⚠️</span>')
    content = content.replace('<span class="pain-icon">💸</span>', '<span class="pain-icon">📋</span>')
    
    # FIX 8 & 9: Pain card content
    # First we match the cards wrapper
    cards_match = re.search(r'(<div class="pain-cards">)(.*?)(</div>\s*</section>)', content, re.DOTALL)
    if cards_match:
        cards_html = cards_match.group(2)
        
        # Replace card 1 (warning icon used to be fire)
        cards_html = re.sub(
            r'(<div class="pain-card">.*?<span class="pain-icon">⚠️</span>.*?<h3>)(.*?)(</h3>.*?<p>)(.*?)(</p>.*?</div>)',
            r'\1"My team is using ChatGPT with client data and I found out by accident."\3Employees paste contracts, financials, and client notes into public AI tools every day. You didn\'t authorize it. You don\'t know how much has already left the building.\5',
            cards_html, count=1, flags=re.DOTALL
        )
        
        # Replace card 2 (clipboard icon used to be money)
        cards_html = re.sub(
            r'(<div class="pain-card">.*?<span class="pain-icon">📋</span>.*?<h3>)(.*?)(</h3>.*?<p>)(.*?)(</p>.*?</div>)',
            r'\1"My cyber insurer sent a renewal form asking about AI governance. I don\'t have answers."\3Insurers are now asking which AI tools your team uses, what policies are in place, and who is responsible. Businesses that can\'t answer are seeing premiums rise — or claims denied.\5',
            cards_html, count=1, flags=re.DOTALL
        )
        
        content = content[:cards_match.start(2)] + cards_html + content[cards_match.end(2):]

    # FIX 10: Offer section sub
    content = re.sub(
        r'(<section[^>]*id="pricing"[^>]*>.*?<p class="section-sub">)(.*?)(</p>)',
        r'\1No per-seat billing. No surprise invoices. Every plan includes a documented AI Acceptable Use Policy, shadow AI audit, and ongoing compliance management. Automation builds included from Growth tier.\3',
        content, count=1, flags=re.DOTALL
    )

    with open(filepath, 'w') as f:
        f.write(content)
        
    print(f"[+] Applied fixes 0-10 on {filename}")

