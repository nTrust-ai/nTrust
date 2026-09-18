#!/bin/bash
echo "=== Git Status Check ==="
git status 2>&1 || echo "Git not initialized or error"
echo ""
echo "=== Remote URLs ==="
git remote -v 2>&1 || echo "No remotes configured"
echo ""
echo "=== Branch ==="
git branch -a 2>&1 || echo "Error checking branches"
echo ""
echo "=== Workspace Files ==="
ls -la
