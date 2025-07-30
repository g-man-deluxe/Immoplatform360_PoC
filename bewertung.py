def berechne_kennzahlen(kaufpreis, flaeche, miete, lage, zustand, zinssatz, laufzeit):
    return {
        "Kaufpreis pro m²": round(kaufpreis / flaeche, 2),
        "Bruttorendite (%)": round((miete * 12) / kaufpreis * 100, 2),
        "Annuität (€)": round(kaufpreis * zinssatz / 100 / (1 - (1 + zinssatz / 100) ** (-laufzeit * 12)), 2),
        "Score-Faktor": round((miete * 12) / kaufpreis, 2),
        "Einschätzung": "🟢 attraktiv" if (miete * 12) / kaufpreis > 0.04 else "🔴 kritisch"
    }
