with open('/opt/data/msp-site/ai-exposure-score.html', 'r') as f:
    template_html = f.read()

# Replace SEO and Meta Titles
template_html = template_html.replace(
    '<title>AI Exposure Risk Score & Readiness Audit | Trueline IT</title>',
    '<title>2026 AI Privacy Risk Assessment | Trueline IT</title>'
)
template_html = template_html.replace(
    'content="Free AI exposure and automation readiness diagnostic for Ontario professionals. Find out your company\'s Shadow AI risk score in 3 minutes."',
    'content="Ontario professional services businesses: Calculate your Shadow AI liability under OPC rulings and Law Society guidelines."'
)

# Extract standard Header and Base
header_split = template_html.split('<!-- HERO -->')
base_html = header_split[0]
remaining_html = header_split[1]

# Rebuild the Page Content using Exact Native Classes
new_content = """<!-- HERO -->
<section class="hero" style="padding-bottom: 40px;">
  <div class="hero-inner">
    <div class="hero-pre" style="background: rgba(249,115,22,0.2); color: var(--orange); border: 1px solid rgba(249,115,22,0.3);">
      URGENT FOR ONTARIO BUSINESSES
    </div>
    <h1>Stop the Bleeding: Find Your<br><em>"Shadow AI"</em> Liability Score</h1>
    <p class="hero-sub" style="margin-bottom: 20px;">
      The Office of the Privacy Commissioner has explicitly ruled on unauthorized AI use under PIPEDA. The Law Society of Ontario is warning about client privilege.<br><br>
      <strong>If you don't have a documented AI policy, cyber insurers treat you as a high-risk liability.</strong>
    </p>
    <div class="hero-trust" style="margin-top: 20px;">
      <div class="trust-item">
        <svg fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path></svg>
        Based on 2026 OPC Rulings
      </div>
      <div class="trust-item">
        <svg fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path></svg>
        100% Confidential
      </div>
    </div>
  </div>
</section>

<!-- PAIN / FORM SECTION -->
<section class="pain" style="padding-top: 50px;">
  <div style="max-width: 1100px; margin: -100px auto 0; position: relative; z-index: 10; display: grid; grid-template-columns: 1.8fr 1.2fr; gap: 0; background: #fff; border-radius: 16px; box-shadow: 0 20px 50px -12px rgba(0,0,0,0.1); border: 1px solid var(--border); overflow: hidden;">
    
    <!-- LEFT: THE AUDIT FORM -->
    <div style="padding: 40px 50px;">
      <div id="form-container">
        <h2 style="font-family: 'Fraunces', serif; font-size: 1.8rem; color: var(--navy); margin-bottom: 8px;">Confidential Audit</h2>
        <p style="color: var(--text-muted); font-size: 0.95rem; margin-bottom: 30px; border-bottom: 1px solid var(--border); padding-bottom: 20px;">Answer honestly. We never share this data.</p>
        
        <form id="risk-assessment-form">
          <div class="form-group" style="margin-bottom: 30px;">
            <label style="display: block; font-size: 1.05rem; font-weight: 700; color: var(--navy); margin-bottom: 8px;">1. Does your business currently have a formally documented AI Acceptable Use Policy signed by all employees?</label>
            <p style="font-size: 0.85rem; color: var(--text-muted); margin-bottom: 12px;">Insurers look for a paper trail proving you attempted to govern staff.</p>
            <div style="display: flex; flex-direction: column; gap: 10px;">
              <label style="display: flex; align-items: flex-start; gap: 12px; padding: 16px; border: 1px solid var(--border); border-radius: 8px; cursor: pointer;">
                <input type="radio" name="q1" value="Yes - Updated" required style="margin-top: 4px;">
                <span style="color: var(--text); font-weight: 500;">Yes, active and updated within the last 12 months.</span>
              </label>
              <label style="display: flex; align-items: flex-start; gap: 12px; padding: 16px; border: 1px solid #fecaca; background: #fef2f2; border-radius: 8px; cursor: pointer;">
                <input type="radio" name="q1" value="No / Drafting" required style="margin-top: 4px;">
                <span style="color: #991b1b; font-weight: 500;">No, or we are drafting one now. (Warning: High Liability)</span>
              </label>
            </div>
          </div>

          <div class="form-group" style="margin-bottom: 30px;">
            <label style="display: block; font-size: 1.05rem; font-weight: 700; color: var(--navy); margin-bottom: 8px;">2. To your knowledge, have employees ever used a free-tier public AI (like ChatGPT, Gemini) to summarize documents, draft emails, or analyze spreadsheets?</label>
            <p style="font-size: 0.85rem; color: var(--text-muted); margin-bottom: 12px;">Free-tier tools train their models on your inputs, breaching confidentiality.</p>
            <div style="display: flex; flex-direction: column; gap: 10px;">
              <label style="display: flex; align-items: flex-start; gap: 12px; padding: 16px; border: 1px solid #fecaca; background: #fef2f2; border-radius: 8px; cursor: pointer;">
                <input type="radio" name="q2" value="Yes" required style="margin-top: 4px;">
                <span style="color: #991b1b; font-weight: 500;">Yes, I am aware this happens.</span>
              </label>
              <label style="display: flex; align-items: flex-start; gap: 12px; padding: 16px; border: 1px solid #fed7aa; background: #fff7ed; border-radius: 8px; cursor: pointer;">
                <input type="radio" name="q2" value="Likely" required style="margin-top: 4px;">
                <span style="color: #9a3412; font-weight: 500;">I'm not sure, but it is highly likely.</span>
              </label>
              <label style="display: flex; align-items: flex-start; gap: 12px; padding: 16px; border: 1px solid var(--border); border-radius: 8px; cursor: pointer;">
                <input type="radio" name="q2" value="No - Blocked" required style="margin-top: 4px;">
                <span style="color: var(--text); font-weight: 500;">Absolutely not. We have technical network blocks in place.</span>
              </label>
            </div>
          </div>

          <div class="form-group" style="margin-bottom: 30px;">
            <label style="display: block; font-size: 1.05rem; font-weight: 700; color: var(--navy); margin-bottom: 8px;">3. Have you updated your client privacy notices to explicitly disclose the use of AI in your business workflows?</label>
            <p style="font-size: 0.85rem; color: var(--text-muted); margin-bottom: 12px;">OPC mandates generic "tech tool" clauses do not equal Meaningful Consent.</p>
            <div style="display: flex; flex-direction: column; gap: 10px;">
              <label style="display: flex; align-items: flex-start; gap: 12px; padding: 16px; border: 1px solid var(--border); border-radius: 8px; cursor: pointer;">
                <input type="radio" name="q3" value="Yes - Explicit" required style="margin-top: 4px;">
                <span style="color: var(--text); font-weight: 500;">Yes, our engagements explicitly outline AI usage limitations.</span>
              </label>
              <label style="display: flex; align-items: flex-start; gap: 12px; padding: 16px; border: 1px solid #fecaca; background: #fef2f2; border-radius: 8px; cursor: pointer;">
                <input type="radio" name="q3" value="No - Implicit" required style="margin-top: 4px;">
                <span style="color: #991b1b; font-weight: 500;">No, we have not specifically addressed AI yet.</span>
              </label>
            </div>
          </div>

          <div style="background: var(--sky); padding: 30px; border-radius: 12px; margin-top: 40px;">
            <h3 style="font-family: 'Fraunces', serif; font-size: 1.3rem; color: var(--navy); margin-bottom: 10px;">Request Your Incident Report</h3>
            <p style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 20px;">Enter your details below. Your custom report warns exactly what your cyber insurer and regulators demand in 2026.</p>
            
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-bottom: 20px;">
              <div class="form-group" style="margin-bottom: 0;">
                <label>Work Email *</label>
                <input type="email" required id="work-email" placeholder="owner@business.ca">
              </div>
              <div class="form-group" style="margin-bottom: 0;">
                <label>Business Size</label>
                <select id="business-size">
                  <option value="1-14 Employees">1-14 Employees</option>
                  <option value="15-50 Employees">15-50 Employees</option>
                  <option value="51-150 Employees">51-150 Employees</option>
                </select>
              </div>
            </div>
            
            <button type="submit" id="submit-btn" class="btn-primary" style="width: 100%; text-align: center;">Book My Free Discovery Call &rarr;</button>
            <p style="font-size: 0.75rem; color: var(--text-muted); text-align: center; margin-top: 15px;">By generating a score, you consent to Trueline IT securely processing this data.</p>
          </div>
        </form>
      </div>

      <div id="success-container" style="display: none; text-align: center; padding: 60px 0;">
        <svg style="width: 60px; height: 60px; color: #10b981; margin: 0 auto 20px;" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
        <h2 style="font-family: 'Fraunces', serif; font-size: 2rem; color: var(--navy); margin-bottom: 15px;">Risk Audit Received</h2>
        <p style="color: var(--text-muted); font-size: 1.05rem;">We are processing your answers against current PIPEDA and regulator frameworks. We will reach out momentarily.</p>
      </div>
    </div>

    <!-- RIGHT: SOCIAL PROOF / WHY -->
    <div style="background: var(--warm-white); border-left: 1px solid var(--border); padding: 40px 35px;">
      <h3 class="section-label" style="margin-bottom: 30px;">Why Take The Audit?</h3>
      
      <div style="display: flex; flex-direction: column; gap: 30px;">
        <div>
          <h4 style="font-weight: 700; color: var(--navy); font-size: 1.05rem; display: flex; align-items: center; gap: 8px;">
            <svg style="width: 20px; height: 20px; color: #ef4444;" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"></path></svg>
            The OPC Ruling
          </h4>
          <p style="color: var(--text-muted); font-size: 0.9rem; margin-top: 6px;">In May 2026, the Office of the Privacy Commissioner ruled that unmanaged ChatGPT usage violates PIPEDA and Quebec Law 25 confidentiality laws.</p>
        </div>

        <div>
          <h4 style="font-weight: 700; color: var(--navy); font-size: 1.05rem; display: flex; align-items: center; gap: 8px;">
            <svg style="width: 20px; height: 20px; color: var(--blue);" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"></path></svg>
            Insurance Renewals
          </h4>
          <p style="color: var(--text-muted); font-size: 0.9rem; margin-top: 6px;">Cyber insurers now explicitly deny coverage to businesses lacking a documented AI Acceptable Use Policy in the event of an AI leak.</p>
        </div>

        <div>
          <h4 style="font-weight: 700; color: var(--navy); font-size: 1.05rem; display: flex; align-items: center; gap: 8px;">
            <svg style="width: 20px; height: 20px; color: var(--orange);" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"></path></svg>
            Law Society Warnings
          </h4>
          <p style="color: var(--text-muted); font-size: 0.9rem; margin-top: 6px;">The LSO warns that using free public AI tools with client data is a breach of privilege. You are responsible for your staff's tools.</p>
        </div>
      </div>

      <div style="margin-top: 40px; padding: 25px 20px; background: rgba(37,99,235,0.05); border: 1px solid var(--border); border-radius: 8px;">
        <p style="color: var(--text); font-size: 0.9rem; font-style: italic; margin-bottom: 12px;">"We thought our staff knew better than to put client PDFs into ChatGPT. The audit Trueline ran proved otherwise. Getting the formalized policy in place saved our cyber renewal."</p>
        <p style="color: var(--navy); font-size: 0.8rem; font-weight: 700;">&mdash; Managing Partner, Toronto Business</p>
      </div>
    </div>

  </div>
</section>
"""

# Extract the footer and the remaining scripts from base
footer_split = remaining_html.split('<!-- FOOTER -->')
new_page = base_html + new_content + '<!-- FOOTER -->' + footer_split[1]

# Inject the Native HubSpot Logic just before the closing </body> tag
hs_logic = """
<script>
  document.getElementById('risk-assessment-form')?.addEventListener('submit', async function(e) {
      e.preventDefault();
      const form = e.target;
      const btn = document.getElementById('submit-btn');
      
      const q1 = form.querySelector('input[name="q1"]:checked')?.value || '';
      const q2 = form.querySelector('input[name="q2"]:checked')?.value || '';
      const q3 = form.querySelector('input[name="q3"]:checked')?.value || '';
      const email = document.getElementById('work-email').value;
      const firmSize = document.getElementById('business-size').value;
      
      btn.disabled = true;
      btn.innerText = 'Processing Audit...';

      const payload = {
          fields: [
              { name: 'email', value: email },
              { name: 'company_size', value: firmSize },
              { name: 'ai_policy_status', value: q1 },
              { name: 'shadow_ai_usage', value: q2 },
              { name: 'client_data_consent', value: q3 },
              { name: 'hubspot_owner_id', value: '89556230' }
          ]
      };

      try {
          const res = await fetch('https://api.hsforms.com/submissions/v3/integration/submit/343087614/e66cbddb-8b74-4166-ab13-6ea81df11466', {
              method: 'POST',
              headers: { 'Content-Type': 'application/json' },
              body: JSON.stringify(payload)
          });
          
          if (res.ok) {
              document.getElementById('form-container').style.display = 'none';
              document.getElementById('success-container').style.display = 'block';
          } else {
              btn.disabled = false;
              btn.innerText = 'Book My Free Discovery Call →';
              alert('There was a server issue submitting your audit. Please try again.');
          }
      } catch (err) {
          btn.disabled = false;
          btn.innerText = 'Book My Free Discovery Call →';
          alert('Connection error. Please try again.');
      }
  });
</script>
"""
new_page = new_page.replace('</body>', hs_logic + '</body>')

with open('/opt/data/msp-site/risk-assessment.html', 'w') as f:
    f.write(new_page)

print("Rewrite complete.")
