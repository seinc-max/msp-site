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
<section class="pain" id="pain">
  <div class="container">
    <div class="section-label">Sound familiar?</div>
    <h2 class="section-title">The call you're dreading has already happened at another business.</h2>
    <p class="section-sub">Most professional services businesses have no AI policy, no visibility into what tools their team is using, and no idea how much client data has already left the building. Here's what managing partners tell us every week.</p>
    <div class="pain-cards">
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

    # 1. Pain points replacement
    # Using regex to find the section between <!-- PAIN POINTS --> or <!-- PAIN --> and the next <!-- comment
    content = re.sub(
        r'<!--\s*(PAIN POINTS|PAIN)\s*-->.*?(?=\n<!--)', 
        pain_replacement.rstrip(),
        content, 
        flags=re.DOTALL | re.IGNORECASE
    )

    # 2. Stat bar paragraph
    content = re.sub(
        r'(<div class="hero-proof">.*?<p>).*?(</p>.*?</div>)',
        f'\\1{ibm_stat}\\2',
        content,
        flags=re.DOTALL
    )

    # 3. How section
    # Label, h2, sub
    content = re.sub(
        r'(<!--\s*HOW.*?(section-label|div class="section-label">)).*?(</.+?>\s*<h2.*?>).*?(</h2>\s*<p class="section-sub">).*?(</p>)',
        r'\1How it works\3From exposure to protected in 30 days.\4We\'ve removed every barrier. Most businesses have their AI governance foundation in place within 30 days.\5',
        content,
        flags=re.DOTALL | re.IGNORECASE
    )
    
    
    content = re.sub(
        r'(<div class="step-num">2</div>.*?<h3>).*?(</h3>.*?<p>).*?(</p>)',
        r'\1We run your AI Risk Audit\2We identify every AI tool in use, assess your data exposure, and build your AI Acceptable Use Policy. Delivered in plain English — ready for your insurer, your regulator, and your clients.\3',
        content,
        flags=re.DOTALL
    )

    content = re.sub(
        r'(<div class="step-num">3</div>.*?<h3>).*?(</h3>.*?<p>).*?(</p>)',
        r'\1We manage it ongoing\2Policy updates as regulations change. New automations built on schedule. Monthly reporting. You get back to running your business with one answer ready: we have this handled.\3',
        content,
        flags=re.DOTALL
    )

    # 4. Stats section
    content = re.sub(
        r'(<!--\s*STAT.*?(section-title|h2 class="section-title">)).*?(</h2>)',
        r'\1Numbers we stand behind.\3',
        content,
        flags=re.DOTALL | re.IGNORECASE
    )
    
    def repl_stat2(m):
        return f'{m.group(1)}<div class="stat-number">100%</div>\n      <div class="stat-label">AI policy coverage</div>\n      <div class="stat-desc">Every client gets a documented AI acceptable use policy on day one</div>\n    </div>'
    
    # Matches the second card specifically by looking for the second <div class="stat-card"> after stats-grid
    content = re.sub(
        r'(<div class="stats-grid">\s*<div class="stat-card">.*?</div>\s*<div class="stat-card">\s*)<div class="stat-number">.*?</div>\s*<div class="stat-label">.*?</div>\s*<div class="stat-desc">.*?</div>\s*</div>',
        repl_stat2,
        content,
        flags=re.DOTALL
    )

    # 5. FAQ section
    content = re.sub(
        r'(<!--\s*FAQ.*?<.*?class="section-label"[^>]*>).*?(</[a-z]+>\s*<h2[^>]*>).*?(</h2>)',
        r'\1Common questions\2You\'ve probably got questions.\3',
        content,
        flags=re.DOTALL | re.IGNORECASE
    )

    with open(filepath, 'w') as f:
        f.write(content)
        
    print(f"[+] Processed: {filename}")

