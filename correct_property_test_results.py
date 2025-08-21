#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hotel Haven - Oikean Property:n testaus
Testaus Property 290658078 lukuoikeuksien lisäämisen jälkeen
"""

def correct_property_test_results():
    """Analysoi tulokset oikealla Property ID:llä"""
    
    print("📊 OIKEAN PROPERTY:N TESTAUS - TULOKSET")
    print("=" * 80)
    print()
    
    print("🔧 ASETUKSET:")
    print("-" * 15)
    print("• Property ID: 290658078 (Hotel Haven oikea)")
    print("• Lukuoikeudet: Lisätty uudelleen")
    print("• Aikaväli: 1.-31.5.2025")
    print()
    
    # Lasketaan kokonaisluvut päivittäisestä datasta
    daily_sessions = [1391, 1169, 1154, 1845, 1225, 1132, 1148, 1003, 1093, 1139]
    daily_users = [1249, 1023, 1044, 1654, 1098, 1044, 1050, 892, 950, 1033]
    daily_new_users = [1023, 826, 828, 1391, 865, 823, 866, 712, 706, 822]
    
    # Kanavittaiset luvut
    channel_sessions = [8354, 7509, 6780, 4203, 2242, 1370, 1260, 618, 487, 73, 30, 23]
    channel_users = [5836, 6884, 5381, 3377, 1735, 1087, 1036, 580, 465, 62, 27, 23]
    
    total_channel_sessions = sum(channel_sessions)
    total_channel_users = sum(channel_users)
    
    # Referral-lähteet
    referral_sources = [
        ("toscanini.fi / referral", 254),
        ("kampcollectionhotels.com / referral", 37),
        ("strawberry.fi / referral", 27),
        ("strawberryhotels.com / referral", 8),
        ("tripadvisor.com / referral", 4),
        ("adola.sharepoint.com / referral", 3),
        ("congress.austropa-interconvention.at / referral", 3),
        ("p1phtl-sabre-sso.epsilon.com / referral", 3)
    ]
    
    total_referral_sessions = sum(sessions for _, sessions in referral_sources)
    
    print("📈 MCP TULOKSET (Property 290658078):")
    print("-" * 45)
    print()
    
    print("KOKONAISLUVUT:")
    print(f"• Sessions (kanavittain): {total_channel_sessions:,}")
    print(f"• Users (kanavittain): {total_channel_users:,}")
    print()
    
    print("TOP 5 KANAVAA (Sessions):")
    channels = [
        ("Organic Search", 8354, 5836),
        ("Paid Social", 7509, 6884),
        ("Paid Search", 6780, 5381),
        ("Direct", 4203, 3377),
        ("Referral", 2242, 1735)
    ]
    
    for i, (channel, sessions, users) in enumerate(channels, 1):
        percentage = (sessions / total_channel_sessions) * 100
        print(f"{i}. {channel}: {sessions:,} sessions ({percentage:.1f}%)")
    
    print()
    print("REFERRAL-LÄHTEET:")
    print(f"• Yhteensä: {total_referral_sessions} sessions")
    print(f"• Toscanini.fi: {referral_sources[0][1]} sessions ({(referral_sources[0][1]/total_referral_sessions)*100:.1f}%)")
    print("• Muut referral-lähteet:")
    for source, sessions in referral_sources[1:5]:
        print(f"  - {source}: {sessions}")
    
    print()
    print("🔍 VERTAILU AIEMPAAN:")
    print("-" * 25)
    print()
    
    print("ONKO DATA MUUTTUNUT?")
    print("• Sessions: SAMA (33,189 vs aiempi)")
    print("• Toscanini.fi: SAMA (254 sessions)")
    print("• Kanavat: SAMAT")
    print("• Referral-lähteet: SAMAT")
    print()
    
    print("❗ JOHTOPÄÄTÖS:")
    print("DATA ON EDELLEEN TÄSMÄLLEEN SAMA!")
    print()
    
    print("🤔 MITÄ TÄMÄ TARKOITTAA:")
    print("-" * 30)
    print()
    
    print("MAHDOLLISET SKENAARIOT:")
    print()
    print("1. 🔗 PROPERTY:T JAKAVAT DATAN")
    print("   • 290658078 ja 290818724 ovat linkitettyjä")
    print("   • Cross-domain tracking")
    print("   • Sama data molemmissa")
    print()
    
    print("2. 🎯 MCP KÄYTTÄÄ EDELLEEN VANHAA")
    print("   • Ympäristömuuttuja ei päivittynyt")
    print("   • Cache-ongelma")
    print("   • API-kutsu menee väärään property:yn")
    print()
    
    print("3. 🏨 HOTEL HAVENIN MONIMUTKAINEN SETUP")
    print("   • Useita property:jä samalle sivustolle")
    print("   • Kaikki keräävät samaa dataa")
    print("   • API aggregoi datan")
    print()
    
    print("🚨 KRIITTINEN KYSYMYS:")
    print("-" * 30)
    print()
    print("JOS MCP NÄKEE EDELLEEN TOSCANINI.FI:TÄ")
    print("MUTTA SINÄ ET NÄKEE SITÄ GA4:SSA:")
    print()
    print("• Onko Property 290658078 oikea Hotel Haven?")
    print("• Näkyykö siinä 33,189 sessioita toukokuulle?")
    print("• Miksi Toscanini.fi ei näy referraleissa?")
    print()
    
    print("💡 SEURAAVA TOIMENPIDE:")
    print("-" * 30)
    print()
    print("VERTAA GA4:SSA:")
    print("1. 📊 Sessions toukokuu Property 290658078: ?")
    print("2. 🔍 Referral-lähteet samassa property:ssä")
    print("3. 📈 Kanavittainen jakautuma")
    print()
    print("JOS GA4 LUVUT ≠ MCP LUVUT:")
    print("→ MCP käyttää edelleen väärää property:ä")
    print("→ Tai property:t jakavat datan")
    print()
    print("JOS GA4 LUVUT = MCP LUVUT:")
    print("→ MCP toimii oikein")
    print("→ Toscanini.fi on suodatettu pois GA4:stä")
    print("→ Internal Traffic tai muu suodatin")
    print()
    
    print("🎯 RATKAISUN LÖYTÄMINEN:")
    print("-" * 30)
    print()
    print("Kerro GA4:n luvut Property 290658078:sta:")
    print("• Sessions toukokuu 2025")
    print("• Top 5 kanavaa")
    print("• Referral-lähteet")
    print("• Näkyykö toscanini.fi missään?")
    print()
    print("Tämä kertoo onko MCP kalibroitu oikein!")

if __name__ == "__main__":
    correct_property_test_results()
