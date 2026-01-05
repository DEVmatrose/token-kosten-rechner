# Token Kosten-Rechner | GPU zu Gewinn 🚀

Berechne deine GPU-Token-Kosten, Arbitrage-Marge und Credit-Pakete in Echtzeit mit **automatisch aktualisierten Live-Preisen** von 6 GPU-Anbietern.

<img width="1397" height="1261" alt="image" src="https://github.com/user-attachments/assets/27b4969e-d34c-4d92-87b7-704ebbfa4c7d" />


## ✨ Features

- **🎯 Live GPU-Preise**: Automatisch aktualisierte Preise von 6 Anbietern (4x täglich)
- **🎛️ Workload-Mix Slider**: Toggle zwischen Text- und Audio-Verarbeitung
- **🎤 Audio-Typ Auswahl**: Meeting (9k Tokens/h) vs. Podcast/Hörbuch (13,5k Tokens/h)
- **💎 Credit-Paket Kalkulator**: Automatische Kalkulation von 3 SaaS-Paketen mit dynamischen Margen
- **📊 Token-Gewichtung**: Audio-Tokens zählen 2x (höherer Marktwert)
- **💰 Echtzeit-Arbitrage**: Sofortige Berechnung von Kosten, Verkauf und Gewinn
- **🧾 MwSt.-Berechnung**: Automatische Netto/Brutto-Umrechnung
- **🎨 Modernes Design**: Responsive UI mit Tailwind CSS und Vue.js

## 🤖 Automatische Preis-Updates

Die GPU-Preise werden automatisch via GitHub Actions aktualisiert:
- **Frequenz**: 4x täglich (00:00, 06:00, 12:00, 18:00 UTC)
- **Quellen**: Vast.ai (Live-API), RunPod, Scaleway (L40S/H100), SaladCloud, lokale Stromkosten
- **Transparenz**: Jeder Update-Zeitstempel ist in `data/prices.json` dokumentiert

```bash
python scripts/fetch_prices.py
```

## 📊 Anbieter-Übersicht (Stand 2026)

| Anbieter | Preis/h | Token/s | GPU | Besonderheit |
|----------|---------|---------|-----|--------------|
| **Vast.ai** | 0,35 € | 90 | RTX 5090 | Günstigster Spot-Markt |
| **RunPod** | 0,45 € | 85 | RTX 4090 | Stabil, EU-verfügbar, gute API |
| **Scaleway L40S** | 1,30 € | 120 | L40S (48GB) | GDPR-konform, Enterprise |
| **Scaleway H100** | 2,90 € | 250 | H100 (80GB) | Ultra-schnell, Batch-Verarbeitung |
| **SaladCloud** | 0,25 € | 70 | Mixed | Consumer-Grid, volatile |
| **Lokal** | 0,28 € | 95 | RTX 5090 | Eigene Hardware (700W @ 0,40€/kWh) |

## 🎬 Workload-Mix & Token-Gewichtung

### Text-Tokens
- **1 Token** ≈ 3-4 Zeichen (Deutsch)
- **1 Seite** (A4) ≈ 450 Tokens (250-300 Wörter)
- **1 Std intensive Nutzung** ≈ 5.000 Tokens (Chat + Analyse)

### Audio-Tokens (2x Faktor)
- **Meeting (5-10 Personen)** ≈ 9.000 Tokens/Std (40-45 Min effektive Sprechzeit)
- **Podcast/Hörbuch** ≈ 13.500 Tokens/Std (kontinuierliches Sprechen)
- **Vollservice Meeting** ≈ 35.000 Tokens/Std (Videoserver-Hosting + Transkription + KI-Protokollierung)
  - 🖥️ Videoserver-Hosting: 1.000 Token/User/Std
  - 🎤 Audio-Transkription: 18.200 Token/Std
  - 🤖 KI-Protokollierung: 15.800 Token/Std
- **2x Gewichtung**: Audio-Tokens sind doppelt so teuer (höherer Marktwert)

**Beispiel bei 50/50 Mix:**
- Kunde kauft 1M Credits für 5€
- Bekommt: 500k Text-Tokens + 250k Audio-Tokens (wegen 2x Faktor)
- Entspricht: ~1.111 Seiten Text ODER ~28 Std Meetings

## 🎥 Video-Service-Strategie-Planer

Zusätzlich zum Token-Kosten-Rechner gibt es einen spezialisierten **Video-Service-Strategie-Planer** für Videokonferenz-Services:

<img width="1467" height="922" alt="image" src="https://github.com/user-attachments/assets/623d449f-d9b7-45c3-a4c4-86f75d4d44ea" />


### Features
- **📊 Server-Auslastung**: Berechnet CPU/RAM-Last für Jitsi Meet & BigBlueButton
- **💰 Wirtschaftlichkeits-Check**: Kalkulation von Selbstkosten vs. Endkundenpreise
- **👥 Skalierungs-Simulation**: Teste verschiedene Teilnehmerzahlen (1-500 User)
- **🎯 Entscheidungshilfe**: Vergleich Jitsi Meet vs. BigBlueButton Features

### Token-Abrechnung
- **Hosting**: 1.000 Token/User/Std (Abrechnung im **15-Minuten-Takt**, aufgerundet)
- **KI-Protokoll Pipeline** (optional, pro Stunde):
  - 🎥 FFmpeg Verarbeitung: 6.000 Token
  - 🎵 Rauschfilter & Stimmoptimierung: 7.000 Token
  - 🎤 Audio-zu-Text (STT): 13.000 Token
  - 📋 Voxtral Meetingprotokoll: 13.000 Token
  - **Gesamt KI**: 39.000 Token/Std

**Pauschale Abrechnung:** Jedes Meeting wird gleich abgerechnet, unabhängig davon, wie viel tatsächlich gesprochen wurde.

[→ Video-Service-Strategie-Planer öffnen](Video-Service-Strategie-Planer.html)

---

## 💎 Credit-Paket System

Verkaufe nicht Roh-Tokens, sondern **Credits** mit verschiedenen Paketen:

| Paket | Preis | Credits | Text | Audio (Meetings) |
|-------|-------|---------|------|-----------------|
| **Starter** | 29€ | 5M | ~5.555 Seiten | ~14 Std |
| **Business** | 99€ | 20M | ~22.222 Seiten | ~56 Std |
| **Pro/API** | 399€ | 100M | ~111.111 Seiten | ~278 Std |

*Bei 100% Audio-Workload; Werte werden dynamisch nach Slider-Position berechnet.*

## 🛠️ Technologie-Stack

- **Frontend**: Vue.js 3 (CDN) + Tailwind CSS (CDN)
- **Backend**: Python 3.11 (Preis-Scraper)
- **Hosting**: GitHub Pages
- **CI/CD**: GitHub Actions (automatische Updates)

## 📦 Installation & Deployment

### Lokale Entwicklung

```bash
# Repository klonen
git clone https://github.com/DEVmatrose/token-kosten-rechner.git
cd token-kosten-rechner

# Mit Python HTTP-Server starten
python -m http.server 8000

# Oder einfach index.html im Browser öffnen
```

### GitHub Pages Deployment

1. Repository in deinen Account forken
2. In Settings → Pages: Source auf `main` Branch setzen
3. Live unter: `https://<dein-username>.github.io/token-kosten-rechner/`

## 🔧 Preis-Scraper erweitern

Neue Anbieter in `scripts/fetch_prices.py` hinzufügen:

```python
def fetch_neuer_anbieter() -> Dict:
    return {
        "name": "Anbieter Name (GPU Modell)",
        "preis": 0.50,  # €/Stunde
        "tps": 100,      # Token pro Sekunde
        "info": "Beschreibung und Besonderheiten",
        "last_update": datetime.utcnow().isoformat()
    }
```

## 📝 Lizenz

MIT License - Nutze das Tool frei für kommerzielle und private Zwecke!

## 🌐 Links

- **Website**: [ogerly.github.io/devmatrose](https://ogerly.github.io/devmatrose/)
- **GitHub**: [@DEVmatrose](https://github.com/DEVmatrose)
- **Live-Demo**: [Token Kosten-Rechner](https://devmatrose.github.io/token-kosten-rechner/)
- **Live-Demo**: [Video-Service-Strategie-Planer](https://devmatrose.github.io/token-kosten-rechner/Video-Service-Strategie-Planer.html)

---

**© 2026 DEVmatrose** | Token-Arbitrage leicht gemacht 🚀
- Keine Installation nötig

## 💻 Verwendung

Einfach `token-kosten-rechner.html` im Browser öffnen - fertig!

## 📦 GitHub Pages

Das Projekt läuft automatisch über GitHub Pages.

---

© 2026 DEVmatrose
