import re

guelph_file = '/data/msp-site/managed-it-services-guelph.html'
burlington_file = '/data/msp-site/managed-it-services-burlington.html'

with open(guelph_file, 'r') as f:
    guelph_content = f.read()

with open(burlington_file, 'r') as f:
    master_content = f.read()
    
# Specifically replace the hero-sub in Guelph to match the others but keep its FAQ
old_hero_sub_guelph = "Guelph continues to expand with over 3,800+ local businesses. The silent risk is that 68% of employees in professional service sectors are actively feeding client information into unapproved AI tools behind their employer’s back right now. Trueline establishes your AI policies, audits shadow systems, and trains your team on secure AI."
new_hero_sub = "In May 2026, Canada's Privacy Commissioner ruled that ChatGPT violated PIPEDA. The Law Society of Ontario has warned lawyers that using public AI tools with client data risks disciplinary action. Your team is doing it right now. Trueline IT gives your Guelph business a documented AI policy, safe tools, and verifiable compliance — starting at $1,500/mo."

guelph_content = guelph_content.replace(old_hero_sub_guelph, new_hero_sub)

# Also fix the hero-pre to match exactly
guelph_content = guelph_content.replace(
    '<div class="hero-pre">AI Governance & Automation for Guelph Businesses</div>',
    '<div class="hero-pre">AI Governance for Guelph</div>'
)

# Fix southern ontario parent page hero-sub (which was caught in my grep and still had MSP language)
southern_ontario_file = '/data/msp-site/managed-it-services-southern-ontario.html'
with open(southern_ontario_file, 'r') as f:
    so_content = f.read()
    
old_so_hero = "Stop managing IT yourself. In our 2026 assessment of 20 Southern Ontario businesses, 78% operated with no IT monitoring, no verified backups, and no after-hours support — exposing them to $8,000–$15,000 daily losses. Trueline IT changes that with proactive, flat-rate managed services. 24/7 coverage. Zero surprises. Full compliance included."
new_so_hero = "In May 2026, Canada's Privacy Commissioner ruled that ChatGPT violated PIPEDA. The Law Society of Ontario has warned lawyers that using public AI tools with client data risks disciplinary action. Your team is doing it right now. Trueline IT gives your Southern Ontario business a documented AI policy, safe tools, and verifiable compliance — starting at $1,500/mo."

so_content = so_content.replace(old_so_hero, new_so_hero)

with open(guelph_file, 'w') as f:
    f.write(guelph_content)
    
with open(southern_ontario_file, 'w') as f:
    f.write(so_content)

print("[+] Aligned Guelph and Southern Ontario hero texts.")

