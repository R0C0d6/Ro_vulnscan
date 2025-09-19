# scanner/ssl_checks.py
import socket, ssl
from urllib.parse import urlparse

def get_tls_info(url, port=None, timeout=5):
    parsed = urlparse(url)
    hostname = parsed.hostname or url
    port = port or (parsed.port or 443)
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    try:
        with socket.create_connection((hostname, port), timeout=timeout) as sock:
            with ctx.wrap_socket(sock, server_hostname=hostname) as ssock:
                cipher = ssock.cipher()
                cert = ssock.getpeercert()
                return {
                    "hostname": hostname,
                    "port": port,
                    "cipher": cipher,
                    "cert": cert
                }
    except Exception as e:
        return {"error": str(e)}
