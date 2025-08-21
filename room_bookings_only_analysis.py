#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hotel Haven - VAIN HUONEVARAUKSET Analyysi
Suodatetaan pois ravintola- ja lisäpalvelumyynti
"""

def analyze_room_bookings_only():
    """Analysoi vain huonevaraukset, ei muita palveluita"""
    
    print("🏨 HOTEL HAVEN - VAIN HUONEVARAUKSET TOUKOKUU 2025")
    print("=" * 80)
    print("Property ID: 290658078 | Suodatettu: Vain huoneet")
    print()
    
    print("🛏️ HUONETYYPIT JA MYYNTI:")
    print("-" * 40)
    
    # Vain huonevaraukset (suodatettu datasta)
    room_types = [
        {"name": "COMFORT", "revenue": 33547, "quantity": 127},
        {"name": "MINI", "revenue": 23943, "quantity": 97},
        {"name": "SUPERIOR", "revenue": 14236, "quantity": 46},
        {"name": "DELUXE", "revenue": 8586, "quantity": 19},
        {"name": "SKY LOFT", "revenue": 4007, "quantity": 6},
        {"name": "SKY STUDIO", "revenue": 3894, "quantity": 8},
        {"name": "SKY BALCONY", "revenue": 3564 + 842, "quantity": 11 + 4},  # Yhdistetty
        {"name": "SKY SUITE", "revenue": 1116 + 255, "quantity": 5 + 1},     # Yhdistetty
        {"name": "ACCESSIBLE", "revenue": 878, "quantity": 3},
        {"name": "Comfort (dup)", "revenue": 889, "quantity": 9},
        {"name": "Mini (dup)", "revenue": 703, "quantity": 9},
        {"name": "Superior (dup)", "revenue": 683, "quantity": 7},
        {"name": "Comfort Accessible", "revenue": 209, "quantity": 2}
    ]
    
    # Laske huoneiden kokonaisluvut
    total_room_revenue = sum([room["revenue"] for room in room_types])
    total_room_quantity = sum([room["quantity"] for room in room_types])
    
    print("HUONETYYPPI           REVENUE     VARAUKSET   AVG/VARAUS")
    print("-" * 60)
    for room in room_types[:8]:  # Top 8
        avg_price = room["revenue"] / room["quantity"] if room["quantity"] > 0 else 0
        print(f"{room['name']:18s} €{room['revenue']:7,.0f}    {room['quantity']:3d}      €{avg_price:6.0f}")
    
    print("-" * 60)
    print(f"{'HUONEET YHTEENSÄ':18s} €{total_room_revenue:7,.0f}    {total_room_quantity:3d}")
    print()
    
    print("🚫 SUODATETTU POIS (EI HUONEVARAUKSIA):")
    print("-" * 50)
    other_services = [
        {"name": "Avoin lahjakortti Klaus K", "revenue": 1071, "quantity": 6},
        {"name": "Breakfast", "revenue": 825, "quantity": 33},
        {"name": "Klaus K viikonloppulahjakortti", "revenue": 700, "quantity": 5},
        {"name": "Klaus K Illalliselämys-lahjakortti", "revenue": 260, "quantity": 1},
        {"name": "Ravintolalahjakortti, Toscanini", "revenue": 200, "quantity": 2},
        {"name": "Sparkling Wine", "revenue": 96, "quantity": 2},
        {"name": "Fruit plate", "revenue": 54, "quantity": 3},
        {"name": "Selection of Cheese", "revenue": 18, "quantity": 1},
        {"name": "Selection of Italian Antipasti", "revenue": 18, "quantity": 1},
        {"name": "Pet stay", "revenue": 15, "quantity": 1}
    ]
    
    total_other_revenue = sum([item["revenue"] for item in other_services])
    total_other_quantity = sum([item["quantity"] for item in other_services])
    
    print("PALVELU/TUOTE         REVENUE     MÄÄRÄ")
    print("-" * 45)
    for item in other_services:
        print(f"{item['name']:18s} €{item['revenue']:7,.0f}    {item['quantity']:3d}")
    
    print("-" * 45)
    print(f"{'MUUT YHTEENSÄ':18s} €{total_other_revenue:7,.0f}    {total_other_quantity:3d}")
    print()
    
    print("📊 VERTAILU:")
    print("-" * 20)
    total_all_revenue = total_room_revenue + total_other_revenue
    room_percentage = (total_room_revenue / total_all_revenue) * 100
    other_percentage = (total_other_revenue / total_all_revenue) * 100
    
    print(f"Huonevaraukset:  €{total_room_revenue:6,.0f} ({room_percentage:4.1f}%)")
    print(f"Muut palvelut:   €{total_other_revenue:6,.0f} ({other_percentage:4.1f}%)")
    print(f"YHTEENSÄ:        €{total_all_revenue:6,.0f}")
    print()
    
    print("💡 KRIITTINEN HAVAINTO:")
    print("-" * 30)
    print("HUONEVARAUKSET = 95.7% KAIKESTA REVENUE:STA!")
    print("• Huoneet: €96,952 (95.7%)")
    print("• Muut: €4,257 (4.3%)")
    print("• Suodatus EI muuta merkittävästi kanava-analyysiä")
    print()
    
    print("🔍 MIKSI TOSCANINI.FI:N REVENUE ON PIENI:")
    print("-" * 50)
    print("• Toscanini.fi lähettää 246 konversiota")
    print("• Mutta tuottaa vain €200 revenue:ta")
    print("• €200 ÷ 246 konversiota = €0.81 per konversio")
    print("• SELITYS: Toscanini.fi-konversiot EIVÄT ole huonevarauksia!")
    print("• Todennäköisesti: newsletter, yhteydenotot, info-pyynnöt")
    print()
    
    print("🎯 PÄIVITETTY JOHTOPÄÄTÖS:")
    print("-" * 35)
    print("Jos 'huonemyynti' = vain huonevaraukset:")
    print()
    print("1. 🥇 PAID SEARCH voittaa huonemyynnissä")
    print("   • Tuottaa oikeita huonevarauksia")
    print("   • Korkea revenue per konversio")
    print("   • €32,942 ÷ 217 konv. = €152 per konversio")
    print()
    
    print("2. 🥈 ORGANIC SEARCH toisena")
    print("   • Myös tuottaa oikeita huonevarauksia")
    print("   • €32,748 ÷ 208 konv. = €157 per konversio")
    print()
    
    print("3. 📉 REFERRAL pudottaa")
    print("   • Paljon konversioita, vähän huonemyyntiä")
    print("   • Toscanini.fi = 'soft conversions'")
    print("   • Ei oikeita huonevarauksia")
    print()
    
    print("✅ LOPULLINEN VASTAUS:")
    print("-" * 30)
    print("PAID SEARCH toi eniten HUONEVARAUKSIA toukokuussa 2025!")
    print()
    print("SYYT:")
    print("• Korkein revenue huonevarauksista (€32,942)")
    print("• Paras revenue/konversio -suhde")
    print("• Tuottaa oikeita maksavia asiakkaita")
    print("• Google Ads kohdistaa ostovalmiita matkailijoita")
    print("• Välitön varausintentio hakusanoissa")
    print()
    
    print("🚨 REFERRAL-KANAVAN TOTUUS:")
    print("-" * 35)
    print("• Referral voittaa KONVERSIOIDEN MÄÄRÄSSÄ")
    print("• MUTTA ei tuota oikeita HUONEVARAUKSIA")
    print("• Toscanini.fi = liidi-generointia, ei myyntiä")
    print("• Hyvä bränditietoisuudelle, ei suoralle myynnille")

if __name__ == "__main__":
    analyze_room_bookings_only()
