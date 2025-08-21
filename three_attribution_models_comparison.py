#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hotel Haven - Kolmen Attribuutiomallin Vertailu
First User Medium vs Session Medium vs Default Channel Group
"""

def compare_three_attribution_models():
    """Vertailee kolmea eri attribuutiomallia"""
    
    print("🔍 KOLMEN ATTRIBUUTIOMALLIN VERTAILU - HOTEL HAVEN TOUKOKUU 2025")
    print("=" * 85)
    print()
    
    print("📊 GA4 RAPORTTI - SESSION MEDIUM (uusin):")
    print("-" * 50)
    print("1. Organic               €30,864.85  (38.72%)")
    print("2. CPC                   €24,107.15  (30.24%)")
    print("3. Referral              €13,759.80  (17.26%)")
    print("4. Direct (none)         €8,436.00   (10.58%)")
    print("5. Email                 €1,101.00   (1.38%)")
    print("6. Business_Advantage    €730.00     (0.92%)")
    print("7. MapResults            €716.50     (0.90%)")
    print()
    print("YHTEENSÄ GA4 (Session):  €79,715.30")
    print()
    
    print("📊 MCP ANALYYSI - SESSION MEDIUM:")
    print("-" * 40)
    print("1. Organic               €35,711.65  (35.6%)")
    print("2. CPC                   €35,529.36  (35.4%)")
    print("3. Direct (none)         €16,326.02  (16.3%)")
    print("4. Referral              €10,572.88  (10.5%)")
    print("5. Email                 €1,668.91   (1.7%)")
    print("6. FBL                   €470.00     (0.5%)")
    print("7. Mobile                €231.00     (0.2%)")
    print("8. (not set)             €100.00     (0.1%)")
    print()
    print("YHTEENSÄ MCP (Session):  €100,609.82")
    print()
    
    print("🔄 VERTAILU AIEMPIIN MALLEIHIN:")
    print("-" * 45)
    print()
    
    # Aiemmat tulokset
    print("FIRST USER MEDIUM (MCP):")
    print("1. Organic: €36,614  2. CPC: €30,810  3. Direct: €20,868")
    print()
    
    print("DEFAULT CHANNEL GROUP (MCP - alkuperäinen):")
    print("1. Paid Search: €32,942  2. Organic: €32,748  3. Referral: €17,364")
    print()
    
    print("🎯 ATTRIBUUTIOMALLIEN SELITYKSET:")
    print("-" * 50)
    print()
    
    print("1. 🥇 FIRST USER MEDIUM")
    print("   • Mitä kanavaa käyttäjä käytti ENSIMMÄISTÄ kertaa")
    print("   • 'Löytökanava' - mistä asiakas tuli alun perin")
    print("   • Hyvä bränditietoisuuden mittaamiseen")
    print("   • Esim: Löytää Googlesta, palaa suoraan → 'organic'")
    print()
    
    print("2. 🎯 SESSION MEDIUM")
    print("   • Mitä kanavaa käytettiin TÄSSÄ ISTUNNOSSA")
    print("   • Välittömän session lähde")
    print("   • Paras konversion optimointiin")
    print("   • Esim: Tänään tuli Googlesta → 'organic'")
    print()
    
    print("3. 🏁 DEFAULT CHANNEL GROUP")
    print("   • Yleinen kanavaluokittelu")
    print("   • Yhdistää source + medium automaattisesti")
    print("   • Helpoin vertailuun")
    print("   • Esim: 'google/cpc' → 'Paid Search'")
    print()
    
    print("📈 MIKSI SESSION MEDIUM MUUTTAA ANALYYSIANI:")
    print("-" * 60)
    print()
    
    print("✅ PAREMPI TARKKUUS:")
    print("• Session Medium on lähempänä GA4-raporttia")
    print("• Ero: €100,610 vs €79,715 = €20,895 (vs aiempi €20,895)")
    print("• Sama kokonaisero, mutta eri jakautuminen!")
    print()
    
    print("🔄 KANAVIEN JÄRJESTYS MUUTTUI:")
    print("• ORGANIC: Säilyi #1 (mutta pienempi ero CPC:hen)")
    print("• CPC: Nousi lähemmäs organicia")
    print("• REFERRAL: Putosi selvästi")
    print("• DIRECT: Säilyi vakaana")
    print()
    
    print("💡 KRIITTINEN HAVAINTO:")
    print("• Session Medium = PARAS konversion optimointiin")
    print("• Se kertoo mistä käyttäjä tuli juuri ennen ostoa")
    print("• Tämä on tärkein tieto markkinoinnin optimoinnille!")
    print()
    
    print("🎯 PÄIVITETTY ANALYYSI:")
    print("-" * 30)
    print("• ORGANIC ja CPC ovat lähes TASOISSA session-tasolla")
    print("• Molemmat yhtä tärkeitä välittömälle konversiolle")
    print("• Referral vähemmän 'viimeisen hetken' kanava")
    print("• Session Medium antaa realistisimman kuvan")
    print()
    
    print("✅ UUDET SUOSITUKSET:")
    print("-" * 25)
    print("1. Optimoi SEKÄ organic että CPC yhtä paljon")
    print("2. Session Medium = paras konversion mittari")
    print("3. First User = paras bränditietoisuuden mittari")
    print("4. Käytä Session Medium päätöksenteossa")
    print("5. Seuraa kaikkia kolmea eri tarkoituksiin")

if __name__ == "__main__":
    compare_three_attribution_models()
