import socket
import ssl
from datetime import datetime
from typing import List

WARNING_DAYS = 30  # Warnschwelle in Tagen


def get_certificate_expiry(hostname: str, port: int = 443) -> datetime | None:
    """Holt das SSL-Zertifikat und gibt das Ablaufdatum zurück (oder None bei Fehler)."""
    try:
        context = ssl.create_default_context()
        with socket.create_connection((hostname, port), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()
        # 'notAfter' ist ein String wie 'Mar 10 12:00:00 2026 GMT'
        not_after_str = cert.get("notAfter")
        if not_after_str is None:
            return None
        return datetime.strptime(not_after_str, "%b %d %H:%M:%S %Y %Z")
    except Exception as e:
        print(f"[FEHLER] Konnte Zertifikat für {hostname} nicht prüfen: {e}")
        return None


def check_domains(domains: List[str]) -> None:
    today = datetime.utcnow()
    print(f"Stand: {today.isoformat()} UTC\n")

    for domain in domains:
        domain = domain.strip()
        if not domain:
            continue

        expiry = get_certificate_expiry(domain)
        if expiry is None:
            print(f"{domain}: Zertifikat konnte nicht ermittelt werden.\n")
            continue

        days_left = (expiry - today).days
        status = "OK"
        if days_left < 0:
            status = "ABGELAUFEN"
        elif days_left < WARNING_DAYS:
            status = "WARNUNG"

        print(f"{domain}:")
        print(f"  Ablaufdatum : {expiry}")
        print(f"  Resttage    : {days_left}")
        print(f"  Status      : {status}\n")


if __name__ == "__main__":
    # domains.txt einlesen
    try:
        with open("domains.txt", "r", encoding="utf-8") as f:
            domain_list = [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        print("Die Datei 'domains.txt' wurde nicht gefunden.")
        domain_list = []

    if not domain_list:
        print("Keine Domains zum Prüfen vorhanden.")
    else:
        check_domains(domain_list)
