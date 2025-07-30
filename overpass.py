import requests

def finde_pois(lat, lon, radius=800):
    overpass_url = "http://overpass-api.de/api/interpreter"
    query = f'''
    [out:json];
    (
      node["shop"="supermarket"](around:{radius},{lat},{lon});
      node["amenity"="kindergarten"](around:{radius},{lat},{lon});
      node["amenity"="school"](around:{radius},{lat},{lon});
      node["public_transport"="platform"](around:{radius},{lat},{lon});
    );
    out center;
    '''
    response = requests.get(overpass_url, params={'data': query}, timeout=30)
    data = response.json()
    pois = []
    for element in data.get("elements", []):
        pois.append({
            "lat": element.get("lat"),
            "lon": element.get("lon"),
            "typ": element.get("tags", {}).get("shop") or element.get("tags", {}).get("amenity") or element.get("tags", {}).get("public_transport", "POI"),
            "name": element.get("tags", {}).get("name", "Unbenannt")
        })
    return pois
