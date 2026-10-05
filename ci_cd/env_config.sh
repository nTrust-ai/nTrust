#!/bin/bash
# nTrust.ai CI/CD Environment Configuration
# Provisioned: 2026-09-12T19:35:00Z
# Requestor: DevArchitect (System Optimizer)
# Context: Unblocking TASK-E1F4B6, TASK-7C1A35, TASK-8F5300 & Cloudflare Pages Deployments

export GITHUB_PAT="${GITHUB_TOKEN:-}"
export CLOUDFLARE_API_TOKEN="${CLOUDFLARE_API_TOKEN:-}"
export CF_ACCOUNT_ID="${CF_ACCOUNT_ID:-}"
export CF_ZONE_ID="${CF_ZONE_ID:-}"

# Git Remote Configuration
export GIT_ORIGIN="https://github.com/ntrust-ai/ntrust.git"
export GIT_BRANCH="main"
export GIT_USER_NAME="DevArchitect"
export GIT_USER_EMAIL="devarchitect@ntrust.ai"

echo "Environment vars set. CI/CD pipeline ready pending RBAC WRITE elevation (apr_c0aac938)."