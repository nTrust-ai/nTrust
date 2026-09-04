/**
 * SunTokenPanel.jsx — SUN-token NFC Security Module UI (Weaver deliverable 2026-09-04)
 * Supports: TASK-35AE4C (SUN-token NFC Security Module — UI Components)
 *
 * Customer-facing, sanitized copy. Accessible tap simulation; real integration points
 * to the NFC reader API are stubbed behind `onTap`/`status` props (server-driven).
 */
import React, { useState } from 'react';

export function SunTokenPanel({
  onTap,
  status = 'ready', // ready | verifying | verified | error | not-supported
  deviceName = 'SUN-token · NFC security key',
  className = '',
}) {
  const [localStatus, setLocalStatus] = useState(status);
  const [errorMsg, setErrorMsg] = useState('');

  const isBusy = localStatus === 'verifying';
  const statusText = {
    ready: 'Tap your security key to authenticate.',
    verifying: 'Verifying your security key…',
    verified: 'Security key verified. Session trust established.',
    error: 'Verification failed. Hold the key closer and try again.',
    'not-supported': 'NFC is not supported on this device.',
  }[localStatus];

  async function handleTap() {
    if (isBusy) return;
    setErrorMsg('');
    setLocalStatus('verifying');
    try {
      if (onTap) {
        await onTap();
      } else {
        await new Promise((r) => setTimeout(r, 900)); // demo latency
      }
      setLocalStatus('verified');
    } catch (err) {
      setLocalStatus('error');
      setErrorMsg(err?.message || '');
    }
  }

  return (
    <section className={`sun-token-panel ${className}`} aria-labelledby="sun-token-heading">
      <h2 id="sun-token-heading" className="sun-token-panel__title">
        Hardware-backed Authentication
      </h2>
      <p className="sun-token-panel__intro">
        Add a physical security key for phishing-resistant, zero-trust sign-in.
      </p>

      <div className="sun-token-card">
        <div className="sun-token-card__visual" aria-hidden="true">
          <span className="sun-token-card__nfc">NFC</span>
        </div>
        <div className="sun-token-card__meta">
          <strong>{deviceName}</strong>
          <span className="sun-token-card__status">{statusText}</span>
          {localStatus === 'error' && errorMsg ? (
            <span className="sun-token-card__error" role="alert">
              {errorMsg}
            </span>
          ) : null}
        </div>
        <button
          type="button"
          className="ntrust-btn ntrust-btn--ghost"
          onClick={handleTap}
          disabled={isBusy || localStatus === 'not-supported'}
        >
          {isBusy ? 'Verifying…' : 'Simulate tap'}
        </button>
      </div>

      <ul className="sun-token-panel__notes">
        <li>Requires a compatible NFC reader and a verified security key.</li>
        <li>Keys are bound to your account and can be revoked at any time.</li>
        <li>No key material ever leaves the device.</li>
      </ul>
    </section>
  );
}

export default SunTokenPanel;
