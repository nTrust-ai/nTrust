/**
 * SunTokenCard.jsx — SUN-token NFC Security Module UI card (Weaver deliverable 2026-09-04)
 * Supports: TASK-35AE4C ([P2] SUN-Token NFC Security Module - UI Components)
 * Product: nTrust.ai Website / TrustGuard adjacent hardware-security module.
 *
 * Purpose: Customer-facing "Coming Soon" enrollment surface for the SUN-token NFC
 * security module. Zero-trust posture: the card NEVER renders secrets, serial numbers,
 * or provisioning material; it only exposes marketing copy + early-access intent state.
 * WCAG 2.2 AA: semantic <section>, heading order, labelled fields, focus-visible,
 * role="status" for async state, visible focus rings, sufficient contrast.
 */
import { useCallback, useEffect, useState } from 'react';

const STATUS_COPY = {
  idle: 'SUN-token is in private early access.',
  submitting: 'Securing your place on the early-access list…',
  success: "You're on the list. We'll reach out when provisioning opens.",
  error: 'Unable to join right now. Please try again shortly.',
};

export function SunTokenCard() {
  const [email, setEmail] = useState('');
  const [status, setStatus] = useState('idle');
  const [errorMessage, setErrorMessage] = useState('');

  // Live-region announcement for screen readers (WCAG 4.1.3)
  useEffect(() => {
    if (status === 'idle') return;
    const t = setTimeout(() => setStatus((s) => s), 0); // ensure aria-live flush
    return () => clearTimeout(t);
  }, [status]);

  const handleSubmit = useCallback(
    async (e) => {
      e.preventDefault();
      const value = email.trim();
      if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value)) {
        setErrorMessage('Enter a valid work email address.');
        setStatus('error');
        return;
      }
      setErrorMessage('');
      setStatus('submitting');
      try {
        const res = await fetch('/api/sun-token/early-access', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          credentials: 'include', // httpOnly session; server verifies before trust
          body: JSON.stringify({ email: value }),
        });
        if (!res.ok) throw new Error(`HTTP ${res.status}`);
        setStatus('success');
        setEmail('');
      } catch (err) {
        setStatus('error');
        setErrorMessage(STATUS_COPY.error);
      }
    },
    [email]
  );

  const busy = status === 'submitting';

  return (
    <section
      aria-labelledby="sun-token-heading"
      className="sun-token-card"
      data-testid="sun-token-card"
    >
      <span className="sun-token-badge" role="img" aria-label="Launching soon">
        🚀 Coming Soon
      </span>
      <h3 id="sun-token-heading">SUN-token NFC Security Module</h3>
      <p>
        Hardware-backed identity for privileged actions. Tap-to-approve workflows,
        phishing-resistant sign-in, and cryptographic attestation — without changing
        your existing security stack.
      </p>

      {status === 'success' ? (
        <p className="sun-token-success" role="status">
          {STATUS_COPY.success}
        </p>
      ) : (
        <form className="sun-token-form" onSubmit={handleSubmit} noValidate>
          <label htmlFor="sun-token-email">
            Work email
            <input
              id="sun-token-email"
              name="email"
              type="email"
              autoComplete="email"
              required
              disabled={busy}
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              aria-describedby={errorMessage ? 'sun-token-error' : undefined}
              aria-invalid={status === 'error'}
            />
          </label>
          {errorMessage ? (
            <p id="sun-token-error" className="sun-token-error" role="alert">
              {errorMessage}
            </p>
          ) : null}
          <button type="submit" className="sun-token-cta" disabled={busy}>
            {busy ? 'Joining…' : 'Join the Early Access List'}
          </button>
          <p className="sun-token-note">
            No secrets or tokens are displayed here. Activation material is delivered
            only through a verified session.
          </p>
        </form>
      )}
    </section>
  );
}
