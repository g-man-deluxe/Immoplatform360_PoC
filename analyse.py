def berechne_nebenkosten(kaufpreis, satz_makler=3.57, satz_notar=1.5, satz_grunderwerb=3.5, instandhaltung_pro_jahr=1000):
    makler = kaufpreis * satz_makler / 100
    notar = kaufpreis * satz_notar / 100
    grunderwerb = kaufpreis * satz_grunderwerb / 100
    nebenkosten = makler + notar + grunderwerb
    gesamtkosten = kaufpreis + nebenkosten
    instandhaltung = instandhaltung_pro_jahr
    return {
        "Maklerkosten (€)": round(makler, 2),
        "Notarkosten (€)": round(notar, 2),
        "Grunderwerbsteuer (€)": round(grunderwerb, 2),
        "Summe Nebenkosten (€)": round(nebenkosten, 2),
        "Gesamtkosten (€)": round(gesamtkosten, 2),
        "Instandhaltung pro Jahr (€)": instandhaltung
    }

def berechne_rendite(kaufpreis, jahresmiete, gesamtkosten, instandhaltung=1000):
    bruttorendite = jahresmiete / kaufpreis * 100
    nettomiete = jahresmiete - instandhaltung
    nettorendite = nettomiete / gesamtkosten * 100
    return {
        "Bruttorendite (%)": round(bruttorendite, 2),
        "Nettorendite (%)": round(nettorendite, 2)
    }

def berechne_break_even(gesamtkosten, jahresmiete, instandhaltung=1000):
    nettoeinnahmen = jahresmiete - instandhaltung
    if nettoeinnahmen <= 0:
        return "Nie (negative Einnahmen)"
    jahre = gesamtkosten / nettoeinnahmen
    return round(jahre, 1)

def score_bewertung(bruttorendite, nettorendite):
    if bruttorendite >= 5 and nettorendite >= 3:
        return "🟢 attraktiv"
    elif bruttorendite >= 3.5:
        return "🟡 neutral"
    else:
        return "🔴 kritisch"
