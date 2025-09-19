# scanner/owasp_checks.py
import re

# simple patterns to look for in page source
XSS_PATTERNS = [
    r"<script.*?>",  # inline scripts found (not always bad)
    r"onerror\s*=",  # image onerror handlers
    r"document\.cookie"
]

SQLI_PATTERNS = [
    r"select\s+.*\s+from", 
    r"union\s+select",
    r"information_schema"
]

def scan_source_for_patterns(text):
    findings = []
    lowered = text.lower()
    # XSS hints
    for pat in XSS_PATTERNS:
        if re.search(pat, lowered):
            findings.append({"type": "XSS hint", "pattern": pat, "severity": "Medium"})
    for pat in SQLI_PATTERNS:
        if re.search(pat, lowered):
            findings.append({"type": "SQLi hint", "pattern": pat, "severity": "High"})
    return findings
