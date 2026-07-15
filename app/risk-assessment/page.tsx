'use client';
import Head from 'next/head';
import { useState } from 'react';

export default function RiskAssessment() {
  const [formData, setFormData] = useState({
    q1: '',
    q2: '',
    email: '',
    firmSize: '1-14 Employees'
  });
  const [status, setStatus] = useState('idle');

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setStatus('submitting');

    const payload = {
      fields: [
        { name: 'email', value: formData.email },
        { name: 'company_size', value: formData.firmSize },
        { name: 'ai_policy_status', value: formData.q1 },
        { name: 'shadow_ai_usage', value: formData.q2 },
        // CRITICAL Rule 51: Hardcoded owner assignment
        { name: 'hubspot_owner_id', value: '89556230' }
      ]
      // CRITICAL Rule 51: Intentionally omitting context object to prevent hutk overwrites
    };

    try {
      const response = await fetch('https://api.hsforms.com/submissions/v3/integration/submit/343087614/e66cbddb-8b74-4166-ab13-6ea81df11466', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(payload)
      });

      if (response.ok) {
        setStatus('success');
      } else {
        setStatus('error');
      }
    } catch (err) {
      setStatus('error');
    }
  };

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
          {status === 'success' ? (
            <div className="text-center py-12">
              <h2 className="text-3xl font-bold text-green-400 mb-4">Risk Audit Received</h2>
              <p className="text-lg text-neutral-300">We are processing your answers against current PIPEDA and Law Society frameworks. Check your inbox in a few minutes for your comprehensive risk report.</p>
            </div>
          ) : (
            <form id="risk-assessment-form" className="space-y-8" onSubmit={handleSubmit}>
              
              <div className="space-y-4">
                <label className="block text-lg font-semibold">1. Does your firm currently have a formally documented AI Acceptable Use Policy signed by all employees?</label>
                <div className="space-y-3">
                  <label className="flex items-center space-x-3 bg-neutral-900 p-4 rounded-lg border border-neutral-700 cursor-pointer hover:border-blue-500 transition">
                    <input type="radio" name="q1" value="Yes - Updated" required onChange={(e) => setFormData({...formData, q1: e.target.value})} className="form-radio text-blue-500 w-5 h-5" />
                    <span>Yes, updated within the last 12 months.</span>
                  </label>
                  <label className="flex items-center space-x-3 bg-neutral-900 p-4 rounded-lg border border-neutral-700 cursor-pointer hover:border-blue-500 transition">
                    <input type="radio" name="q1" value="No / Drafting" required onChange={(e) => setFormData({...formData, q1: e.target.value})} className="form-radio text-blue-500 w-5 h-5" />
                    <span>No, or we are drafting one now.</span>
                  </label>
                </div>
              </div>

              <div className="space-y-4">
                <label className="block text-lg font-semibold">2. To your knowledge, have employees ever used a free-tier public AI (like ChatGPT, Gemini, or Claude) to summarize documents, draft emails, or analyze spreadsheets?</label>
                <div className="space-y-3">
                  <label className="flex items-center space-x-3 bg-neutral-900 p-4 rounded-lg border border-neutral-700 cursor-pointer hover:border-blue-500 transition">
                    <input type="radio" name="q2" value="Yes" required onChange={(e) => setFormData({...formData, q2: e.target.value})} className="form-radio text-blue-500 w-5 h-5" />
                    <span>Yes, I am aware this happens.</span>
                  </label>
                  <label className="flex items-center space-x-3 bg-neutral-900 p-4 rounded-lg border border-neutral-700 cursor-pointer hover:border-blue-500 transition">
                    <input type="radio" name="q2" value="Likely" required onChange={(e) => setFormData({...formData, q2: e.target.value})} className="form-radio text-blue-500 w-5 h-5" />
                    <span>I'm not sure, but it is highly likely.</span>
                  </label>
                  <label className="flex items-center space-x-3 bg-neutral-900 p-4 rounded-lg border border-neutral-700 cursor-pointer hover:border-blue-500 transition">
                    <input type="radio" name="q2" value="No - Blocked" required onChange={(e) => setFormData({...formData, q2: e.target.value})} className="form-radio text-blue-500 w-5 h-5" />
                    <span>Absolutely not. We have technical network blocks in place.</span>
                  </label>
                </div>
              </div>

              <div className="pt-8 border-t border-neutral-700">
                <h3 className="text-xl font-bold mb-4">Get Your Instant Risk Report</h3>
                <p className="text-sm text-neutral-400 mb-6">Your report will highlight specific regulatory gaps and how cyber insurers view your current setup.</p>
                
                <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
                  <div>
                    <label className="block text-sm text-neutral-400 mb-2">Work Email</label>
                    <input type="email" required value={formData.email} onChange={(e) => setFormData({...formData, email: e.target.value})} className="w-full bg-neutral-900 border border-neutral-600 rounded-lg px-4 py-3 text-white focus:outline-none focus:border-blue-500" placeholder="partner@lawfirm.ca" />
                  </div>
                  <div>
                    <label className="block text-sm text-neutral-400 mb-2">Firm Size</label>
                    <select value={formData.firmSize} onChange={(e) => setFormData({...formData, firmSize: e.target.value})} className="w-full bg-neutral-900 border border-neutral-600 rounded-lg px-4 py-3 text-white focus:outline-none focus:border-blue-500">
                      <option value="1-14 Employees">1-14 Employees</option>
                      <option value="15-50 Employees">15-50 Employees</option>
                      <option value="51-150 Employees">51-150 Employees</option>
                    </select>
                  </div>
                </div>
                
                <button 
                  type="submit" 
                  disabled={status === 'submitting'}
                  className="w-full bg-blue-600 hover:bg-blue-500 disabled:bg-neutral-600 text-white font-bold py-4 rounded-lg transition"
                >
                  {status === 'submitting' ? 'Analyzing Risk...' : "Analyze My Firm's Risk Profile"}
                </button>
                {status === 'error' && <p className="text-red-400 mt-4 text-center">There was an issue submitting your risk assessment. Please try again.</p>}
              </div>

            </form>
          )}
        </section>
      </main>
    </div>
  );
}
