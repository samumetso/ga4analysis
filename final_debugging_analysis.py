#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hotel Haven - Lopullinen Debuggausanalyysi
Miksi MCP:n ja GA4:n Room-luvut eivät täsmää
"""

def final_debugging_analysis():
    """Lopullinen analyysi erojen syistä"""
    
    print("🔍 LOPULLINEN DEBUGGAUSANALYYSI")
    print("=" * 80)
    print()
    
    # GA4:n Room-raportin luvut
    ga4_room_total = 79715.30
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
    
    # MCP:n sessionDefaultChannelGroup + itemCategory='Room' luvut
    mcp_session_room_total = 93770.55  # Laskettu edellisestä
    mcp_session_channels = {
        "Paid Search": 34843.25,
        "Organic Search": 34400.65,
        "Direct": 13517.35,
        "Referral": 8607.75,
        "Email": 948.75,
        "Organic Social": 818.00,
        "Unassigned": 470.00,
        "Mobile Push Notifications": 165.00
    }
    
    # MCP:n itemName-perusteinen Room-laskenta (kaikki huonetyypit yhteensä)
    room_items_total = (33547.10 + 23943.35 + 14236.40 + 8585.70 + 
                       4007.00 + 3893.50 + 3564.00 + 1116.00 + 877.70)
    # = €93,770.75
    
    print("📊 KOLME ERI LASKENTAA:")
    print("-" * 35)
    print(f"1. GA4 Room-raportti:                €{ga4_room_total:8,.0f}")
    print(f"2. MCP sessionDefaultChannelGroup:   €{mcp_session_room_total:8,.0f}")
    print(f"3. MCP itemName-yhteenlaskenta:      €{room_items_total:8,.0f}")
    print()
    
    print("🎯 KRIITTINEN HAVAINTO:")
    print("-" * 30)
    print("MCP:n kaksi laskentaa täsmäävät keskenään!")
    print(f"• SessionChannelGroup: €{mcp_session_room_total:,.0f}")
    print(f"• ItemName-summa:      €{room_items_total:,.0f}")
    print(f"• ERO: €{abs(mcp_session_room_total - room_items_total):.0f} (pyöristysero)")
    print()
    print("→ MCP:n laskenta on sisäisesti johdonmukainen!")
    print()
    
    print("🚨 ONGELMA ON GA4:N JA MCP:N VÄLILLÄ:")
    print("-" * 45)
    print(f"• GA4:  €{ga4_room_total:,.0f}")
    print(f"• MCP:  €{room_items_total:,.0f}")
    print(f"• ERO:  €{room_items_total - ga4_room_total:+,.0f} ({((room_items_total - ga4_room_total) / ga4_room_total * 100):+.1f}%)")
    print()
    
    print("🔍 MAHDOLLISET SYYT:")
    print("-" * 25)
    print()
    
    print("1. 📅 AIKAVYÖHYKE-ERO (TODENNÄKÖISIN)")
    print("   • GA4 UI: Helsinki-aika (UTC+3)")
    print("   • MCP API: UTC-aika")
    print("   • VAIKUTUS: 3h siirtymä = eri päivämäärät")
    print("   • ESIM: GA4 31.5. klo 22:00 = MCP 1.6. klo 01:00")
    print("   • TULOS: MCP sisältää enemmän dataa")
    print()
    
    print("2. 🔄 DATAN KÄSITTELYN EROT")
    print("   • GA4 UI: Aggregointi raportointihetkellä")
    print("   • MCP API: Raw data + server-side aggregointi")
    print("   • VAIKUTUS: Eri laskentalogiikka")
    print()
    
    print("3. 🎯 SUODATUKSET/SEGMENTIT")
    print("   • GA4: Mahdolliset piilotetut suodattimet")
    print("   • MCP: Ei automaattisia suodattimia")
    print("   • ESIM: Sisäinen liikenne, testiliikenne")
    print()
    
    print("4. 📊 REVENUE-MÄÄRITELMÄN EROT")
    print("   • GA4 'Item revenue': Mahdollisesti eri laskenta")
    print("   • MCP 'itemRevenue': Raw GA4 API data")
    print("   • VAIKUTUS: UI vs API erot")
    print()
    
    print("💡 TESTAUSSUOSITUKSET:")
    print("-" * 30)
    print()
    
    print("TEST 1: AIKAVYÖHYKE")
    print("• Aseta MCP käyttämään Helsinki-aikaa")
    print("• Vertaa uudelleen samalla aikavyöhykkeellä")
    print()
    
    print("TEST 2: LYHYEMPI AIKAVÄLI")
    print("• Testaa vain 1 päivä (esim. 15.5.2025)")
    print("• Tarkista täsmääkö päivätasolla")
    print()
    
    print("TEST 3: GA4:N SUODATTIMIEN TARKISTUS")
    print("• Poista kaikki mahdolliset suodattimet GA4:stä")
    print("• Vertaa 'raakalukkuja'")
    print()
    
    print("🎯 VÄLITÖN SUOSITUS:")
    print("-" * 25)
    print()
    
    if abs((room_items_total - ga4_room_total) / ga4_room_total * 100) < 20:
        print("✅ ERO HYVÄKSYTTÄVISSÄ RAJOISSA (<20%)")
        print("• MCP:tä voi käyttää trendianalyysiin")
        print("• Käytä GA4:ää tarkoille luvuille")
        print("• Mainitse aina datalähde raporteissa")
    else:
        print("❌ ERO LIIAN SUURI (>20%)")
        print("• ÄLÄ käytä MCP:tä asiakasraportoinnissa")
        print("• Tutki aikavyöhyke-eroja")
        print("• Käytä vain GA4:n lukuja")
    
    print()
    print("🏆 LOPULLINEN PÄÄTÖS:")
    print("-" * 25)
    print()
    print("KÄYTÄ GA4:N ROOM-RAPORTTIA virallisena lukuna:")
    print("• Organic Search: €30,864.85 (38.7%)")
    print("• Paid Search: €23,722.15 (29.8%)")
    print("• Referral: €12,934.80 (16.2%)")
    print()
    print("MCP = analyysityökalu trendeille ja syvemmälle analyysille")
    print("GA4 = virallinen raportointi asiakkaalle")
    print()
    print("⚠️ AINA mainitse datalähde ja mahdolliset erot!")

if __name__ == "__main__":
    final_debugging_analysis()
