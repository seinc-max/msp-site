import re

with open('/opt/data/msp-site/index.html', 'r') as f:
    master_html = f.read()

style_match = re.search(r'(<style>.*?</style>)', master_html, re.DOTALL)
master_style = style_match.group(1) if style_match else ""
font_match = re.search(r'(<link href="https://fonts\.googleapis\.com/css2[^"]*".*?>)', master_html)
font_link = font_match.group(1) if font_match else ""
nav_match = re.search(r'(<nav>.*?</nav>)', master_html, re.DOTALL)
master_nav = nav_match.group(1) if nav_match else ""
footer_match = re.search(r'(<footer>.*?</footer>)', master_html, re.DOTALL)
master_footer = footer_match.group(1) if footer_match else ""

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Shadow AI Liability Audit | Trueline IT</title>
    <meta name="description" content="Calculate your business's Shadow AI liability exposure under 2026 PIPEDA and Law Society guidelines.">
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="icon" type="image/svg+xml" href="/favicon.svg">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    [FONT_LINK]
    [MASTER_STYLE]
    <style>
        /* Paco Coursey UI / Nielsen UX Extensions */
        .audit-step {
            display: none;
            animation: slideUpFade 0.4s cubic-bezier(0.16, 1, 0.3, 1) forwards;
        }
        .audit-step.active {
            display: block;
        }
        @keyframes slideUpFade {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
        .radio-card {
            border: 1.5px solid var(--border);
            transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
        }
        .radio-card:hover { border-color: var(--blue-light); box-shadow: 0 4px 15px rgba(37,99,235,0.08); transform: translateY(-1px); }
        .radio-card.selected-safe { border-color: var(--blue); background-color: var(--sky); }
        .radio-card.selected-risk { border-color: #ef4444; background-color: #fef2f2; }
    </style>
</head>
<body class="antialiased" style="font-family: 'DM Sans', sans-serif; background-color: var(--warm-white); color: var(--text);">

[MASTER_NAV]

<main class="min-h-[calc(100vh-68px)] flex items-center py-12 px-5 sm:px-8 relative overflow-hidden" style="background: var(--warm-white);">
    <!-- Paco Ambient Glow -->
    <div class="absolute top-[-20%] left-[10%] w-[600px] h-[600px] rounded-full blur-[140px] opacity-[0.06] pointer-events-none" style="background: var(--blue);"></div>
    <div class="absolute bottom-[-10%] right-[-5%] w-[800px] h-[800px] rounded-full blur-[140px] opacity-[0.04] pointer-events-none" style="background: var(--orange);"></div>

    <div class="max-w-[800px] mx-auto w-full relative z-10">
        
        <!-- Header (Wiebe / Moesta Messaging) -->
        <div class="text-center mb-10 max-w-2xl mx-auto">
            <div class="inline-flex items-center gap-2 px-3 py-1.5 rounded-full border text-[0.7rem] font-bold tracking-widest uppercase mb-6 shadow-sm" style="background: rgba(249,115,22,0.08); border-color: rgba(249,115,22,0.2); color: var(--orange);">
                <span class="relative flex h-2 w-2">
                    <span class="animate-ping absolute inline-flex h-full w-full rounded-full opacity-75" style="background: var(--orange);"></span>
                    <span class="relative inline-flex rounded-full h-2 w-2" style="background: var(--orange);"></span>
                </span>
                2026 Cyber Liability Diagnostic
            </div>
            
            <h1 class="text-3xl sm:text-4xl lg:text-[2.8rem] font-bold leading-[1.12] tracking-tight mb-5" style="font-family: 'Fraunces', serif; color: var(--navy);">
                Are your employees voiding your cyber insurance with "Shadow AI"?
            </h1>
            
            <p class="text-[1.05rem] leading-relaxed mx-auto" style="color: var(--text-muted); max-width: 580px;">
                OPC and Law Society rulings make unmanaged ChatGPT use an actionable breach of client privilege. <strong style="color: var(--navy); font-weight: 600;">Identify your business's exact liability gaps in 60 seconds.</strong>
            </p>
        </div>

        <!-- The Tool (Peep Laja / Jakob Nielsen Progressive Disclosure UI) -->
        <div class="rounded-2xl shadow-[0_20px_60px_-15px_rgba(0,0,0,0.05)] bg-white relative overflow-hidden" style="border: 1px solid var(--border);">
            
            <!-- System Status (Nielsen) -->
            <div class="w-full h-1.5 bg-gray-100">
                <div id="progress-bar" class="h-full w-[25%] transition-all duration-500 ease-out" style="background: var(--blue);"></div>
            </div>

            <div class="p-8 sm:p-12 relative" style="min-height: 420px;">
                <form id="risk-assessment-form">
                    
                    <!-- STEP 1 -->
                    <div id="step-1" class="audit-step active">
                        <div class="mb-8">
                            <span class="text-sm font-bold tracking-widest uppercase mb-2 block" style="color: var(--blue);">Question 1 of 3</span>
                            <h2 class="text-2xl font-bold leading-snug" style="color: var(--navy); font-family: 'Fraunces', serif;">
                                Does your business enforce a formally documented AI Acceptable Use Policy signed by all employees?
                            </h2>
                            <p class="text-sm mt-3" style="color: var(--text-muted);"><em>Why it matters: Cyber insurers look for a paper trail proving you attempted to govern staff prior to a breach window.</em></p>
                        </div>
                        
                        <div class="space-y-4">
                            <label class="radio-card flex items-start p-5 rounded-xl cursor-pointer bg-white group">
                                <input type="radio" name="q1" value="Yes - Updated" class="sr-only" onchange="handleSelection(1, true)">
                                <div class="w-5 h-5 rounded-full border-2 mt-0.5 mr-4 flex-shrink-0 flex items-center justify-center transition-colors indicator" style="border-color: #cbd5e1;"></div>
                                <div>
                                    <span class="block font-semibold text-[1.05rem]" style="color: var(--navy);">Yes, we have an active policy.</span>
                                    <span class="block text-sm mt-1" style="color: var(--text-muted);">It has been updated and signed within the last 12 months.</span>
                                </div>
                            </label>
                            
                            <label class="radio-card flex items-start p-5 rounded-xl cursor-pointer bg-white group">
                                <input type="radio" name="q1" value="No / Drafting" class="sr-only" onchange="handleSelection(1, false)">
                                <div class="w-5 h-5 rounded-full border-2 mt-0.5 mr-4 flex-shrink-0 flex items-center justify-center transition-colors indicator" style="border-color: #cbd5e1;"></div>
                                <div>
                                    <span class="block font-semibold text-[1.05rem]" style="color: var(--navy);">No, or we are drafting one now.</span>
                                    <span class="block text-sm mt-1" style="color: var(--text-muted);">We do not have a signed policy currently enforced.</span>
                                </div>
                            </label>
                        </div>
                    </div>

                    <!-- STEP 2 -->
                    <div id="step-2" class="audit-step">
                        <div class="mb-8">
                            <span class="text-sm font-bold tracking-widest uppercase mb-2 block" style="color: var(--blue);">Question 2 of 3</span>
                            <h2 class="text-2xl font-bold leading-snug" style="color: var(--navy); font-family: 'Fraunces', serif;">
                                Have employees ever used free-tier AI (like ChatGPT) to summarize client documents or draft emails?
                            </h2>
                            <p class="text-sm mt-3" style="color: var(--text-muted);"><em>Why it matters: Free-tier tools explicitly train their models on user inputs, automatically stripping confidentiality from any pasted data.</em></p>
                        </div>
                        
                        <div class="space-y-4">
                            <label class="radio-card flex items-start p-5 rounded-xl cursor-pointer bg-white group">
                                <input type="radio" name="q2" value="Yes / Likely" class="sr-only" onchange="handleSelection(2, false)">
                                <div class="w-5 h-5 rounded-full border-2 mt-0.5 mr-4 flex-shrink-0 flex items-center justify-center transition-colors indicator" style="border-color: #cbd5e1;"></div>
                                <div>
                                    <span class="block font-semibold text-[1.05rem]" style="color: var(--navy);">Yes, or I strongly suspect they do.</span>
                                    <span class="block text-sm mt-1" style="color: var(--text-muted);">Employees use public AI tools without technical restriction.</span>
                                </div>
                            </label>
                            
                            <label class="radio-card flex items-start p-5 rounded-xl cursor-pointer bg-white group">
                                <input type="radio" name="q2" value="No - Blocked" class="sr-only" onchange="handleSelection(2, true)">
                                <div class="w-5 h-5 rounded-full border-2 mt-0.5 mr-4 flex-shrink-0 flex items-center justify-center transition-colors indicator" style="border-color: #cbd5e1;"></div>
                                <div>
                                    <span class="block font-semibold text-[1.05rem]" style="color: var(--navy);">No, we have hard network blocks.</span>
                                    <span class="block text-sm mt-1" style="color: var(--text-muted);">It is technically impossible for staff to access free AI tools.</span>
                                </div>
                            </label>
                        </div>
                    </div>

                    <!-- STEP 3 -->
                    <div id="step-3" class="audit-step">
                        <div class="mb-8">
                            <span class="text-sm font-bold tracking-widest uppercase mb-2 block" style="color: var(--blue);">Question 3 of 3</span>
                            <h2 class="text-2xl font-bold leading-snug" style="color: var(--navy); font-family: 'Fraunces', serif;">
                                Do your standard client contracts explicitly and specifically disclose how generative AI is used?
                            </h2>
                            <p class="text-sm mt-3" style="color: var(--text-muted);"><em>Why it matters: The 2026 OPC mandate clarified that relying on an old, generic "we use tech tools" clause does not constitute Meaningful Consent under PIPEDA.</em></p>
                        </div>
                        
                        <div class="space-y-4">
                            <label class="radio-card flex items-start p-5 rounded-xl cursor-pointer bg-white group">
                                <input type="radio" name="q3" value="Yes - Explicit" class="sr-only" onchange="handleSelection(3, true)">
                                <div class="w-5 h-5 rounded-full border-2 mt-0.5 mr-4 flex-shrink-0 flex items-center justify-center transition-colors indicator" style="border-color: #cbd5e1;"></div>
                                <div>
                                    <span class="block font-semibold text-[1.05rem]" style="color: var(--navy);">Yes, our privacy notices strictly mention AI.</span>
                                    <span class="block text-sm mt-1" style="color: var(--text-muted);">Clients explicitly sign off on AI processing.</span>
                                </div>
                            </label>
                            
                            <label class="radio-card flex items-start p-5 rounded-xl cursor-pointer bg-white group">
                                <input type="radio" name="q3" value="No - Implicit" class="sr-only" onchange="handleSelection(3, false)">
                                <div class="w-5 h-5 rounded-full border-2 mt-0.5 mr-4 flex-shrink-0 flex items-center justify-center transition-colors indicator" style="border-color: #cbd5e1;"></div>
                                <div>
                                    <span class="block font-semibold text-[1.05rem]" style="color: var(--navy);">No, we rely on generic confidentiality clauses.</span>
                                    <span class="block text-sm mt-1" style="color: var(--text-muted);">We have not updated contracts to isolate AI usage.</span>
                                </div>
                            </label>
                        </div>
                    </div>

                    <!-- STEP 4 (Capture) -->
                    <div id="step-4" class="audit-step">
                        <div class="text-center mb-8">
                            <div class="w-16 h-16 rounded-full mx-auto flex items-center justify-center mb-4" style="background: var(--sky); color: var(--blue);">
                                <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"></path></svg>
                            </div>
                            <h2 class="text-2xl font-bold leading-snug" style="color: var(--navy); font-family: 'Fraunces', serif;">
                                Audit complete. Your Liability Score is ready.
                            </h2>
                            <p class="text-[0.95rem] mt-3" style="color: var(--text-muted);">Where should we securely deliver your business's custom gap analysis report?</p>
                        </div>
                        
                        <div class="max-w-md mx-auto space-y-5">
                            <div>
                                <label class="block text-[0.8rem] font-bold uppercase tracking-wider mb-2" style="color: var(--text-muted);">Work Email <span class="text-red-500">*</span></label>
                                <input type="email" id="work-email" required placeholder="managingpartner@business.com" class="w-full text-base rounded-xl outline-none transition-all duration-200" style="background: #f8fafc; border: 1.5px solid var(--border); padding: 14px 16px; color: var(--navy);" onfocus="this.style.borderColor='var(--blue)'; this.style.background='#fff'" onblur="this.style.borderColor='var(--border)'; this.style.background='#f8fafc'">
                            </div>
                            
                            <div>
                                <label class="block text-[0.8rem] font-bold uppercase tracking-wider mb-2" style="color: var(--text-muted);">Business Size</label>
                                <select id="business-size" class="w-full text-base rounded-xl outline-none transition-all duration-200 appearance-none bg-no-repeat" style="background-color: #f8fafc; background-image: url('data:image/svg+xml;charset=US-ASCII,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%22292.4%22%20height%3D%22292.4%22%3E%3Cpath%20fill%3D%22%235a6a8a%22%20d%3D%22M287%2069.4a17.6%2017.6%200%200%200-13-5.4H18.4c-5%200-9.3%201.8-12.9%205.4A17.6%2017.6%200%200%200%200%2082.2c0%205%201.8%209.3%205.4%2012.9l128%20127.9c3.6%203.6%207.8%205.4%2012.8%205.4s9.2-1.8%2012.8-5.4L287%2095c3.5-3.5%205.4-7.8%205.4-12.8%200-5-1.9-9.2-5.5-12.8z%22%2F%3E%3C%2Fsvg%3E'); background-size: 0.65rem auto; background-position: right 1rem center; border: 1.5px solid var(--border); padding: 14px 16px; color: var(--navy);" onfocus="this.style.borderColor='var(--blue)'; this.style.background='#fff'" onblur="this.style.borderColor='var(--border)'; this.style.background='#f8fafc'">
                                    <option value="1-14 Employees">1-14 Employees</option>
                                    <option value="15-50 Employees">15-50 Employees</option>
                                    <option value="51-150 Employees">51-150 Employees</option>
                                </select>
                            </div>

                            <div class="pt-4">
                                <!-- RULE 5: Exact mandated CTA -->
                                <button type="submit" id="submit-btn" class="w-full font-bold text-[1.05rem] py-4 rounded-xl transition-all duration-200 transform hover:-translate-y-0.5 relative overflow-hidden" style="background: var(--orange); color: #fff; box-shadow: 0 8px 25px rgba(249,115,22,0.25);">
                                    <span id="btn-text">Book My Free Discovery Call &rarr;</span>
                                </button>
                                <p class="text-xs text-center font-medium mt-4 flex items-center justify-center gap-1.5" style="color: var(--text-muted);">
                                    <svg class="w-3.5 h-3.5" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M5 9V7a5 5 0 0110 0v2a2 2 0 012 2v5a2 2 0 01-2 2H5a2 2 0 01-2-2v-5a2 2 0 012-2zm8-2v2H7V7a3 3 0 016 0z" clip-rule="evenodd"></path></svg>
                                    Securely routed to Trueline IT (Subject to PIPEDA).
                                </p>
                            </div>
                        </div>
                    </div>

                    <!-- SUCCESS STATE -->
                    <div id="success-container" class="hidden text-center py-10 px-8">
                        <div class="w-20 h-20 mx-auto rounded-full flex items-center justify-center mb-6" style="background: var(--sky); color: var(--blue);">
                            <svg class="w-10 h-10" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"></path></svg>
                        </div>
                        <h2 class="text-3xl font-bold mb-4" style="font-family: 'Fraunces', serif; color: var(--navy);">Audit Securely Submitted</h2>
                        <p class="text-[1.05rem] max-w-sm mx-auto" style="color: var(--text-muted);">We are cross-referencing your inputs with established PIPEDA precedents. Check your inbox momentarily.</p>
                    </div>

                </form>
            </div>
        </div>

    </div>
</main>

[MASTER_FOOTER]

<!-- Logic & Interactivity (Vanilla JS, HubSpot Rule 51) -->
<script>
    const steps = [
        document.getElementById('step-1'),
        document.getElementById('step-2'),
        document.getElementById('step-3'),
        document.getElementById('step-4')
    ];
    const progressBar = document.getElementById('progress-bar');
    const form = document.getElementById('risk-assessment-form');

    function handleSelection(stepNumber, isSafe) {
        // Style the clicked radio visually (Nielsen system feedback)
        const currentStepDiv = steps[stepNumber - 1];
        const radios = currentStepDiv.querySelectorAll('input[type="radio"]');
        
        radios.forEach(radio => {
            const card = radio.closest('.radio-card');
            const indicator = card.querySelector('.indicator');
            if (radio.checked) {
                if (isSafe) {
                    card.classList.add('selected-safe');
                    card.classList.remove('selected-risk');
                    indicator.innerHTML = '<svg class="w-3 h-3 text-blue-600" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"></path></svg>';
                    indicator.style.borderColor = 'var(--blue)';
                } else {
                    card.classList.add('selected-risk');
                    card.classList.remove('selected-safe');
                    indicator.innerHTML = '<svg class="w-3 h-3 text-red-600" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"></path></svg>';
                    indicator.style.borderColor = '#ef4444';
                }
            } else {
                card.classList.remove('selected-safe', 'selected-risk');
                indicator.innerHTML = '';
                indicator.style.borderColor = '#cbd5e1';
            }
        });

        // Delay progression slightly for user validation
        setTimeout(() => {
            currentStepDiv.classList.remove('active');
            if(stepNumber < 4) {
                steps[stepNumber].classList.add('active');
                progressBar.style.width = ((stepNumber + 1) * 25) + '%';
            }
        }, 400);
    }

    // HubSpot Native API Fetch (Rule 51 compliant)
    form.addEventListener('submit', async function(e) {
        e.preventDefault();
        const btn = document.getElementById('submit-btn');
        const btnText = document.getElementById('btn-text');
        
        const q1 = form.querySelector('input[name="q1"]:checked')?.value || '';
        const q2 = form.querySelector('input[name="q2"]:checked')?.value || '';
        const q3 = form.querySelector('input[name="q3"]:checked')?.value || '';
        const email = document.getElementById('work-email').value;
        const businessSize = document.getElementById('business-size').value;
        
        btn.disabled = true;
        btnText.innerText = 'Calculating Liability...';
        btn.style.opacity = '0.8';

        // Rule 51: No hutk, hardcoded owner_id
        const payload = {
            fields: [
                { name: 'email', value: email },
                { name: 'company_size', value: businessSize },
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
                steps[3].classList.remove('active');
                document.getElementById('success-container').classList.remove('hidden');
                document.getElementById('success-container').classList.add('active');
                progressBar.style.background = '#10b981';
            } else {
                btn.disabled = false;
                btnText.innerText = 'Book My Free Discovery Call →';
                btn.style.opacity = '1';
                alert('Connection issue submitting your audit. Please try again.');
            }
        } catch (err) {
            btn.disabled = false;
            btnText.innerText = 'Book My Free Discovery Call →';
            btn.style.opacity = '1';
            alert('Network error. Please try again.');
        }
    });

    // Prevent enter key from accidentally submitting early
    form.addEventListener('keydown', function(event) {
        if(event.key === 'Enter') { event.preventDefault(); }
    });
</script>
</body>
</html>"""

html_content = html_content.replace('[MASTER_STYLE]', master_style)
html_content = html_content.replace('[FONT_LINK]', font_link)
html_content = html_content.replace('[MASTER_NAV]', master_nav)
html_content = html_content.replace('[MASTER_FOOTER]', master_footer)

with open('/opt/data/msp-site/risk-assessment.html', 'w') as f:
    f.write(html_content)
