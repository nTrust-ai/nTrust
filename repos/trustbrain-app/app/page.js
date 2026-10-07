import { DIFFERENTIATORS, MITRE, FRAMEWORKS } from '@/lib/tiers'

export default function Home() {
  return (
    <main className="container">
      <section className="hero">
        <span className="eyebrow">Sovereign AI Security Reasoning</span>
        <h1>TrustBrain<span className="grad">™</span> — The Autonomous Security Reasoning Copilot</h1>
        <p className="lead">
          Turn a raw finding into a verified, reversible, multi-format remediation playbook — without ever
          exposing infrastructure secrets. Detection is commoditized. Reasoning is the moat.
        </p>
        <div style={{ display: 'flex', gap: 12, flexWrap: 'wrap' }}>
          <a className="btn primary" href="/portal">Explore Licensing & Install</a>
          <a className="btn ghost" href="#why">Why TrustBrain</a>
        </div>
        <div style={{ marginTop: 20, display: 'flex', gap: 8, flexWrap: 'wrap' }}>
          <span className="badge live">Engine v0 · 12/12 tests green</span>
          <span className="badge coming">Live demo — Coming Soon</span>
          <span className="badge coming">Design-partner pilots — Coming Soon</span>
        </div>
      </section>

      <section className="section" id="why">
        <h2>Why TrustBrain</h2>
        <p className="sub">
          The AI-copilot market is crowded horizontally but empty vertically for a privacy-preserving,
          reversible-by-design reasoning engine you can deploy on your own infrastructure — no telemetry to a hyperscaler.
        </p>
        <div className="grid cols-3">
          {DIFFERENTIATORS.map((d) => (
            <div className="card" key={d.title}>
              <h3>{d.title}</h3>
              <p>{d.body}</p>
            </div>
          ))}
        </div>
      </section>

      <section className="section" id="positioning">
        <h2>Positioning</h2>
        <p className="sub">
          For security and platform teams in regulated enterprises who cannot ship telemetry to a vendor cloud, TrustBrain™
          is the sovereign reasoning copilot that turns a raw finding into a verified, reversible, multi-format remediation
          playbook — without ever exposing infrastructure secrets.
        </p>
        <div className="grid cols-2">
          <div className="card">
            <h3>Built for regulated mid-market</h3>
            <p>
              ISO 27001 / SOC 2 readiness, GDPR Art. 32/33, DPIA & breach readiness, and MSP multi-tenant hardening.
              Zero-knowledge reasoning unlocks the largest unserved segment.
            </p>
          </div>
          <div className="card">
            <h3>Dual-Agent Core (Separation of Duties)</h3>
            <p>
              A Worker proposes; a Governor authorizes. Reversibility is enforced by policy — no rollback path means
              a remediation is POLICY_DENIED and never executable.
            </p>
          </div>
        </div>
      </section>

      <section className="section">
        <h2>Threat & Compliance Coverage</h2>
        <div className="card">
          <h3>MITRE ATT&amp;CK Enterprise v14.1</h3>
          <div style={{ marginTop: 8 }}>
            {MITRE.map((m) => <span className="chip" key={m}>{m}</span>)}
          </div>
          <h3 style={{ marginTop: 22 }}>Compliance frameworks</h3>
          <div style={{ marginTop: 8 }}>
            {FRAMEWORKS.map((f) => <span className="chip" key={f}>{f}</span>)}
          </div>
        </div>
      </section>

      <section className="section">
        <h2>Get Started</h2>
        <p className="sub">
          Provision a free Community tier, review entitlements, and deploy the engine on your own infrastructure.
        </p>
        <a className="btn primary" href="/portal">Open Licensing Portal</a>
      </section>
    </main>
  )
}
