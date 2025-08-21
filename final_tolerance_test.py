#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hotel Haven - Lopullinen Toleranssitesti
Lisätään 31.5. data takaisin ja katsotaan lopputulos
"""

def final_tolerance_test():
    """Lopullinen testi ±5% toleranssin saavuttamiseksi"""
    
    print("🎯 LOPULLINEN TOLERANSSITESTI")
    print("=" * 80)
    print()
    
    # GA4:n luvut (koko toukokuu 1.-31.5.)
    ga4_total = 79715.30
    
    # MCP 1.-30.5. data
    mcp_may_1_30 = 91540  # Edellisestä analyysistä
    
    # MCP 31.5. data
    may_31_data = {
        "Referral": 707.00,
        "Paid Search": 560.00,
        "Organic Search": 416.25,
        "Email": 387.00,
        "Direct": 161.00
    }
    may_31_total = sum(may_31_data.values())
    
    # MCP yhteensä (1.-31.5.)
    mcp_complete_may = mcp_may_1_30 + may_31_total
    
    print("📊 TÄYDELLINEN VERTAILU:")
    print("-" * 30)
    print(f"GA4 Room-raportti (1.-31.5.):  €{ga4_total:8,.0f}")
    print(f"MCP 1.-30.5.:                  €{mcp_may_1_30:8,.0f}")
    print(f"MCP 31.5.:                     €{may_31_total:8,.0f}")
    print(f"MCP YHTEENSÄ (1.-31.5.):       €{mcp_complete_may:8,.0f}")
    print()
    
    # Eron laskenta
    final_diff = mcp_complete_may - ga4_total
    final_diff_pct = (final_diff / ga4_total) * 100
    
    print("🔍 LOPULLINEN ERO:")
    print("-" * 25)
    print(f"ERO: {final_diff:+,.0f} ({final_diff_pct:+.1f}%)")
    print()
    
    # Toleranssin tarkistus
    tolerance_5pct = ga4_total * 0.05
    acceptable_min = ga4_total - tolerance_5pct
    acceptable_max = ga4_total + tolerance_5pct
    
    print("🎯 ±5% TOLERANSSI-TARKISTUS:")
    print("-" * 35)
    print(f"Hyväksyttävä väli:    €{acceptable_min:8,.0f} - €{acceptable_max:8,.0f}")
    print(f"MCP tulos:            €{mcp_complete_may:8,.0f}")
    print()
    
    if acceptable_min <= mcp_complete_may <= acceptable_max:
        print("✅ ONNISTUI! MCP on ±5% toleranssin sisällä!")
        status = "HYVÄKSYTTY"
        color = "🟢"
    elif abs(final_diff_pct) <= 10:
        print("⚠️ LÄHELLÄ! Ero alle 10% mutta yli 5%.")
        status = "RAJATAPAUS"
        color = "🟡"
    else:
        print("❌ EPÄONNISTUI! Ero yli 10%.")
        status = "HYLÄTTY"
        color = "🔴"
    
    print()
    print("🚨 LOPULLINEN PÄÄTÖS:")
    print("-" * 25)
    print(f"{color} STATUS: {status}")
    print(f"{color} ERO: {final_diff_pct:+.1f}%")
    print()
    
    if status == "HYVÄKSYTTY":
        print("✅ MCP HYVÄKSYTTY KÄYTTÖÖN!")
        print()
        print("KÄYTTÖOHJEET:")
        print("• Käytä oikeita parametreja:")
        print("  - Dimensio: sessionDefaultChannelGroup")
        print("  - Suodatin: itemCategory = 'Room'") 
        print("  - Mittari: itemRevenue")
        print("• Ero on hyväksyttävissä rajoissa (±5%)")
        print("• Mainitse aina datalähde raporteissa")
        print("• Käytä GA4:ää virallisiin lukuihin")
        print()
        
    elif status == "RAJATAPAUS":
        print("⚠️ MCP RAJATAPAUKSESSA!")
        print()
        print("VAIHTOEHDOT:")
        print("1. HYVÄKSY 10% toleranssi analyysityökalulle")
        print("2. TUTKI vielä GA4:n suodattimia")
        print("3. KÄYTÄ vain GA4:ää")
        print()
        print("SUOSITUS: Hyväksy suurempi toleranssi analyysille,")
        print("mutta käytä aina GA4:ää virallisiin lukuihin.")
        print()
        
    else:
        print("❌ MCP HYLÄTTY!")
        print()
        print("ERO ON LIIAN SUURI LUOTETTAVAAN ANALYYSIIN.")
        print()
        print("LOPULLINEN PÄÄTÖS:")
        print("• ÄLÄ käytä MCP:tä asiakasraportoinnissa")
        print("• ÄLÄ käytä MCP:tä päätöksentekoon")
        print("• KÄYTÄ vain GA4 UI:ta")
        print("• MCP:n data on epäluotettava")
        print()
    
    print("📋 YHTEENVETO DEBUGGAUSPROSESSISTA:")
    print("-" * 45)
    print("1. ✅ Löydettiin oikeat parametrit:")
    print("   sessionDefaultChannelGroup + itemCategory='Room'")
    print("2. ✅ Tunnistettiin aikavyöhyke-ongelma")
    print("3. ✅ Korjattiin kesäkuun datan vuoto")
    print("4. ✅ Testattiin ±5% toleranssi")
    print()
    print(f"LOPPUTULOS: {status} ({final_diff_pct:+.1f}% ero)")
    
    if status != "HYVÄKSYTTY":
        print()
        print("💡 VIIMEINEN MAHDOLLISUUS:")
        print("Tutki GA4:n Account/Property-tason suodattimet.")
        print("Jos GA4:ssä on aktiivisia suodattimia,")
        print("ne selittäisivät jäljellä olevan eron.")

if __name__ == "__main__":
    final_tolerance_test()
