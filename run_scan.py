# run_scan.py
import argparse
from scanner.crawler import crawl
from scanner.http_client import fetch
from scanner.header_checks import check_security_headers
from scanner.owasp_checks import scan_source_for_patterns
from scanner.ssl_checks import get_tls_info
from scanner.shodan_integration import shodan_lookup
from scanner.report import render_html, render_pdf
import socket
from urllib.parse import urlparse
import tldextract
import os

def default_severity_map():
    return {"Critical": 4, "High": 3, "Medium": 2, "Low": 1, "Info": 0}

def score_findings(findings):
    # simple scoring example: higher total = worse
    map_ = default_severity_map()
    score = 0
    for f in findings:
        s = map_.get(f.get("severity","Info"), 0)
        score += s
    return score

def run(target, max_pages=30, use_shodan=False):
    print(f"[+] Crawling {target} ...")
    pages = crawl(target, max_pages=max_pages)
    print(f"[+] Found {len(pages)} pages.")
    all_results = []
    for p in pages:
        res = fetch(p)
        url = res.get("url", p)
        headers = res.get("headers", {})
        text = res.get("text", "")
        header_findings = check_security_headers(headers)
        pattern_findings = scan_source_for_patterns(text or "")
        # SSL info for host (only once per domain)
        parsed = urlparse(p)
        host = parsed.hostname
        sslinfo = get_tls_info(p) if parsed.scheme == "https" else {}
        combined = header_findings + pattern_findings
        severity_score = score_findings(combined)
        shodan_info = None
        if use_shodan:
            try:
                shodan_info = shodan_lookup(host)
            except Exception as e:
                shodan_info = {"error": str(e)}
        all_results.append({
            "url": url,
            "headers": headers,
            "findings": combined,
            "severity_score": severity_score,
            "ssl": sslinfo,
            "shodan": shodan_info
        })
    # aggregate summary
    total_score = sum([r["severity_score"] for r in all_results])
    report = {
        "target": target,
        "summary_score": total_score,
        "results": all_results
    }
    html = render_html(report, out_path="vuln_report.html")
    try:
        pdf = render_pdf(html, pdf_path="vuln_report.pdf")
        print("[+] PDF report written to", pdf)
    except Exception as e:
        print("[!] PDF generation failed:", e)
    print("[+] HTML report written to", html)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="VulnScan - simple scanner")
    parser.add_argument("target", help="Target (eg https://example.com)")
    parser.add_argument("--pages", type=int, default=20)
    parser.add_argument("--shodan", action="store_true")
    args = parser.parse_args()
    run(args.target, max_pages=args.pages, use_shodan=args.shodan)
