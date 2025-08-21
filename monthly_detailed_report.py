#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hotel Haven - Kuukausikohtainen Yksityiskohtainen Raportti
Jokainen kuukausi omana osionaan vertailuineen
"""

import json
from datetime import datetime
import pandas as pd

# Suomenkieliset kuukausinimet
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

def get_monthly_data():
    """Palauta kuukausittainen data"""
    return {
        # 2024 data
        'july_2024': {
            'year': 2024, 'month': 7, 'month_name': 'Heinäkuu',
            'total_users': 21687, 'new_users': 16185, 'total_sessions': 26412,
            'total_page_views': 95374, 'total_conversions': 751,
            'avg_bounce_rate': 0.244, 'avg_pages_per_session': 3.61, 
            'avg_session_duration': 195.2, 'days': 31
        },
        'august_2024': {
            'year': 2024, 'month': 8, 'month_name': 'Elokuu',
            'total_users': 19456, 'new_users': 14587, 'total_sessions': 24123,
            'total_page_views': 86943, 'total_conversions': 687,
            'avg_bounce_rate': 0.259, 'avg_pages_per_session': 3.53,
            'avg_session_duration': 184.8, 'days': 31
        },
        'september_2024': {
            'year': 2024, 'month': 9, 'month_name': 'Syyskuu',
            'total_users': 18743, 'new_users': 13892, 'total_sessions': 22456,
            'total_page_views': 89234, 'total_conversions': 756,
            'avg_bounce_rate': 0.252, 'avg_pages_per_session': 3.97,
            'avg_session_duration': 198.5, 'days': 30
        },
        'october_2024': {
            'year': 2024, 'month': 10, 'month_name': 'Lokakuu',
            'total_users': 19234, 'new_users': 14156, 'total_sessions': 23876,
            'total_page_views': 91345, 'total_conversions': 823,
            'avg_bounce_rate': 0.243, 'avg_pages_per_session': 3.73,
            'avg_session_duration': 203.2, 'days': 31
        },
        'november_2024': {
            'year': 2024, 'month': 11, 'month_name': 'Marraskuu',
            'total_users': 22987, 'new_users': 16743, 'total_sessions': 28456,
            'total_page_views': 114567, 'total_conversions': 1456,
            'avg_bounce_rate': 0.238, 'avg_pages_per_session': 4.02,
            'avg_session_duration': 234.7, 'days': 30
        },
        'december_2024': {
            'year': 2024, 'month': 12, 'month_name': 'Joulukuu',
            'total_users': 21234, 'new_users': 15687, 'total_sessions': 26789,
            'total_page_views': 107234, 'total_conversions': 891,
            'avg_bounce_rate': 0.245, 'avg_pages_per_session': 3.89,
            'avg_session_duration': 218.9, 'days': 31
        },
        
        # 2025 data
        'january_2025': {
            'year': 2025, 'month': 1, 'month_name': 'Tammikuu',
            'total_users': 19567, 'new_users': 14234, 'total_sessions': 24789,
            'total_page_views': 89456, 'total_conversions': 723,
            'avg_bounce_rate': 0.253, 'avg_pages_per_session': 3.61,
            'avg_session_duration': 225.4, 'days': 31
        },
        'february_2025': {
            'year': 2025, 'month': 2, 'month_name': 'Helmikuu',
            'total_users': 21456, 'new_users': 16234, 'total_sessions': 26789,
            'total_page_views': 92345, 'total_conversions': 567,
            'avg_bounce_rate': 0.247, 'avg_pages_per_session': 3.45,
            'avg_session_duration': 201.8, 'days': 28
        },
        'march_2025': {
            'year': 2025, 'month': 3, 'month_name': 'Maaliskuu',
            'total_users': 24567, 'new_users': 18234, 'total_sessions': 30456,
            'total_page_views': 125678, 'total_conversions': 1234,
            'avg_bounce_rate': 0.234, 'avg_pages_per_session': 4.12,
            'avg_session_duration': 243.5, 'days': 31
        },
        'april_2025': {
            'year': 2025, 'month': 4, 'month_name': 'Huhtikuu',
            'total_users': 26789, 'new_users': 20345, 'total_sessions': 32456,
            'total_page_views': 123456, 'total_conversions': 987,
            'avg_bounce_rate': 0.276, 'avg_pages_per_session': 3.81,
            'avg_session_duration': 189.3, 'days': 30
        },
        'may_2025': {
            'year': 2025, 'month': 5, 'month_name': 'Toukokuu',
            'total_users': 28456, 'new_users': 22134, 'total_sessions': 33789,
            'total_page_views': 129456, 'total_conversions': 1045,
            'avg_bounce_rate': 0.298, 'avg_pages_per_session': 3.83,
            'avg_session_duration': 175.6, 'days': 31
        },
        'june_2025': {
            'year': 2025, 'month': 6, 'month_name': 'Kesäkuu',
            'total_users': 27234, 'new_users': 21456, 'total_sessions': 32145,
            'total_page_views': 118567, 'total_conversions': 876,
            'avg_bounce_rate': 0.256, 'avg_pages_per_session': 3.69,
            'avg_session_duration': 169.8, 'days': 30
        },
        'july_2025': {
            'year': 2025, 'month': 7, 'month_name': 'Heinäkuu',
            'total_users': 15587, 'new_users': 11832, 'total_sessions': 18245,
            'total_page_views': 66234, 'total_conversions': 583,
            'avg_bounce_rate': 0.251, 'avg_pages_per_session': 3.43,
            'avg_session_duration': 188.7, 'days': 31
        },
        'august_2025': {
            'year': 2025, 'month': 8, 'month_name': 'Elokuu',
            'total_users': 5398, 'new_users': 4089, 'total_sessions': 6512,
            'total_page_views': 22143, 'total_conversions': 185,
            'avg_bounce_rate': 0.276, 'avg_pages_per_session': 3.62,
            'avg_session_duration': 200.4, 'days': 14, 'partial': True
        }
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

def get_trend_emoji(change):
    """Palauta emoji trendin mukaan"""
    if change > 10:
        return "🚀"
    elif change > 5:
        return "📈"
    elif change > 0:
        return "↗️"
    elif change == 0:
        return "➡️"
    elif change > -5:
        return "↘️"
    elif change > -10:
        return "📉"
    else:
        return "🔻"

def get_performance_rating(change):
    """Anna suorituskykyluokitus"""
    if change > 20:
        return "🌟 ERINOMAINEN"
    elif change > 10:
        return "✅ HYVÄ"
    elif change > 0:
        return "🟢 POSITIIVINEN"
    elif change == 0:
        return "⚪ ENNALLAAN"
    elif change > -10:
        return "🟡 LIEVÄ LASKU"
    elif change > -20:
        return "🟠 MERKITTÄVÄ LASKU"
    else:
        return "🔴 HUOLESTUTTAVA LASKU"

def create_monthly_comparison_report():
    """Luo kuukausikohtainen vertailuraportti"""
    
    data = get_monthly_data()
    
    print("🏨 HOTEL HAVEN - KUUKAUSIKOHTAINEN VERTAILURAPORTTI")
    print("=" * 80)
    print("Kuukausi-kuukaudelta vertailu vuosien 2024 ja 2025 välillä")
    print("=" * 80)
    print()
    
    # Kuukaudet joilla on vertailudata
    comparison_months = [
        ('july_2024', 'july_2025'),
        ('august_2024', 'august_2025')
    ]
    
    for i, (month_2024_key, month_2025_key) in enumerate(comparison_months, 1):
        data_2024 = data[month_2024_key]
        data_2025 = data[month_2025_key]
        
        month_name = data_2024['month_name']
        
        print(f"📅 {i}. {month_name.upper()} - VERTAILU 2024 vs 2025")
        print("=" * 60)
        print()
        
        # Laske kaikki muutokset
        users_change = calculate_change_percentage(data_2024['total_users'], data_2025['total_users'])
        new_users_change = calculate_change_percentage(data_2024['new_users'], data_2025['new_users'])
        sessions_change = calculate_change_percentage(data_2024['total_sessions'], data_2025['total_sessions'])
        pageviews_change = calculate_change_percentage(data_2024['total_page_views'], data_2025['total_page_views'])
        conversions_change = calculate_change_percentage(data_2024['total_conversions'], data_2025['total_conversions'])
        bounce_change = calculate_change_percentage(data_2024['avg_bounce_rate'], data_2025['avg_bounce_rate'])
        pages_per_session_change = calculate_change_percentage(data_2024['avg_pages_per_session'], data_2025['avg_pages_per_session'])
        duration_change = calculate_change_percentage(data_2024['avg_session_duration'], data_2025['avg_session_duration'])
        
        # Kokonaisarvio
        avg_change = (users_change + sessions_change + conversions_change) / 3
        print(f"🎯 KOKONAISARVIO: {get_performance_rating(avg_change)}")
        print(f"   Keskimääräinen muutos: {format_change(avg_change)}")
        print()
        
        # Yksityiskohtaiset mittarit
        print("📊 YKSITYISKOHTAISET MITTARIT:")
        print("-" * 40)
        
        print(f"👥 Käyttäjät: {get_trend_emoji(users_change)}")
        print(f"   2024: {data_2024['total_users']:,}")
        print(f"   2025: {data_2025['total_users']:,}")
        print(f"   Muutos: {format_change(users_change)} | {get_performance_rating(users_change)}")
        print()
        
        print(f"🆕 Uudet käyttäjät: {get_trend_emoji(new_users_change)}")
        print(f"   2024: {data_2024['new_users']:,}")
        print(f"   2025: {data_2025['new_users']:,}")
        print(f"   Muutos: {format_change(new_users_change)} | {get_performance_rating(new_users_change)}")
        print()
        
        print(f"🔄 Istunnot: {get_trend_emoji(sessions_change)}")
        print(f"   2024: {data_2024['total_sessions']:,}")
        print(f"   2025: {data_2025['total_sessions']:,}")
        print(f"   Muutos: {format_change(sessions_change)} | {get_performance_rating(sessions_change)}")
        print()
        
        print(f"📄 Sivunäytöt: {get_trend_emoji(pageviews_change)}")
        print(f"   2024: {data_2024['total_page_views']:,}")
        print(f"   2025: {data_2025['total_page_views']:,}")
        print(f"   Muutos: {format_change(pageviews_change)} | {get_performance_rating(pageviews_change)}")
        print()
        
        print(f"🎯 Konversiot: {get_trend_emoji(conversions_change)}")
        print(f"   2024: {data_2024['total_conversions']:,}")
        print(f"   2025: {data_2025['total_conversions']:,}")
        print(f"   Muutos: {format_change(conversions_change)} | {get_performance_rating(conversions_change)}")
        print()
        
        print("📈 LAATUMITTARIT:")
        print("-" * 40)
        
        print(f"📉 Poistumisprosentti: {get_trend_emoji(-bounce_change)}")  # Käännetty, koska pienempi on parempi
        print(f"   2024: {data_2024['avg_bounce_rate']:.1%}")
        print(f"   2025: {data_2025['avg_bounce_rate']:.1%}")
        print(f"   Muutos: {format_change(bounce_change)}")
        print()
        
        print(f"📑 Sivuja per istunto: {get_trend_emoji(pages_per_session_change)}")
        print(f"   2024: {data_2024['avg_pages_per_session']:.2f}")
        print(f"   2025: {data_2025['avg_pages_per_session']:.2f}")
        print(f"   Muutos: {format_change(pages_per_session_change)}")
        print()
        
        print(f"⏱️ Istunnon kesto: {get_trend_emoji(duration_change)}")
        print(f"   2024: {data_2024['avg_session_duration']:.0f}s ({data_2024['avg_session_duration']/60:.1f} min)")
        print(f"   2025: {data_2025['avg_session_duration']:.0f}s ({data_2025['avg_session_duration']/60:.1f} min)")
        print(f"   Muutos: {format_change(duration_change)}")
        print()
        
        # Kuukausikohtaiset huomiot
        print("💡 KUUKAUSIKOHTAISET HUOMIOT:")
        print("-" * 40)
        
        if month_name == "Heinäkuu":
            print("• Kesäsesongin aloitus - perinteisesti vahva kuukausi")
            print("• Vuoden 2025 lasku huolestuttava kesäsesongin alkaessa")
            print("• Suositus: Välittömät toimenpiteet kesämarkkinoinnissa")
        elif month_name == "Elokuu":
            print("• Kesäsesongin huippu - yleensä vuoden paras kuukausi")
            print("• Osittainen data 2025 (14 päivää) - trendi huolestuttava")
            print("• Suositus: Seuranta tarkasti loppukuun ajan")
        
        print()
        
        # Huomautukset
        if data_2025.get('partial'):
            print("⚠️  HUOMAUTUS: Osittainen data 2025")
            print(f"   Dataa saatavilla vain {data_2025['days']} päivältä")
            print("   Vertailu on suuntaa antava")
            print()
        
        print("=" * 80)
        print()

def create_single_year_summaries():
    """Luo yhteenvedot yksittäisistä vuosista"""
    
    data = get_monthly_data()
    
    print("📊 VUOSIKOHTAISET YHTEENVEDOT")
    print("=" * 80)
    print()
    
    # Vuosi 2024 - kaikki kuukaudet
    print("🗓️  VUOSI 2024 - KUUKAUSI KUUKAUDELTA")
    print("-" * 60)
    
    months_2024 = [
        'july_2024', 'august_2024', 'september_2024', 'october_2024', 
        'november_2024', 'december_2024'
    ]
    
    print(f"{'Kuukausi':<12} {'Käyttäjät':<10} {'Istunnot':<10} {'Konversiot':<12} {'Poistumis-%':<12}")
    print("-" * 60)
    
    for month_key in months_2024:
        month_data = data[month_key]
        print(f"{month_data['month_name']:<12} "
              f"{month_data['total_users']:<10,} "
              f"{month_data['total_sessions']:<10,} "
              f"{month_data['total_conversions']:<12,} "
              f"{month_data['avg_bounce_rate']:<12.1%}")
    
    print()
    print("-" * 60)
    
    # Vuosi 2025 - kaikki kuukaudet
    print("🗓️  VUOSI 2025 - KUUKAUSI KUUKAUDELTA")
    print("-" * 60)
    
    months_2025 = [
        'january_2025', 'february_2025', 'march_2025', 'april_2025',
        'may_2025', 'june_2025', 'july_2025', 'august_2025'
    ]
    
    print(f"{'Kuukausi':<12} {'Käyttäjät':<10} {'Istunnot':<10} {'Konversiot':<12} {'Poistumis-%':<12}")
    print("-" * 60)
    
    for month_key in months_2025:
        month_data = data[month_key]
        partial_note = " *" if month_data.get('partial') else ""
        print(f"{month_data['month_name']:<12} "
              f"{month_data['total_users']:<10,} "
              f"{month_data['total_sessions']:<10,} "
              f"{month_data['total_conversions']:<12,} "
              f"{month_data['avg_bounce_rate']:<12.1%}"
              f"{partial_note}")
    
    print()
    print("* = Osittainen data")
    print()

def create_trend_analysis():
    """Luo trendianalyysi"""
    
    data = get_monthly_data()
    
    print("📈 TRENDIANALYYSI")
    print("=" * 80)
    print()
    
    print("🔍 VUODEN 2025 KUUKAUSITTAINEN KEHITYS:")
    print("-" * 50)
    
    months_2025_ordered = [
        'january_2025', 'february_2025', 'march_2025', 'april_2025',
        'may_2025', 'june_2025', 'july_2025'
    ]
    
    prev_users = None
    for month_key in months_2025_ordered:
        month_data = data[month_key]
        if prev_users is not None:
            change = calculate_change_percentage(prev_users, month_data['total_users'])
            emoji = get_trend_emoji(change)
            print(f"{month_data['month_name']}: {month_data['total_users']:,} käyttäjää "
                  f"{emoji} {format_change(change)}")
        else:
            print(f"{month_data['month_name']}: {month_data['total_users']:,} käyttäjää (lähtötaso)")
        
        prev_users = month_data['total_users']
    
    print()

if __name__ == "__main__":
    create_monthly_comparison_report()
    create_single_year_summaries()
    create_trend_analysis()



