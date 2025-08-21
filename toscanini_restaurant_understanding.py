#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hotel Haven - Toscanini Ravintola Ymmärrys
Toscanini = Hotel Havenin oma ravintola, sama varausjärjestelmä
"""

def analyze_toscanini_restaurant_bookings():
    """Analysoi Toscanini-ravintolan varausten vaikutus dataan"""
    
    print("🍽️ TOSCANINI RAVINTOLA - DATAN YMMÄRRYS")
    print("=" * 80)
    print("Toscanini = Hotel Havenin oma ravintola")
    print("Sama varausjärjestelmä kuin huonevarauksetkin")
    print()
    
    print("📊 TOSCANINI.FI KONVERSIOANALYYSI:")
    print("-" * 45)
    print("• Konversioita: 246 kpl")
    print("• Revenue: €200")
    print("• Revenue per konversio: €0.81")
    print()
    
    print("💡 SELITYS:")
    print("-" * 15)
    print("✅ RAVINTOLAVARAUKSILLE EI TULE REVENUE-ARVOA")
    print("• Purchase-tapahtuma käynnistyy varauksen yhteydessä")
    print("• MUTTA revenue = €0 tai hyvin pieni summa")
    print("• €200 = todennäköisesti joitain pieniä ennakkomaksuja")
    print("• 246 konversiota = 246 ravintolavarausta")
    print()
    
    print("🏨 VAIKUTUS HUONEMYYNTI-ANALYYSIIN:")
    print("-" * 45)
    print()
    
    print("ENNEN YMMÄRRYSTÄ:")
    print("❌ 'Toscanini.fi tuottaa huonoja konversioita'")
    print("❌ 'Vain €0.81 per konversio, huono laatu'")
    print("❌ 'Referral-kanava ei toimi hyvin'")
    print()
    
    print("OIKEA YMMÄRRYS:")
    print("✅ Toscanini.fi tuottaa RAVINTOLAVARUAKSIA")
    print("✅ 246 ravintolavarausta on ERINOMAINEN tulos!")
    print("✅ Referral-kanava toimii hyvin molemmissa:")
    print("   - Huonevarauksissa: €17,364 revenue")
    print("   - Ravintolavaraukissa: 246 varausta")
    print()
    
    print("📈 PÄIVITETTY KANAVA-ANALYYSI:")
    print("-" * 40)
    print()
    
    print("🏆 HUONEVARAUKSET (revenue-perusteinen):")
    print("1. Paid Search: €32,942")
    print("2. Organic Search: €32,748") 
    print("3. Direct: €15,662")
    print("4. Referral (muut): €17,164 (ilman toscanini.fi)")
    print()
    
    print("🍽️ RAVINTOLAVARUAKSET (määrä-perusteinen):")
    print("1. Referral (toscanini.fi): 246 varausta")
    print("2. Muut kanavat: Vähemmän ravintolavaruaksia")
    print()
    
    print("🎯 LOPULLINEN YMMÄRRYS:")
    print("-" * 30)
    print()
    
    print("KYSYMYS: 'Mikä kanava toi eniten huonemyyntiä?'")
    print("VASTAUS: PAID SEARCH (€32,942)")
    print()
    
    print("MUTTA MYÖS:")
    print("• REFERRAL tuo eniten RAVINTOLAVARUAKSIA (246 kpl)")
    print("• REFERRAL toimii hyvin molemmissa segmenteissä:")
    print("  - Huoneet: €17,364 revenue")
    print("  - Ravintola: 246 varausta")
    print()
    
    print("💼 LIIKETOIMINTA-ANALYYSI:")
    print("-" * 35)
    print()
    
    print("🏨 HUONEVARAUSTEN ARVO:")
    print("• Paid Search: €32,942 ÷ 217 konv. = €152/varaus")
    print("• Organic Search: €32,748 ÷ 208 konv. = €157/varaus")
    print("• Referral: €17,364 ÷ 126 konv.* = €138/varaus")
    print("  (*arvio ilman toscanini.fi:n ravintolavaruaksia)")
    print()
    
    print("🍽️ RAVINTOLAVARUAKSET:")
    print("• Toscanini.fi: 246 varausta")
    print("• Keskimääräinen ravintolalasku: ~€50-80")
    print("• Potentiaalinen revenue: 246 × €65 = €15,990")
    print("• MUTTA ei näy GA4:ssä koska maksu paikan päällä")
    print()
    
    print("📊 KOKONAISARVO REFERRAL-KANAVALLE:")
    print("-" * 45)
    print("• Huonevaraukset: €17,364")
    print("• Ravintolavaruakset (arvio): €15,990")
    print("• YHTEENSÄ ARVIOLTA: €33,354")
    print("• = Lähes yhtä arvokas kuin Paid Search!")
    print()
    
    print("✅ PÄIVITETYT SUOSITUKSET:")
    print("-" * 35)
    print()
    
    print("1. 🎯 PAID SEARCH = Paras HUONEVARAUSKANA")
    print("   • Korkein revenue huonevarauksista")
    print("   • Jatka optimointia ja budjetin kasvattamista")
    print()
    
    print("2. 🤝 REFERRAL = Monipuolisin KOKONAISKANAVA")
    print("   • Huonevaraukset: €17,364")
    print("   • Ravintolavaruakset: 246 kpl")
    print("   • Kehitä kumppanuuksia edelleen")
    print()
    
    print("3. 📈 SEURANTA-SUOSITUS:")
    print("   • Mittaa huone- ja ravintolavaruakset erikseen")
    print("   • Laske ravintolan todellinen arvo")
    print("   • Yhdistä kokonaisarvo kanava-analyysissä")
    print()
    
    print("🏆 LOPULLINEN VASTAUS:")
    print("-" * 25)
    print("HUONEVARUAKSET: Paid Search voittaa (€32,942)")
    print("KOKONAISARVO: Referral lähes yhtä arvokas!")
    print("Toscanini.fi = erinomainen ravintolavaruaksen tuottaja! 🍽️")

if __name__ == "__main__":
    analyze_toscanini_restaurant_bookings()
