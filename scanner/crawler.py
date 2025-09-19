# scanner/crawler.py
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import tldextract

def same_domain(a, b):
    return tldextract.extract(a).registered_domain == tldextract.extract(b).registered_domain

def crawl(start_url, max_pages=50):
    seen = set()
    queue = [start_url]

    while queue and len(seen) < max_pages:
        url = queue.pop(0)
        if url in seen:
            continue
        seen.add(url)

        from scanner.http_client import fetch
        res = fetch(url)
        if not res.get("text"):
            continue
        soup = BeautifulSoup(res["text"], "html.parser")
        for a in soup.find_all('a', href=True):
            href = a['href']
            # normalize
            next_url = urljoin(url, href)
            if next_url not in seen and same_domain(start_url, next_url):
                queue.append(next_url)
    return list(seen)
