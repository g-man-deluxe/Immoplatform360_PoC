def faktor_lage(lage):
    return {"einfach": 0.8, "mittel": 1.0, "gut": 1.2, "sehr gut": 1.4}.get(lage, 1.0)

def faktor_zustand(zustand):
    return {"renovierungsbedürftig": 0.7, "durchschnittlich": 1.0, "gut": 1.2, "neuwertig": 1.4}.get(zustand, 1.0)

def berechne_kennzahlen(kaufpreis, flaeche, miete, lage, zustand, zinssatz, laufzeit):
    qm_preis = kaufpreis / flaeche
    miete_jahr = miete * 12
    rendite = (miete_jahr / kaufpreis) * 100
    lagef = faktor_lage(lage)
    zustandf = faktor_zustand(zustand)
    score = lagef * zustandf
    zinssatz_monat = zinssatz / 100 / 12
    monate = laufzeit * 12
    annuitaet = (zinssatz_monat * kaufpreis) / (1 - (1 + zinssatz_monat) ** -monate)
    return {
        "Kaufpreis pro m²": round(qm_preis, 2),
        "Bruttorendite (%)": round(rendite, 2),
        "Annuität (€)": round(annuitaet, 2),
        "Score-Faktor": round(score, 2),
        "Einschätzung": "🟢 attraktiv" if rendite > 4 and score >= 1.0 else "🔴 kritisch"
    }
