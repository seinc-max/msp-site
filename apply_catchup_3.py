import os

filepath = "/data/msp-site/ai-exposure-score.html"

with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# CHANGE 1
old1 = """<div class="stat-number">&lt; 15 min</div>
      <div class="stat-label">Average response time</div>
      <div class="stat-desc">For all support requests during business hours</div>"""
new1 = """<div class="stat-number">30 days</div>
      <div class="stat-label">To full AI governance</div>
      <div class="stat-desc">From discovery call to documented AI policy, shadow audit, and M365 configuration</div>"""
content = content.replace(old1, new1)

# CHANGE 2
old2 = """<div class="stat-number">99.9%</div>
      <div class="stat-label">Uptime guarantee</div>
      <div class="stat-desc">Proactive monitoring keeps your team online</div>"""
new2 = """<div class="stat-number">100%</div>
      <div class="stat-label">AI policy coverage</div>
      <div class="stat-desc">Every client gets a documented AI acceptable use policy on day one</div>"""
content = content.replace(old2, new2)

# CHANGE 3
old3 = """<p class="offer-card-label">Complete</p>
          <h3>$199<span> / user / mo</span></h3>
          <p class="offer-price-note">Everything in Professional, plus:</p>"""
new3 = """<p class="offer-card-label">Transform</p>
          <h3>$4,500<span> / mo</span></h3>
          <p class="offer-price-note">For businesses with 75–150 employees.</p>"""
content = content.replace(old3, new3)

# CHANGE 4
old4 = """<li>24/7 emergency support</li>
            <li>Advanced threat protection</li>
            <li>Compliance reporting</li>
            <li>Quarterly IT reviews</li>"""
new4 = """<li>Unlimited active automations</li>
            <li>Fractional Chief AI Officer (vCAIO)</li>
            <li>Quarterly partner meeting attendance</li>
            <li>Board-ready AI governance reporting</li>"""
content = content.replace(old4, new4)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Applied files to {filepath}")
