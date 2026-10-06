#!/usr/bin/env node
/**
 * build.js — nTrust.ai Static Site Build & Verification Script
 * 
 * Synchronizes the canonical static website from frontend/dist into dist/ and public/,
 * guaranteeing that Cloudflare Pages native build (`npm run build`) deploys the complete,
 * multi-page site with /naveed executive profile, Spine product links pointing to spine.ntrust.ai,
 * and zero open-source references.
 * 
 * If a build failure occurs, automatically sends an incident alert to Atlas (DevOps Director)
 * via SendGrid using SENDGRID_API_KEY.
 */

import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const SRC_DIR = path.join(__dirname, 'frontend', 'dist');
const DIST_DIR = path.join(__dirname, 'dist');
const PUBLIC_DIR = path.join(__dirname, 'public');

function escapeHtml(str) {
  if (!str) return '';
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#039;');
}

async function sendBuildFailureAlert(summary, details = []) {
  const apiKey = (process.env.SENDGRID_API_KEY || '').trim();
  if (!apiKey) {
    console.warn('⚠️ [nTrust Build Alert] SENDGRID_API_KEY not configured in build environment. Skipping alert email.');
    return;
  }

  const commitSha = process.env.CF_PAGES_COMMIT_SHA || process.env.COMMIT_HASH || 'Local / Unknown';
  const branch = process.env.CF_PAGES_BRANCH || 'main';
  const fromEmail = (process.env.SENDGRID_FROM_EMAIL || 'noreply@ntrust.ai').trim();
  const toRecipients = [
    { email: 'atlas@ntrust.ai', name: 'Atlas (DevOps Director)' },
    { email: 'naveed@ntrust.ai', name: 'Naveed ul Islam' }
  ];

  const timestamp = new Date().toUTCString();
  const subject = `🚨 [CF Pages Build Failed] ntrust.ai build failed on branch '${branch}' (${commitSha.slice(0, 7)})`;

  const detailsListHtml = details.length > 0
    ? `<ul>${details.map(d => `<li style="color:#ef4444;font-family:monospace;margin-bottom:4px;">${escapeHtml(d)}</li>`).join('')}</ul>`
    : `<p style="font-family:monospace;color:#ef4444;">${escapeHtml(summary)}</p>`;

  const html = `
<!DOCTYPE html>
<html>
<head>
  <style>
    body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; line-height: 1.6; color: #1e293b; background: #0f172a; padding: 20px; }
    .card { max-width: 650px; margin: 0 auto; background: #ffffff; border-radius: 8px; overflow: hidden; border: 1px solid #e2e8f0; }
    .header { background: #991b1b; color: #ffffff; padding: 20px; }
    .header h2 { margin: 0; font-size: 20px; color: #ffffff; }
    .content { padding: 24px; color: #334155; }
    .meta-table { width: 100%; border-collapse: collapse; margin-bottom: 20px; }
    .meta-table td { padding: 6px 10px; border-bottom: 1px solid #f1f5f9; font-size: 14px; }
    .meta-table td.label { font-weight: 600; width: 140px; color: #64748b; background: #f8fafc; }
    .error-box { background: #fef2f2; border-left: 4px solid #ef4444; padding: 16px; border-radius: 4px; margin-bottom: 20px; }
    .footer { background: #f8fafc; padding: 14px 20px; font-size: 12px; color: #64748b; text-align: center; border-top: 1px solid #e2e8f0; }
  </style>
</head>
<body>
  <div class="card">
    <div class="header">
      <h2>🚨 Cloudflare Pages Build Failed</h2>
      <p style="margin:4px 0 0;font-size:13px;opacity:0.9;">Project: ntrust-ai | Target: Production</p>
    </div>
    <div class="content">
      <table class="meta-table">
        <tr><td class="label">Project</td><td>ntrust-ai (Cloudflare Pages)</td></tr>
        <tr><td class="label">Branch</td><td><strong>${escapeHtml(branch)}</strong></td></tr>
        <tr><td class="label">Commit SHA</td><td><code>${escapeHtml(commitSha)}</code></td></tr>
        <tr><td class="label">Triggered At</td><td>${timestamp}</td></tr>
        <tr><td class="label">Target Agent</td><td><strong>Atlas (DevOps & Infrastructure Director)</strong></td></tr>
      </table>

      <h3 style="color:#0f172a;margin-bottom:8px;">Failure Diagnostics:</h3>
      <div class="error-box">
        <strong>Summary:</strong> ${escapeHtml(summary)}
        ${detailsListHtml}
      </div>

      <div style="background:#f1f5f9;padding:12px;border-radius:6px;font-size:13px;">
        <strong>Actionable Remediation for Atlas:</strong>
        <ol style="margin:6px 0 0 16px;padding:0;">
          <li>Inspect the latest commit diff for regressions or missing files.</li>
          <li>Run <code>npm run build</code> locally in <code>data/orgs/org_ntrust/</code> to reproduce the error.</li>
          <li>Patch the issue, test locally, and push to <code>main</code>.</li>
        </ol>
      </div>
    </div>
    <div class="footer">
      Dispatched automatically by nTrust Build CI via SendGrid to atlas@ntrust.ai.
    </div>
  </div>
</body>
</html>
  `;

  try {
    console.log('📡 [nTrust Build Alert] Dispatching failure alert to atlas@ntrust.ai via SendGrid...');
    const res = await fetch('https://api.sendgrid.com/v3/mail/send', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${apiKey}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        personalizations: [{ to: toRecipients, subject }],
        from: { email: fromEmail, name: 'nTrust CI Build Watchdog' },
        content: [
          { type: 'text/html', value: html }
        ]
      })
    });

    if (res.status === 202 || res.status === 200) {
      console.log('✅ [nTrust Build Alert] Build failure email delivered successfully to atlas@ntrust.ai!');
    } else {
      const err = await res.text().catch(() => '');
      console.error(`❌ [nTrust Build Alert] SendGrid API returned status ${res.status}:`, err);
    }
  } catch (e) {
    console.error('❌ [nTrust Build Alert] Failed to dispatch failure email:', e.message);
  }
}

// Global crash handlers
process.on('uncaughtException', async (err) => {
  const msg = err && err.stack ? err.stack : String(err);
  console.error('💥 [Uncaught Exception in Build]', msg);
  await sendBuildFailureAlert(`Uncaught exception in build: ${err.message || err}`, [msg]);
  process.exit(1);
});

process.on('unhandledRejection', async (reason) => {
  const msg = String(reason);
  console.error('💥 [Unhandled Rejection in Build]', msg);
  await sendBuildFailureAlert(`Unhandled rejection in build: ${msg}`, [msg]);
  process.exit(1);
});

console.log('🚀 [nTrust Build] Starting build from:', SRC_DIR);

if (!fs.existsSync(SRC_DIR)) {
  const msg = `Source directory missing: ${SRC_DIR}`;
  console.error('❌ [nTrust Build]', msg);
  await sendBuildFailureAlert(msg, [msg]);
  process.exit(1);
}

function copyRecursiveSync(src, dest) {
  const exists = fs.existsSync(src);
  const stats = exists && fs.statSync(src);
  const isDirectory = exists && stats.isDirectory();
  if (isDirectory) {
    if (!fs.existsSync(dest)) {
      fs.mkdirSync(dest, { recursive: true });
    }
    fs.readdirSync(src).forEach((childItemName) => {
      copyRecursiveSync(path.join(src, childItemName), path.join(dest, childItemName));
    });
  } else {
    fs.mkdirSync(path.dirname(dest), { recursive: true });
    fs.copyFileSync(src, dest);
  }
}

// 1. Clean & populate dist
if (!fs.existsSync(DIST_DIR)) {
  fs.mkdirSync(DIST_DIR, { recursive: true });
}
copyRecursiveSync(SRC_DIR, DIST_DIR);
console.log('✅ [nTrust Build] Synchronized frontend/dist -> dist/');

// 2. Mirror to public/ as fail-safe
if (!fs.existsSync(PUBLIC_DIR)) {
  fs.mkdirSync(PUBLIC_DIR, { recursive: true });
}
copyRecursiveSync(SRC_DIR, PUBLIC_DIR);
console.log('✅ [nTrust Build] Synchronized frontend/dist -> public/');

// 3. Mirror canonical index.html to repo root index.html
const rootIndex = path.join(__dirname, 'index.html');
const canonicalIndex = path.join(SRC_DIR, 'index.html');
if (fs.existsSync(canonicalIndex)) {
  fs.copyFileSync(canonicalIndex, rootIndex);
  console.log('✅ [nTrust Build] Updated repo root index.html to canonical homepage');
}

// 4. Critical File Verification Gate
const CRITICAL_FILES = [
  'index.html',
  'about.html',
  'pricing.html',
  'contact.html',
  'spine.html',
  'assets/site.css',
  'naveed/index.html',
  '_redirects',
  '_headers',
  'robots.txt',
  'sitemap.xml',
  'products/index.html',
  'products/trustguard.html',
  'products/tokenshield.html',
  'products/enterprise-security-audit.html',
  'products/privacyguard.html',
  'products/trustaudit.html',
  'products/ntrust-shield.html',
  'products/sun-token.html',
  'products/managed-appsec.html',
  'products/ntrust-core.html',
  'products/portal.html'
];

let errors = 0;
const failureDetails = [];

for (const relPath of CRITICAL_FILES) {
  const destPath = path.join(DIST_DIR, relPath);
  if (!fs.existsSync(destPath)) {
    const msg = `Missing critical file in dist/: ${relPath}`;
    console.error(`❌ [Verification Failed] ${msg}`);
    failureDetails.push(msg);
    errors++;
  } else {
    const sz = fs.statSync(destPath).size;
    if (sz === 0) {
      const msg = `Empty critical file in dist/: ${relPath}`;
      console.error(`❌ [Verification Failed] ${msg}`);
      failureDetails.push(msg);
      errors++;
    }
  }
}

// 5. Check index.html for required updates
const indexContent = fs.readFileSync(path.join(DIST_DIR, 'index.html'), 'utf8');
if (!indexContent.includes('/naveed')) {
  const msg = 'dist/index.html does not link to /naveed';
  console.error(`❌ [Verification Failed] ${msg}`);
  failureDetails.push(msg);
  errors++;
}
if (/open[\s-]source/i.test(indexContent)) {
  const msg = 'dist/index.html still contains Open Source references';
  console.error(`❌ [Verification Failed] ${msg}`);
  failureDetails.push(msg);
  errors++;
}
if (!indexContent.includes('spine.ntrust.ai')) {
  const msg = 'dist/index.html does not link to spine.ntrust.ai';
  console.error(`❌ [Verification Failed] ${msg}`);
  failureDetails.push(msg);
  errors++;
}

if (errors > 0) {
  const summary = `Build verification FAILED with ${errors} error(s).`;
  console.error(`🚨 [nTrust Build] ${summary}`);
  await sendBuildFailureAlert(summary, failureDetails);
  process.exit(1);
}

console.log('🎉 [nTrust Build] All 22 critical endpoints verified successfully! Ready for Cloudflare Pages deployment.');
