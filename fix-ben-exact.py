import re
import os

files_to_update = [
    "managed-it-services-burlington.html",
    "managed-it-services-hamilton.html",
    "managed-it-services-guelph.html",
    "managed-it-services-waterloo.html",
    "managed-it-services-cambridge.html",
    "managed-it-services-kitchener-waterloo.html"
]

cwd = '/data/msp-site'

pain_replacement = """<!-- PAIN POINTS -->
<section class="pain">
 <div class="pain-inner">
 <p class="section-label">Sound familiar?</p>
 <h2 class="section-title">The call you're dreading has already happened at another business.</h2>
 <p class="section-sub">Most professional services businesses have no AI policy, no visibility into what tools their team is using, and no idea how much client data has already left the building. Here's what managing partners tell us every week.</p>
 <div class="pain-grid">
 <div class="pain-card">
 <span class="pain-icon">⚠️</span>
 <h3>"My team is using ChatGPT with client data and I found out by accident."</h3>
 <p>Employees paste contracts, financials, and client notes into public AI tools every day. You didn't authorize it. You don't know how much has already left the building.</p>
 </div>
 <div class="pain-card">
 <span class="pain-icon">📋</span>
 <h3>"My cyber insurer sent a renewal form asking about AI governance. I don't have answers."</h3>
 <p>Insurers are now asking which AI tools your team uses, what policies are in place, and who is responsible. Businesses that can't answer are seeing premiums rise — or claims denied.</p>
 </div>
 <div class="pain-card">
 <span class="pain-icon">😟</span>
 <h3>"A client asked me directly: what is your AI data handling policy?"</h3>
 <p>You didn't have a good answer. Neither does most of your competition — yet. The businesses that get ahead of this question will win the clients who ask it.</p>
 </div>
 </div>
 </div>
</section>
"""

ibm_stat = r'<strong>76% of employees admit to using unauthorized AI tools at work.</strong> Most of their managers don\'t know. — IBM Institute for Business Value, 2025'

for filename in files_to_update:
    filepath = os.path.join(cwd, filename)
    if not os.path.exists(filepath):
        print(f"[!] NOT FOUND: {filename}")
        continue
        
    with open(filepath, 'r') as f:
        content = f.read()

    # Find the comment <!-- PAIN POINTS --> or <!-- PAIN --> and replace until the next <!--
    content = re.sub(
        r'<!--\s*(PAIN POINTS|PAIN)\s*-->.*?(?=\n<!--)', 
        pain_replacement.rstrip(),
        content, 
        flags=re.DOTALL | re.IGNORECASE
    )

    # Stat bar
    # "replace the stat bar paragraph with: <strong>76%..."
    content = re.sub(
        r'(<!--\s*STAT BAR\s*-->.*?<div class="hero-proof">.*?<p>).*?(</p>\s*</div>)',
        f'\\g<1>{ibm_stat}\\g<2>',
        content,
        flags=re.DOTALL | re.IGNORECASE
    )

    # How it works section
    content = re.sub(
        r'(<!--\s*HOW.*?<[a-z0-9]+ class="section-label"[^>]*>).*?(</[a-z0-9]+>)',
        r'\g<1>How it works\g<2>',
        content,
        flags=re.DOTALL | re.IGNORECASE
    )
    # Target only the title inside the HOW section
    how_match = re.search(r'(<!--\s*HOW.*?)(<!--)', content, re.DOTALL | re.IGNORECASE)
    if how_match:
        how_section = how_match.group(1)
        how_section = re.sub(r'(<h2 class="section-title"[^>]*>).*?(</h2>)', r'\g<1>From exposure to protected in 30 days.\g<2>', how_section)
        how_section = re.sub(r'(<p class="section-sub"[^>]*>).*?(</p>)', r'\g<1>We\'ve removed every barrier. Most businesses have their AI governance foundation in place within 30 days.\g<2>', how_section)
        # Step 2
        how_section = re.sub(r'(<div class="step-num">2</div>.*?<h3>).*?(</h3>.*?<p>).*?(</p>)', r'\g<1>We run your AI Risk Audit\g<2>We identify every AI tool in use, assess your data exposure, and build your AI Acceptable Use Policy. Delivered in plain English — ready for your insurer, your regulator, and your clients.\g<3>', how_section, flags=re.DOTALL)
        # Step 3
        how_section = re.sub(r'(<div class="step-num">3</div>.*?<h3>).*?(</h3>.*?<p>).*?(</p>)', r'\g<1>We manage it ongoing\g<2>Policy updates as regulations change. New automations built on schedule. Monthly reporting. You get back to running your business with one answer ready: we have this handled.\g<3>', how_section, flags=re.DOTALL)
        
        content = content[:how_match.start(1)] + how_section + content[how_match.end(1):]

    # Stats section
    stat_match = re.search(r'(<!--\s*STAT(?:S[ -]SECTION)?[ -].*?)(<!--)', content, re.DOTALL | re.IGNORECASE)
    if stat_match:
        stat_section = stat_match.group(1)
        stat_section = re.sub(r'(<h2 class="section-title"[^>]*>).*?(</h2>)', r'\g<1>Numbers we stand behind.\g<2>', stat_section)
        
        def insert_stat2(m):
            return f'{m.group(1)}<div class="stat-number">100%</div>\n      <div class="stat-label">AI policy coverage</div>\n      <div class="stat-desc">Every client gets a documented AI acceptable use policy on day one</div>\n    </div>'

        stat_section = re.sub(
            r'(<div class="stats-grid">\s*<div class="stat-card">.*?</div>\s*<div class="stat-card">\s*)<div class="stat-number">.*?</div>\s*<div class="stat-label">.*?</div>\s*<div class="stat-desc">.*?</div>\s*(?:</div>)',
            insert_stat2,
            stat_section,
            flags=re.DOTALL
        )
        content = content[:stat_match.start(1)] + stat_section + content[stat_match.end(1):]


    # FAQ section label and title
    faq_match = re.search(r'(<!--\s*FAQ.*?)(<!--)', content, re.DOTALL | re.IGNORECASE)
    if faq_match:
        faq_section = faq_match.group(1)
        faq_section = re.sub(r'(<[a-z]+ class="(?:section-label|section-label text-center)"[^>]*>).*?(</[a-z]+>)', r'\g<1>Common questions\g<2>', faq_section)
        faq_section = re.sub(r'(<h2 class="section-title|h2 class="(?:section-title|section-title text-center)"[^>]*>).*?(</h2>)', r'\g<1>You\'ve probably got questions.\g<2>', faq_section)
        content = content[:faq_match.start(1)] + faq_section + content[faq_match.end(1):]

    with open(filepath, 'w') as f:
        f.write(content)
        
    print(f"[+] Processed cleanly: {filename}")

