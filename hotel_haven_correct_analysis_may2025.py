#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hotel Haven - OIKEA ANALYYSI Toukokuu 2025
Huonemyyntikanavat oikealla Property ID:llä (290658078)
"""

def analyze_hotel_haven_correct_data():
    """Analysoi Hotel Havenin oikea data toukokuulta 2025"""
    
    print("🏨 HOTEL HAVEN - OIKEA ANALYYSI TOUKOKUU 2025")
    print("=" * 80)
    print("Property ID: 290658078 (OIKEA Hotel Haven)")
    print()
    
    print("📊 HUONEMYYNTI KANAVITTAIN:")
    print("-" * 50)
    print()
    
    # Oikea data Property ID 290658078
    channel_data = [
        {"channel": "Referral", "conversions": 372.38, "revenue": 17364, "sessions": 327, "users": 323},
        {"channel": "Paid Search", "conversions": 217.16, "revenue": 32942, "sessions": 185, "users": 183},
        {"channel": "Organic Search", "conversions": 208.34, "revenue": 32748, "sessions": 200, "users": 194},
        {"channel": "Direct", "conversions": 96.00, "revenue": 15662, "sessions": 60, "users": 59},
        {"channel": "Paid Social", "conversions": 89.00, "revenue": 0, "sessions": 85, "users": 84},
        {"channel": "Email", "conversions": 8.22, "revenue": 622, "sessions": 18, "users": 17},
        {"channel": "Organic Social", "conversions": 6.00, "revenue": 818, "sessions": 5, "users": 5},
        {"channel": "Mobile Push", "conversions": 2.00, "revenue": 231, "sessions": 4, "users": 3},
        {"channel": "Unassigned", "conversions": 1.90, "revenue": 222, "sessions": 4, "users": 4},
        {"channel": "Cross-network", "conversions": 1.00, "revenue": 0, "sessions": 1, "users": 1}
    ]
    
    total_conversions = sum([c["conversions"] for c in channel_data])
    total_revenue = sum([c["revenue"] for c in channel_data])
    
    print("KANAVA              KONVERSIOT    REVENUE      SESSIONS   USERS")
    print("-" * 70)
    for i, data in enumerate(channel_data, 1):
        conv_pct = (data["conversions"] / total_conversions) * 100
        rev_pct = (data["revenue"] / total_revenue) * 100 if total_revenue > 0 else 0
        print(f"{i:2d}. {data['channel']:15s} {data['conversions']:8.1f} ({conv_pct:4.1f}%) €{data['revenue']:8,.0f} ({rev_pct:4.1f}%) {data['sessions']:4d} {data['users']:4d}")
    
    print("-" * 70)
    print(f"{'YHTEENSÄ':17s} {total_conversions:8.1f}        €{total_revenue:8,.0f}")
    print()
    
    print("🏆 VOITTAJAKANAVA KONVERSIOISSA:")
    print("-" * 40)
    winner = channel_data[0]  # Referral
    print(f"Kanava: {winner['channel']}")
    print(f"Konversiot: {winner['conversions']:.1f}")
    print(f"Osuus konversioista: {(winner['conversions']/total_conversions)*100:.1f}%")
    print(f"Revenue: €{winner['revenue']:,.0f}")
    print()
    
    print("💰 HUONEMYYNNIN TOP LÄHTEET:")
    print("-" * 40)
    top_sources = [
        {"source": "google / cpc", "conversions": 218.16, "revenue": 32942},
        {"source": "toscanini.fi / referral", "conversions": 246.44, "revenue": 200},
        {"source": "google / organic", "conversions": 172.70, "revenue": 23621},
        {"source": "(direct) / (none)", "conversions": 96.00, "revenue": 15662},
        {"source": "fb / cpc", "conversions": 48.40, "revenue": 0},
        {"source": "kampcollectionhotels.com / referral", "conversions": 47.15, "revenue": 4134},
        {"source": "strawberry.fi / referral", "conversions": 42.43, "revenue": 5589}
    ]
    
    for i, source in enumerate(top_sources[:5], 1):
        print(f"{i}. {source['source']:35s} {source['conversions']:6.1f} konv. €{source['revenue']:6,.0f}")
    
    print()
    
    print("🔍 MIKSI REFERRAL VOITTI KONVERSIOISSA:")
    print("-" * 55)
    print()
    
    print("1. 📈 SUURIN KONVERSIOMÄÄRÄ")
    print("   • 372.4 konversiota (37.1% kaikista)")
    print("   • 155 konversiota enemmän kuin toiseksi paras")
    print("   • Selkeä voittaja määrässä")
    print()
    
    print("2. 🎯 TOSCANINI.FI DOMINOI")
    print("   • 246.4 konversiota pelkästään toscanini.fi:stä")
    print("   • 66% referral-konversioista")
    print("   • Vahva paikallinen kumppani")
    print()
    
    print("3. 🏨 HOTELLIALALLE TYYPILLISTÄ")
    print("   • Matkailusivustot tuottavat paljon varauksia")
    print("   • Asiakkaat vertailevat hotelleja")
    print("   • Luottamus kolmannen osapuolen suosituksiin")
    print()
    
    print("4. 💡 MUTTA HUOMIO: REVENUE-PARADOKSI!")
    print("   • Referral: 372 konversiota = €17,364 revenue")
    print("   • Paid Search: 217 konversiota = €32,942 revenue")
    print("   • SELITYS: Eri konversiotyypit!")
    print("   • Toscanini.fi tuottaa vähän revenue:ta per konversio")
    print()
    
    print("🚨 KRIITTINEN HAVAINTO:")
    print("-" * 30)
    print("REFERRAL VOITTI KONVERSIOT, MUTTA EI REVENUE:TA!")
    print()
    print("• Referral-konversiot = Ehkä 'soft conversions'")
    print("• Paid Search konversiot = 'Hard conversions' (oikeat varaukset)")
    print("• Toscanini.fi: 246 konversiota, vain €200 revenue")
    print("• Google Ads: 218 konversiota, €32,942 revenue")
    print()
    
    print("💡 SELITYS:")
    print("-" * 15)
    print("1. Toscanini.fi lähettää liikennettä, mutta ei tuota revenue:ta")
    print("2. Mahdollisesti eri konversion määritelmä")
    print("3. Tai toscanini.fi-konversiot ovat esim. newsletter-tilauksia")
    print("4. Oikeat huonevaraukset tulevat Google Ads:sta")
    print()
    
    print("🎯 JOHTOPÄÄTÖS:")
    print("-" * 20)
    print("REFERRAL voitti KONVERSIOIDEN MÄÄRÄSSÄ")
    print("PAID SEARCH voitti HUONEMYYNNIN ARVOSSA")
    print()
    print("• Jos mittaat konversioita → Referral #1")
    print("• Jos mittaat revenue:ta → Paid Search #1")
    print("• Riippuu mitä 'huonemyyntiä' tarkoittaa!")
    print()
    
    print("✅ SUOSITUKSET:")
    print("-" * 20)
    print("1. Selvitä toscanini.fi:n konversioiden laatu")
    print("2. Varmista konversion määritelmä")
    print("3. Optimoi Paid Search (paras revenue/konversio)")
    print("4. Kehitä referral-kumppanuuksia (paras volyymi)")
    print("5. Mittaa sekä määrää että arvoa")

if __name__ == "__main__":
    analyze_hotel_haven_correct_data()
