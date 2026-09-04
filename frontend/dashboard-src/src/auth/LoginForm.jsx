/**
 * LoginForm.jsx — Accessible, secure login form (WCAG 2.2 AA) (Weaver deliverable 2026-09-04)
 * Supports: TASK-6D2960 (Authentication System — Secure Login/Logout Flow), TASK-1D1912 (Dashboard Authentication & Security Layer)
 *
 * - Labels associated via htmlFor/id; visible focus states; error summary with role="alert".
 * - Rate-limit hint surfaced from server; no internal codes or identifiers in UI copy.
 */
import React, { useState } from 'react';
import { useAuth } from './AuthContext';

export function LoginForm({ onSuccess, className = '' }) {
  const { login } = useAuth();
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [showPassword, setShowPassword] = useState(false);
  const [error, setError] = useState(null);
  const [submitting, setSubmitting] = useState(false);

  async function handleSubmit(e) {
    e.preventDefault();
    setError(null);
    if (!email || !password) {
      setError('Please enter both your email address and password.');
      return;
    }
    setSubmitting(true);
    try {
      const user = await login({ email, password });
      if (onSuccess) onSuccess(user);
    } catch (err) {
      setError(err.message || 'Unable to sign in. Please try again.');
    } finally {
      setSubmitting(false);
    }
  }

  return (
    <form onSubmit={handleSubmit} className={`login-form ${className}`} noValidate>
      {error && (
        <p role="alert" className="form-error" data-testid="login-error">
          {error}
        </p>
      )}
      <div className="field">
        <label htmlFor="login-email">Work email</label>
        <input
          id="login-email"
          name="email"
          type="email"
          autoComplete="email"
          required
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />
      </div>
      <div className="field">
        <label htmlFor="login-password">Password</label>
        <input
          id="login-password"
          name="password"
          type={showPassword ? 'text' : 'password'}
          autoComplete="current-password"
          required
          minLength={8}
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        <button
          type="button"
          className="link-btn"
          aria-pressed={showPassword}
          onClick={() => setShowPassword((v) => !v)}
        >
          {showPassword ? 'Hide password' : 'Show password'}
        </button>
      </div>
      <button type="submit" className="btn btn-primary" disabled={submitting}>
        {submitting ? 'Signing in…' : 'Sign in'}
      </button>
    </form>
  );
}
