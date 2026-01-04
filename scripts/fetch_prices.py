#!/usr/bin/env python3
"""
GPU Price Fetcher für Token-Kosten-Rechner
Holt aktuelle Preise von verschiedenen GPU-Anbietern
"""

import requests
import json
from datetime import datetime
from typing import List, Dict

def fetch_vastai_prices() -> Dict:
    """Holt RTX 5090 Spot-Preise von Vast.ai"""
    try:
        # Vast.ai bietet eine öffentliche API für verfügbare Instanzen
        url = "https://console.vast.ai/api/v0/bundles/"
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            # Filtere nach RTX 5090 und nehme Durchschnitt der günstigsten 10
            rtx5090_instances = [
                inst for inst in data.get('offers', [])
                if '5090' in inst.get('gpu_name', '').upper()
            ]
            
            if rtx5090_instances:
                # Sortiere nach Preis und nehme Top 10
                sorted_prices = sorted(rtx5090_instances, key=lambda x: x.get('dph_total', 999))[:10]
                avg_price = sum(x.get('dph_total', 0) for x in sorted_prices) / len(sorted_prices)
                return {
                    "name": "Vast.ai (RTX 5090 Spot)",
                    "preis": round(avg_price, 2),
                    "tps": 90,
                    "info": "Günstigster Marktplatz, schwankende Stabilität.",
                    "last_update": datetime.utcnow().isoformat()
                }
    except Exception as e:
        print(f"Vast.ai Fetch Error: {e}")
    
    # Fallback auf Default-Werte
    return {
        "name": "Vast.ai (RTX 5090 Spot)",
        "preis": 0.35,
        "tps": 90,
        "info": "Günstigster Marktplatz, schwankende Stabilität.",
        "last_update": datetime.utcnow().isoformat(),
        "status": "fallback"
    }

def fetch_runpod_prices() -> Dict:
    """RunPod - meist stabile Preise, hier als Schätzung"""
    # RunPod hat keine öffentliche API, daher manueller Fallback
    # Könnte später durch Selenium/Playwright ergänzt werden
    return {
        "name": "RunPod (RTX 4090 On-Demand)",
        "preis": 0.45,
        "tps": 85,
        "info": "Sehr stabil, gute API, EU-Regionen verfügbar.",
        "last_update": datetime.utcnow().isoformat(),
        "status": "manual"
    }

def fetch_scaleway_prices() -> Dict:
    """Scaleway Enterprise L40S"""
    return {
        "name": "Scaleway (L40S Enterprise)",
        "preis": 1.30,
        "tps": 120,
        "info": "Echte EU-Cloud, GDPR-konform, ideal für Parallelbetrieb.",
        "last_update": datetime.utcnow().isoformat(),
        "status": "manual"
    }

def fetch_saladcloud_prices() -> Dict:
    """SaladCloud Consumer Grid"""
    return {
        "name": "SaladCloud (Consumer Grid)",
        "preis": 0.25,
        "tps": 70,
        "info": "Extrem günstig, aber Jobs können unterbrochen werden.",
        "last_update": datetime.utcnow().isoformat(),
        "status": "manual"
    }

def fetch_local_prices() -> Dict:
    """Lokale RTX 5090 mit Stromkosten"""
    # Berechnung: 700W * 0.40€/kWh = 0.28€/h
    return {
        "name": "Lokal (RTX 5090 Stromkosten)",
        "preis": 0.28,
        "tps": 95,
        "info": "Deine Hardware (basiert auf 0,40€/kWh bei 700W).",
        "last_update": datetime.utcnow().isoformat(),
        "status": "calculated"
    }

def main():
    """Hauptfunktion - sammelt alle Preise und speichert sie"""
    print("🚀 Starte GPU-Preis-Fetch...")
    
    presets = [
        fetch_vastai_prices(),
        fetch_runpod_prices(),
        fetch_scaleway_prices(),
        fetch_saladcloud_prices(),
        fetch_local_prices()
    ]
    
    # Metadaten hinzufügen
    output = {
        "last_updated": datetime.utcnow().isoformat() + "Z",
        "version": "1.0",
        "presets": presets
    }
    
    # In JSON-Datei schreiben
    with open('data/prices.json', 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    
    print("✅ Preise erfolgreich aktualisiert!")
    print(f"   → {len(presets)} Anbieter erfasst")
    print(f"   → Zeitstempel: {output['last_updated']}")

if __name__ == "__main__":
    main()
