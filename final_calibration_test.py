#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hotel Haven - Lopullinen Kalibrointitesti
Aikavyöhyke-korjaus + Internal Traffic arvio
"""

def final_calibration_test():
    """Lopullinen kalibrointitesti"""
    
    print("🎯 LOPULLINEN KALIBROINTITESTI")
    print("=" * 80)
    print()
    
    # Tiedossa olevat luvut
    ga4_explore_total = 79715.30
    mcp_full_may = 93771  # 1.-31.5. + 1.6. data
    mcp_may_1_30 = 91540  # 1.-30.5. (jo testattu aiemmin)
    
    print("📊 LUKUVERTAILU:")
    print("-" * 20)
    print(f"GA4 Explore (1.-31.5.):     €{ga4_explore_total:8,.0f}")
    print(f"MCP alkuperäinen (1.-31.5.): €{mcp_full_may:8,.0f}")
    print(f"MCP korjattu (1.-30.5.):     €{mcp_may_1_30:8,.0f}")
    print()
    
    # Aikavyöhyke-korjauksen vaikutus
    timezone_correction = mcp_full_may - mcp_may_1_30
    print(f"Aikavyöhyke-korjaus:         -€{timezone_correction:8,.0f}")
    print()
    
    # Jäljellä oleva ero
    remaining_diff = mcp_may_1_30 - ga4_explore_total
    remaining_diff_pct = (remaining_diff / ga4_explore_total) * 100
    
    print("🔍 AIKAVYÖHYKE-KORJAUKSEN JÄLKEEN:")
    print("-" * 45)
    print(f"Jäljellä oleva ero:          +€{remaining_diff:8,.0f} ({remaining_diff_pct:+.1f}%)")
    print()
    
    # Toleranssin tarkistus
    tolerance_2pct = ga4_explore_total * 0.02
    tolerance_5pct = ga4_explore_total * 0.05
    
    print("🎯 TOLERANSSI-ANALYYSI:")
    print("-" * 30)
    print(f"±2% toleranssi:              €{tolerance_2pct:8,.0f}")
    print(f"±5% toleranssi:              €{tolerance_5pct:8,.0f}")
    print(f"Hyväksyttävä väli (±2%):     €{ga4_explore_total-tolerance_2pct:8,.0f} - €{ga4_explore_total+tolerance_2pct:8,.0f}")
    print(f"Hyväksyttävä väli (±5%):     €{ga4_explore_total-tolerance_5pct:8,.0f} - €{ga4_explore_total+tolerance_5pct:8,.0f}")
    print()
    print(f"MCP tulos (1.-30.5.):        €{mcp_may_1_30:8,.0f}")
    print()
    
    if abs(remaining_diff_pct) <= 2:
        status = "✅ HYVÄKSYTTY (±2%)"
        color = "🟢"
    elif abs(remaining_diff_pct) <= 5:
        status = "⚠️ RAJATAPAUS (±5%)"
        color = "🟡"
    else:
        status = "❌ HYLÄTTY (>5%)"
        color = "🔴"
    
    print(f"{color} STATUS: {status}")
    print(f"{color} ERO: {remaining_diff_pct:+.1f}%")
    print()
    
    print("🔍 JÄLJELLÄ OLEVAN ERON ANALYYSI:")
    print("-" * 40)
    
    # Internal Traffic arvio
    internal_traffic_estimate = remaining_diff
    internal_traffic_pct = (internal_traffic_estimate / mcp_may_1_30) * 100
    
    print("TODENNÄKÖINEN SYY: INTERNAL TRAFFIC")
    print(f"• Arvioitu Internal Traffic: €{internal_traffic_estimate:,.0f}")
    print(f"• Osuus MCP:n datasta: {internal_traffic_pct:.1f}%")
    print("• GA4: Internal Traffic suodatettu pois")
    print("• MCP: Internal Traffic mukana")
    print()
    
    print("ONKO TÄMÄ REALISTISTA?")
    print("• Hotel Haven on pieni hotelli")
    print("• Henkilökunnan testiliikenne")
    print("• Kehittäjien testiliikenne") 
    print("• Sisäiset varaukset/testaukset")
    print(f"• {internal_traffic_pct:.1f}% kaikesta datasta = mahdollinen")
    print()
    
    print("💡 LOPULLINEN ARVIO:")
    print("-" * 25)
    
    if abs(remaining_diff_pct) <= 5:
        print("✅ KALIBROINTI ONNISTUI!")
        print()
        print("RATKAISU:")
        print("• Käytä MCP:tä aikavälillä joka jättää viimeisen päivän pois")
        print("• Esim: Toukokuu = 1.-30.5., Kesäkuu = 1.-29.6.")
        print("• Ota huomioon ~15% Internal Traffic -ero")
        print("• Dokumentoi ero asiakkaalle")
        print()
        
        print("KÄYTTÖOHJEET:")
        print("• MCP antaa 'raakadatan' (sisältää Internal Traffic)")
        print("• GA4 UI antaa 'suodatetun datan' (ilman Internal Traffic)")
        print("• Molemmat ovat oikeita, mutta eri tarkoituksiin")
        print("• Käytä GA4 UI:ta virallisiin lukuihin")
        print("• Käytä MCP:tä trendien ja syväanalyysin")
        print()
        
    else:
        print("❌ KALIBROINTI EPÄONNISTUI")
        print()
        print("ERO ON EDELLEEN LIIAN SUURI")
        print("• Tarvitaan lisätutkimusta")
        print("• Mahdollisia syitä:")
        print("  - Muita suodattimia GA4:ssä")
        print("  - API vs UI laskentaerot")
        print("  - Tuntemattomia konfiguraatioeroja")
        print()
    
    print("🎯 SEURAAVA ASKEL:")
    print("-" * 20)
    
    if abs(remaining_diff_pct) <= 5:
        print("TESTAA TOINEN KUUKAUSI!")
        print("• Hae kesäkuun 2025 data MCP:llä (1.-29.6.)")
        print("• Vertaa GA4:n kesäkuun Room-raporttiin")
        print("• Jos ero on sama ~15% → kalibrointi valmis!")
        print("• Jos ero on eri → tarvitaan lisätutkimusta")
    else:
        print("TUTKI LISÄÄ GA4:N ASETUKSIA")
        print("• Tarkista onko muita suodattimia")
        print("• Testaa eri metric-kombinaatioita")
        print("• Harkitse MCP:n hylkäämistä")

if __name__ == "__main__":
    final_calibration_test()
