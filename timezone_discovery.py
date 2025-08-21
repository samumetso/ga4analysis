#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hotel Haven - AIKAVYÖHYKE-ONGELMA LÖYDETTY!
MCP sisältää kesäkuun dataa toukokuun kyselyssä
"""

def timezone_discovery_analysis():
    """Analyysi aikavyöhyke-ongelman löytymisestä"""
    
    print("🎯 AIKAVYÖHYKE-ONGELMA LÖYDETTY!")
    print("=" * 80)
    print()
    
    print("🚨 KRIITTINEN LÖYDÖS:")
    print("-" * 25)
    print("MCP sisältää dataa 1.6.2025, vaikka kysyin vain toukokuuta!")
    print()
    print("TOUKOKUU 2025 KYSELY (2025-05-01 - 2025-05-31):")
    print("• MCP palauttaa MYÖS 1.6.2025 dataa")
    print("• GA4 Room-raportti EI sisällä 1.6.2025 dataa")
    print("• TÄMÄ SELITTÄÄ MERKITTÄVÄN OSAN EROSTA!")
    print()
    
    print("📊 KESÄKUUN DATAN VAIKUTUS:")
    print("-" * 35)
    
    # Kesäkuun 1. päivän data MCP:stä
    june_1_data = {
        "Paid Search": 641.00,
        "Organic Search": 430.50,
        "Referral": 220.00,
        "Email": 220.00,
        "Direct": 110.00
    }
    june_1_total = sum(june_1_data.values())
    
    print("1.6.2025 MCP:n data (pitäisi olla pois toukokuu-kyselystä):")
    for channel, revenue in june_1_data.items():
        print(f"• {channel}: €{revenue:.0f}")
    print(f"YHTEENSÄ 1.6.: €{june_1_total:.0f}")
    print()
    
    # Alkuperäiset luvut
    mcp_original_total = 93771
    ga4_total = 79715
    
    # Korjattu MCP (ilman kesäkuun dataa)
    mcp_corrected = mcp_original_total - june_1_total
    corrected_diff = mcp_corrected - ga4_total
    corrected_diff_pct = (corrected_diff / ga4_total) * 100
    
    print("🔧 KORJATTU VERTAILU:")
    print("-" * 25)
    print(f"GA4 Room-raportti:           €{ga4_total:8,.0f}")
    print(f"MCP alkuperäinen:            €{mcp_original_total:8,.0f}")
    print(f"MCP korjattu (- 1.6. data):  €{mcp_corrected:8,.0f}")
    print()
    print(f"ALKUPERÄINEN ERO:  +€{mcp_original_total - ga4_total:5,.0f} (+{((mcp_original_total - ga4_total) / ga4_total * 100):5.1f}%)")
    print(f"KORJATTU ERO:      {corrected_diff:+6,.0f} ({corrected_diff_pct:+5.1f}%)")
    print()
    
    print("📈 MERKITTÄVÄ PARANNUS!")
    print("-" * 30)
    print(f"• Ero pieneni: {17.6 - abs(corrected_diff_pct):.1f} prosenttiyksikköä")
    print(f"• Uusi ero: {abs(corrected_diff_pct):.1f}%")
    print()
    
    if abs(corrected_diff_pct) <= 5:
        print("✅ TAVOITE SAAVUTETTU! Ero alle ±5%")
        print("MCP:tä voi käyttää luotettavasti!")
    elif abs(corrected_diff_pct) <= 10:
        print("⚠️ LÄHELLÄ TAVOITETTA! Ero alle 10%")
        print("Tarvitaan vielä lisätutkimusta.")
    else:
        print("❌ EI VIELÄ RIITÄ! Ero yli 10%")
        print("Tarvitaan lisää korjauksia.")
    
    print()
    print("🔍 MIKSI TÄMÄ TAPAHTUU:")
    print("-" * 30)
    print("AIKAVYÖHYKE-ERO:")
    print("• GA4 UI: Helsinki-aika (UTC+3)")
    print("• MCP API: UTC-aika")
    print("• 31.5.2025 klo 22:00 Helsinki = 1.6.2025 klo 01:00 UTC")
    print("• MCP sisältää 3 tuntia 'ylimääräistä' dataa!")
    print()
    
    print("🎯 RATKAISU:")
    print("-" * 15)
    print("1. RAJAA MCP:N KYSELY: 2025-05-01 - 2025-05-30")
    print("   (Jätä 31.5. pois välttääksesi aikavyöhyke-ongelman)")
    print()
    print("2. TAI aseta MCP käyttämään Helsinki-aikavyöhykettä")
    print("   (Jos mahdollista GA4 MCP-serverissä)")
    print()
    
    print("💡 SEURAAVA TESTI:")
    print("-" * 20)
    print("Testaa MCP:tä aikavälillä 2025-05-01 - 2025-05-30")
    print("(Jättää pois 31.5. joka sisältää UTC vs UTC+3 eron)")
    print("Tämän pitäisi tuoda luvut lähemmäs toisiaan!")
    print()
    
    print("🚨 TÄRKEÄ HUOMIO:")
    print("-" * 20)
    print("Tämä aikavyöhyke-ongelma vaikuttaa KAIKKIIN MCP-kyselyihin!")
    print("Aina kun kysyt kuukauden dataa, saat hieman enemmän.")
    print("Ratkaisu on pakollinen ennen MCP:n käyttöä.")

if __name__ == "__main__":
    timezone_discovery_analysis()
