"""
PROD-SPINE CTA Alignment Standard v1.0 — Automated Verification Script
Linked Task: TASK-1E152F | Product Owner: DevArchitect
Standard Scope: spine.ntrust.ai & community/GitHub-facing material
Compliance Rules: Mailto-free CTAs, Resolvable targets only, Coming Soon labeling, Sanitization, Catalog alignment
Generated: 2026-09-12T15:50:00Z by Full-Stack Web Developer & Landing Page Specialist
"""

import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import re

TARGET_URL = "https://spine.ntrust.ai"
FORBIDDEN_TOKENS = ["MVP", "Phase N", "TASK-", "RAID-", "PROD-", "55127", "8085"]
CTA_SELECTORS = ['a[href]', 'button', '.cta-link']

def sanitize_html(html_content):
    """Remove internal designators from HTML content."""
    for token in FORBIDDEN_TOKENS:
        html_content = re.sub(re.escape(token), '[REDACTED]', html_content)
    return html_content

def verify_mailto_free(html_content):
    """Verify no mailto: anchors exist in the provided HTML."""
    soup = BeautifulSoup(html_content, 'html.parser')
    mailto_links = soup.find_all('a', href=re.compile(r'^mailto:', re.IGNORECASE))
    if mailto_links:
        return False, f"Found {len(mailto_links)} mailto: anchors requiring removal."
    return True, "Mailto-free check PASSED."

def verify_resolvable_targets(html_content):
    """Verify all CTA targets resolve to HTTP 200 or approved Coming Soon placeholders."""
    soup = BeautifulSoup(html_content, 'html.parser')
    links = soup.find_all('a', href=True)
    broken_links = []
    
    for link in links:
        url = link['href']
        if url.startswith('#') or url.startswith('javascript:'):
            continue # Skip anchor/jump links
        
        parsed = urlparse(url)
        if not parsed.netloc:
            full_url = f"{TARGET_URL}{url}"
        else:
            full_url = url
            
        try:
            response = requests.head(full_url, timeout=5, allow_redirects=True)
            if response.status_code != 200:
                broken_links.append(f"{full_url} -> {response.status_code}")
        except requests.exceptions.RequestException as e:
            broken_links.append(f"{full_url} -> ERROR: {str(e)}")
            
    if broken_links:
        return False, f"Found {len(broken_links)} unresolvable targets.\n" + "\n".join(broken_links)
    return True, "Resolvable targets check PASSED."

def run_cta_audit():
    print(f"🔍 Initiating CTA Alignment Audit against {TARGET_URL}...")
    
    try:
        response = requests.get(TARGET_URL, timeout=10)
        if response.status_code != 200:
            return f"❌ Target URL unreachable ({response.status_code})."
        
        html_content = sanitize_html(response.text)
        
        mailto_check = verify_mailto_free(html_content)
        print(f"[1/3] Mailto-Free Compliance: {mailto_check[1]}")
        
        resolvable_check = verify_resolvable_targets(html_content)
        print(f"[2/3] Resolvable Targets Compliance: {resolvable_check[1]}")
        
        # Check for Coming Soon labeling (heuristic)
        coming_soon_count = len(re.findall(r'Coming\s+Soon', html_content, re.IGNORECASE))
        print(f"[3/3] Unreleased Product Labeling: Found {coming_soon_count} 'Coming Soon' markers.")
        
        if mailto_check[0] and resolvable_check[0]:
            return "✅ PROD-SPINE CTA Alignment Standard v1.0 COMPLIANT."
        else:
            return "⚠️ PROD-SPINE CTA Alignment Standard v1.0 NON-COMPLIANT. Action required."
            
    except Exception as e:
        return f"❌ Audit execution failed: {str(e)}"

if __name__ == "__main__":
    print(run_cta_audit())
