import requests

def analysiere_standort(plz):
    try:
        url = f"https://nominatim.openstreetmap.org/search?postalcode={plz}&country=Germany&format=json"
        r = requests.get(url, headers={"User-Agent": "Immo360"})
        daten = r.json()
        if not daten:
            return {"Fehler": "PLZ nicht gefunden"}
        ort = daten[0].get("display_name", "Unbekannt")
        lat, lon = daten[0]["lat"], daten[0]["lon"]
        return {
            "Ort": ort,
            "Latitude": lat,
            "Longitude": lon,
            "Kommentar": "Standortdaten erfolgreich geladen"
        }
    except Exception as e:
        return {"Fehler": str(e)}
