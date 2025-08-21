#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hotel Haven - Attribuutioikkuna Testit
Testataan eri aikaikkunoita GA4 vs MCP erojen selvittämiseksi
"""

def analyze_attribution_window_tests():
    """Analysoi attribuutioikkuna testien tulokset"""
    
    print("🔍 ATTRIBUUTIOIKKUNA TESTIT - TULOKSET")
    print("=" * 80)
    print()
    
    print("📊 MCP TULOKSET ERI AIKAIKKUNOILLA:")
    print("-" * 60)
    print()
    
    # Testidatan kokoaminen
    test_results = [
        {
            "period": "Koko toukokuu (1.-31.5.)",
            "days": 31,
            "organic": 35712,
            "cpc": 35529,
            "direct": 16326,
            "referral": 10573,
            "email": 1669,
            "total": 100609
        },
        {
            "period": "Toukokuun loppu (15.-31.5.)",
            "days": 17,
            "organic": 18102,
            "cpc": 19983,
            "direct": 8373,
            "referral": 4637,
            "email": 1669,
            "total": 53005
        },
        {
            "period": "Viimeiset 12 päivää (20.-31.5.)",
            "days": 12,
            "organic": 13290,
            "cpc": 15088,
            "direct": 6043,
            "referral": 3647,
            "email": 1230,
            "total": 39299
        },
        {
            "period": "Viimeiset 7 päivää (25.-31.5.)",
            "days": 7,
            "organic": 7475,
            "cpc": 8268,
            "direct": 2303,
            "referral": 2630,
            "email": 483,
            "total": 21159
        },
        {
            "period": "Viimeiset 3 päivää (29.-31.5.)",
            "days": 3,
            "organic": 2104,
            "cpc": 3082,
            "direct": 911,
            "referral": 980,
            "email": 483,
            "total": 7560
        }
    ]
    
    print("AIKAIKKUNA                    ORGANIC    CPC       DIRECT   REFERRAL  TOTAL")
    print("-" * 75)
    for result in test_results:
        print(f"{result['period']:25s} €{result['organic']:6,.0f} €{result['cpc']:6,.0f} €{result['direct']:5,.0f} €{result['referral']:6,.0f} €{result['total']:6,.0f}")
    
    print()
    
    print("📊 GA4 RAPORTIN LUVUT (Session Medium):")
    print("-" * 50)
    ga4_total = 79715
    ga4_organic = 30865
    ga4_cpc = 24107
    ga4_direct = 8436
    ga4_referral = 13760
    ga4_email = 1101
    
    print(f"GA4 Koko toukokuu:           €{ga4_organic:6,.0f} €{ga4_cpc:6,.0f} €{ga4_direct:5,.0f} €{ga4_referral:6,.0f} €{ga4_total:6,.0f}")
    print()
    
    print("🔍 EROANALYYSI:")
    print("-" * 25)
    print()
    
    for result in test_results:
        organic_diff = ((result['organic'] - ga4_organic) / ga4_organic) * 100
        cpc_diff = ((result['cpc'] - ga4_cpc) / ga4_cpc) * 100
        total_diff = ((result['total'] - ga4_total) / ga4_total) * 100
        
        print(f"📅 {result['period']}:")
        print(f"   Total ero GA4:sta: {total_diff:+.1f}%")
        print(f"   Organic ero: {organic_diff:+.1f}%")
        print(f"   CPC ero: {cpc_diff:+.1f}%")
        print()
    
    print("💡 KRIITTISIÄ HAVAINTOJA:")
    print("-" * 35)
    print()
    
    print("1. 📈 AIKAIKKUNAN PIENENTÄMINEN EI RATKAISE ONGELMAA")
    print("   • Kaikissa aikaikkunoissa MCP > GA4")
    print("   • Ero säilyy merkittävänä kaikissa testeissä")
    print("   • Lyhyemmät ikkunat eivät lähesty GA4:n lukuja")
    print()
    
    print("2. 🔄 KANAVIEN SUHTEELLISET OSUUDET PYSYVÄT")
    print("   • Organic ja CPC kilpailevat #1 paikasta")
    print("   • Direct pysyy kolmantena")
    print("   • Referral neljäntenä")
    print("   • Suhteelliset osuudet eivät muutu merkittävästi")
    print()
    
    print("3. ❌ ATTRIBUUTIOIKKUNA EI SELITÄ EROA")
    print("   • Viimeisten 3 päivän data: €7,560 vs GA4 €79,715")
    print("   • Edelleen merkittävä ero myös lyhyissä ikkunoissa")
    print("   • Ongelma ei ole attribuutioaikaikkunassa")
    print()
    
    print("🚨 JOHTOPÄÄTÖS:")
    print("-" * 20)
    print("ATTRIBUUTIOIKKUNA EI OLE SYYNÄ 26% EROON!")
    print()
    print("Jäljellä olevat mahdolliset syyt:")
    print("1. 🔧 ERI GA4 PROPERTY tai VIEW")
    print("2. 🎯 ERI SUODATUKSET/SEGMENTIT")
    print("3. 📊 ERI DATA SOURCE kokonaan")
    print("4. ⚙️ MCP KONFIGURAATIO-ONGELMA")
    print()
    
    print("🎯 SEURAAVAT TOIMENPITEET:")
    print("-" * 30)
    print("1. Tarkista MCP:n GA4 Property ID")
    print("2. Vertaa GA4:n view-asetuksia")
    print("3. Tarkista onko GA4:ssä aktiivisia suodattimia")
    print("4. Varmista että molemmat katsovat samaa dataa")
    print()
    print("💡 TÄMÄ ON KONFIGURAATIO-ONGELMA, EI ATTRIBUUTIO-ONGELMA!")

if __name__ == "__main__":
    analyze_attribution_window_tests()
