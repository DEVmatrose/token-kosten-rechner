# Token Kosten-Rechner | GPU zu Gewinn 🚀

<img width="1072" height="1178" alt="image" src="https://github.com/user-attachments/assets/7bdcf1eb-0448-41db-b16d-ab2a8550b9c5" />

Berechne deine GPU-Token-Kosten und Gewinnmarge in Echtzeit mit **automatisch aktualisierten Live-Preisen** von 5 GPU-Anbietern.

## ✨ Features

- **🎯 Live GPU-Preise**: Automatisch aktualisierte Preise von 5 großen Anbietern (4x täglich)
- **💰 Echtzeit-Kalkulation**: Sofortige Berechnung von Kosten, Verkauf und Gewinn
- **📊 Durchsatz-Analyse**: Token pro Sekunde, Minute und Stunde bei Volllast
- **🧾 MwSt.-Berechnung**: Automatische Netto/Brutto-Umrechnung
- **🎨 Modernes Design**: Responsive UI mit Tailwind CSS und Vue.js

## 🤖 Automatische Preis-Updates

Die GPU-Preise werden automatisch via GitHub Actions aktualisiert:
- **Frequenz**: 4x täglich (00:00, 06:00, 12:00, 18:00 UTC)
- **Quellen**: Vast.ai (Live-API), RunPod, Scaleway, SaladCloud, lokale Stromkosten
- **Transparenz**: Jeder Update-Zeitstempel ist in `data/prices.json` dokumentiert

### Manuelle Preis-Aktualisierung

```bash
python scripts/fetch_prices.py
```

## 🛠️ Technologie-Stack

- **Frontend**: Vue.js 3 (CDN)
- **Styling**: Tailwind CSS (CDN)
- **Backend**: Python 3.11 (Preis-Scraper)
- **CI/CD**: GitHub Actions
- **Hosting**: GitHub Pages ready

## 📦 Installation & Deployment

### Lokale Entwicklung

1. Repository klonen:
```bash
git clone https://github.com/DEVmatrose/token-kosten-rechner.git
cd token-kosten-rechner
```

2. HTML-Datei öffnen:
```bash
# Mit Python HTTP-Server
python -m http.server 8000
# Oder einfach index.html im Browser öffnen
```

### GitHub Pages Deployment

1. Repository pushen
2. In Settings → Pages: Source auf `main` Branch setzen
3. Fertig! Deine Seite ist live unter: `https://devmatrose.github.io/token-kosten-rechner/`

## 🔧 Preis-Scraper erweitern

Neue Anbieter hinzufügen in `scripts/fetch_prices.py`:

```python
def fetch_neuer_anbieter() -> Dict:
    return {
        "name": "Anbieter Name",
        "preis": 0.50,  # €/Stunde
        "tps": 100,      # Token pro Sekunde
        "info": "Beschreibung",
        "last_update": datetime.utcnow().isoformat()
    }
```

## 📊 Anbieter-Übersicht (Stand 2026)

| Anbieter | Preis/h | Token/s | Besonderheit |
|----------|---------|---------|--------------|
| **Vast.ai** | 0,35 € | 90 | Günstigster Spot-Markt |
| **RunPod** | 0,45 € | 85 | Stabil, EU-verfügbar |
| **Scaleway** | 1,30 € | 120 | GDPR-konform, Enterprise |
| **SaladCloud** | 0,25 € | 70 | Consumer-Grid, volatil |
| **Lokal (RTX 5090)** | 0,28 € | 95 | Eigene Hardware (700W @ 0,40€/kWh) |

## 🚀 Live Demo


[https://devmatrose.github.io/token-kosten-rechner/](https://devmatrose.github.io/token-kosten-rechner/)

## 📋 Was macht es?

Ein einfacher Rechner um:
- GPU-Stundenkosten in Token-Preise umzurechnen
- Verkaufspreis (inkl. MwSt.) zu kalkulieren
- Gewinnmarge zu berechnen

## 🛠️ Technologie

- Pure HTML/CSS/JavaScript
- Vue.js 3 (CDN)
- Tailwind CSS (CDN)
- Keine Installation nötig

## 💻 Verwendung

Einfach `token-kosten-rechner.html` im Browser öffnen - fertig!

## 📦 GitHub Pages

Das Projekt läuft automatisch über GitHub Pages.

---

© 2026 DEVmatrose
