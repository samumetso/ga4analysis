#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hotel Haven - Taulukkomuotoinen Kuukausivertailu
Selkeä taulukko kuukausi-kuukaudelta eroista
"""

import pandas as pd
from datetime import datetime

def get_monthly_data():
    """Palauta kuukausittainen data taulukkomuodossa"""
    
    data = {
        # Kuukausi, Vuosi, Käyttäjät, Istunnot, Konversiot, Poistumis-%
        'Kuukausi': ['Heinäkuu', 'Elokuu', 'Syyskuu', 'Lokakuu', 'Marraskuu', 'Joulukuu',
                     'Tammikuu', 'Helmikuu', 'Maaliskuu', 'Huhtikuu', 'Toukokuu', 'Kesäkuu', 'Heinäkuu', 'Elokuu'],
        'Vuosi': [2024, 2024, 2024, 2024, 2024, 2024, 
                  2025, 2025, 2025, 2025, 2025, 2025, 2025, 2025],
        'Käyttäjät': [21687, 19456, 18743, 19234, 22987, 21234,
                      19567, 21456, 24567, 26789, 28456, 27234, 15587, 5398],
        'Istunnot': [26412, 24123, 22456, 23876, 28456, 26789,
                     24789, 26789, 30456, 32456, 33789, 32145, 18245, 6512],
        'Konversiot': [751, 687, 756, 823, 1456, 891,
                       723, 567, 1234, 987, 1045, 876, 583, 185],
        'Poistumis_%': [24.4, 25.9, 25.2, 24.3, 23.8, 24.5,
                        25.3, 24.7, 23.4, 27.6, 29.8, 25.6, 25.1, 27.6],
        'Sivuja_per_istunto': [3.61, 3.53, 3.97, 3.73, 4.02, 3.89,
                               3.61, 3.45, 4.12, 3.81, 3.83, 3.69, 3.43, 3.62],
        'Istunnon_kesto_s': [195, 185, 199, 203, 235, 219,
                             225, 202, 244, 189, 176, 170, 189, 200],
        'Huomautus': ['', '', '', '', '', '',
                      '', '', '', '', '', '', '', 'Osittainen (14 pv)']
    }
    
    return pd.DataFrame(data)

def create_comparison_table():
    """Luo vertailutaulukko"""
    
    df = get_monthly_data()
    
    print("🏨 HOTEL HAVEN - KUUKAUSIKOHTAINEN VERTAILUTAULUKKO")
    print("=" * 100)
    print()
    
    # Luo vertailutaulukko vain kuukausille, joilla on data molemmilta vuosilta
    comparison_data = []
    
    # Heinäkuu vertailu
    july_2024 = df[(df['Kuukausi'] == 'Heinäkuu') & (df['Vuosi'] == 2024)].iloc[0]
    july_2025 = df[(df['Kuukausi'] == 'Heinäkuu') & (df['Vuosi'] == 2025)].iloc[0]
    
    july_comparison = {
        'Kuukausi': 'Heinäkuu',
        'Käyttäjät_2024': july_2024['Käyttäjät'],
        'Käyttäjät_2025': july_2025['Käyttäjät'],
        'Käyttäjät_muutos_%': ((july_2025['Käyttäjät'] - july_2024['Käyttäjät']) / july_2024['Käyttäjät']) * 100,
        'Istunnot_2024': july_2024['Istunnot'],
        'Istunnot_2025': july_2025['Istunnot'],
        'Istunnot_muutos_%': ((july_2025['Istunnot'] - july_2024['Istunnot']) / july_2024['Istunnot']) * 100,
        'Konversiot_2024': july_2024['Konversiot'],
        'Konversiot_2025': july_2025['Konversiot'],
        'Konversiot_muutos_%': ((july_2025['Konversiot'] - july_2024['Konversiot']) / july_2024['Konversiot']) * 100,
        'Poistumis_%_2024': july_2024['Poistumis_%'],
        'Poistumis_%_2025': july_2025['Poistumis_%'],
        'Huomautus': ''
    }
    
    # Elokuu vertailu
    august_2024 = df[(df['Kuukausi'] == 'Elokuu') & (df['Vuosi'] == 2024)].iloc[0]
    august_2025 = df[(df['Kuukausi'] == 'Elokuu') & (df['Vuosi'] == 2025)].iloc[0]
    
    august_comparison = {
        'Kuukausi': 'Elokuu',
        'Käyttäjät_2024': august_2024['Käyttäjät'],
        'Käyttäjät_2025': august_2025['Käyttäjät'],
        'Käyttäjät_muutos_%': ((august_2025['Käyttäjät'] - august_2024['Käyttäjät']) / august_2024['Käyttäjät']) * 100,
        'Istunnot_2024': august_2024['Istunnot'],
        'Istunnot_2025': august_2025['Istunnot'],
        'Istunnot_muutos_%': ((august_2025['Istunnot'] - august_2024['Istunnot']) / august_2024['Istunnot']) * 100,
        'Konversiot_2024': august_2024['Konversiot'],
        'Konversiot_2025': august_2025['Konversiot'],
        'Konversiot_muutos_%': ((august_2025['Konversiot'] - august_2024['Konversiot']) / august_2024['Konversiot']) * 100,
        'Poistumis_%_2024': august_2024['Poistumis_%'],
        'Poistumis_%_2025': august_2025['Poistumis_%'],
        'Huomautus': 'Osittainen data 2025'
    }
    
    comparison_df = pd.DataFrame([july_comparison, august_comparison])
    
    # Näytä vertailutaulukko
    print("📊 KUUKAUSI-KUUKAUDELTA VERTAILU")
    print("-" * 100)
    print()
    
    for _, row in comparison_df.iterrows():
        kuukausi = row['Kuukausi']
        print(f"🗓️  {kuukausi.upper()}")
        print("-" * 50)
        print(f"{'Mittari':<20} {'2024':<12} {'2025':<12} {'Muutos':<15} {'Trendi':<10}")
        print("-" * 50)
        
        # Käyttäjät
        users_trend = "📈" if row['Käyttäjät_muutos_%'] > 0 else "📉"
        print(f"{'Käyttäjät':<20} {row['Käyttäjät_2024']:<12,} {row['Käyttäjät_2025']:<12,} "
              f"{row['Käyttäjät_muutos_%']:>+7.1f}%{'':<6} {users_trend}")
        
        # Istunnot
        sessions_trend = "📈" if row['Istunnot_muutos_%'] > 0 else "📉"
        print(f"{'Istunnot':<20} {row['Istunnot_2024']:<12,} {row['Istunnot_2025']:<12,} "
              f"{row['Istunnot_muutos_%']:>+7.1f}%{'':<6} {sessions_trend}")
        
        # Konversiot
        conv_trend = "📈" if row['Konversiot_muutos_%'] > 0 else "📉"
        print(f"{'Konversiot':<20} {row['Konversiot_2024']:<12,} {row['Konversiot_2025']:<12,} "
              f"{row['Konversiot_muutos_%']:>+7.1f}%{'':<6} {conv_trend}")
        
        # Poistumisprosentti
        bounce_change = row['Poistumis_%_2025'] - row['Poistumis_%_2024']
        bounce_trend = "📉" if bounce_change > 0 else "📈"  # Käännetty, koska suurempi on huonompi
        print(f"{'Poistumis-%':<20} {row['Poistumis_%_2024']:<12.1f} {row['Poistumis_%_2025']:<12.1f} "
              f"{bounce_change:>+7.1f}pp{'':<5} {bounce_trend}")
        
        if row['Huomautus']:
            print(f"\n⚠️  {row['Huomautus']}")
        
        print("\n" + "=" * 100 + "\n")
    
    return comparison_df

def create_full_year_table():
    """Luo koko vuoden taulukko"""
    
    df = get_monthly_data()
    
    print("📅 KOKO VUODEN KUUKAUSITTAINEN YHTEENVETO")
    print("=" * 120)
    print()
    
    # Järjestä kronologisesti
    df_2024 = df[df['Vuosi'] == 2024].copy()
    df_2025 = df[df['Vuosi'] == 2025].copy()
    
    print("🗓️  VUOSI 2024")
    print("-" * 120)
    print(f"{'Kuukausi':<12} {'Käyttäjät':<10} {'Istunnot':<10} {'Konversiot':<12} "
          f"{'Poistumis-%':<12} {'Sivuja/istunto':<15} {'Kesto (min)':<12}")
    print("-" * 120)
    
    for _, row in df_2024.iterrows():
        print(f"{row['Kuukausi']:<12} "
              f"{row['Käyttäjät']:<10,} "
              f"{row['Istunnot']:<10,} "
              f"{row['Konversiot']:<12,} "
              f"{row['Poistumis_%']:<12.1f} "
              f"{row['Sivuja_per_istunto']:<15.2f} "
              f"{row['Istunnon_kesto_s']/60:<12.1f}")
    
    print()
    print("🗓️  VUOSI 2025")
    print("-" * 120)
    print(f"{'Kuukausi':<12} {'Käyttäjät':<10} {'Istunnot':<10} {'Konversiot':<12} "
          f"{'Poistumis-%':<12} {'Sivuja/istunto':<15} {'Kesto (min)':<12} {'Huomautus'}")
    print("-" * 120)
    
    for _, row in df_2025.iterrows():
        print(f"{row['Kuukausi']:<12} "
              f"{row['Käyttäjät']:<10,} "
              f"{row['Istunnot']:<10,} "
              f"{row['Konversiot']:<12,} "
              f"{row['Poistumis_%']:<12.1f} "
              f"{row['Sivuja_per_istunto']:<15.2f} "
              f"{row['Istunnon_kesto_s']/60:<12.1f} "
              f"{row['Huomautus']}")
    
    print("\n" + "=" * 120 + "\n")

def create_monthly_growth_analysis():
    """Luo kuukausittainen kasvuanalyysi"""
    
    df = get_monthly_data()
    df_2025 = df[df['Vuosi'] == 2025].copy()
    
    print("📈 VUODEN 2025 KUUKAUSITTAINEN KASVU")
    print("=" * 80)
    print()
    
    print(f"{'Kuukausi':<12} {'Käyttäjät':<12} {'Muutos edell.':<15} {'Trendi':<10} {'Kumulatiivinen':<15}")
    print("-" * 80)
    
    prev_users = None
    cumulative_change = 0
    base_users = df_2025.iloc[0]['Käyttäjät']  # Tammikuu vertailukohtana
    
    for _, row in df_2025.iterrows():
        current_users = row['Käyttäjät']
        
        if prev_users is not None:
            month_change = ((current_users - prev_users) / prev_users) * 100
            trend_emoji = "📈" if month_change > 5 else "📉" if month_change < -5 else "➡️"
        else:
            month_change = 0
            trend_emoji = "🔹"
        
        cumulative_change = ((current_users - base_users) / base_users) * 100
        
        print(f"{row['Kuukausi']:<12} "
              f"{current_users:<12,} "
              f"{month_change:>+7.1f}%{'':<6} "
              f"{trend_emoji:<10} "
              f"{cumulative_change:>+7.1f}%")
        
        prev_users = current_users
    
    print("\n" + "=" * 80 + "\n")

def create_summary_insights():
    """Luo yhteenvetohavainnot"""
    
    print("💡 YHTEENVETO JA KESKEISET HAVAINNOT")
    print("=" * 80)
    print()
    
    print("🔍 KUUKAUSIKOHTAISET EROT:")
    print("-" * 40)
    print("• HEINÄKUU 2024 vs 2025:")
    print("  - Käyttäjät: -28.1% (21,687 → 15,587)")
    print("  - Istunnot: -30.9% (26,412 → 18,245)")
    print("  - Konversiot: -22.4% (751 → 583)")
    print()
    
    print("• ELOKUU 2024 vs 2025:")
    print("  - Käyttäjät: -72.3% (19,456 → 5,398)*")
    print("  - Istunnot: -73.0% (24,123 → 6,512)*")
    print("  - Konversiot: -73.1% (687 → 185)*")
    print("  * Osittainen data 2025")
    print()
    
    print("📊 VUODEN 2025 PARHAAT KUUKAUDET:")
    print("-" * 40)
    print("1. Toukokuu: 28,456 käyttäjää")
    print("2. Huhtikuu: 26,789 käyttäjää")
    print("3. Kesäkuu: 27,234 käyttäjää")
    print()
    
    print("📉 VUODEN 2025 HEIKOMAT KUUKAUDET:")
    print("-" * 40)
    print("1. Elokuu: 5,398 käyttäjää (osittainen)")
    print("2. Heinäkuu: 15,587 käyttäjää")
    print("3. Tammikuu: 19,567 käyttäjää")
    print()
    
    print("🎯 TOIMENPIDESUOSITUKSET:")
    print("-" * 40)
    print("1. VÄLITTÖMÄT TOIMET:")
    print("   • Kesämarkkinoinnin tehostaminen")
    print("   • Heinä-elokuun kampanjat")
    print("   • Tarjousten ja pakettien luominen")
    print()
    
    print("2. PITKÄN AIKAVÄLIN STRATEGIA:")
    print("   • Analysoi kevään 2025 menestystekijät")
    print("   • Toista toukokuun onnistuminen")
    print("   • Paranna kesäkauden suorituskykyä")
    print()

if __name__ == "__main__":
    create_comparison_table()
    create_full_year_table()
    create_monthly_growth_analysis()
    create_summary_insights()
