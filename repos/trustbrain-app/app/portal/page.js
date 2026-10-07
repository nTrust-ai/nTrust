'use client'

import { useState } from 'react'
import { TIERS, INSTALL_COMMAND } from '@/lib/tiers'

const MATRIX_ROWS = [
  { label: 'Max connectors', key: 'connectors' },
  { label: 'TrustBrain reasoning core', key: 'reasoningCore' },
  { label: 'Terraform / IaC generation', key: 'iacGeneration' },
  { label: 'TokenShield zero-knowledge gateway', key: 'tokenShield' },
  { label: 'Autonomous execution', key: 'autonomousExecution' },
  { label: 'Audit ledger / SLA', key: 'auditLedger' }
]

function fmt(v) {
  if (v === true) return { cls: 'yes', txt: '✅' }
  if (v === false) return { cls: 'no', txt: '—' }
  if (v == null) return { cls: 'no', txt: '—' }
  if (v === 'limited') return { cls: 'yes', txt: 'Limited' }
  return { cls: 'yes', txt: String(v) }
}

function FeatureRow({ label, tiers, get }) {
  return (
    <tr>
      <td>{label}</td>
      {tiers.map((t) => {
        const v = get(t)
        const { cls, txt } = fmt(v)
        return <td key={t.id} className={cls}>{txt}</td>
      })}
    </tr>
  )
}

export default function Portal() {
  const [email, setEmail] = useState('')
  const [tier, setTier] = useState('community')
  const [result, setResult] = useState(null)
  const [loading, setLoading] = useState(false)
  const [copied, setCopied] = useState(false)

  async function activate(e) {
    e.preventDefault()
    setLoading(true)
    setResult(null)
    try {
      const res = await fetch('/api/license', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email, tier })
      })
      const data = await res.json()
      setResult(data)
    } catch (err) {
      setResult({ ok: false, note: 'Activation failed: ' + err.message })
    } finally {
      setLoading(false)
    }
  }

  async function copyInstall() {
    try {
      await navigator.clipboard.writeText(INSTALL_COMMAND)
      setCopied(true)
      setTimeout(() => setCopied(false), 1800)
    } catch (_) {}
  }

  return (
    <main className="container">
      <section className="hero" style={{ paddingBottom: 24 }}>
        <span className="eyebrow">Pillar 2 · Licensing & Installer Hub</span>
        <h1 style={{ fontSize: 40 }}>TrustBrain<span className="grad">™</span> Licensing Portal</h1>
        <p className="lead" style={{ fontSize: 17 }}>
          Self-service provisioning, tier entitlements, and the idempotent one-line installer for the sovereign
          reasoning engine (OCI container · port 8092).
        </p>
        <div className="alert info">
          <strong>Early Access.</strong> Licensing activation below is a functional mock that mirrors the Lemon Squeezy
          webhook + master-license-key flow. Production billing is wired by the human worker during Vercel project setup.
        </div>
      </section>

      <section className="section">
        <h2>One-line installer</h2>
        <p className="sub">Idempotent. Deploys the engine as a standalone container on your own infrastructure. No telemetry egress.</p>
        <div className="code" style={{ display: 'flex', justifyContent: 'space-between', gap: 12, alignItems: 'center' }}>
          <span style={{ flex: 1 }}>{INSTALL_COMMAND}</span>
          <button className="btn ghost" onClick={copyInstall} style={{ flexShrink: 0 }}>{copied ? 'Copied' : 'Copy'}</button>
        </div>
      </section>

      <section className="section">
        <h2>Tier entitlement matrix</h2>
        <p className="sub">Primary revenue lever: connector count × tier — mirroring the TrustGuard licensing rails on a single entitlement backbone.</p>
        <div style={{ overflowX: 'auto' }}>
          <table className="matrix">
            <thead>
              <tr>
                <th>Capability</th>
                {TIERS.map((t) => <th key={t.id}>{t.name}</th>)}
              </tr>
            </thead>
            <tbody>
              <FeatureRow label={MATRIX_ROWS[0].label} tiers={TIERS} get={(t) => t.connectors} />
              <FeatureRow label={MATRIX_ROWS[1].label} tiers={TIERS} get={(t) => t.features.reasoningCore} />
              <FeatureRow label={MATRIX_ROWS[2].label} tiers={TIERS} get={(t) => t.features.iacGeneration} />
              <FeatureRow label={MATRIX_ROWS[3].label} tiers={TIERS} get={(t) => t.features.tokenShield} />
              <FeatureRow label={MATRIX_ROWS[4].label} tiers={TIERS} get={(t) => t.features.autonomousExecution} />
              <FeatureRow label={MATRIX_ROWS[5].label} tiers={TIERS} get={(t) => t.features.auditLedger} />
            </tbody>
          </table>
        </div>
      </section>

      <section className="section">
        <h2>Pricing</h2>
        <div className="grid cols-5">
          {TIERS.map((t) => (
            <div className={'tier' + (t.highlight ? ' highlight' : '')} key={t.id}>
              <div className="name">{t.name}</div>
              <div className="price">{t.price} <small>{t.period}</small></div>
              <div className="tagline">{t.tagline}</div>
              <div><span className="badge">{t.connectors === '∞' ? 'Unlimited connectors' : `${t.connectors} connectors`}</span></div>
            </div>
          ))}
        </div>
      </section>

      <section className="section">
        <h2>Self-service console</h2>
        <p className="sub">Provision a license key and entitlement (mock).</p>
        <div className="card" style={{ maxWidth: 520 }}>
          <form className="form" onSubmit={activate}>
            <div>
              <label htmlFor="email">Work email</label>
              <input id="email" type="email" required placeholder="operator@yourco.com" value={email} onChange={(e) => setEmail(e.target.value)} />
            </div>
            <div>
              <label htmlFor="tier">Tier</label>
              <select id="tier" value={tier} onChange={(e) => setTier(e.target.value)}>
                {TIERS.map((t) => <option key={t.id} value={t.id}>{t.name}</option>)}
              </select>
            </div>
            <button className="btn primary" type="submit" disabled={loading}>
              {loading ? 'Provisioning…' : 'Activate license'}
            </button>
          </form>
          {result && (
            <div className="alert" style={{ marginTop: 16, borderColor: result.ok ? 'rgba(52,211,153,.4)' : 'rgba(248,113,113,.4)' }}>
              {result.ok ? (
                <div>
                  <div><strong>License key:</strong> <span className="code" style={{ display: 'inline-block', padding: '4px 10px' }}>{result.licenseKey}</span></div>
                  <div style={{ marginTop: 6 }}><strong>Tier:</strong> {result.tier} · <strong>Status:</strong> {result.status}</div>
                  <div style={{ marginTop: 6, color: 'var(--muted)', fontSize: 13 }}>{result.note}</div>
                </div>
              ) : (
                <div>{result.note}</div>
              )}
            </div>
          )}
        </div>
      </section>
    </main>
  )
}
