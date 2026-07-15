import Head from 'next/head';

export default function RiskAssessment() {
  return (
    <div className="min-h-screen bg-neutral-900 text-white font-sans">
      <Head>
        <title>AI Privacy Risk Assessment | Trueline IT</title>
        <meta name="description" content="Discover your firm's exposure to Shadow AI and PIPEDA violations in 3 minutes." />
      </Head>

      <main className="max-w-4xl mx-auto px-6 py-16">
        <header className="text-center mb-16">
          <h1 className="text-4xl md:text-5xl font-bold mb-4 tracking-tight">Is Your Firm Exposed to Shadow AI?</h1>
          <p className="text-xl text-neutral-400 max-w-2xl mx-auto">
            Employees are using public AI tools. If they process client data, you may be violating PIPEDA, Law Society guidelines, and your cyber insurance terms. Find out your risk score in 3 minutes.
          </p>
        </header>

        <section className="bg-neutral-800 rounded-xl p-8 md:p-12 shadow-2xl border border-neutral-700">
          <form id="risk-assessment-form" className="space-y-8" onSubmit={(e) => e.preventDefault()}>
            
            {/* Question 1 */}
            <div className="space-y-4">
              <label className="block text-lg font-semibold">1. Does your firm currently have a formally documented AI Acceptable Use Policy signed by all employees?</label>
              <div className="space-y-3">
                <label className="flex items-center space-x-3 bg-neutral-900 p-4 rounded-lg border border-neutral-700 cursor-pointer hover:border-blue-500 transition">
                  <input type="radio" name="q1" value="yes" className="form-radio text-blue-500 w-5 h-5" />
                  <span>Yes, updated within the last 12 months.</span>
                </label>
                <label className="flex items-center space-x-3 bg-neutral-900 p-4 rounded-lg border border-neutral-700 cursor-pointer hover:border-blue-500 transition">
                  <input type="radio" name="q1" value="no" className="form-radio text-blue-500 w-5 h-5" />
                  <span>No, or we are drafting one now.</span>
                </label>
              </div>
            </div>

            {/* Question 2 */}
            <div className="space-y-4">
              <label className="block text-lg font-semibold">2. To your knowledge, have employees ever used a free-tier public AI (like ChatGPT, Gemini, or Claude) to summarize documents, draft emails, or analyze spreadsheets?</label>
              <div className="space-y-3">
                <label className="flex items-center space-x-3 bg-neutral-900 p-4 rounded-lg border border-neutral-700 cursor-pointer hover:border-blue-500 transition">
                  <input type="radio" name="q2" value="yes" className="form-radio text-blue-500 w-5 h-5" />
                  <span>Yes, I am aware this happens.</span>
                </label>
                <label className="flex items-center space-x-3 bg-neutral-900 p-4 rounded-lg border border-neutral-700 cursor-pointer hover:border-blue-500 transition">
                  <input type="radio" name="q2" value="maybe" className="form-radio text-blue-500 w-5 h-5" />
                  <span>I'm not sure, but it is highly likely.</span>
                </label>
                <label className="flex items-center space-x-3 bg-neutral-900 p-4 rounded-lg border border-neutral-700 cursor-pointer hover:border-blue-500 transition">
                  <input type="radio" name="q2" value="no" className="form-radio text-blue-500 w-5 h-5" />
                  <span>Absolutely not. We have technical network blocks in place.</span>
                </label>
              </div>
            </div>

            {/* Form Capture */}
            <div className="pt-8 border-t border-neutral-700">
              <h3 className="text-xl font-bold mb-4">Get Your Instant Risk Report</h3>
              <p className="text-sm text-neutral-400 mb-6">Your report will highlight specific regulatory gaps and how cyber insurers view your current setup.</p>
              
              <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
                <div>
                  <label className="block text-sm text-neutral-400 mb-2">Work Email</label>
                  <input type="email" required className="w-full bg-neutral-900 border border-neutral-600 rounded-lg px-4 py-3 text-white focus:outline-none focus:border-blue-500" placeholder="partner@lawfirm.ca" />
                </div>
                <div>
                  <label className="block text-sm text-neutral-400 mb-2">Firm Size</label>
                  <select className="w-full bg-neutral-900 border border-neutral-600 rounded-lg px-4 py-3 text-white focus:outline-none focus:border-blue-500">
                    <option>1-14 Employees</option>
                    <option>15-50 Employees</option>
                    <option>51-150 Employees</option>
                  </select>
                </div>
              </div>
              
              <button 
                type="button" 
                onClick={() => alert('In production, this triggers Nancy’s webhook to log in HubSpot and calculate the score!')}
                className="w-full bg-blue-600 hover:bg-blue-500 text-white font-bold py-4 rounded-lg transition"
              >
                Analyze My Firm's Risk Profile
              </button>
            </div>

          </form>
        </section>
      </main>
    </div>
  );
}
