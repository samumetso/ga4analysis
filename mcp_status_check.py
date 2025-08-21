#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hotel Haven - MCP Status Check
Tarkistetaan MCP:n nykyinen tilanne
"""

import os

def mcp_status_check():
    """Tarkista MCP:n nykyinen tilanne"""
    
    print("🔍 MCP STATUS CHECK")
    print("=" * 80)
    print()
    
    # Tarkista ympäristömuuttuja
    property_id = os.environ.get("GA4_PROPERTY_ID", "EI ASETETTU")
    
    print("🔧 KONFIGURAATIO:")
    print("-" * 20)
    print(f"• GA4_PROPERTY_ID: {property_id}")
    print("• Service Account: ga4analysis@ga4analysis-468917.iam.gserviceaccount.com")
    print()
    
    print("🚨 MCP ONGELMA:")
    print("-" * 20)
    print("• MCP antaa virheen: 'list' object is not callable")
    print("• Ei pysty hakemaan dataa tällä hetkellä")
    print("• Mahdollisia syitä:")
    print("  - Oikeuksien muutos aiheutti ongelman")
    print("  - MCP cache/session ongelma")
    print("  - API kutsujen muoto muuttunut")
    print()
    
    print("📊 MITÄ HALUSIMME TESTATA:")
    print("-" * 35)
    print()
    print("ENNEN (Klaus K oikeudet):")
    print("• Sessions: ~33,000")
    print("• Toscanini.fi referral: 254 sessions")
    print("• Referral yhteensä: 2,242 sessions")
    print()
    print("JÄLKEEN (vain Hotel Haven):")
    print("• Sessions: ? (pitäisi olla vähemmän)")
    print("• Toscanini.fi referral: 0 (pitäisi kadota)")
    print("• Referral yhteensä: ? (pitäisi olla vähemmän)")
    print()
    
    print("🔧 MAHDOLLISET RATKAISUT:")
    print("-" * 30)
    print()
    print("1. 🔄 MCP RESTART")
    print("   • Sammuta MCP prosessi")
    print("   • Käynnistä uudelleen")
    print("   • Testaa uudelleen")
    print()
    print("2. 🧹 CACHE TYHJENNYS")
    print("   • Tyhjennä MCP:n välimuisti")
    print("   • Pakota uusi API yhteys")
    print()
    print("3. 🔑 OIKEUKSIEN TARKISTUS")
    print("   • Varmista että Hotel Haven oikeudet toimivat")
    print("   • Tarkista että Klaus K oikeudet on poistettu")
    print()
    print("4. 📞 YKSINKERTAINEN API TESTI")
    print("   • Kokeile yksinkertaisinta mahdollista kyselyä")
    print("   • Esim. vain sessions yhteensä")
    print()
    
    print("💡 SEURAAVAT ASKELEET:")
    print("-" * 25)
    print()
    print("VÄLITÖN:")
    print("1. Tarkista GA4:stä että Klaus K oikeudet on poistettu")
    print("2. Varmista että Hotel Haven oikeudet on voimassa")
    print("3. Kokeile MCP:n restart jos mahdollista")
    print()
    print("VERTAILU:")
    print("4. Kerro Hotel Havenin GA4 luvut toukokuulta:")
    print("   • Sessions yhteensä")
    print("   • Referral sessions")
    print("   • Top kanavat")
    print()
    print("ANALYYSI:")
    print("5. Vertaa GA4 lukuja aiempiin MCP lukuihin")
    print("6. Laske kuinka paljon Klaus K:n poisto vaikutti")
    print()
    
    print("🎯 ODOTETTU TULOS:")
    print("-" * 25)
    print()
    print("JOS KLAUS K OIKEUDET POISTETTU ONNISTUNEESTI:")
    print("• MCP:n Sessions laskee merkittävästi")
    print("• Toscanini.fi katoaa referraleista")
    print("• MCP:n luvut alkavat täsmätä GA4:n kanssa")
    print("• Saavutamme ±5% toleranssin")
    print()
    
    print("JOS ONGELMA JATKUU:")
    print("• MCP:ssä on tekninen ongelma")
    print("• Tarvitaan syvempi troubleshooting")
    print("• Mahdollisesti MCP:n uudelleenasennus")
    print()
    
    print("📋 TOIMENPIDELISTA:")
    print("-" * 25)
    print()
    print("☐ Tarkista Klaus K oikeuksien poisto GA4:stä")
    print("☐ Varmista Hotel Haven oikeudet")
    print("☐ Kokeile MCP restart")
    print("☐ Testaa MCP:n API yhteys")
    print("☐ Kerro GA4:n Hotel Haven luvut")
    print("☐ Vertaa lukuja ja laske ero")
    print()
    
    print("Kerro mitä näet GA4:ssä nyt kun Klaus K oikeudet on poistettu!")

if __name__ == "__main__":
    mcp_status_check()
