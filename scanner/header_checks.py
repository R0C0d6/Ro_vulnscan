# scanner/header_checks.py
SECURITY_HEADERS = {
    "Content-Security-Policy": "CSP helps prevent XSS and data injection.",
    "Strict-Transport-Security": "HSTS forces browsers to use HTTPS.",
    "X-Frame-Options": "Prevents clickjacking.",
    "X-Content-Type-Options": "Stops content sniffing (nosniff).",
    "Referrer-Policy": "Controls what referrer data is sent.",
    "Permissions-Policy": "Limits browser features."
}

def check_security_headers(headers):
    findings = []
    for name, desc in SECURITY_HEADERS.items():
        if name not in headers:
            findings.append({
                "type": "Missing Header",
                "header": name,
                "description": desc,
                "severity": "Medium" if name in ["Content-Security-Policy","Strict-Transport-Security"] else "Low"
            })
    # additional checks
    if "Server" in headers and "cloudflare" not in headers.get("Server","").lower():
        # revealing Server header could be info disclosure
        findings.append({
            "type": "Info Disclosure",
            "header": "Server",
            "description": f"Server header reveals {headers.get('Server')}",
            "severity": "Low"
        })
    return findings
