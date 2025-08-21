#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hotel Haven - CookiePro Toteutuksen Testaustyökalu
Interaktiivinen testaus ongelman löytämiseksi
"""

import requests
import json
import re
from urllib.parse import urlparse, urljoin
import time
from datetime import datetime

class CookieProTester:
    def __init__(self, website_url):
        self.website_url = website_url.rstrip('/')
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        })
        self.test_results = {}
        
    def test_page_load(self):
        """Testaa sivun latautuminen ja perustiedot"""
        print("🌐 TESTAA SIVUN LATAUTUMINEN")
        print("-" * 40)
        
        try:
            response = self.session.get(self.website_url, timeout=10)
            
            print(f"✅ Status Code: {response.status_code}")
            print(f"✅ Response Time: {response.elapsed.total_seconds():.2f}s")
            print(f"✅ Content Length: {len(response.content):,} bytes")
            
            self.test_results['page_load'] = {
                'status': 'success',
                'status_code': response.status_code,
                'response_time': response.elapsed.total_seconds(),
                'content_length': len(response.content)
            }
            
            return response.text
            
        except Exception as e:
            print(f"❌ Virhe sivun latauksessa: {str(e)}")
            self.test_results['page_load'] = {'status': 'error', 'error': str(e)}
            return None
    
    def test_cookiepro_presence(self, html_content):
        """Testaa CookiePron läsnäolo"""
        print("\n🍪 TESTAA COOKIEPRO LÄSNÄOLO")
        print("-" * 40)
        
        # Etsi CookiePro-skriptejä
        cookiepro_patterns = [
            r'cookiepro\.com',
            r'onetrust\.com',
            r'OneTrust',
            r'OptanonWrapper',
            r'otSDKStub',
            r'cookielaw\.org'
        ]
        
        found_patterns = []
        for pattern in cookiepro_patterns:
            matches = re.findall(pattern, html_content, re.IGNORECASE)
            if matches:
                found_patterns.append(pattern)
                print(f"✅ Löytyi: {pattern} ({len(matches)} kpl)")
        
        if found_patterns:
            print(f"✅ CookiePro löytyi! ({len(found_patterns)} indikaattoria)")
            self.test_results['cookiepro_presence'] = {
                'status': 'found',
                'patterns': found_patterns
            }
        else:
            print("❌ CookiePro ei löytynyt!")
            self.test_results['cookiepro_presence'] = {
                'status': 'not_found'
            }
        
        return len(found_patterns) > 0
    
    def test_ga4_presence(self, html_content):
        """Testaa GA4:n läsnäolo"""
        print("\n📊 TESTAA GA4 LÄSNÄOLO")
        print("-" * 40)
        
        # Etsi GA4-skriptejä
        ga4_patterns = [
            r'googletagmanager\.com/gtag/js',
            r'google-analytics\.com',
            r'gtag\(',
            r'G-[A-Z0-9]{10}',  # GA4 Measurement ID
            r'UA-\d+-\d+',      # Universal Analytics ID
            r'dataLayer'
        ]
        
        found_ga4 = []
        for pattern in ga4_patterns:
            matches = re.findall(pattern, html_content, re.IGNORECASE)
            if matches:
                found_ga4.append(pattern)
                print(f"✅ Löytyi: {pattern} ({len(matches)} kpl)")
                if 'G-' in pattern or 'UA-' in pattern:
                    print(f"   IDs: {matches}")
        
        if found_ga4:
            print(f"✅ GA4/Analytics löytyi! ({len(found_ga4)} indikaattoria)")
            self.test_results['ga4_presence'] = {
                'status': 'found',
                'patterns': found_ga4
            }
        else:
            print("❌ GA4/Analytics ei löytynyt!")
            self.test_results['ga4_presence'] = {
                'status': 'not_found'
            }
        
        return len(found_ga4) > 0
    
    def test_gtm_presence(self, html_content):
        """Testaa Google Tag Managerin läsnäolo"""
        print("\n🏷️ TESTAA GOOGLE TAG MANAGER")
        print("-" * 40)
        
        # Etsi GTM-skriptejä
        gtm_patterns = [
            r'googletagmanager\.com/gtm\.js',
            r'GTM-[A-Z0-9]{7}',  # GTM Container ID
            r'dataLayer\.push',
            r'google_tag_manager'
        ]
        
        found_gtm = []
        gtm_ids = []
        
        for pattern in gtm_patterns:
            matches = re.findall(pattern, html_content, re.IGNORECASE)
            if matches:
                found_gtm.append(pattern)
                print(f"✅ Löytyi: {pattern} ({len(matches)} kpl)")
                if 'GTM-' in pattern:
                    gtm_ids.extend(matches)
        
        if gtm_ids:
            print(f"📋 GTM Container IDs: {list(set(gtm_ids))}")
        
        if found_gtm:
            print(f"✅ GTM löytyi! ({len(found_gtm)} indikaattoria)")
            self.test_results['gtm_presence'] = {
                'status': 'found',
                'patterns': found_gtm,
                'container_ids': list(set(gtm_ids))
            }
        else:
            print("❌ GTM ei löytynyt!")
            self.test_results['gtm_presence'] = {
                'status': 'not_found'
            }
        
        return len(found_gtm) > 0
    
    def test_consent_mode(self, html_content):
        """Testaa Consent Mode -toteutus"""
        print("\n🔒 TESTAA CONSENT MODE")
        print("-" * 40)
        
        # Etsi Consent Mode -koodia
        consent_patterns = [
            r'gtag\([\'"]consent[\'"]',
            r'analytics_storage',
            r'ad_storage',
            r'ad_user_data',
            r'ad_personalization',
            r'wait_for_update',
            r'consent.*default',
            r'consent.*update'
        ]
        
        found_consent = []
        for pattern in consent_patterns:
            matches = re.findall(pattern, html_content, re.IGNORECASE)
            if matches:
                found_consent.append(pattern)
                print(f"✅ Löytyi: {pattern} ({len(matches)} kpl)")
        
        # Etsi OptanonWrapper-funktio
        optanon_pattern = r'function OptanonWrapper\(\)'
        optanon_matches = re.findall(optanon_pattern, html_content, re.IGNORECASE)
        if optanon_matches:
            print(f"✅ OptanonWrapper-funktio löytyi ({len(optanon_matches)} kpl)")
            found_consent.append('OptanonWrapper')
        
        if found_consent:
            print(f"✅ Consent Mode löytyi! ({len(found_consent)} indikaattoria)")
            self.test_results['consent_mode'] = {
                'status': 'found',
                'patterns': found_consent
            }
        else:
            print("❌ Consent Mode ei löytynyt!")
            self.test_results['consent_mode'] = {
                'status': 'not_found'
            }
        
        return len(found_consent) > 0
    
    def analyze_loading_order(self, html_content):
        """Analysoi skriptien latausjärjestys"""
        print("\n📋 ANALYSOI SKRIPTIEN LATAUSJÄRJESTYS")
        print("-" * 50)
        
        # Etsi kaikki script-tagit järjestyksessä
        script_pattern = r'<script[^>]*(?:src=[\'"]([^\'"]+)[\'"])?[^>]*>(.*?)</script>'
        scripts = re.findall(script_pattern, html_content, re.DOTALL | re.IGNORECASE)
        
        important_scripts = []
        for i, (src, inline_content) in enumerate(scripts, 1):
            script_type = "inline" if not src else "external"
            
            # Tunnista tärkeät skriptit
            if src:
                if 'cookiepro.com' in src or 'onetrust.com' in src:
                    important_scripts.append(f"{i}. CookiePro ({script_type}): {src}")
                elif 'googletagmanager.com/gtm.js' in src:
                    important_scripts.append(f"{i}. GTM ({script_type}): {src}")
                elif 'googletagmanager.com/gtag/js' in src:
                    important_scripts.append(f"{i}. GA4 ({script_type}): {src}")
            else:
                if 'gtag(' in inline_content and 'consent' in inline_content:
                    important_scripts.append(f"{i}. Consent Mode (inline)")
                elif 'dataLayer' in inline_content:
                    important_scripts.append(f"{i}. DataLayer (inline)")
                elif 'OptanonWrapper' in inline_content:
                    important_scripts.append(f"{i}. OptanonWrapper (inline)")
        
        if important_scripts:
            print("🔍 TÄRKEÄT SKRIPTIT LATAUSJÄRJESTYKSESSÄ:")
            for script in important_scripts:
                print(f"   {script}")
        else:
            print("❌ Ei löytynyt tärkeitä skriptejä!")
        
        self.test_results['loading_order'] = important_scripts
        return important_scripts
    
    def run_full_test(self):
        """Suorita täydellinen testi"""
        print("🧪 HOTEL HAVEN - COOKIEPRO TOTEUTUKSEN TESTI")
        print("=" * 60)
        print(f"Testattava sivusto: {self.website_url}")
        print(f"Testin ajankohta: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 60)
        
        # 1. Lataa sivu
        html_content = self.test_page_load()
        if not html_content:
            return self.test_results
        
        # 2. Testaa komponenttien läsnäolo
        cookiepro_found = self.test_cookiepro_presence(html_content)
        ga4_found = self.test_ga4_presence(html_content)
        gtm_found = self.test_gtm_presence(html_content)
        consent_mode_found = self.test_consent_mode(html_content)
        
        # 3. Analysoi latausjärjestys
        loading_order = self.analyze_loading_order(html_content)
        
        # 4. Yhteenveto ja diagnoosi
        self.create_diagnosis()
        
        return self.test_results
    
    def create_diagnosis(self):
        """Luo diagnoosi testituloksista"""
        print("\n🩺 DIAGNOOSI JA SUOSITUKSET")
        print("=" * 60)
        
        cookiepro_ok = self.test_results.get('cookiepro_presence', {}).get('status') == 'found'
        ga4_ok = self.test_results.get('ga4_presence', {}).get('status') == 'found'
        gtm_ok = self.test_results.get('gtm_presence', {}).get('status') == 'found'
        consent_ok = self.test_results.get('consent_mode', {}).get('status') == 'found'
        
        # Arvioi kokonaistilanne
        total_score = sum([cookiepro_ok, ga4_ok, gtm_ok, consent_ok])
        
        if total_score == 4:
            status = "🟢 HYVÄ"
            message = "Kaikki komponentit löytyvät. Ongelma todennäköisesti asetuksissa."
        elif total_score == 3:
            status = "🟡 KOHTALAINEN"
            message = "Useimmat komponentit löytyvät. Yksi puuttuu tai on väärin."
        elif total_score == 2:
            status = "🟠 HUONO"
            message = "Puolet komponenteista puuttuu. Merkittäviä ongelmia."
        else:
            status = "🔴 KRIITTINEN"
            message = "Useimmat komponentit puuttuvat. Vakava implementointi-ongelma."
        
        print(f"📊 KOKONAISARVIO: {status}")
        print(f"💬 {message}")
        print()
        
        # Yksityiskohtaiset suositukset
        print("🔧 YKSITYISKOHTAISET SUOSITUKSET:")
        print("-" * 40)
        
        if not cookiepro_ok:
            print("❌ CookiePro puuttuu:")
            print("   • Tarkista onko CookiePro-skripti lisätty sivulle")
            print("   • Varmista että domain on oikein konfiguroitu")
            print()
        
        if not consent_ok:
            print("❌ Consent Mode puuttuu:")
            print("   • Implementoi Consent Mode v2")
            print("   • Lisää OptanonWrapper-funktio")
            print("   • Aseta oletusasetukset 'denied'-tilaan")
            print()
        
        if ga4_ok and not consent_ok:
            print("⚠️  GA4 löytyi mutta Consent Mode puuttuu:")
            print("   • TÄMÄ ON TODENNÄKÖINEN ONGELMA!")
            print("   • GA4 latautuu aina, vaikka evästeet hylätään")
            print("   • Implementoi Consent Mode välittömästi")
            print()
        
        if not gtm_ok and ga4_ok:
            print("ℹ️  GA4 suoraan, ei GTM:n kautta:")
            print("   • Harkitse GTM:n käyttöä helpompaa hallintaa varten")
            print("   • GTM tekee Consent Mode -implementoinnista helpompaa")
            print()
        
        # Tallenna diagnoosi
        self.test_results['diagnosis'] = {
            'status': status,
            'score': total_score,
            'message': message,
            'cookiepro_ok': cookiepro_ok,
            'ga4_ok': ga4_ok,
            'gtm_ok': gtm_ok,
            'consent_ok': consent_ok
        }

def create_manual_testing_guide():
    """Luo manuaalinen testausopas"""
    
    print("\n" + "=" * 80)
    print("🧪 MANUAALINEN TESTAUSOPAS - COOKIEPRO & GA4")
    print("=" * 80)
    print()
    
    print("🔍 VAIHE 1: PERUSTARKISTUS SELAIMESSA")
    print("-" * 50)
    print("1. Avaa Hotel Havenin sivusto incognito-tilassa")
    print("2. Avaa Developer Tools (F12)")
    print("3. Mene Console-välilehdelle")
    print("4. Kirjoita ja suorita seuraavat komennot:")
    print()
    print("   // Tarkista CookiePro")
    print("   typeof OneTrust")
    print("   → Pitäisi näyttää 'object' jos CookiePro on ladattu")
    print()
    print("   // Tarkista GA4")
    print("   typeof gtag")
    print("   → Pitäisi näyttää 'function' jos GA4 on ladattu")
    print()
    print("   // Tarkista DataLayer")
    print("   window.dataLayer")
    print("   → Pitäisi näyttää array jos GTM/GA4 on ladattu")
    print()
    
    print("🔍 VAIHE 2: CONSENT-TILOJEN TARKISTUS")
    print("-" * 50)
    print("Kirjoita Consoleen (korvaa GA_MEASUREMENT_ID oikealla ID:llä):")
    print()
    print("   gtag('get', 'GA_MEASUREMENT_ID', 'consent')")
    print()
    print("Odotettu tulos ENNEN evästehyväksyntää:")
    print("   {")
    print("     ad_storage: 'denied',")
    print("     analytics_storage: 'denied',")
    print("     ad_user_data: 'denied',")
    print("     ad_personalization: 'denied'")
    print("   }")
    print()
    
    print("🔍 VAIHE 3: EVÄSTEHYVÄKSYNTÄTESTI")
    print("-" * 50)
    print("1. Hyväksy evästeet sivustolla")
    print("2. Suorita uudelleen consent-komento:")
    print("   gtag('get', 'GA_MEASUREMENT_ID', 'consent')")
    print()
    print("Odotettu tulos JÄLKEEN evästehyväksynnän:")
    print("   {")
    print("     ad_storage: 'granted',")
    print("     analytics_storage: 'granted',")
    print("     ad_user_data: 'granted',")
    print("     ad_personalization: 'granted'")
    print("   }")
    print()
    
    print("🔍 VAIHE 4: NETWORK-LIIKENNE")
    print("-" * 50)
    print("1. Mene Network-välilehdelle")
    print("2. Tyhjennä logi (Clear-painike)")
    print("3. Päivitä sivu (F5)")
    print("4. Etsi seuraavia pyyntöjä:")
    print()
    print("   ENNEN evästehyväksyntää:")
    print("   ❌ EI pitäisi näkyä: google-analytics.com/collect")
    print("   ❌ EI pitäisi näkyä: google-analytics.com/g/collect")
    print("   ✅ Pitäisi näkyä: cookiepro.com tai onetrust.com")
    print()
    print("   JÄLKEEN evästehyväksynnän:")
    print("   ✅ Pitäisi näkyä: google-analytics.com/g/collect")
    print("   ✅ Pitäisi näkyä: googletagmanager.com")
    print()

def run_interactive_test():
    """Suorita interaktiivinen testi"""
    
    print("🧪 HOTEL HAVEN - COOKIEPRO INTERAKTIIVINEN TESTI")
    print("=" * 60)
    print()
    
    # Kysy sivuston URL
    website_url = input("Anna Hotel Havenin sivuston URL (esim. https://hotelhaven.fi): ").strip()
    
    if not website_url:
        website_url = "https://hotelhaven.fi"  # Oletus
        print(f"Käytetään oletussivustoa: {website_url}")
    
    # Luo testaustyökalu
    tester = CookieProTester(website_url)
    
    # Suorita testit
    print(f"\n🚀 Aloitetaan testaus sivustolle: {website_url}")
    print("-" * 60)
    
    results = tester.run_full_test()
    
    # Tallenna tulokset
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    results_file = f"cookiepro_test_results_{timestamp}.json"
    
    with open(results_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    
    print(f"\n💾 Testitulokset tallennettu tiedostoon: {results_file}")
    
    # Näytä manuaalinen testausopas
    create_manual_testing_guide()
    
    return results

if __name__ == "__main__":
    # Suorita interaktiivinen testi
    test_results = run_interactive_test()
    
    print("\n🎯 YHTEENVETO:")
    print("=" * 60)
    
    diagnosis = test_results.get('diagnosis', {})
    print(f"Status: {diagnosis.get('status', 'Tuntematon')}")
    print(f"Viesti: {diagnosis.get('message', 'Ei viestiä')}")
    
    print("\n🔧 SEURAAVAT ASKELEET:")
    print("1. Suorita manuaalinen testaus selaimessa")
    print("2. Tarkista löydetyt ongelmat")
    print("3. Korjaa implementointi")
    print("4. Testaa uudelleen")
    print()
    print("📞 Jos tarvitset apua, lähetä testitulokset GA4-asiantuntijalle!")
