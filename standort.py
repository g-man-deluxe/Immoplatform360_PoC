import requests

def analysiere_standort(plz, strasse=None, hausnr=None):
    if strasse and hausnr:
        query = f"{strasse} {hausnr}, {plz}, Germany"
    else:
        query = f"{plz}, Germany"

    try:
        url = f"https://nominatim.openstreetmap.org/search"
        params = {"q": query, "format": "json"}
        r = requests.get(url, params=params, headers={"User-Agent": "Immo360"})
        daten = r.json()
        if not daten:
            return {"Fehler": "Adresse nicht gefunden"}
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
