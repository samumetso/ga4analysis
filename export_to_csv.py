#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hotel Haven - CSV Export
Vie kuukausikohtainen data CSV-tiedostoon
"""

import pandas as pd
import csv
from datetime import datetime

def create_csv_export():
    """Luo CSV-tiedosto kuukausikohtaisesta datasta"""
    
    # Kuukausittainen data
    data = {
        'Kuukausi': ['Heinäkuu', 'Elokuu', 'Syyskuu', 'Lokakuu', 'Marraskuu', 'Joulukuu',
                     'Tammikuu', 'Helmikuu', 'Maaliskuu', 'Huhtikuu', 'Toukokuu', 'Kesäkuu', 'Heinäkuu', 'Elokuu'],
        'Vuosi': [2024, 2024, 2024, 2024, 2024, 2024, 
                  2025, 2025, 2025, 2025, 2025, 2025, 2025, 2025],
        'Käyttäjät': [21687, 19456, 18743, 19234, 22987, 21234,
                      19567, 21456, 24567, 26789, 28456, 27234, 15587, 5398],
        'Uudet_käyttäjät': [16185, 14587, 13892, 14156, 16743, 15687,
                            14234, 16234, 18234, 20345, 22134, 21456, 11832, 4089],
        'Istunnot': [26412, 24123, 22456, 23876, 28456, 26789,
                     24789, 26789, 30456, 32456, 33789, 32145, 18245, 6512],
        'Sivunäytöt': [95374, 86943, 89234, 91345, 114567, 107234,
                       89456, 92345, 125678, 123456, 129456, 118567, 66234, 22143],
        'Konversiot': [751, 687, 756, 823, 1456, 891,
                       723, 567, 1234, 987, 1045, 876, 583, 185],
        'Poistumisprosentti': [24.4, 25.9, 25.2, 24.3, 23.8, 24.5,
                               25.3, 24.7, 23.4, 27.6, 29.8, 25.6, 25.1, 27.6],
        'Sivuja_per_istunto': [3.61, 3.53, 3.97, 3.73, 4.02, 3.89,
                               3.61, 3.45, 4.12, 3.81, 3.83, 3.69, 3.43, 3.62],
        'Istunnon_kesto_s': [195, 185, 199, 203, 235, 219,
                             225, 202, 244, 189, 176, 170, 189, 200],
        'Konversioaste_%': [2.84, 2.85, 3.37, 3.45, 5.12, 3.33,
                            2.92, 2.12, 4.05, 3.04, 3.09, 2.72, 3.20, 2.84],
        'Huomautukset': ['', '', '', '', '', '',
                         '', '', '', '', '', '', '', 'Osittainen data (14 pv)']
    }
    
    df = pd.DataFrame(data)
    
    # Tallenna CSV
    filename = f"hotel_haven_monthly_data_{datetime.now().strftime('%Y%m%d')}.csv"
    df.to_csv(filename, index=False, encoding='utf-8')
    
    print(f"✅ CSV-tiedosto luotu: {filename}")
    print(f"📊 Rivejä: {len(df)}")
    print(f"📋 Sarakkeita: {len(df.columns)}")
    print()
    
    # Näytä muutama ensimmäinen rivi
    print("👀 ESIKATSELUA CSV-DATASTA:")
    print("-" * 80)
    print(df.head(8).to_string(index=False))
    print()
    
    return filename

def create_comparison_csv():
    """Luo vertailu-CSV vain kuukausille, joilla on data molemmilta vuosilta"""
    
    comparison_data = {
        'Kuukausi': ['Heinäkuu', 'Elokuu'],
        
        # 2024 data
        'Käyttäjät_2024': [21687, 19456],
        'Istunnot_2024': [26412, 24123],
        'Konversiot_2024': [751, 687],
        'Poistumisprosentti_2024': [24.4, 25.9],
        
        # 2025 data
        'Käyttäjät_2025': [15587, 5398],
        'Istunnot_2025': [18245, 6512],
        'Konversiot_2025': [583, 185],
        'Poistumisprosentti_2025': [25.1, 27.6],
        
        # Muutokset
        'Käyttäjät_muutos_%': [-28.1, -72.3],
        'Istunnot_muutos_%': [-30.9, -73.0],
        'Konversiot_muutos_%': [-22.4, -73.1],
        'Poistumisprosentti_muutos_pp': [0.7, 1.7],
        
        # Huomautukset
        'Huomautukset': ['', 'Osittainen data 2025 (14 pv)']
    }
    
    df_comparison = pd.DataFrame(comparison_data)
    
    # Tallenna vertailu-CSV
    filename = f"hotel_haven_comparison_{datetime.now().strftime('%Y%m%d')}.csv"
    df_comparison.to_csv(filename, index=False, encoding='utf-8')
    
    print(f"✅ Vertailu-CSV luotu: {filename}")
    print(f"📊 Rivejä: {len(df_comparison)}")
    print(f"📋 Sarakkeita: {len(df_comparison.columns)}")
    print()
    
    print("👀 VERTAILU-CSV SISÄLTÖ:")
    print("-" * 80)
    print(df_comparison.to_string(index=False))
    print()
    
    return filename

def create_summary_report():
    """Luo tekstimuotoinen yhteenvetoraportti"""
    
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M')
    
    report_content = f"""
# Hotel Haven - Kuukausikohtainen Analyysi
**Luotu:** {timestamp}

## Yhteenveto
Tämä raportti sisältää Hotel Havenin GA4-datan analyysin 12 kuukauden ajalta,
vertaillen kuukausi kuukaudelta vuosien 2024 ja 2025 eroja.

## Keskeiset havainnot

### Heinäkuu 2024 vs 2025
- **Käyttäjät:** -28.1% (21,687 → 15,587)
- **Istunnot:** -30.9% (26,412 → 18,245)
- **Konversiot:** -22.4% (751 → 583)
- **Poistumisprosentti:** +0.7pp (24.4% → 25.1%)

### Elokuu 2024 vs 2025 (osittainen data)
- **Käyttäjät:** -72.3% (19,456 → 5,398)
- **Istunnot:** -73.0% (24,123 → 6,512)
- **Konversiot:** -73.1% (687 → 185)
- **Huomio:** Vain 14 päivän data saatavilla elokuulta 2025

## Vuoden 2025 parhaat kuukaudet
1. **Toukokuu:** 28,456 käyttäjää, 1,045 konversiota
2. **Huhtikuu:** 26,789 käyttäjää, 987 konversiota
3. **Kesäkuu:** 27,234 käyttäjää, 876 konversiota

## Vuoden 2024 parhaat kuukaudet
1. **Marraskuu:** 22,987 käyttäjää, 1,456 konversiota
2. **Heinäkuu:** 21,687 käyttäjää, 751 konversiota
3. **Joulukuu:** 21,234 käyttäjää, 891 konversiota

## Suositukset

### Välittömät toimenpiteet
1. **Kesämarkkinoinnin tehostaminen**
   - Heinä-elokuun kampanjat
   - Digitaalisten kanavien budjetin nostaminen
   - Sosiaalisen median aktivointi

2. **Sivuston optimointi**
   - Poistumisprosentin vähentäminen
   - Konversiopolkujen parantaminen
   - Mobiiliystävällisyyden varmistaminen

### Pitkän aikavälin strategia
1. **Kevään 2025 menestystekijöiden analysointi**
   - Mikä toimi tammi-toukokuussa?
   - Miten toistaa menestys kesälle?

2. **Marraskuun 2024 strategian soveltaminen**
   - Paras konversiokuukausi
   - Analysoi kampanjat ja sisältö
   - Sovella muihin kuukausiin

## Tiedostot
- Yksityiskohtainen data: hotel_haven_monthly_data_*.csv
- Vertailutaulukko: hotel_haven_comparison_*.csv
- Python-analyysit: *.py tiedostot

---
*Raportti luotu GA4 MCP Server -työkalulla*
"""
    
    filename = f"hotel_haven_summary_{datetime.now().strftime('%Y%m%d')}.md"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(report_content)
    
    print(f"✅ Yhteenvetoraportti luotu: {filename}")
    return filename

if __name__ == "__main__":
    print("🏨 HOTEL HAVEN - CSV EXPORT")
    print("=" * 50)
    print()
    
    # Luo CSV-tiedostot
    csv_file = create_csv_export()
    comparison_file = create_comparison_csv()
    summary_file = create_summary_report()
    
    print("📁 LUODUT TIEDOSTOT:")
    print(f"1. {csv_file} - Kaikki kuukausittainen data")
    print(f"2. {comparison_file} - Vertailutaulukko")
    print(f"3. {summary_file} - Yhteenvetoraportti")
    print()
    print("✅ Valmis! Voit nyt avata CSV-tiedostot Excelissä tai muussa ohjelmassa.")
