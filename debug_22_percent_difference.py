#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hotel Haven - 22% Eron Debuggaus
Systemaattinen lähestyminen MCP vs GA4 erojen selvittämiseen
"""

def debug_systematic_approach():
    """Systemaattinen debuggaussuunnitelma"""
    
    print("🔍 SYSTEMAATTINEN DEBUGGAUS - 22% ERON SELVITYS")
    print("=" * 80)
    print()
    
    print("🚨 ONGELMA:")
    print("-" * 15)
    print("• GA4 Room-raportti: €79,715")
    print("• MCP huoneanalyysi: €97,352") 
    print("• ERO: +€17,637 (+22.1%)")
    print("• KRIITTINEN: Ero liian suuri luotettavaan analyysiin")
    print()
    
    print("🎯 DEBUGGAUSSTRATEGIA:")
    print("-" * 30)
    print()
    
    print("VAIHE 1: ATTRIBUUTIOMALLIN TESTAUS")
    print("🔍 Testaa GA4:n 'Session primary channel group' MCP:llä")
    print("   → sessionDefaultChannelGrouping vai sessionPrimaryChannelGroup?")
    print("   → Vertaa tuloksia GA4:n lukuihin")
    print()
    
    print("VAIHE 2: ITEM CATEGORY SUODATUKSEN TESTAUS") 
    print("🔍 Käytä MCP:ssä itemCategory = 'Room' suodatinta")
    print("   → Sama kuin GA4:n Room-suodatin")
    print("   → Vertaa itemRevenue vs totalRevenue")
    print()
    
    print("VAIHE 3: AIKAVYÖHYKKEEN VALIDOINTI")
    print("🔍 Testaa eri aikavyöhykkeitä")
    print("   → UTC vs Helsinki-aika")
    print("   → Tarkista päivämäärien rajaukset")
    print()
    
    print("VAIHE 4: YKSITTÄISEN PÄIVÄN TESTAUS")
    print("🔍 Ota yksi päivä ja vertaa tarkasti")
    print("   → Esim. 15.5.2025")
    print("   → Sama päivä GA4:ssä ja MCP:ssä")
    print()
    
    print("VAIHE 5: PURCHASE-TAPAHTUMIEN ANALYYSI")
    print("🔍 Tarkista purchase-eventien määrät")
    print("   → Onko MCP:ssä enemmän purchase-tapahtumia?")
    print("   → Duplikaatit tai eri event-tyypit?")
    print()
    
    print("📋 TESTAUSSUUNNITELMA:")
    print("-" * 25)
    print("1. Hae MCP:llä sama data kuin GA4:ssä:")
    print("   • Dimensiot: sessionPrimaryChannelGroup (jos löytyy)")
    print("   • Mittarit: itemRevenue") 
    print("   • Suodatin: itemCategory = 'Room'")
    print("   • Aikaväli: 2025-05-01 - 2025-05-31")
    print()
    
    print("2. Jos ei toimi, kokeile:")
    print("   • sessionDefaultChannelGrouping")
    print("   • defaultChannelGroup + itemCategory-suodatin")
    print("   • purchaseRevenue mittaria")
    print()
    
    print("3. Yksittäisen päivän deep-dive:")
    print("   • Ota 15.5.2025")
    print("   • Hae kaikki Room-ostot")
    print("   • Vertaa GA4:ään päivä-tasolla")
    print()
    
    print("🎯 TAVOITE:")
    print("-" * 15)
    print("Saada MCP:n luvut <5% eroon GA4:stä")
    print("Jos ei onnistu → dokumentoi syy ja käytä GA4:ää")
    print("Jos onnistuu → MCP on luotettava analyysityökalu")
    print()
    
    print("⚠️  KRIITTINEN HUOMIO:")
    print("-" * 25)
    print("Ennen kuin jatkan mitään analyysiä, TÄYTYY ratkaista tämä ero!")
    print("22% heitto tekee kaikista tuloksista epäluotettavia.")
    print("Asiakas ei voi luottaa analyyseihin jos perustiedot eivät täsmää.")

if __name__ == "__main__":
    debug_systematic_approach()
