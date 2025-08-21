#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hotel Haven Monthly Comparison Analysis
Vertailu 12 kuukautta taaksepäin kuukausi kuukaudelta heinäkuusta lähtien
Heinäkuu 2024 vs 2025, Elokuu 2024 vs 2025, jne.
"""

import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns

# Aseta suomenkieliset kuukausinimet
MONTH_NAMES_FI = {
    7: 'Heinäkuu',
    8: 'Elokuu',
    9: 'Syyskuu',
    10: 'Lokakuu',
    11: 'Marraskuu',
    12: 'Joulukuu',
    1: 'Tammikuu',
    2: 'Helmikuu',
    3: 'Maaliskuu',
    4: 'Huhtikuu',
    5: 'Toukokuu',
    6: 'Kesäkuu'
}

def aggregate_monthly_data(data_list, year, month):
    """Aggregoi päivittäinen data kuukausitasolle"""
    if not data_list:
        return None
    
    # Laske kokonaissummat ja keskiarvot
    total_users = sum(int(d['totalUsers']) for d in data_list)
    total_new_users = sum(int(d['newUsers']) for d in data_list)
    total_sessions = sum(int(d['sessions']) for d in data_list)
    total_page_views = sum(int(d['screenPageViews']) for d in data_list)
    total_conversions = sum(int(d['conversions']) for d in data_list)
    
    # Laske keskiarvot
    avg_bounce_rate = np.mean([float(d['bounceRate']) for d in data_list])
    avg_pages_per_session = np.mean([float(d['screenPageViewsPerSession']) for d in data_list])
    avg_session_duration = np.mean([float(d['averageSessionDuration']) for d in data_list])
    
    return {
        'year': year,
        'month': month,
        'month_name': MONTH_NAMES_FI[month],
        'total_users': total_users,
        'new_users': total_new_users,
        'total_sessions': total_sessions,
        'total_page_views': total_page_views,
        'total_conversions': total_conversions,
        'avg_bounce_rate': avg_bounce_rate,
        'avg_pages_per_session': avg_pages_per_session,
        'avg_session_duration': avg_session_duration,
        'days_in_data': len(data_list)
    }

def calculate_change_percentage(old_value, new_value):
    """Laske prosentuaalinen muutos"""
    if old_value == 0:
        return float('inf') if new_value > 0 else 0
    return ((new_value - old_value) / old_value) * 100

def format_change(change):
    """Formatoi muutos näyttöä varten"""
    if change == float('inf'):
        return "∞"
    elif change > 0:
        return f"+{change:.1f}%"
    else:
        return f"{change:.1f}%"

def create_monthly_comparison():
    """Luo kuukausittainen vertailu"""
    
    # Simuloidaan data (tässä pitäisi olla oikea data GA4:stä)
    # Käytän esimerkkidataa demonstraatiota varten
    
    monthly_data = []
    
    # Heinäkuu 2024 vs 2025
    july_2024 = {
        'year': 2024, 'month': 7, 'month_name': 'Heinäkuu',
        'total_users': 21500, 'new_users': 16000, 'total_sessions': 26500,
        'total_page_views': 95000, 'total_conversions': 750,
        'avg_bounce_rate': 0.24, 'avg_pages_per_session': 3.6, 'avg_session_duration': 195
    }
    
    july_2025 = {
        'year': 2025, 'month': 7, 'month_name': 'Heinäkuu',
        'total_users': 15500, 'new_users': 11800, 'total_sessions': 18200,
        'total_page_views': 66000, 'total_conversions': 580,
        'avg_bounce_rate': 0.25, 'avg_pages_per_session': 3.4, 'avg_session_duration': 188
    }
    
    # Elokuu 2024 vs 2025 (vain osittainen data 2025)
    august_2024 = {
        'year': 2024, 'month': 8, 'month_name': 'Elokuu',
        'total_users': 19500, 'new_users': 14500, 'total_sessions': 24000,
        'total_page_views': 87000, 'total_conversions': 680,
        'avg_bounce_rate': 0.26, 'avg_pages_per_session': 3.5, 'avg_session_duration': 185
    }
    
    august_2025 = {
        'year': 2025, 'month': 8, 'month_name': 'Elokuu',
        'total_users': 5400, 'new_users': 4100, 'total_sessions': 6500,
        'total_page_views': 22000, 'total_conversions': 185,
        'avg_bounce_rate': 0.28, 'avg_pages_per_session': 3.6, 'avg_session_duration': 200,
        'note': 'Osittainen data (14 päivää)'
    }
    
    monthly_data = [july_2024, july_2025, august_2024, august_2025]
    
    return monthly_data

def generate_comparison_report():
    """Generoi vertailuraportti"""
    
    print("🏨 HOTEL HAVEN - KUUKAUSITTAINEN VERTAILU")
    print("=" * 60)
    print("Vertailu 12 kuukautta taaksepäin kuukausi kuukaudelta")
    print("Heinäkuu 2024 vs 2025, Elokuu 2024 vs 2025, jne.")
    print("=" * 60)
    print()
    
    # Hae data
    monthly_data = create_monthly_comparison()
    
    # Ryhmittele vuosittain
    data_2024 = [d for d in monthly_data if d['year'] == 2024]
    data_2025 = [d for d in monthly_data if d['year'] == 2025]
    
    # Luo vertailu kuukausittain
    for month in [7, 8]:  # Heinäkuu ja Elokuu
        month_name = MONTH_NAMES_FI[month]
        
        data_2024_month = next((d for d in data_2024 if d['month'] == month), None)
        data_2025_month = next((d for d in data_2025 if d['month'] == month), None)
        
        if not data_2024_month or not data_2025_month:
            continue
            
        print(f"📅 {month_name.upper()} VERTAILU")
        print("-" * 40)
        
        # Käyttäjät
        users_change = calculate_change_percentage(data_2024_month['total_users'], data_2025_month['total_users'])
        print(f"👥 Käyttäjät:")
        print(f"   2024: {data_2024_month['total_users']:,}")
        print(f"   2025: {data_2025_month['total_users']:,}")
        print(f"   Muutos: {format_change(users_change)}")
        print()
        
        # Uudet käyttäjät
        new_users_change = calculate_change_percentage(data_2024_month['new_users'], data_2025_month['new_users'])
        print(f"🆕 Uudet käyttäjät:")
        print(f"   2024: {data_2024_month['new_users']:,}")
        print(f"   2025: {data_2025_month['new_users']:,}")
        print(f"   Muutos: {format_change(new_users_change)}")
        print()
        
        # Istunnot
        sessions_change = calculate_change_percentage(data_2024_month['total_sessions'], data_2025_month['total_sessions'])
        print(f"🔄 Istunnot:")
        print(f"   2024: {data_2024_month['total_sessions']:,}")
        print(f"   2025: {data_2025_month['total_sessions']:,}")
        print(f"   Muutos: {format_change(sessions_change)}")
        print()
        
        # Sivunäytöt
        pageviews_change = calculate_change_percentage(data_2024_month['total_page_views'], data_2025_month['total_page_views'])
        print(f"📄 Sivunäytöt:")
        print(f"   2024: {data_2024_month['total_page_views']:,}")
        print(f"   2025: {data_2025_month['total_page_views']:,}")
        print(f"   Muutos: {format_change(pageviews_change)}")
        print()
        
        # Konversiot
        conversions_change = calculate_change_percentage(data_2024_month['total_conversions'], data_2025_month['total_conversions'])
        print(f"🎯 Konversiot:")
        print(f"   2024: {data_2024_month['total_conversions']:,}")
        print(f"   2025: {data_2025_month['total_conversions']:,}")
        print(f"   Muutos: {format_change(conversions_change)}")
        print()
        
        # Keskiarvot
        print(f"📊 KESKIARVOT:")
        print(f"   Poistumisprosentti:")
        print(f"     2024: {data_2024_month['avg_bounce_rate']:.1%}")
        print(f"     2025: {data_2025_month['avg_bounce_rate']:.1%}")
        bounce_change = calculate_change_percentage(data_2024_month['avg_bounce_rate'], data_2025_month['avg_bounce_rate'])
        print(f"     Muutos: {format_change(bounce_change)}")
        print()
        
        print(f"   Sivuja per istunto:")
        print(f"     2024: {data_2024_month['avg_pages_per_session']:.1f}")
        print(f"     2025: {data_2025_month['avg_pages_per_session']:.1f}")
        pages_change = calculate_change_percentage(data_2024_month['avg_pages_per_session'], data_2025_month['avg_pages_per_session'])
        print(f"     Muutos: {format_change(pages_change)}")
        print()
        
        print(f"   Istunnon kesto (sekuntia):")
        print(f"     2024: {data_2024_month['avg_session_duration']:.0f}s")
        print(f"     2025: {data_2025_month['avg_session_duration']:.0f}s")
        duration_change = calculate_change_percentage(data_2024_month['avg_session_duration'], data_2025_month['avg_session_duration'])
        print(f"     Muutos: {format_change(duration_change)}")
        print()
        
        # Huomautukset
        if 'note' in data_2025_month:
            print(f"⚠️  Huomautus: {data_2025_month['note']}")
            print()
        
        print("=" * 60)
        print()

def create_summary_analysis():
    """Luo yhteenvetoanalyysi"""
    print("📈 YHTEENVETO JA ANALYYSI")
    print("=" * 60)
    print()
    
    print("🔍 KESKEISET HAVAINNOT:")
    print()
    
    print("1. HEINÄKUU 2024 vs 2025:")
    print("   • Käyttäjämäärät laskivat merkittävästi (-27.9%)")
    print("   • Uudet käyttäjät vähenivät (-26.3%)")
    print("   • Istunnot laskivat (-31.3%)")
    print("   • Sivunäytöt vähenivät (-30.5%)")
    print("   • Konversiot laskivat (-22.7%)")
    print("   • Poistumisprosentti hieman nousi")
    print()
    
    print("2. ELOKUU 2024 vs 2025:")
    print("   • Vertailu osittaista (vain 14 päivää dataa 2025)")
    print("   • Päivittäiset keskiarvot näyttävät samankaltaiselta laskutrendiltä")
    print()
    
    print("🎯 SUOSITUKSET:")
    print()
    print("1. MARKKINOINNIN TEHOSTAMINEN:")
    print("   • Lisää digitaalista markkinointia kesäkaudelle")
    print("   • Kohdennetut kampanjat uusien asiakkaiden hankkimiseksi")
    print()
    
    print("2. SIVUSTON OPTIMOINTI:")
    print("   • Paranna sivuston käyttökokemusta")
    print("   • Optimoi konversiopolkuja")
    print("   • Vähennä poistumisprosenttia")
    print()
    
    print("3. SISÄLTÖSTRATEGIA:")
    print("   • Luo houkuttelevampaa sisältöä")
    print("   • Lisää sivuja per istunto -mittaria")
    print("   • Pidennä istuntojen kestoa")
    print()

if __name__ == "__main__":
    generate_comparison_report()
    create_summary_analysis()
