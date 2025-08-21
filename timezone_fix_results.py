#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hotel Haven - Aikavyöhyke-korjauksen tulokset
Testaus aikavälillä 1.-30.5. (ilman 31.5.)
"""

def timezone_fix_results():
    """Analysoi aikavyöhyke-korjauksen tulokset"""
    
    print("🔧 AIKAVYÖHYKE-KORJAUKSEN TULOKSET")
    print("=" * 80)
    print()
    
    # GA4:n luvut (koko toukokuu 1.-31.5.)
    ga4_total = 79715.30
    ga4_channels = {
        "Organic Search": 30864.85,
        "Paid Search": 23722.15,
        "Referral": 12934.80,
        "Direct": 8436.00,
        "Organic Social": 1555.00,
        "Email": 1101.00,
        "Unassigned": 716.50,
        "Paid Social": 385.00
    }
    
    # MCP:n uudet luvut (1.-30.5., ilman 31.5.)
    mcp_may_1_30_data = {
        "Paid Search": 34283.25,
        "Organic Search": 33984.40,
        "Direct": 13356.35,
        "Referral": 7900.75,
        "Organic Social": 818.00,
        "Email": 561.75,
        "Unassigned": 470.00,
        "Mobile Push Notifications": 165.00
    }
    mcp_may_1_30_total = sum(mcp_may_1_30_data.values())
    
    # Alkuperäiset MCP luvut (1.-31.5. + 1.6. data)
    mcp_original_total = 93771
    
    print("📊 KOLME VERSIOTA:")
    print("-" * 25)
    print(f"1. GA4 Room-raportti (1.-31.5.):     €{ga4_total:8,.0f}")
    print(f"2. MCP alkuperäinen (1.-31.5.+1.6.): €{mcp_original_total:8,.0f}")
    print(f"3. MCP korjattu (1.-30.5.):          €{mcp_may_1_30_total:8,.0f}")
    print()
    
    # Erojen laskenta
    original_diff = mcp_original_total - ga4_total
    original_diff_pct = (original_diff / ga4_total) * 100
    
    corrected_diff = mcp_may_1_30_total - ga4_total
    corrected_diff_pct = (corrected_diff / ga4_total) * 100
    
    print("📈 EROJEN VERTAILU:")
    print("-" * 25)
    print(f"ALKUPERÄINEN ERO:  +€{original_diff:5,.0f} (+{original_diff_pct:5.1f}%)")
    print(f"KORJATTU ERO:      {corrected_diff:+6,.0f} ({corrected_diff_pct:+5.1f}%)")
    print(f"PARANNUS:          {original_diff_pct - abs(corrected_diff_pct):6.1f} prosenttiyksikköä")
    print()
    
    # Toleranssin tarkistus
    tolerance_5pct = ga4_total * 0.05
    acceptable_min = ga4_total - tolerance_5pct
    acceptable_max = ga4_total + tolerance_5pct
    
    print("🎯 ±5% TOLERANSSI-ANALYYSI:")
    print("-" * 35)
    print(f"GA4 perustaso:        €{ga4_total:8,.0f}")
    print(f"±5% toleranssi:       €{tolerance_5pct:8,.0f}")
    print(f"Hyväksyttävä väli:    €{acceptable_min:8,.0f} - €{acceptable_max:8,.0f}")
    print(f"MCP korjattu tulos:   €{mcp_may_1_30_total:8,.0f}")
    print()
    
    if acceptable_min <= mcp_may_1_30_total <= acceptable_max:
        print("✅ TAVOITE SAAVUTETTU! MCP on ±5% toleranssin sisällä!")
        print("MCP:tä voi käyttää luotettavasti analyysiin.")
        status = "HYVÄKSYTTY"
    elif abs(corrected_diff_pct) <= 10:
        print("⚠️ LÄHELLÄ TAVOITETTA! Ero alle 10% mutta yli 5%.")
        print("Harkitse lisätutkimusta tai hyväksy suurempi toleranssi.")
        status = "RAJATAPAUS"
    else:
        print("❌ EI VIELÄ RIITÄ! Ero yli 10%.")
        print("Tarvitaan lisää korjauksia.")
        status = "HYLÄTTY"
    
    print()
    print("🔍 JÄLJELLÄ OLEVAN ERON ANALYYSI:")
    print("-" * 40)
    
    if status != "HYVÄKSYTTY":
        print("MAHDOLLISET SYYT:")
        print("1. 📅 31.5. PÄIVÄN PUUTTUMINEN MCP:stä")
        print("   • GA4 sisältää 31.5. datan")
        print("   • MCP ei sisällä (jätetty pois aikavyöhyke-ongelman takia)")
        print("   • Ratkaisu: Laske 31.5. data erikseen ja lisää")
        print()
        print("2. 🎯 GA4:N SUODATTIMET")
        print("   • Sisäinen liikenne, bot-suodatus jne.")
        print("   • MCP näkee 'raakadatan'")
        print()
        print("3. 🔄 UI vs API LASKENTAEROT")
        print("   • GA4 UI ja API voivat laskea hieman eri tavalla")
        print()
    
    print("💡 SEURAAVAT TOIMENPITEET:")
    print("-" * 30)
    
    if status == "HYVÄKSYTTY":
        print("✅ MCP KÄYTTÖVALMIS!")
        print("• Käytä aina aikaväliä joka jättää viimeisen päivän pois")
        print("• Esim: Toukokuu = 1.-30.5., Kesäkuu = 1.-29.6. jne.")
        print("• Dokumentoi aikavyöhyke-rajoitus")
    elif status == "RAJATAPAUS":
        print("1. Testaa 31.5. datan lisääminen MCP:hen")
        print("2. Tutki GA4:n mahdolliset suodattimet")
        print("3. Harkitse 10% toleranssin hyväksymistä")
    else:
        print("1. PAKOLLINEN: Tutki GA4:n suodattimet")
        print("2. Testaa 31.5. datan vaikutus")
        print("3. Jos ei riitä → Lopeta MCP:n käyttö")
    
    print()
    print("🏆 TÄMÄNHETKINEN TILA:")
    print("-" * 30)
    print(f"STATUS: {status}")
    print(f"ERO: {corrected_diff_pct:+.1f}%")
    
    if status == "HYVÄKSYTTY":
        print("MCP:tä voi käyttää luotettavasti!")
    else:
        print("MCP:n käyttö ei ole vielä suositeltavaa.")

if __name__ == "__main__":
    timezone_fix_results()
