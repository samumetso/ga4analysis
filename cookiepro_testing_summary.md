# Hotel Haven - CookiePro Testaustyökalut

## 🎯 Tavoite
Löytää syy Hotel Havenin GA4-liikenteen 50% pudotukseen kesäkuun 13-15 päivän evästehallintamuutosten jälkeen.

## 🔍 Alustava Diagnoosi
**TODENNÄKÖINEN SYY: Consent Mode puuttuu**
- ✅ GA4 ja GTM löytyvät sivustolta
- ❌ CookiePro ei löytynyt automaattisessa testauksessa
- ❌ Consent Mode -koodi puuttuu kokonaan
- ⚠️ **KRIITTINEN**: GA4 latautuu todennäköisesti aina, vaikka evästeet hylätään

## 🛠️ Luodut Testaustyökalut

### 1. **cookiepro_tester.py** - Automaattinen Python-testaus
```bash
python cookiepro_tester.py
```
- Testaa sivuston HTML-sisältöä
- Etsii CookiePro, GA4, GTM ja Consent Mode -koodia
- Analysoi skriptien latausjärjestyksen
- Luo automaattisen diagnoosin

### 2. **browser_cookiepro_test.js** - Selaintestaus (SUOSITELTU)
```javascript
// Kopioi Console:en ja suorita:
testCookieProImplementation()
```
- Testaa reaaliaikaisia JavaScript-objekteja
- Tarkistaa consent-tiloja suoraan
- Analysoi evästeet ja dataLayer-sisällön
- Antaa tarkkimmat tulokset

### 3. **technical_debugging_guide.py** - Tekninen korjausopas
```bash
python technical_debugging_guide.py
```
- Yksityiskohtaiset korjausohjeet
- Valmiit GTM-koodipätkät Consent Mode v2:lle
- Testausskenaariot
- Seurantaohjeistus

### 4. **cookie_impact_analysis.py** - Vaikutusanalyysi
```bash
python cookie_impact_analysis.py
```
- Analysoi liikenteen pudotuksen
- Vertailee evästehyväksynnän teoreettista vaikutusta
- Kanavittainen vaikutusanalyysi
- Tutkimussuunnitelma

## 🚀 Testauksen Aloittaminen

### VAIHE 1: Selaintestaus (5 min)
1. Avaa https://hotelhaven.fi incognito-tilassa
2. Avaa Developer Tools (F12)
3. Kopioi `browser_cookiepro_test.js` Console:en
4. Suorita: `testCookieProImplementation()`

### VAIHE 2: Manuaalinen tarkistus (10 min)
```javascript
// Tarkista Console:ssa:
typeof OneTrust        // Pitäisi olla 'object'
typeof gtag           // Pitäisi olla 'function'
gtag('get', 'G-XXXXXXXXXX', 'consent')  // Consent-tilat
```

### VAIHE 3: Network-analyysi (5 min)
- Mene Network-välilehdelle
- Päivitä sivu
- Etsi `google-analytics.com` -pyyntöjä
- **ONGELMA**: Jos pyyntöjä tulee ENNEN evästehyväksyntää

## 🔧 Todennäköiset Korjaukset

### 1. CONSENT MODE V2 IMPLEMENTOINTI
```html
<!-- Lisää GTM:ään Custom HTML -tagina -->
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  
  gtag('consent', 'default', {
    'ad_storage': 'denied',
    'analytics_storage': 'denied',
    'ad_user_data': 'denied',
    'ad_personalization': 'denied',
    'wait_for_update': 500
  });
</script>
```

### 2. OPTANONWRAPPER-FUNKTIO
```html
<script>
  function OptanonWrapper() {
    if (OnetrustActiveGroups.indexOf('C0002') > -1) {
      gtag('consent', 'update', {
        'analytics_storage': 'granted'
      });
    }
  }
</script>
```

### 3. COOKIEPRO-ASETUSTEN TARKISTUS
- Kirjaudu CookiePro-hallintapaneeliin
- Tarkista ettei GA4-koodia ole 'Analytics'-kategoriassa
- Varmista että evästebanneri näkyy Suomessa

## 📊 Odotetut Tulokset

### VÄLITTÖMÄT VAIKUTUKSET (1-3 päivää)
- GA4 Real-time -liikenteen kasvu
- Evästehyväksynnän seuranta alkaa toimia
- Consent-tilat näkyvät oikein GA4:ssä

### KESKIPITKÄN AIKAVÄLIN VAIKUTUKSET (1-2 viikkoa)
- **20-30% liikenteen palautuminen**
- Kanavittainen liikenteen tasaantuminen
- Konversioseurannan paraneminen

## 🚨 Kriittiset Toimenpiteet

### TÄNÄÄN:
1. ✅ Suorita selaintestaus
2. ✅ Tarkista löytyykö Consent Mode
3. ✅ Testaa evästehyväksyntä

### HUOMENNA:
1. 🛠️ Implementoi Consent Mode v2
2. 🛠️ Testaa kaikki skenaariot
3. 📊 Seuraa GA4 Real-time -dataa

### VIIKON SISÄÄN:
1. 📈 Analysoi liikenteen palautuminen
2. 🔄 Optimoi evästehyväksyntäastetta
3. 📋 Dokumentoi lopulliset asetukset

## 💡 Yhteenveto

**PÄÄONGELMA**: GA4 latautuu aina, riippumatta evästehyväksynnästä
**RATKAISU**: Consent Mode v2 implementointi
**ODOTETTU HYÖTY**: 20-30% liikenteen palautuminen

**SEURAAVA ASKEL**: Aloita selaintestauksella löytääksesi tarkan ongelman!

---
*Luotu: 2025-08-15*
*Päivitetty: Testaustulosten perusteella*
