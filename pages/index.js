import Head from "next/head";

export default function Home() {
  return (
    <>
      <Head>
        <title>Trueline IT - Worry-Free IT Support</title>
        <meta name="description" content="24/7 helpdesk, security monitoring, and daily backups. Fixed, transparent pricing for small businesses." />
      </Head>
      <div style={{ fontFamily: "system-ui, -apple-system, sans-serif", color: "#333", background: "#f7f9fb", margin: 0, padding: 0, minHeight: "100vh" }}>
        <header style={{ background: "#003D82", color: "white", padding: "16px 20px", fontWeight: "bold" }}>
          TRUELINE IT
        </header>
        
        <main>
          <section style={{ background: "linear-gradient(135deg, #003D82 0%, #0056b3 100%)", color: "white", padding: "80px 20px", textAlign: "center" }}>
            <h1 style={{ fontSize: "2.5rem", margin: "0 0 16px 0", lineHeight: 1.2 }}>Combat IT Downtime with Frictionless Support</h1>
            <p style={{ fontSize: "1.1rem", margin: "0 0 24px 0", opacity: 0.9 }}>24/7 helpdesk, security monitoring, and daily backups. Flat-rate billing.</p>
            <a href="#contact" style={{ display: "inline-block", background: "#FF6B35", color: "white", padding: "14px 28px", borderRadius: "6px", textDecoration: "none", fontWeight: "bold" }}>Book Discovery Call</a>
          </section>

          <section style={{ padding: "60px 20px", maxWidth: "1000px", margin: "0 auto", display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(280px, 1fr))", gap: "24px" }}>
            <div style={{ background: "white", padding: "24px", borderRadius: "8px", boxShadow: "0 2px 8px rgba(0,0,0,0.05)" }}>
              <h3 style={{ color: "#003D82", marginTop: 0 }}>24/7 Helpdesk</h3>
              <p style={{ margin: 0, color: "#555" }}>Always-on support with fast responses.</p>
            </div>
            <div style={{ background: "white", padding: "24px", borderRadius: "8px", boxShadow: "0 2px 8px rgba(0,0,0,0.05)" }}>
              <h3 style={{ color: "#003D82", marginTop: 0 }}>Security Monitoring</h3>
              <p style={{ margin: 0, color: "#555" }}>Threat detection and proactive protection.</p>
            </div>
            <div style={{ background: "white", padding: "24px", borderRadius: "8px", boxShadow: "0 2px 8px rgba(0,0,0,0.05)" }}>
              <h3 style={{ color: "#003D82", marginTop: 0 }}>Daily Backups</h3>
              <p style={{ margin: 0, color: "#555" }}>Automated cloud backups and quick restores.</p>
            </div>
          </section>
        </main>

        <footer style={{ textAlign: "center", padding: "40px 20px", color: "#666", fontSize: "0.9rem" }}>
          &copy; 2026 Trueline IT. All rights reserved.
        </footer>
      </div>
    </>
  );
}
