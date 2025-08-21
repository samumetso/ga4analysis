#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hotel Haven - Nopea CookiePro Testausdemo
Demonstroi testaustyökalun käyttöä
"""

import sys
from cookiepro_tester import CookieProTester

def run_demo_test():
    """Suorita demo-testaus Hotel Havenille"""
    
    print("🧪 HOTEL HAVEN - COOKIEPRO TESTAUSDEMO")
    print("=" * 60)
    print()
    
    # Käytä Hotel Havenin todennäköistä URL:ää
    website_url = "https://hotelhaven.fi"
    
    print(f"🎯 Testattava sivusto: {website_url}")
    print("📝 Huom: Jos URL on väärä, muokkaa sitä cookiepro_tester.py:ssä")
    print("-" * 60)
    
    # Luo testaustyökalu
    tester = CookieProTester(website_url)
    
    try:
        # Suorita testit
        results = tester.run_full_test()
        
        print("\n" + "=" * 80)
        print("🎯 DEMO VALMIS - SEURAAVAT ASKELEET")
        print("=" * 80)
        print()
        
        print("1. 🌐 SELAINTESTAUS (SUOSITELTU):")
        print("   • Avaa Hotel Havenin sivusto")
        print("   • Avaa Developer Tools (F12)")
        print("   • Kopioi browser_cookiepro_test.js Console:en")
        print("   • Suorita: testCookieProImplementation()")
        print()
        
        print("2. 🔍 MANUAALINEN TARKISTUS:")
        print("   • Testaa sivusto incognito-tilassa")
        print("   • Tarkista näkyykö evästebanneri")
        print("   • Testaa evästehyväksyntä")
        print("   • Seuraa Network-välilehdeltä GA4-pyyntöjä")
        print()
        
        print("3. 📊 GA4 REAL-TIME SEURANTA:")
        print("   • Kirjaudu GA4-tilille")
        print("   • Avaa Real-time reports")
        print("   • Seuraa liikenteen määrää testauksen aikana")
        print()
        
        print("4. 🛠️ TEKNINEN KORJAUS:")
        print("   • Jos Consent Mode puuttuu → Implementoi välittömästi")
        print("   • Jos GA4 latautuu aina → Korjaa CookiePro-asetukset")
        print("   • Jos evästebanneri ei näy → Tarkista geo-asetukset")
        print()
        
        diagnosis = results.get('diagnosis', {})
        if diagnosis:
            print(f"🩺 NOPEA DIAGNOOSI: {diagnosis.get('status', 'Tuntematon')}")
            print(f"💬 {diagnosis.get('message', 'Ei viestiä')}")
        
        return results
        
    except Exception as e:
        print(f"\n❌ VIRHE TESTAUKSESSA: {str(e)}")
        print("\n🔧 RATKAISUVAIHTOEHDOT:")
        print("1. Tarkista internet-yhteys")
        print("2. Varmista että Hotel Havenin URL on oikea")
        print("3. Käytä selainpohjaista testausta (browser_cookiepro_test.js)")
        print("4. Testaa manuaalisesti Developer Tools:lla")
        
        return None

def show_browser_instructions():
    """Näytä selaintestauksen ohjeet"""
    
    print("\n" + "=" * 80)
    print("🌐 SELAINTESTAUKSEN OHJEET")
    print("=" * 80)
    print()
    
    print("1. VALMISTELU:")
    print("   • Avaa Hotel Haven sivusto uudessa incognito-välilehdessä")
    print("   • Avaa Developer Tools (F12 tai Cmd+Option+I)")
    print("   • Mene Console-välilehdelle")
    print()
    
    print("2. LATAA TESTAUSTYÖKALU:")
    print("   • Kopioi browser_cookiepro_test.js sisältö")
    print("   • Liitä se Console:en ja paina Enter")
    print("   • Näet viestin: 'Hotel Haven CookiePro Testaustyökalu ladattu!'")
    print()
    
    print("3. SUORITA TESTAUS:")
    print("   • Kirjoita Console:en: testCookieProImplementation()")
    print("   • Paina Enter")
    print("   • Odota testien valmistumista")
    print()
    
    print("4. ANALYSOI TULOKSET:")
    print("   • Lue testitulosten yhteenveto")
    print("   • Kiinnitä huomiota suosituksiin")
    print("   • Tallenna tulokset myöhempää käyttöä varten")
    print()
    
    print("5. LISÄTESTIT:")
    print("   • checkConsentState('G-XXXXXXXXXX') - Tarkista consent-tilat")
    print("   • simulateConsentAccept() - Simuloi evästehyväksyntä")
    print("   • window.cookieProTestResults - Näe kaikki tulokset")
    print()

def create_action_plan():
    """Luo toimenpidesuunnitelma"""
    
    print("\n" + "=" * 80)
    print("📋 TOIMENPIDESUUNNITELMA - COOKIEPRO ONGELMAN RATKAISU")
    print("=" * 80)
    print()
    
    print("🔥 VÄLITTÖMÄT TOIMET (1-2 tuntia):")
    print("-" * 40)
    print("1. ✅ Suorita selaintestaus (browser_cookiepro_test.js)")
    print("2. ✅ Tarkista löytyykö Consent Mode -koodi")
    print("3. ✅ Testaa evästehyväksyntä incognito-tilassa")
    print("4. ✅ Seuraa GA4 Real-time -dataa testauksen aikana")
    print()
    
    print("⚡ TEKNINEN KORJAUS (1-2 päivää):")
    print("-" * 40)
    print("1. 🛠️ Jos Consent Mode puuttuu:")
    print("   • Implementoi technical_debugging_guide.py:n GTM-koodi")
    print("   • Testaa kaikki consent-skenaariot")
    print("   • Varmista että GA4 ei lataudu ilman hyväksyntää")
    print()
    print("2. 🛠️ Jos CookiePro-asetukset väärin:")
    print("   • Kirjaudu CookiePro-hallintapaneeliin")
    print("   • Siirrä GA4-koodi pois 'Analytics'-kategoriasta")
    print("   • Aseta GA4 latautumaan vain GTM:n kautta")
    print()
    print("3. 🛠️ Jos evästebanneri ei toimi:")
    print("   • Tarkista geo-asetukset (Suomi)")
    print("   • Testaa eri selaimilla")
    print("   • Varmista että banneri näkyy ensikäynnillä")
    print()
    
    print("📊 SEURANTA JA VALIDOINTI (1-2 viikkoa):")
    print("-" * 40)
    print("1. 📈 Päivittäinen GA4-seuranta")
    print("2. 🍪 Evästehyväksyntäasteen seuranta")
    print("3. 📺 Kanavittainen liikenteen palautuminen")
    print("4. 🔄 Toista testaus viikon kuluttua")
    print()
    
    print("🎯 ODOTETTU TULOS:")
    print("20-30% liikenteen palautuminen 1-2 viikossa teknisen korjauksen jälkeen")
    print()

if __name__ == "__main__":
    # Suorita demo
    results = run_demo_test()
    
    # Näytä lisäohjeet
    show_browser_instructions()
    create_action_plan()
    
    print("\n🚀 VALMIS ALOITTAMAAN TESTAUKSEN!")
    print("Aloita selaintestauksella - se antaa tarkkimmat tulokset.")
