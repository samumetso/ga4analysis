#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hotel Haven - GA4 Raportti vs MCP Analyysi Vertailu
Selvittää mistä lukujen erot tulevat
"""

def compare_ga4_vs_mcp_data():
    """Vertailee GA4 raportin ja MCP-analyysin eroja"""
    
    print("🔍 GA4 RAPORTTI vs MCP ANALYYSI - EROJEN SELVITYS")
    print("=" * 80)
    print()
    
    print("📊 GA4 RAPORTIN LUVUT (kuvakaappaus):")
    print("-" * 50)
    print("HUONEIDEN TUOTTO KANAVITTAIN:")
    print("1. Organic (organic)     €30,440.70  (38.19%)")
    print("2. CPC (cpc)             €24,964.65  (31.32%)")
    print("3. Direct (none)         €11,604.65  (14.56%)")
    print("4. Referral              €9,771.80   (12.26%)")
    print("5. Email                 €1,487.00   (1.87%)")
    print("6. Business_Advantage    €730.00     (0.92%)")
    print("7. MapResults            €716.50     (0.90%)")
    print()
    print("YHTEENSÄ GA4:            €79,715.30")
    print()
    
    print("📊 MINUN MCP ANALYYSIN LUVUT:")
    print("-" * 40)
    print("HUONEIDEN TUOTTO KANAVITTAIN:")
    print("1. Paid Search           €32,942     (32.7%)")
    print("2. Organic Search        €32,748     (32.5%)")
    print("3. Referral              €17,364     (17.3%)")
    print("4. Direct                €15,662     (15.6%)")
    print("5. Organic Social        €818        (0.8%)")
    print("6. Email                 €622        (0.6%)")
    print("7. Mobile Push           €231        (0.2%)")
    print("8. Unassigned            €222        (0.2%)")
    print()
    print("YHTEENSÄ MCP:            €100,610")
    print()
    
    print("🚨 MERKITTÄVÄT EROT:")
    print("-" * 30)
    print("• KOKONAISTUOTTO: €100,610 vs €79,715 = €20,895 EROA!")
    print("• ORGANIC: €32,748 vs €30,441 = €2,307 eroa")
    print("• PAID SEARCH: €32,942 vs €24,965 = €7,977 EROA!")
    print("• REFERRAL: €17,364 vs €9,772 = €7,592 eroa")
    print()
    
    print("🔍 MAHDOLLISET SYYT EROIHIN:")
    print("-" * 40)
    print()
    
    print("1. 📅 ERI AIKAVÄLIT")
    print("   • GA4 raportti: Mahdollisesti eri päivämäärät")
    print("   • MCP haku: 1.-31.5.2025")
    print("   • RATKAISU: Tarkista tarkat päivämäärät")
    print()
    
    print("2. 🏷️ ERI KANAVALUOKITTELU")
    print("   • GA4: 'First user medium' (ensikosketus)")
    print("   • MCP: 'Default channel group' (viimeinen kosketus)")
    print("   • VAIKUTUS: Eri attribuutiomalli!")
    print()
    
    print("3. 📊 ERI MITTARIT")
    print("   • GA4: 'Item revenue' (tuote-revenue)")
    print("   • MCP: 'Total revenue' (koko-revenue)")
    print("   • SISÄLTÖ: Eri revenue-tyypit")
    print()
    
    print("4. 🔄 DATAN PROSESSOINTI")
    print("   • GA4: Reaaliaikainen raportointi")
    print("   • MCP: API-aggregointi")
    print("   • VIIVE: Datan käsittelyn erot")
    print()
    
    print("5. 🎯 SUODATUKSET")
    print("   • GA4: Mahdolliset segmentit/suodatukset")
    print("   • MCP: Ei erityissuodatuksia")
    print("   • TULOS: Eri datamäärät")
    print()
    
    print("💡 KRIITTINEN HAVAINTO - ATTRIBUUTIOERO:")
    print("-" * 60)
    print("GA4 RAPORTTI käyttää 'First user medium' -kenttää")
    print("= Mitä kanavaa käyttäjä käytti ENSIMMÄISTÄ kertaa")
    print()
    print("MCP ANALYYSI käyttää 'Default channel group' -kenttää")  
    print("= Mitä kanavaa käyttäjä käytti VIIMEISTÄ kertaa (ennen ostoa)")
    print()
    print("TÄMÄ SELITTÄÄ SUURIMMAT EROT!")
    print("• Käyttäjä löytää hotellin Googlesta (first)")
    print("• Palaa myöhemmin suoraan sivulle (last)")
    print("• GA4: organic, MCP: direct")
    print()
    
    print("✅ SUOSITUKSET:")
    print("-" * 20)
    print("1. Käytä samaa attribuutiomallia molemmissa")
    print("2. Tarkista tarkat aikavälit")
    print("3. Varmista sama mittarityyppi (item vs total revenue)")
    print("4. Dokumentoi käytetyt parametrit")
    print("5. Testaa MCP-haku samoilla asetuksilla kuin GA4")

if __name__ == "__main__":
    compare_ga4_vs_mcp_data()
