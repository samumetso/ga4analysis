#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hotel Haven - Room Data Vertailu
GA4 Room-suodatettu raportti vs MCP analyysi
"""

def compare_room_data():
    """Vertaa GA4:n Room-raportin ja MCP:n analyysien eroja"""
    
    print("🛏️ ROOM DATA VERTAILU - GA4 vs MCP")
    print("=" * 80)
    print("GA4 Raportti: 'Room revenue by channel' (suodatettu vain Room)")
    print("MCP Analyysi: itemName-perusteinen huonevarausanalyysi")
    print()
    
    print("📊 LUKUVERTAILU:")
    print("-" * 50)
    print()
    
    # GA4 Room-raportin luvut (kuvakaappauksesta)
    ga4_room_data = [
        {"channel": "Organic Search", "revenue": 30864.85, "purchases": 60, "added_to_cart": 182, "views": 254},
        {"channel": "Paid Search", "revenue": 23722.15, "purchases": 56, "added_to_cart": 118, "views": 294},
        {"channel": "Referral", "revenue": 12934.80, "purchases": 32, "added_to_cart": 63, "views": 94},
        {"channel": "Direct", "revenue": 8436.00, "purchases": 18, "added_to_cart": 70, "views": 141},
        {"channel": "Organic Social", "revenue": 1555.00, "purchases": 2, "added_to_cart": 3, "views": 11},
        {"channel": "Email", "revenue": 1101.00, "purchases": 5, "added_to_cart": 9, "views": 73},
        {"channel": "Unassigned", "revenue": 716.50, "purchases": 3, "added_to_cart": 6, "views": 16},
        {"channel": "Paid Social", "revenue": 385.00, "purchases": 1, "added_to_cart": 7, "views": 31}
    ]
    
    # MCP:n huonevarausluvut (aikaisemmasta analyysista)
    mcp_data = [
        {"channel": "Paid Search", "revenue": 32942, "conversions": 217.16},
        {"channel": "Organic Search", "revenue": 32748, "conversions": 208.34},
        {"channel": "Direct", "revenue": 15662, "conversions": 96.00},
        {"channel": "Referral", "revenue": 17364, "conversions": 372.38}  # Sisältää toscanini.fi
    ]
    
    ga4_total = sum([item["revenue"] for item in ga4_room_data])
    mcp_total_rooms_only = 97352  # Aikaisemmin laskettu huoneiden revenue
    
    print("KANAVA              GA4 ROOM      MCP HUONEET    ERO €      ERO %")
    print("-" * 70)
    
    # Vertailu kanavittain
    for ga4_item in ga4_room_data[:4]:  # Top 4 kanavaa
        channel = ga4_item["channel"]
        ga4_rev = ga4_item["revenue"]
        
        # Etsi vastaava MCP:stä
        mcp_item = None
        for mcp in mcp_data:
            if ("Organic" in channel and "Organic" in mcp["channel"]) or \
               ("Paid" in channel and "Paid" in mcp["channel"]) or \
               (channel == "Direct" and mcp["channel"] == "Direct") or \
               (channel == "Referral" and mcp["channel"] == "Referral"):
                mcp_item = mcp
                break
        
        if mcp_item:
            mcp_rev = mcp_item["revenue"]
            diff = mcp_rev - ga4_rev
            diff_pct = (diff / ga4_rev) * 100 if ga4_rev > 0 else 0
            print(f"{channel:18s} €{ga4_rev:8,.0f}  €{mcp_rev:8,.0f}  {diff:+8,.0f}  {diff_pct:+6.1f}%")
        else:
            print(f"{channel:18s} €{ga4_rev:8,.0f}  {'N/A':>9s}      {'N/A':>7s}   {'N/A':>6s}")
    
    print("-" * 70)
    print(f"{'YHTEENSÄ':18s} €{ga4_total:8,.0f}  €{mcp_total_rooms_only:8,.0f}  {mcp_total_rooms_only-ga4_total:+8,.0f}  {((mcp_total_rooms_only-ga4_total)/ga4_total)*100:+6.1f}%")
    print()
    
    print("🚨 MERKITTÄVÄT EROT:")
    print("-" * 25)
    print("• GA4 Room Total:  €79,715")
    print("• MCP Huoneet:     €97,352")
    print("• ERO:             €17,637 (+22.1%)")
    print()
    
    print("🔍 MAHDOLLISET SYYT EROIHIN:")
    print("-" * 40)
    print()
    
    print("1. 📊 ERI MITTARIT")
    print("   GA4: 'Item revenue' Room-kategoriassa")
    print("   MCP: 'itemRevenue' itemName-perusteinen")
    print("   → Mahdollisesti eri laskentalogiikka")
    print()
    
    print("2. 🏷️ ERI ATTRIBUUTIOMALLIT")
    print("   GA4 Raportti: 'Session primary channel group'")
    print("   MCP: 'defaultChannelGroup'")
    print("   → Eri attribuutio voi aiheuttaa eroja")
    print()
    
    print("3. 📅 ERI AIKARAJAUS")
    print("   GA4: Mahdollisesti eri aikavyöhyke")
    print("   MCP: UTC vs. paikallinen aika")
    print("   → Päivämäärien siirtymä")
    print()
    
    print("4. 🔄 DATAN KÄSITTELYN VIIVE")
    print("   GA4 UI: Reaaliaikainen aggregointi")
    print("   MCP API: Mahdollinen cache/viive")
    print("   → Eri päivitysajat")
    print()
    
    print("5. 🎯 SUODATUSEROT")
    print("   GA4: 'Room' item category suodatin")
    print("   MCP: itemName-perusteinen suodatus")
    print("   → Eri tuotteet mukana/pois")
    print()
    
    print("💡 TODENNÄKÖISIN SYYT:")
    print("-" * 30)
    print()
    
    print("🎯 ATTRIBUUTIOERO (TODENNÄKÖISIN)")
    print("• GA4: 'Session primary channel group'")
    print("• MCP: 'defaultChannelGroup'")
    print("• Session primary = ensimmäinen kanava sessionissa")
    print("• Default = yleinen kanavaluokittelu")
    print("• VAIKUTUS: Eri kanavien välinen jakautuminen")
    print()
    
    print("📊 MITTARIERO")
    print("• GA4 Room-raportti: Item revenue Room-kategoriassa")
    print("• MCP: Kaikki itemName-pohjaiset huoneet")
    print("• VAIKUTUS: Eri tuotteet mukana laskennassa")
    print()
    
    print("✅ SUOSITUS:")
    print("-" * 15)
    print("1. KÄYTÄ GA4:N ROOM-RAPORTTIA virallisena lukuna")
    print("2. MCP = analyysityökalu, ei raportointi")
    print("3. Varmista sama attribuutiomalli molemmissa")
    print("4. Dokumentoi erot ja käytetyt parametrit")
    print()
    
    print("🏆 LOPULLINEN VASTAUS (GA4 Room-raportin mukaan):")
    print("-" * 60)
    print("ORGANIC SEARCH toi eniten huonemyyntiä toukokuussa 2025!")
    print("• €30,864.85 (38.72%)")
    print("• 60 huonevarausta")
    print("• €514 per varaus")
    print()
    print("Toisena PAID SEARCH:")
    print("• €23,722.15 (29.76%)")
    print("• 56 huonevarausta") 
    print("• €424 per varaus")

if __name__ == "__main__":
    compare_room_data()
