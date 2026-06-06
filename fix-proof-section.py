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

old_proof_section_pattern = r'<section class="proof">.*?</section>'

new_proof_section = """<section class="proof">
  <div class="text-center">
    <p class="section-label">What clients say</p>
    <h2 class="section-title">Real businesses. Real results.</h2>
    <p class="section-sub">Professional services businesses across Southern Ontario.</p>
  </div>
  <div class="testimonials">
    <div class="testimonial">      <div class="stars">★★★★★</div>
      <blockquote>"We were using ChatGPT for patient communications without realizing the privacy risk. Trueline flagged it, fixed it, and set up a proper policy in a week. We sleep better now."</blockquote>
      <p class="testimonial-author">Sarah M. <span>— Managing Partner, Maple Ridge Medical Group</span></p>
    </div>
    <div class="testimonial">      <div class="stars">★★★★★</div>
      <blockquote>"Trueline automated our client follow-up and it saved my team 6 hours a week. The flat rate makes it easy to justify to the partners."</blockquote>
      <p class="testimonial-author">James T. <span>— COO, Northside Advisory Group</span></p>
    </div>
    <div class="testimonial">      <div class="stars">★★★★★</div>
      <blockquote>"As a financial services business we had real concerns about AI compliance. Trueline assessed our exposure, built our AI use policy, and now manages everything. One less thing to worry about."</blockquote>
      <p class="testimonial-author">Priya K. <span>— Director, Clearview Financial Services</span></p>
    </div>
  </div>
  <div class="partners">
    <!-- Microsoft -->
    <div class="partner-item" title="Microsoft">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 23 23" width="40" height="40">
        <rect x="1" y="1" width="10" height="10" fill="#f25022"/>
        <rect x="12" y="1" width="10" height="10" fill="#7fba00"/>
        <rect x="1" y="12" width="10" height="10" fill="#00a4ef"/>
        <rect x="12" y="12" width="10" height="10" fill="#ffb900"/>
      </svg>
    </div>
    <!-- Google Workspace -->
    <div class="partner-item" title="Google Workspace">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="38" height="38">
        <path d="M21.8 12.2c0-.7-.1-1.4-.2-2H12v3.8h5.5a4.7 4.7 0 0 1-2 3.1v2.5h3.3c1.9-1.8 3-4.4 3-7.4z" fill="#4285F4"/>
        <path d="M12 22c2.7 0 5-0.9 6.7-2.4l-3.3-2.5c-.9.6-2.1 1-3.4 1-2.6 0-4.8-1.8-5.6-4.1H3v2.6A10 10 0 0 0 12 22z" fill="#34A853"/>
        <path d="M6.4 14c-.2-.6-.3-1.3-.3-2s.1-1.4.3-2V7.4H3A10 10 0 0 0 2 12c0 1.6.4 3.2 1 4.6L6.4 14z" fill="#FBBC05"/>
        <path d="M12 5.9c1.5 0 2.8.5 3.8 1.5l2.8-2.8A10 10 0 0 0 3 7.4L6.4 10c.8-2.3 3-3.9 5.6-4.1z" fill="#EA4335"/>
      </svg>
    </div>
    <!-- OpenAI -->
    <div class="partner-item" title="OpenAI" style="filter: invert(1); opacity: 0.8;">
      <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 2406 2406" width="40" height="40">
        <path d="M1 578.4C1 259.5 259.5 1 578.4 1h1249.1c319 0 577.5 258.5 577.5 577.4V2406H578.4C259.5 2406 1 2147.5 1 1828.6V578.4z" fill="#74aa9c"/>
        <path id="a" d="M1107.3 299.1c-197.999 0-373.9 127.3-435.2 315.3L650 743.5v427.9c0 21.4 11 40.4 29.4 51.4l344.5 198.515V833.3h.1v-27.9L1372.7 604c33.715-19.52 70.44-32.857 108.47-39.828L1447.6 450.3C1361 353.5 1237.1 298.5 1107.3 299.1zm0 117.5-.6.6c79.699 0 156.3 27.5 217.6 78.4-2.5 1.2-7.4 4.3-11 6.1L952.8 709.3c-18.4 10.4-29.4 30-29.4 51.4V1248l-155.1-89.4V755.8c-.1-187.099 151.601-338.9 339-339.2z" fill="#fff"/>
        <use xlink:href="#a" transform="rotate(60 1203 1203)"/>
          <use xlink:href="#a" transform="rotate(120 1203 1203)"/>
        <use xlink:href="#a" transform="rotate(180 1203 1203)"/>
        <use xlink:href="#a" transform="rotate(240 1203 1203)"/>
        <use xlink:href="#a" transform="rotate(300 1203 1203)"/>
      </svg>
    </div>
    <!-- Anthropic -->
    <div class="partner-item" title="Anthropic" style="filter: invert(1); opacity: 0.8; margin-top: -2px;">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 541.36 512" width="46" height="46">
        <path d="M129.21,123.63L234.33,306H109.91L4.79,123.63H129.21ZM308.28,306l105.12-182.37h124.42L367.6,423.86l-59.31-117.86ZM235.34,307.74l96.79,167.64V123.63h-96.79v184.11Z" fill="#000000"/>
      </svg>
    </div>
    <!-- n8n -->
    <div class="partner-item" title="n8n" style="filter: grayscale(1); opacity: 0.6; margin-top: 2px;">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 183 91.135" width="70" height="35">
        <path d="M43.7 85.34a26.685 26.685 0 0 1-13.882-3.8 28.243 28.243 0 0 1-15.61-22.186L12.59 47.78V85.34H.579V5.795H12.59v37.56l1.618-11.574A28.241 28.241 0 0 1 29.818 9.595 26.685 26.685 0 0 1 43.7 5.795c7.098.026 13.9 2.664 19.141 7.424 5.378 4.887 8.441 11.666 8.528 18.868v53.254h-12.01V32.087a15.753 15.753 0 0 0-30.82-5.461L25.337 49.33v36.01h12.01L40.548 64.912a15.751 15.751 0 0 0 14.156-11.688V85.34H43.7z" fill="#000000"/>
        <path d="M72.035 23.364V38.9h4.316a13.342 13.342 0 1 1 0 26.685h-4.316v19.756h-12.01V65.586H55.71v-26.68l4.315-.005V10.155A4.316 4.316 0 0 1 64.34 5.84v17.525h7.694zm-12.011 30.222h16.326a1.332 1.332 0 0 0 0-26.64H60.024v26.64zM108.064 85.34a26.684 26.684 0 0 1-13.883-3.8 28.24 28.24 0 0 1-15.609-22.185l-1.618-11.575V85.34H64.945V5.795h12.01v37.56l1.617-11.574a28.24 28.24 0 0 1 15.61-22.186 26.685 26.685 0 0 1 13.883-3.8c11.758.077 21.678 8.163 24.364 19.851.306 1.307.458 2.643.453 3.987V85.34h-12.01V32.087a15.753 15.753 0 0 0-30.82-5.46L86.85 49.33v36.01h12.011L102.062 64.91a15.75 15.75 0 0 0 14.156-11.687V85.34h-8.154z" fill="#000000"/>
        <path d="M182.42 85.34V32.087a15.753 15.753 0 0 0-30.82-5.461l-3.2 22.703v36.011h12.01l3.202-20.428a15.75 15.75 0 0 0 14.156-11.688V85.34h4.652z" fill="#FC5D65"/>
        <path d="M148.4 26.85v12.05H136.39V5.795H148.4v14.167a28.24 28.24 0 0 1 15.61-22.186 26.685 26.685 0 0 1 18.665.253v11.968a30.297 30.297 0 0 0-4.782-.416c-7.098-.026-13.9 2.614-19.141 7.373-5.378 4.887-8.441 11.666-8.528 18.868L148.4 26.85z" fill="#000000"/>
      </svg>
    </div>
  </div>
</section>"""

for filename in files_to_update:
    filepath = os.path.join(cwd, filename)
    if not os.path.exists(filepath):
        print(f"[!] File not found: {filename}")
        continue
        
    with open(filepath, 'r') as f:
        content = f.read()

    # Find and replace the proofs section using RegEx because of differences in the indentation and content
    matched = re.search(old_proof_section_pattern, content, re.DOTALL)
    if matched:
        content = content[:matched.start()] + new_proof_section + content[matched.end():]
        print(f"[+] Replaced proof section in: {filename}")
    else:
        print(f"[-] Could not find the proof section in: {filename}")
        
    with open(filepath, 'w') as f:
        f.write(content)

