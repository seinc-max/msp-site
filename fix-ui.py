with open('/opt/data/msp-site/risk-assessment.html', 'r') as f:
    html = f.read()

# Fix the structural CSS to ensure grid layouts work on mobile
html = html.replace(
    '<div style="max-width: 1100px; margin: -100px auto 0; position: relative; z-index: 10; display: grid; grid-template-columns: 1.8fr 1.2fr; gap: 0; background: #fff; border-radius: 16px; box-shadow: 0 20px 50px -12px rgba(0,0,0,0.1); border: 1px solid var(--border); overflow: hidden;">',
    '<div class="pain-container" style="max-width: 1100px; margin: -100px auto 0; position: relative; z-index: 10; display: flex; flex-wrap: wrap; background: #fff; border-radius: 16px; box-shadow: 0 20px 50px -12px rgba(0,0,0,0.1); border: 1px solid var(--border); overflow: hidden;">'
)

# Fix the left (form) column width
html = html.replace(
    '<!-- LEFT: THE AUDIT FORM -->\n    <div style="padding: 40px 50px;">',
    '<!-- LEFT: THE AUDIT FORM -->\n    <div style="flex: 1 1 600px; padding: clamp(20px, 5vw, 50px);">'
)

# Fix the right (social proof) column width
html = html.replace(
    '<!-- RIGHT: SOCIAL PROOF / WHY -->\n    <div style="background: var(--warm-white); border-left: 1px solid var(--border); padding: 40px 35px;">',
    '<!-- RIGHT: SOCIAL PROOF / WHY -->\n    <div style="flex: 1 1 350px; background: var(--warm-white); border-left: 1px solid var(--border); padding: clamp(20px, 5vw, 40px);">'
)

# Improve input styling so it doesn't look native/ugly
html = html.replace(
    '<input type="email" required id="work-email" placeholder="owner@business.ca">',
    '<input type="email" required id="work-email" placeholder="owner@business.ca" style="width:100%; padding:14px 16px; border:1.5px solid var(--border); border-radius:8px; font-family:\'DM Sans\',sans-serif; background:#f8fafc; outline:none; transition:0.2s;" onfocus="this.style.borderColor=\'var(--blue)\'; this.style.background=\'#fff\'" onblur="this.style.borderColor=\'var(--border)\'; this.style.background=\'#f8fafc\'">'
)

html = html.replace(
    '<select id="business-size">',
    '<select id="business-size" style="width:100%; padding:14px 16px; border:1.5px solid var(--border); border-radius:8px; font-family:\'DM Sans\',sans-serif; background:#f8fafc; outline:none; transition:0.2s;" onfocus="this.style.borderColor=\'var(--blue)\'; this.style.background=\'#fff\'" onblur="this.style.borderColor=\'var(--border)\'; this.style.background=\'#f8fafc\'">'
)

# Improve radio button hover/states
html = html.replace('cursor: pointer;"', 'cursor: pointer; transition: all 0.2s ease;" onmouseover="this.style.transform=\'translateY(-1px)\'; this.style.boxShadow=\'0 4px 12px rgba(0,0,0,0.05)\'" onmouseout="this.style.transform=\'none\'; this.style.boxShadow=\'none\'"')

with open('/opt/data/msp-site/risk-assessment.html', 'w') as f:
    f.write(html)
