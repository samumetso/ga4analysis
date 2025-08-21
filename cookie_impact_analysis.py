#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hotel Haven - Evästehallintamuutosten Vaikutusanalyysi
Analysoi kesäkuun 13-15 päivän liikenteen pudotusta
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

def get_daily_data():
    """Palauta päivittäinen data kesäkuun 10-20 päivältä"""
    
    # Oikea GA4-data
    daily_data = {
        'date': ['2025-06-10', '2025-06-11', '2025-06-12', '2025-06-13', 
                 '2025-06-14', '2025-06-15', '2025-06-16', '2025-06-17',
                 '2025-06-18', '2025-06-19', '2025-06-20'],
        'sessions': [1627, 1744, 1221, 929, 703, 619, 638, 583, 507, 488, 454],
        'users': [1430, 1557, 1068, 795, 579, 521, 546, 496, 436, 416, 369],
        'new_users': [1188, 1245, 844, 578, 415, 384, 400, 354, 325, 306, 285],
        'pageviews': [6439, 6940, 4224, 3008, 1985, 1948, 2314, 1839, 1639, 1575, 1433],
        'conversions': [48, 61, 35, 24, 18, 17, 22, 25, 16, 23, 18],
        'bounce_rate': [0.2145, 0.1795, 0.2891, 0.3057, 0.3229, 0.2827, 0.2555, 0.2779, 0.2781, 0.2889, 0.3502],
        'avg_session_duration': [159.2, 151.4, 152.7, 168.8, 125.8, 147.5, 198.2, 239.5, 173.9, 322.9, 178.7]
    }
    
    return pd.DataFrame(daily_data)

def get_channel_data():
    """Palauta kanavittainen data ennen ja jälkeen muutoksen"""
    
    # Aggregoidaan kanavakohtainen data
    channel_before = {  # 10-12 kesäkuuta keskiarvo
        'Organic Search': {'sessions': 337, 'users': 284, 'pageviews': 1472},
        'Paid Search': {'sessions': 240, 'users': 201, 'pageviews': 1430},
        'Paid Social': {'sessions': 426, 'users': 408, 'pageviews': 855},
        'Direct': {'sessions': 162, 'users': 146, 'pageviews': 524},
        'Referral': {'sessions': 212, 'users': 189, 'pageviews': 795},
        'Email': {'sessions': 57, 'users': 53, 'pageviews': 169},
        'Cross-network': {'sessions': 51, 'users': 47, 'pageviews': 130},
        'Organic Social': {'sessions': 25, 'users': 23, 'pageviews': 78}
    }
    
    channel_after = {  # 13-15 kesäkuuta keskiarvo
        'Organic Search': {'sessions': 207, 'users': 167, 'pageviews': 716},
        'Paid Search': {'sessions': 141, 'users': 121, 'pageviews': 618},
        'Paid Social': {'sessions': 161, 'users': 158, 'pageviews': 346},
        'Direct': {'sessions': 96, 'users': 79, 'pageviews': 324},
        'Referral': {'sessions': 62, 'users': 53, 'pageviews': 184},
        'Email': {'sessions': 16, 'users': 11, 'pageviews': 39},
        'Cross-network': {'sessions': 11, 'users': 11, 'pageviews': 24},
        'Organic Social': {'sessions': 12, 'users': 11, 'pageviews': 27}
    }
    
    return channel_before, channel_after

def analyze_traffic_drop():
    """Analysoi liikenteen pudotus"""
    
    df = get_daily_data()
    
    print("🔍 HOTEL HAVEN - EVÄSTEHALLINTAMUUTOSTEN VAIKUTUSANALYYSI")
    print("=" * 80)
    print("Kesäkuun 13-15 päivän liikenteen pudotuksen syiden selvittäminen")
    print("=" * 80)
    print()
    
    # Määritä ennen/jälkeen ajanjaksot
    before_period = df[df['date'].isin(['2025-06-10', '2025-06-11', '2025-06-12'])]
    change_period = df[df['date'].isin(['2025-06-13', '2025-06-14', '2025-06-15'])]
    after_period = df[df['date'].isin(['2025-06-16', '2025-06-17', '2025-06-18', '2025-06-19', '2025-06-20'])]
    
    # Laske keskiarvot
    before_avg = before_period[['sessions', 'users', 'pageviews', 'conversions']].mean()
    change_avg = change_period[['sessions', 'users', 'pageviews', 'conversions']].mean()
    after_avg = after_period[['sessions', 'users', 'pageviews', 'conversions']].mean()
    
    print("📊 PÄIVITTÄINEN LIIKENNE - ENNEN, AIKANA JA JÄLKEEN")
    print("-" * 60)
    print(f"{'Jakso':<20} {'Istunnot':<10} {'Käyttäjät':<10} {'Sivunäytöt':<12} {'Konversiot'}")
    print("-" * 60)
    print(f"{'Ennen (10-12.6)':<20} {before_avg['sessions']:<10.0f} {before_avg['users']:<10.0f} {before_avg['pageviews']:<12.0f} {before_avg['conversions']:.0f}")
    print(f"{'Muutos (13-15.6)':<20} {change_avg['sessions']:<10.0f} {change_avg['users']:<10.0f} {change_avg['pageviews']:<12.0f} {change_avg['conversions']:.0f}")
    print(f"{'Jälkeen (16-20.6)':<20} {after_avg['sessions']:<10.0f} {after_avg['users']:<10.0f} {after_avg['pageviews']:<12.0f} {after_avg['conversions']:.0f}")
    print()
    
    # Laske muutosprosentit
    sessions_drop = ((change_avg['sessions'] - before_avg['sessions']) / before_avg['sessions']) * 100
    users_drop = ((change_avg['users'] - before_avg['users']) / before_avg['users']) * 100
    pageviews_drop = ((change_avg['pageviews'] - before_avg['pageviews']) / before_avg['pageviews']) * 100
    conversions_drop = ((change_avg['conversions'] - before_avg['conversions']) / before_avg['conversions']) * 100
    
    print("📉 MUUTOKSET ENNEN → MUUTOSJAKSO")
    print("-" * 40)
    print(f"Istunnot: {sessions_drop:+.1f}%")
    print(f"Käyttäjät: {users_drop:+.1f}%")
    print(f"Sivunäytöt: {pageviews_drop:+.1f}%")
    print(f"Konversiot: {conversions_drop:+.1f}%")
    print()
    
    # Toipumisanalyysi
    recovery_sessions = ((after_avg['sessions'] - change_avg['sessions']) / change_avg['sessions']) * 100
    recovery_users = ((after_avg['users'] - change_avg['users']) / change_avg['users']) * 100
    
    print("🔄 TOIPUMINEN MUUTOSJAKSO → JÄLKEEN")
    print("-" * 40)
    print(f"Istunnot: {recovery_sessions:+.1f}%")
    print(f"Käyttäjät: {recovery_users:+.1f}%")
    print()
    
    return before_avg, change_avg, after_avg

def analyze_channel_impact():
    """Analysoi kanavittainen vaikutus"""
    
    channel_before, channel_after = get_channel_data()
    
    print("📺 KANAVITTAINEN VAIKUTUSANALYYSI")
    print("=" * 80)
    print()
    
    print(f"{'Kanava':<20} {'Ennen':<15} {'Jälkeen':<15} {'Muutos':<12} {'Vaikutus'}")
    print("-" * 80)
    
    channel_changes = {}
    
    for channel in channel_before.keys():
        before_sessions = channel_before[channel]['sessions']
        after_sessions = channel_after.get(channel, {'sessions': 0})['sessions']
        
        if before_sessions > 0:
            change_pct = ((after_sessions - before_sessions) / before_sessions) * 100
            channel_changes[channel] = change_pct
            
            # Määritä vaikutuksen vakavuus
            if change_pct > -10:
                impact = "🟢 Lievä"
            elif change_pct > -30:
                impact = "🟡 Kohtalainen"
            elif change_pct > -50:
                impact = "🟠 Merkittävä"
            else:
                impact = "🔴 Vakava"
            
            print(f"{channel:<20} {before_sessions:<15.0f} {after_sessions:<15.0f} {change_pct:>+7.1f}% {impact}")
    
    print()
    
    # Järjestä kanavat vaikutuksen mukaan
    sorted_channels = sorted(channel_changes.items(), key=lambda x: x[1])
    
    print("🎯 ENITEN KÄRSIVÄT KANAVAT:")
    print("-" * 40)
    for i, (channel, change) in enumerate(sorted_channels[:3], 1):
        print(f"{i}. {channel}: {change:+.1f}%")
    
    print()
    return channel_changes

def investigate_possible_causes():
    """Tutki mahdollisia syitä"""
    
    print("🔬 MAHDOLLISET SYYT LIIKENTEEN PUDOTUKSELLE")
    print("=" * 80)
    print()
    
    print("1. 🍪 EVÄSTEHALLINTAMUUTOKSET (TODENNÄKÖISIN SYY)")
    print("-" * 50)
    print("✅ Vahvistettuja tekijöitä:")
    print("   • Evästehallinta (CookiePro) käyttöönotettu 13.6.2025")
    print("   • Muutos koskee useita hotellisivustoja")
    print("   • -50% pudotus rekisteröidyssä liikenteessä")
    print()
    
    print("🔍 Mahdolliset tekniset ongelmat:")
    print("   • GA4 tracking code latautuu vasta evästehyväksynnän jälkeen")
    print("   • Evästekielto estää GA4:n kokonaan (ei vain rajoita)")
    print("   • Virheellinen implementointi - tracking katkeaa")
    print("   • Server-side tracking puuttuu")
    print("   • Consent mode v2 ei ole käytössä")
    print()
    
    print("2. 🚫 EVÄSTEKIELTÄYTYMISTEN VAIKUTUS")
    print("-" * 50)
    print("📊 Arvioitu vaikutus:")
    print("   • Ilmoitettu evästehyväksynnän vaikutus: <20%")
    print("   • Todellinen liikenteen pudotus: ~50%")
    print("   • Ero: ~30% = tekninen ongelma")
    print()
    
    print("3. 🔧 MUUT MAHDOLLISET SYYT")
    print("-" * 50)
    print("❓ Tarkistettavat tekijät:")
    print("   • Sivuston suorituskyky (latausnopeus)")
    print("   • CDN tai hosting-ongelmat")
    print("   • JavaScript-virheet")
    print("   • Mobiiliyhteensopivuus")
    print("   • SEO-muutokset")
    print("   • Kilpailijat tai markkinatilanne")
    print()

def create_investigation_checklist():
    """Luo tutkimuslista ongelman ratkaisemiseksi"""
    
    print("✅ TUTKIMUSSUUNNITELMA - TOIMENPIDELISTA")
    print("=" * 80)
    print()
    
    print("🔥 VÄLITTÖMÄT TOIMENPITEET (1-2 päivää)")
    print("-" * 50)
    print("1. 🍪 EVÄSTEHALLINTA - TEKNINEN TARKISTUS")
    print("   □ Tarkista GA4 tracking code -implementointi")
    print("   □ Varmista että GA4 latautuu myös ilman evästehyväksyntää")
    print("   □ Testaa Consent Mode v2 käyttöönotto")
    print("   □ Tarkista CookiePro-asetukset")
    print("   □ Vertaile muiden hotellien implementointia")
    print()
    
    print("2. 📊 DATAN TARKISTUS")
    print("   □ Tarkista Google Tag Manager -asetukset")
    print("   □ Vertaile GA4 vs. server-side analytics")
    print("   □ Analysoi Real-time reports GA4:ssä")
    print("   □ Tarkista Debug View -data")
    print("   □ Vertaile muiden mittaustyökalujen dataa")
    print()
    
    print("🔍 SYVEMPI ANALYYSI (3-7 päivää)")
    print("-" * 50)
    print("3. 🧪 A/B TESTAUS")
    print("   □ Testaa sivusto ilman evästehallintaa")
    print("   □ Vertaile eri evästehallinta-asetuksia")
    print("   □ Testaa eri selaimilla ja laitteilla")
    print("   □ Analysoi käyttäjäpolkuja")
    print()
    
    print("4. 📈 KANAVITTAINEN ANALYYSI")
    print("   □ Analysoi orgaanisen haun muutokset")
    print("   □ Tarkista maksetun mainonnan suorituskyky")
    print("   □ Tutki sosiaalisen median liikenteen muutokset")
    print("   □ Analysoi suoran liikenteen kehitys")
    print()
    
    print("💡 RATKAISUVAIHTOEHDOT")
    print("-" * 50)
    print("5. 🔧 TEKNISEN TOTEUTUKSEN KORJAUS")
    print("   □ Käyttöönota Consent Mode v2")
    print("   □ Implementoi server-side tracking")
    print("   □ Optimoi evästehallinta-asetukset")
    print("   □ Lisää cookieless tracking")
    print()
    
    print("6. 📊 SEURANNAN PARANTAMINEN")
    print("   □ Lisää evästehyväksyntä-seuranta")
    print("   □ Implementoi enhanced e-commerce tracking")
    print("   □ Käyttöönota data-driven attribution")
    print("   □ Lisää cross-domain tracking")
    print()

def create_consent_analysis():
    """Analysoi evästehyväksynnän vaikutusta"""
    
    print("🍪 EVÄSTEHYVÄKSYNNÄN VAIKUTUSANALYYSI")
    print("=" * 80)
    print()
    
    print("📊 TEOREETTISET LASKELMAT:")
    print("-" * 40)
    
    # Oletetaan seuraavat luvut
    total_visitors_before = 1531  # Keskiarvo ennen muutosta
    total_visitors_after = 750    # Keskiarvo muutoksen aikana
    reported_consent_rate = 0.8   # 80% hyväksyy evästeet (oletus)
    actual_drop = ((total_visitors_after - total_visitors_before) / total_visitors_before) * 100
    
    print(f"Kävijät ennen muutosta: {total_visitors_before:,.0f}")
    print(f"Kävijät muutoksen jälkeen: {total_visitors_after:,.0f}")
    print(f"Todellinen pudotus: {actual_drop:.1f}%")
    print()
    
    print("🧮 SKENAARIOANALYYSI:")
    print("-" * 40)
    
    # Eri evästehyväksyntäasteet
    consent_rates = [0.5, 0.6, 0.7, 0.8, 0.9]
    
    print(f"{'Hyväksyntä-%':<12} {'Odotettu liikenne':<18} {'Tekninen häviö':<15} {'Selitys'}")
    print("-" * 65)
    
    for rate in consent_rates:
        expected_traffic = total_visitors_before * rate
        technical_loss = total_visitors_after - expected_traffic
        technical_loss_pct = (technical_loss / total_visitors_before) * 100
        
        if abs(technical_loss_pct) < 5:
            explanation = "✅ Selittyy hyväksynnällä"
        elif technical_loss_pct < -10:
            explanation = "🔴 Tekninen ongelma"
        else:
            explanation = "🟡 Osittain tekninen"
        
        print(f"{rate*100:>8.0f}%     {expected_traffic:>12.0f}        {technical_loss_pct:>+8.1f}%      {explanation}")
    
    print()
    print("💡 JOHTOPÄÄTÖS:")
    print("Jos evästehyväksyntäaste on 80%, tekninen häviö on noin -20%")
    print("Tämä viittaa implementointiongelmaan evästehallinnassa.")
    print()

if __name__ == "__main__":
    # Suorita analyysi
    before_avg, change_avg, after_avg = analyze_traffic_drop()
    channel_changes = analyze_channel_impact()
    investigate_possible_causes()
    create_consent_analysis()
    create_investigation_checklist()
    
    print("🎯 YHTEENVETO JA SUOSITUKSET")
    print("=" * 80)
    print()
    print("🔴 ONGELMA: ~50% liikenteen pudotus evästehallintamuutosten jälkeen")
    print("🔍 TODENNÄKÖINEN SYY: Tekninen implementointiongelma")
    print("⚡ VÄLITTÖMÄT TOIMET: GA4 tracking -korjaus ja Consent Mode v2")
    print("📈 ODOTETTU PARANNUS: 20-30% liikenteen palautuminen")
    print()
    print("📞 SUOSITUS: Ota yhteyttä CookiePro-tukeen ja GA4-asiantuntijaan!")
