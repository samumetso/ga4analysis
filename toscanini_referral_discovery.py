#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hotel Haven - Toscanini Referral-liikenteen löytö
Toscanini.fi ohjaa liikennettä Hotel Havenin sivustolle
"""

def toscanini_referral_discovery():
    """Analysoi Toscanini referral-liikenne"""
    
    print("🎯 TOSCANINI REFERRAL-LIIKENTEEN LÖYTÖ!")
    print("=" * 80)
    print()
    
    # Referral-lähteet toukokuu 2025
    referral_sources = [
        {"source": "toscanini.fi / referral", "sessions": 254, "users": 251},
        {"source": "kampcollectionhotels.com / referral", "sessions": 37, "users": 36},
        {"source": "strawberry.fi / referral", "sessions": 27, "users": 27},
        {"source": "strawberryhotels.com / referral", "sessions": 8, "users": 8},
        {"source": "tripadvisor.com / referral", "sessions": 4, "users": 4},
        {"source": "adola.sharepoint.com / referral", "sessions": 3, "users": 3},
        {"source": "congress.austropa-interconvention.at / referral", "sessions": 3, "users": 3},
        {"source": "p1phtl-sabre-sso.epsilon.com / referral", "sessions": 3, "users": 2},
        {"source": "app.cookiepro.com / referral", "sessions": 1, "users": 1},
        {"source": "interconvention.eventsair.com / referral", "sessions": 1, "users": 1},
        {"source": "l.instagram.com / referral", "sessions": 1, "users": 1},
        {"source": "privacywall.org / referral", "sessions": 1, "users": 1},
        {"source": "stadissa.fi / referral", "sessions": 1, "users": 1},
        {"source": "startpage.com / referral", "sessions": 1, "users": 1},
        {"source": "statics.teams.cdn.office.net / referral", "sessions": 1, "users": 1},
        {"source": "tagassistant.google.com / referral", "sessions": 1, "users": 1}
    ]
    
    total_referral_sessions = sum(item["sessions"] for item in referral_sources)
    total_referral_users = sum(item["users"] for item in referral_sources)
    
    print("📊 REFERRAL-LÄHTEET TOUKOKUU 2025:")
    print("-" * 40)
    print()
    
    print("TOP REFERRAL-LÄHTEET:")
    for i, source in enumerate(referral_sources[:10], 1):
        percentage = (source["sessions"] / total_referral_sessions) * 100
        print(f"{i:2}. {source['source']:<45} {source['sessions']:3} sessions ({percentage:4.1f}%)")
    
    print()
    print(f"YHTEENSÄ: {total_referral_sessions} sessions, {total_referral_users} users")
    print()
    
    # Toscanini analyysi
    toscanini_sessions = 254
    toscanini_percentage = (toscanini_sessions / total_referral_sessions) * 100
    
    print("🍝 TOSCANINI.FI ANALYYSI:")
    print("-" * 30)
    print()
    print(f"• Sessions: {toscanini_sessions}")
    print(f"• Users: 251")
    print(f"• Osuus referral-liikenteestä: {toscanini_percentage:.1f}%")
    print(f"• Suhde kokonais-referraliin: {toscanini_sessions}/{total_referral_sessions}")
    print()
    
    print("🔍 MIKÄ ON TOSCANINI.FI?")
    print("-" * 30)
    print()
    print("Toscanini.fi on todennäköisesti:")
    print("• 🍝 Ravintola Toscanini (Hotel Havenin ravintola)")
    print("• 🌐 Erillinen verkkosivusto ravintolalle")
    print("• 🔗 Linkittää Hotel Havenin sivustolle")
    print("• 📱 Mahdollisesti varausjärjestelmä")
    print()
    
    print("💡 MIKSI TOSCANINI OHJAA LIIKENNETTÄ:")
    print("-" * 45)
    print()
    print("MAHDOLLISET SYYT:")
    print("1. 🏨 HOTELLIVARAUKSET")
    print("   • Ravintolan sivustolla linkki hotelliin")
    print("   • 'Varaa yöpyminen' -painike")
    print("   • Pakettivaraukset (illallinen + yöpyminen)")
    print()
    print("2. 🍽️ RAVINTOLAN TIEDOT")
    print("   • Hotellin sivustolla ravintolan tiedot")
    print("   • Takaisin ravintolan sivustolle")
    print("   • Ruokalistat, aukioloajat")
    print()
    print("3. 🎯 MARKKINOINTIYHTEISTYÖ")
    print("   • Ristiin markkinointia")
    print("   • Yhteisiä kampanjoita")
    print("   • Cross-selling")
    print()
    
    print("📈 LIIKETOIMINTAVAIKUTUS:")
    print("-" * 30)
    print()
    print("TOSCANINI → HOTEL HAVEN:")
    print(f"• {toscanini_sessions} sessioita kuukaudessa")
    print("• Potentiaalisia hotellivarauksia")
    print("• Lisämyyntiä ravintolan kautta")
    print()
    
    # Vertaa muihin lähteisiin
    print("🏆 VERTAILU MUIHIN REFERRAL-LÄHTEISIIN:")
    print("-" * 50)
    print()
    print("Toscanini.fi on:")
    print(f"• #{1} suurin referral-lähde")
    print(f"• {toscanini_percentage:.1f}% kaikesta referral-liikenteestä")
    print(f"• {toscanini_sessions/37:.1f}x suurempi kuin #2 (kampcollectionhotels.com)")
    print()
    
    # Kanavittainen konteksti
    total_sessions_may = 33189  # Aikaisemmasta analyysistä
    referral_channel_sessions = 2242  # Aikaisemmasta analyysistä
    
    toscanini_vs_total = (toscanini_sessions / total_sessions_may) * 100
    toscanini_vs_referral_channel = (toscanini_sessions / referral_channel_sessions) * 100
    
    print("🌐 LAAJEMPI KONTEKSTI:")
    print("-" * 25)
    print()
    print(f"Toscanini.fi osuus:")
    print(f"• Kaikesta liikenteestä: {toscanini_vs_total:.2f}%")
    print(f"• Referral-kanavasta: {toscanini_vs_referral_channel:.1f}%")
    print()
    
    print("💭 JOHTOPÄÄTÖKSET:")
    print("-" * 25)
    print()
    print("1. ✅ TOSCANINI ON MERKITTÄVÄ LIIKENTEEN LÄHDE")
    print("   • Suurin yksittäinen referral-lähde")
    print("   • Vakaa käyttäjämäärä (254 sessioita)")
    print()
    print("2. 🔗 VAHVA YHTEYS HOTEL HAVENIIN")
    print("   • Todennäköisesti sama yritys/konserni")
    print("   • Strateginen linkitys sivustojen välillä")
    print()
    print("3. 🎯 LIIKETOIMINTAMAHDOLLISUUS")
    print("   • Optimoi linkitys entisestään")
    print("   • Seuraa konversioita Toscaninista")
    print("   • Kehitä yhteisiä kampanjoita")
    print()
    
    print("🔍 SUOSITUS JATKOTUTKIMUKSELLE:")
    print("-" * 40)
    print()
    print("ANALYSOI TOSCANINI-LIIKENTEEN LAATU:")
    print("• Konversiot (varaukset)")
    print("• Revenue per session")
    print("• Bounce rate")
    print("• Session duration")
    print()
    print("Tämä kertoo onko Toscanini-liikenne")
    print("laadukasta vai vain 'ohikulkua'.")

if __name__ == "__main__":
    toscanini_referral_discovery()
