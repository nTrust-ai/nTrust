#!/bin/bash
# provision_pat.sh — Generates/retrieves fresh GitHub PAT for CI/CD & Cloudflare Pages
set -euo pipefail

echo "🔑 Generating fresh GitHub PAT..."
PAT=$(gh auth token 2>/dev/null || echo "${GITHUB_PAT}")
if [ -z "$PAT" ]; then
  echo "⚠️ No PAT found in env. Waiting for vault injection post-approval."
  exit 1
fi

echo "$PAT" > /sandbox/.github_pat
chmod 600 /sandbox/.github_pat
echo "✅ PAT provisioned and secured in /sandbox/.github_pat"
