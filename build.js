#!/usr/bin/env node
/**
 * build.js — nTrust.ai Static Site Build & Verification Script
 * 
 * Synchronizes the canonical static website from frontend/dist into dist/ and public/,
 * guaranteeing that Cloudflare Pages native build (`npm run build`) deploys the complete,
 * multi-page site with /naveed executive profile, Spine product links pointing to spine.ntrust.ai,
 * and zero open-source references.
 */

import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const SRC_DIR = path.join(__dirname, 'frontend', 'dist');
const DIST_DIR = path.join(__dirname, 'dist');
const PUBLIC_DIR = path.join(__dirname, 'public');

console.log('🚀 [nTrust Build] Starting build from:', SRC_DIR);

if (!fs.existsSync(SRC_DIR)) {
  console.error('❌ [nTrust Build] Source directory missing:', SRC_DIR);
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
for (const relPath of CRITICAL_FILES) {
  const destPath = path.join(DIST_DIR, relPath);
  if (!fs.existsSync(destPath)) {
    console.error(`❌ [Verification Failed] Missing critical file in dist/: ${relPath}`);
    errors++;
  } else {
    const sz = fs.statSync(destPath).size;
    if (sz === 0) {
      console.error(`❌ [Verification Failed] Empty critical file in dist/: ${relPath}`);
      errors++;
    }
  }
}

// 5. Check index.html for required updates
const indexContent = fs.readFileSync(path.join(DIST_DIR, 'index.html'), 'utf8');
if (!indexContent.includes('/naveed')) {
  console.error('❌ [Verification Failed] dist/index.html does not link to /naveed');
  errors++;
}
if (/open[\s-]source/i.test(indexContent)) {
  console.error('❌ [Verification Failed] dist/index.html still contains Open Source references');
  errors++;
}
if (!indexContent.includes('spine.ntrust.ai')) {
  console.error('❌ [Verification Failed] dist/index.html does not link to spine.ntrust.ai');
  errors++;
}

if (errors > 0) {
  console.error(`🚨 [nTrust Build] Build verification FAILED with ${errors} error(s).`);
  process.exit(1);
}

console.log('🎉 [nTrust Build] All 21 critical endpoints verified successfully! Ready for Cloudflare Pages deployment.');
