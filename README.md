# TLS Certificate Check

Ein kleines Python-Skript, das für eine Liste von Domains die SSL/TLS-Zertifikate
abfragt und das Ablaufdatum prüft. So lassen sich Zertifikate identifizieren,
die bald ablaufen und ein Risiko für Verfügbarkeit und Vertrauenswürdigkeit darstellen.

## Use-Case

Das Skript unterstützt bei der Überwachung von SSL/TLS-Zertifikaten, z. B. für
Websites oder APIs. Für jede Domain wird das Ablaufdatum des Zertifikats ermittelt
und ein Status ausgegeben:

- **OK**: Zertifikat läuft in mehr als 30 Tagen ab.
- **WARNUNG**: Zertifikat läuft in weniger als 30 Tagen ab.
- **ABGELAUFEN**: Zertifikat ist bereits abgelaufen.

Das Tool kann als einfache Ergänzung zu regelmäßigen Sicherheits- und
Verfügbarkeitschecks eingesetzt werden.

## Hinweis

Das Skript nutzt Standardbibliotheken von Python (`ssl`, `socket`, `datetime`)
und kann ohne zusätzliche Abhängigkeiten ausgeführt werden. Die Datei `domains.txt`
enthält Beispiel-Domains und kann nach Bedarf angepasst werden.

## Verwendung

1. Python 3 installieren.
2. Repository lokal klonen oder als ZIP herunterladen.
3. Im Projektordner die Datei `domains.txt` anpassen (Domains pro Zeile).
4. Skript ausführen:

```bash
python cert_check.py
