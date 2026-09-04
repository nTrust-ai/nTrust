/**
 * UserProfileCard.jsx (Weaver deliverable 2026-09-04) — TASK-B31DEE (Dashboard Core Authentication & User Profile Module)
 * Renders the verified session user's profile summary. No sensitive data (tokens/secrets) is ever surfaced.
 */
import React from 'react';
import { useAuth } from './AuthContext';

export function UserProfileCard({ className = '' }) {
  const { user } = useAuth();
  if (!user) return null;
  return (
    <section aria-label="Account" className={`user-profile ${className}`}>
      <h2 className="profile-name">{user.name}</h2>
      <p className="profile-email">{user.email}</p>
      {user.organization ? <p className="profile-org">{user.organization}</p> : null}
      {Array.isArray(user.roles) && user.roles.length > 0 ? (
        <ul className="profile-roles" aria-label="Permissions">
          {user.roles.map((role) => (
            <li key={role} className="role-chip">
              {role}
            </li>
          ))}
        </ul>
      ) : null}
    </section>
  );
}
