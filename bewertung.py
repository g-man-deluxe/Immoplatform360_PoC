def lage_faktor(lage):
    return {
        "einfach": 0.8,
        "mittel": 1.0,
        "gut": 1.2,
        "sehr gut": 1.4
    }.get(lage, 1.0)

def zustand_faktor(zustand):
    return {
        "renovierungsbedürftig": 0.7,
        "durchschnittlich": 1.0,
        "gut": 1.2,
        "neuwertig": 1.4
    }.get(zustand, 1.0)

def bewerte_immobilie(kaufpreis, wohnfläche, lage, zustand, mieteinnahmen):
    qm_preis = kaufpreis / wohnfläche
    lagef = lage_faktor(lage)
    zustandf = zustand_faktor(zustand)
    faktor = lagef * zustandf
    kapitalrendite = (mieteinnahmen * 12) / kaufpreis * 100

    if kapitalrendite >= 5 and faktor >= 1.0:
        return f"👍 Attraktiv (Rendite: {kapitalrendite:.2f}%)"
    elif kapitalrendite >= 3:
        return f"⚠️ Mittelmäßig (Rendite: {kapitalrendite:.2f}%)"
    else:
        return f"👎 Unattraktiv (Rendite: {kapitalrendite:.2f}%)"
