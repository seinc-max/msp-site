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
    <title>AI Governance Pricing & The Cyber Shield Guarantee | Trueline IT</title>
    <meta name="description" content="Flat monthly retainers for Ontario professional services businesses. Includes our PIPEDA Policy Guarantee: if your insurer rejects our policy, we refund your setup fee.">
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="icon" type="image/svg+xml" href="/favicon.svg">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    [FONT_LINK]
    [MASTER_STYLE]
    <style>
        .pricing-card {
            border: 1.5px solid var(--border);
            transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
        }
        .pricing-card:hover { border-color: var(--blue-light); box-shadow: 0 10px 40px -15px rgba(37,99,235,0.15); transform: translateY(-3px); }
        .pricing-card.popular {
            border-color: var(--navy);
            box-shadow: 0 10px 40px -15px rgba(26,39,68,0.25);
            transform: scale(1.02);
        }
        .pricing-card.popular:hover { transform: scale(1.03); }
        
        .feature-item::before {
            content: '✓';
            background: var(--blue);
            color: #fff;
            width: 18px; height: 18px;
            border-radius: 50%;
            display: inline-flex; justify-content: center; align-items: center;
            font-size: 0.65rem; font-weight: 700;
            flex-shrink: 0; margin-top: 3px; margin-right: 12px;
        }

        .cta-btn {
            display: inline-block;
            background: var(--orange);
            color: #fff;
            font-family: 'DM Sans', sans-serif;
            font-weight: 700;
            font-size: 1.05rem;
            padding: 16px 32px;
            border-radius: 8px;
            text-decoration: none;
            transition: all 0.2s;
            box-shadow: 0 4px 20px rgba(249,115,22,0.3);
            text-align: center;
        }
        .cta-btn:hover { background: #ea6c0a; transform: translateY(-2px); box-shadow: 0 8px 25px rgba(249,115,22,0.4); }
        .cta-outline {
            background: transparent; color: var(--navy); border: 2px solid var(--border); box-shadow: none;
        }
        .cta-outline:hover { background: var(--sky); border-color: var(--blue); transform: translateY(-2px); }
    </style>
</head>
<body class="antialiased" style="font-family: 'DM Sans', sans-serif; background-color: var(--warm-white); color: var(--text);">

[MASTER_NAV]

<!-- HERO (Paco/Hormozi) -->
<section class="min-h-[50vh] flex flex-col items-center justify-center py-20 px-5 sm:px-8 relative overflow-hidden" style="background: var(--navy);">
    <div class="absolute top-[-20%] left-[20%] w-[600px] h-[600px] rounded-full blur-[140px] opacity-[0.1] pointer-events-none" style="background: var(--blue);"></div>
    
    <div class="max-w-4xl mx-auto text-center relative z-10">
        <div class="inline-flex items-center gap-2 px-3 py-1.5 rounded-full border text-xs font-bold tracking-widest uppercase mb-6" style="background: rgba(255,255,255,0.05); border-color: rgba(255,255,255,0.1); color: var(--sky);">
            Transparent Flat-Fee Retainers
        </div>
        <h1 class="text-4xl sm:text-5xl lg:text-6xl font-bold leading-tight tracking-tight mb-6" style="font-family: 'Fraunces', serif; color: #fff;">
            Ironclad Cyber Liability Protection.<br>
            <span style="color: var(--sky); font-style: italic;">Zero Hourly IT Fees.</span>
        </h1>
        <p class="text-lg leading-relaxed mx-auto" style="color: rgba(255,255,255,0.65); max-width: 600px;">
            The mid-market alternative to Big 4 consulting. We charge a flat monthly fee per business to govern your AI risk, lock down M365 Copilot, and pass your cyber insurance renewals.
        </p>
    </div>
</section>

<!-- THE HORMOZI GUARANTEE (Risk Reversal) -->
<section style="background: var(--sky); padding: 40px 5%; border-bottom: 1px solid var(--border);">
    <div class="max-w-[900px] mx-auto bg-white rounded-2xl p-8 sm:p-12 shadow-sm border" style="border-color: var(--border); transform: translateY(-80px);">
        <div class="flex flex-col sm:flex-row items-center gap-8">
            <div class="flex-shrink-0 w-20 h-20 rounded-full flex items-center justify-center" style="background: var(--navy); color: var(--orange);">
                <svg class="w-10 h-10" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"></path></svg>
            </div>
            <div>
                <h2 class="text-2xl font-bold mb-2" style="font-family: 'Fraunces', serif; color: var(--navy);">The PIPEDA Shield Guarantee</h2>
                <p class="text-[1rem] leading-relaxed" style="color: var(--text-muted);">
                    <strong>We eliminate the risk of starting.</strong> If our custom AI Acceptable Use Policy is rejected by your Cyber Insurer, or if we don't locate at least 3 critical data vulnerabilities during our initial Shadow AI audit, <strong style="color: var(--navy);">we will refund your $3,000 setup fee immediately</strong> and you keep the policy.
                </p>
            </div>
        </div>
    </div>
</section>

<!-- PRICING TIERS -->
<section class="py-10 px-5 sm:px-8" style="background: var(--warm-white);">
    <div class="max-w-[1200px] mx-auto w-full grid grid-cols-1 md:grid-cols-3 gap-8 relative z-10" style="margin-top: -30px;">
        
        <!-- TIER 1 -->
        <div class="pricing-card bg-white rounded-2xl p-8 sm:p-10 flex flex-col relative">
            <div class="mb-8">
                <h3 class="text-xl font-bold mb-2" style="font-family: 'Fraunces', serif; color: var(--navy);">Foundation</h3>
                <p class="text-sm" style="color: var(--text-muted); min-height: 42px;">Best for 15–30 person businesses implementing basic AI governance.</p>
                <div class="mt-6 flex items-baseline">
                    <span class="text-4xl font-bold" style="color: var(--navy); font-family: 'Fraunces', serif;">$1,500</span>
                    <span class="text-sm font-medium ml-2" style="color: var(--text-muted);">/ mo</span>
                </div>
                <p class="text-xs mt-2" style="color: var(--text-muted);">+$3,000 One-Time Setup Audit</p>
            </div>
            <ul class="space-y-4 mb-10 flex-grow text-[0.95rem]" style="color: var(--text);">
                <li class="flex items-start feature-item">Maintain AI Acceptable Use Policy</li>
                <li class="flex items-start feature-item">Quarterly Shadow AI Audits</li>
                <li class="flex items-start feature-item">Insurer-Ready Compliance Docs</li>
                <li class="flex items-start feature-item">Monthly 30-Min Strategy Call</li>
                <li class="flex items-start feature-item">1 Active Workflow Automation</li>
            </ul>
            <!-- MANDATORY RULE 52: Exact CTA -->
            <a href="#contact" class="cta-btn cta-outline w-full cursor-pointer">Book My Free Discovery Call &rarr;</a>
        </div>

        <!-- TIER 2 (POPULAR) -->
        <div class="pricing-card popular bg-white rounded-2xl p-8 sm:p-10 flex flex-col relative shadow-xl z-20">
            <div class="absolute top-0 left-1/2 transform -translate-x-1/2 -translate-y-1/2 bg-blue-600 text-white text-xs font-bold uppercase tracking-wider py-1.5 px-4 rounded-full" style="background: var(--blue);">
                Most Popular
            </div>
            <div class="mb-8">
                <h3 class="text-xl font-bold mb-2" style="font-family: 'Fraunces', serif; color: var(--navy);">Growth</h3>
                <p class="text-sm" style="color: var(--text-muted); min-height: 42px;">Best for 30–75 person businesses requiring M365 Copilot enforcement.</p>
                <div class="mt-6 flex items-baseline">
                    <span class="text-4xl font-bold" style="color: var(--navy); font-family: 'Fraunces', serif;">$2,500</span>
                    <span class="text-sm font-medium ml-2" style="color: var(--text-muted);">/ mo</span>
                </div>
                <p class="text-xs mt-2" style="color: var(--text-muted);">+$5,000 One-Time Setup & Briefing</p>
            </div>
            <ul class="space-y-4 mb-10 flex-grow text-[0.95rem]" style="color: var(--text);">
                <li class="flex items-start feature-item"><strong>Everything in Foundation</strong></li>
                <li class="flex items-start feature-item">M365 Copilot Tenant Security Lockdown</li>
                <li class="flex items-start feature-item">Department-Level Policy Customization</li>
                <li class="flex items-start feature-item">Up to 3 Active Workflow Automations</li>
                <li class="flex items-start feature-item">Monthly AI Usage Reports</li>
                <li class="flex items-start feature-item"><strong style="color: var(--blue);">Bonus:</strong> Team Training Briefing Session</li>
            </ul>
            <!-- MANDATORY RULE 52: Exact CTA -->
            <a href="#contact" class="cta-btn w-full cursor-pointer">Book My Free Discovery Call &rarr;</a>
        </div>

        <!-- TIER 3 -->
        <div class="pricing-card bg-white rounded-2xl p-8 sm:p-10 flex flex-col relative">
            <div class="mb-8">
                <h3 class="text-xl font-bold mb-2" style="font-family: 'Fraunces', serif; color: var(--navy);">Transform</h3>
                <p class="text-sm" style="color: var(--text-muted); min-height: 42px;">Best for 75–150 person businesses requiring Fractional AI Executive leadership.</p>
                <div class="mt-6 flex items-baseline">
                    <span class="text-4xl font-bold" style="color: var(--navy); font-family: 'Fraunces', serif;">$4,500</span>
                    <span class="text-sm font-medium ml-2" style="color: var(--text-muted);">/ mo</span>
                </div>
                <p class="text-xs mt-2" style="color: var(--text-muted);">+$7,500 One-Time Exec Board Presentation</p>
            </div>
            <ul class="space-y-4 mb-10 flex-grow text-[0.95rem]" style="color: var(--text);">
                <li class="flex items-start feature-item"><strong>Everything in Growth</strong></li>
                <li class="flex items-start feature-item">Virtual Chief AI Officer (vCAIO)</li>
                <li class="flex items-start feature-item">Quarterly Board Meeting Attendance</li>
                <li class="flex items-start feature-item">Unlimited Active Automations</li>
                <li class="flex items-start feature-item">1 New Automation Build At a Time</li>
                <li class="flex items-start feature-item">Bespoke Enterprise Readiness Report</li>
            </ul>
            <!-- MANDATORY RULE 52: Exact CTA -->
            <a href="#contact" class="cta-btn cta-outline w-full cursor-pointer">Book My Free Discovery Call &rarr;</a>
        </div>

    </div>
</section>

<!-- BOTTOM CTA SECTION -->
<section style="background: var(--sky); padding: 80px 5%; margin-top: 60px;">
    <div class="max-w-[700px] mx-auto text-center">
        <h2 class="text-3xl font-bold mb-4" style="font-family: 'Fraunces', serif; color: var(--navy);">Stop guessing your liability.</h2>
        <p class="text-[1.05rem] leading-relaxed mb-8" style="color: var(--text-muted);">
            Get the AI Risk Audit covering Month 1 labor, M365 config recommendations, and your insurer-ready report. Protected by the absolute PIPEDA Shield Guarantee.
        </p>
        <!-- MANDATORY RULE 52: Exact CTA -->
        <a id="contact" href="mailto:hello@truelineit.com" class="cta-btn cursor-pointer">Book My Free Discovery Call &rarr;</a>
    </div>
</section>

[MASTER_FOOTER]

</body>
</html>"""

html_content = html_content.replace('[MASTER_STYLE]', master_style)
html_content = html_content.replace('[FONT_LINK]', font_link)
html_content = html_content.replace('[MASTER_NAV]', master_nav)
html_content = html_content.replace('[MASTER_FOOTER]', master_footer)

with open('/opt/data/msp-site/ai-consulting-pricing.html', 'w') as f:
    f.write(html_content)

print("Pricing page rewriten successfully.")
