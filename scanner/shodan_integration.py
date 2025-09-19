# scanner/shodan_integration.py
import os
try:
    import shodan
except Exception:
    shodan = None

def shodan_lookup(ip_or_host):
    key = os.getenv("SHODAN_API_KEY")
    if not key or not shodan:
        return {"error": "Shodan not configured or library missing."}
    api = shodan.Shodan(key)
    try:
        return api.host(ip_or_host)
    except shodan.APIError as e:
        return {"error": str(e)}
