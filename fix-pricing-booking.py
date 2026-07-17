import re

with open('/opt/data/msp-site/ai-consulting-pricing.html', 'r') as f:
    html = f.read()

# Fix the booking links
# Currently the buttons just jump to the bottom of the page (#contact) and open a generic "mailto:" link.
# A true conversion trap must go to a friction-less booking flow (HubSpot Meetings).

# Replace the Nav button
html = html.replace('<a href="#contact" class="nav-cta">Book My Free Discovery Call</a>', '<a href="https://meetings-na3.hubspot.com/ben-trueline" target="_blank" class="nav-cta">Book My Free Discovery Call &rarr;</a>')

# Replace the Pricing Card buttons
html = html.replace('<a href="#contact" class="cta-btn cta-outline w-full cursor-pointer">Book My Free Discovery Call &rarr;</a>', '<a href="https://meetings-na3.hubspot.com/ben-trueline" target="_blank" class="cta-btn cta-outline w-full cursor-pointer">Book My Free Discovery Call &rarr;</a>')
html = html.replace('<a href="#contact" class="cta-btn w-full cursor-pointer">Book My Free Discovery Call &rarr;</a>', '<a href="https://meetings-na3.hubspot.com/ben-trueline" target="_blank" class="cta-btn w-full cursor-pointer">Book My Free Discovery Call &rarr;</a>')

# Replace the Bottom CTA
html = html.replace('<a id="contact" href="mailto:hello@truelineit.com" class="cta-btn cursor-pointer">Book My Free Discovery Call &rarr;</a>', '<a id="contact" href="https://meetings-na3.hubspot.com/ben-trueline" target="_blank" class="cta-btn cursor-pointer">Book My Free Discovery Call &rarr;</a>')

with open('/opt/data/msp-site/ai-consulting-pricing.html', 'w') as f:
    f.write(html)
