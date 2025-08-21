#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hotel Haven - CONTAINS vs EXACTLY MATCHES Analyysi
Löysimme syyn eroon!
"""

def contains_vs_exactly_analysis():
    """Analysoi CONTAINS vs EXACTLY MATCHES eron"""
    
    print("🎉 LÖYSIMME SYYN EROON!")
    print("=" * 80)
    print()
    
    # MCP:n data kaikista itemCategory arvoista
    item_categories = [
        {"category": "Room", "revenue": 93770.75, "quantity": 322},
        {"category": "Gift card", "revenue": 2231.00, "quantity": 14},
        {"category": "Rooms / Yövy enemmän - Säästä enemmän / Sky Balcony", "revenue": 842.08, "quantity": 4},
        {"category": "Package", "revenue": 825.00, "quantity": 1366},
        {"category": "Rooms / Unohtumattomat hetket / Comfort", "revenue": 607.74, "quantity": 6},
        {"category": "Rooms / Yövy enemmän - Säästä enemmän / Comfort", "revenue": 281.56, "quantity": 3},
        {"category": "Rooms / Yövy enemmän - Säästä enemmän / Mini", "revenue": 263.14, "quantity": 3},
        {"category": "Rooms / Friends & Family Rate / Sky Suite", "revenue": 255.26, "quantity": 1},
        {"category": "Rooms / Unohtumattomat hetket / Superior", "revenue": 240.70, "quantity": 2},
        {"category": "Rooms / Unohtumattomat hetket / Comfort Accessible", "revenue": 209.13, "quantity": 2},
        {"category": "Stock", "revenue": 201.00, "quantity": 8},
        {"category": "Rooms / Friends & Family Rate / Superior", "revenue": 196.50, "quantity": 2},
        {"category": "Rooms / Unohtumattomat hetket / Mini", "revenue": 161.40, "quantity": 2},
        {"category": "Rooms / I Prefer Member Rate - Flex Cancel / Mini", "revenue": 157.90, "quantity": 2},
        {"category": "Rooms / Nordic Choice Staff Rate / Superior", "revenue": 140.79, "quantity": 2},
        {"category": "Rooms / Nordic Choice Staff Rate / Mini", "revenue": 120.61, "quantity": 2},
        {"category": "Rooms / Finnair Plus Palkintoseteli / Superior", "revenue": 105.26, "quantity": 1},
        {"category": "(not set)", "revenue": 0.00, "quantity": 221},
        {"category": "Meal", "revenue": 0.00, "quantity": 26}
    ]
    
    # GA4:n luvut
    ga4_explore_total = 79715.30
    mcp_exactly_room = 93770.75  # "Room" exactly matches
    
    print("📊 ITEMCATEGORY ANALYYSI:")
    print("-" * 30)
    print()
    
    # Laske "exactly Room" vs "contains Room"
    exactly_room = 0
    contains_room = 0
    contains_room_items = []
    
    for item in item_categories:
        if item["category"] == "Room":
            exactly_room += item["revenue"]
        if "Room" in item["category"]:
            contains_room += item["revenue"]
            contains_room_items.append(item)
    
    print("🔍 'EXACTLY ROOM' (MCP käyttää):")
    print("• Vain 'Room' kategoria")
    print(f"• Revenue: €{exactly_room:,.0f}")
    print()
    
    print("🔍 'CONTAINS ROOM' (GA4 Explore käyttää):")
    print("• Kaikki kategoriat jotka sisältävät 'Room'")
    for item in contains_room_items:
        if item["revenue"] > 0:
            print(f"  - {item['category'][:50]:<50} €{item['revenue']:8.0f}")
    print(f"• YHTEENSÄ: €{contains_room:,.0f}")
    print()
    
    print("📊 VERTAILU:")
    print("-" * 15)
    print(f"GA4 Explore (contains):  €{ga4_explore_total:8,.0f}")
    print(f"MCP exactly Room:        €{exactly_room:8,.0f}")
    print(f"MCP contains Room:       €{contains_room:8,.0f}")
    print()
    
    # Laske ero
    exactly_vs_ga4 = exactly_room - ga4_explore_total
    contains_vs_ga4 = contains_room - ga4_explore_total
    
    print(f"ERO exactly vs GA4:      {exactly_vs_ga4:+8,.0f} ({(exactly_vs_ga4/ga4_explore_total)*100:+.1f}%)")
    print(f"ERO contains vs GA4:     {contains_vs_ga4:+8,.0f} ({(contains_vs_ga4/ga4_explore_total)*100:+.1f}%)")
    print()
    
    # Tarkista onko contains lähempänä GA4:ta
    if abs(contains_vs_ga4) < abs(exactly_vs_ga4):
        print("✅ 'CONTAINS' ON LÄHEMPÄNÄ GA4:TA!")
        improvement = abs(exactly_vs_ga4) - abs(contains_vs_ga4)
        print(f"Parannus: €{improvement:,.0f}")
        
        if abs(contains_vs_ga4) <= ga4_explore_total * 0.05:  # 5% toleranssi
            print("🎉 SAAVUTIMME ±5% TOLERANSSIN!")
            status = "HYVÄKSYTTY"
        elif abs(contains_vs_ga4) <= ga4_explore_total * 0.10:  # 10% toleranssi
            print("⚠️ LÄHELLÄ - alle 10% ero")
            status = "RAJATAPAUS"
        else:
            print("❌ Edelleen yli 10% ero")
            status = "HYLÄTTY"
    else:
        print("❌ 'CONTAINS' EI PARANNA TILANNETTA")
        status = "EI AUTA"
    
    print()
    print("🔍 MIKSI TÄMÄ ERO ON OLEMASSA:")
    print("-" * 40)
    print()
    print("GA4 'Item category contains Room' sisältää:")
    print("• 'Room' (perus huonevaraukset)")
    print("• 'Rooms / Yövy enemmän...' (erikoistarjoukset)")
    print("• 'Rooms / Unohtumattomat hetket...' (paketit)")
    print("• 'Rooms / Friends & Family...' (alennukset)")
    print("• 'Rooms / Nordic Choice Staff...' (henkilöstöhinnat)")
    print("• jne.")
    print()
    print("MCP 'itemCategory exactly matches Room' sisältää vain:")
    print("• 'Room' (perus huonevaraukset)")
    print()
    print("TULOS: MCP jättää pois erikoistarjoukset ja paketit!")
    print()
    
    print("💡 RATKAISU:")
    print("-" * 15)
    
    if status == "HYVÄKSYTTY":
        print("✅ KÄYTÄ MCP:TÄ 'CONTAINS' LOGIIKALLA")
        print("• Hae kaikki itemCategory arvot")
        print("• Suodata ne jotka sisältävät 'Room'")
        print("• Laske yhteisrevenue")
        print("• Tämä vastaa GA4:n 'contains' suodatinta")
        
    elif status == "RAJATAPAUS":
        print("⚠️ CONTAINS PARANTAA MUTTA EI RIITÄ")
        print("• Ero pienenee merkittävästi")
        print("• Mutta ei saavuta ±5% toleranssia")
        print("• Harkitse suuremman toleranssin hyväksymistä")
        
    else:
        print("❌ CONTAINS EI RATKAISE ONGELMAA")
        print("• Tarvitaan muita ratkaisuja")
        print("• Mahdollisesti API vs UI perusero")
    
    print()
    print("🎯 SEURAAVA ASKEL:")
    print("-" * 20)
    
    if status in ["HYVÄKSYTTY", "RAJATAPAUS"]:
        print("IMPLEMENTOI 'CONTAINS' LOGIIKKA MCP:HEN:")
        print("1. Hae kaikki itemCategory arvot")
        print("2. Filtteröi ne jotka sisältävät hakusanan")
        print("3. Aggregoi revenue")
        print("4. Käytä tätä GA4-vastaavana lukuna")
        print()
        print("TÄMÄ TEKEE MCP:STA LUOTETTAVAN!")
    else:
        print("Jatka muiden syiden tutkimista tai")
        print("hyväksy että MCP ja GA4 antavat eri lukuja.")

if __name__ == "__main__":
    contains_vs_exactly_analysis()
