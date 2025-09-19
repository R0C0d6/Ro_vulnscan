# scanner/http_client.py
import requests
from urllib.parse import urljoin

DEFAULT_HEADERS = {
    "User-Agent": "VulnScan/1.0 (+https://github.com/yourname/vulnscan)"
}

def fetch(url, allow_redirects=True, timeout=10):
    try:
        r = requests.get(url, headers=DEFAULT_HEADERS, allow_redirects=allow_redirects, timeout=timeout, verify=False)
        return {
            "url": r.url,
            "status_code": r.status_code,
            "headers": dict(r.headers),
            "text": r.text,
            "ok": r.ok
        }
    except requests.RequestException as e:
        return {"url": url, "error": str(e)}
