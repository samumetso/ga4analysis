/**
 * Hotel Haven - CookiePro Selaintestaus
 * Suorita tämä koodi suoraan sivuston Console:ssa (F12)
 */

// Testaustyökalun pääfunktio
function testCookieProImplementation() {
    console.clear();
    console.log('🧪 HOTEL HAVEN - COOKIEPRO TOTEUTUKSEN TESTAUS');
    console.log('='.repeat(60));
    console.log('Suoritetaan automaattinen testaus...\n');
    
    const results = {
        timestamp: new Date().toISOString(),
        tests: {},
        summary: {},
        recommendations: []
    };
    
    // Suorita testit
    results.tests.cookiepro = testCookieProPresence();
    results.tests.ga4 = testGA4Presence();
    results.tests.gtm = testGTMPresence();
    results.tests.consent = testConsentMode();
    results.tests.dataLayer = testDataLayer();
    results.tests.cookies = testCurrentCookies();
    
    // Luo yhteenveto
    results.summary = createSummary(results.tests);
    results.recommendations = createRecommendations(results.tests);
    
    // Näytä tulokset
    displayResults(results);
    
    // Tallenna globaalisti debuggausta varten
    window.cookieProTestResults = results;
    
    return results;
}

// Testaa CookiePron läsnäolo
function testCookieProPresence() {
    console.log('🍪 TESTAA COOKIEPRO LÄSNÄOLO');
    console.log('-'.repeat(40));
    
    const test = {
        name: 'CookiePro Presence',
        status: 'unknown',
        details: {},
        issues: []
    };
    
    // Tarkista OneTrust-objekti
    if (typeof OneTrust !== 'undefined') {
        console.log('✅ OneTrust-objekti löytyi');
        test.details.oneTrust = true;
        test.details.onetrustVersion = OneTrust.version || 'Tuntematon';
    } else {
        console.log('❌ OneTrust-objekti ei löytynyt');
        test.details.oneTrust = false;
        test.issues.push('OneTrust-objekti puuttuu');
    }
    
    // Tarkista Optanon-funktiot
    if (typeof OptanonWrapper === 'function') {
        console.log('✅ OptanonWrapper-funktio löytyi');
        test.details.optanonWrapper = true;
    } else {
        console.log('❌ OptanonWrapper-funktio ei löytynyt');
        test.details.optanonWrapper = false;
        test.issues.push('OptanonWrapper-funktio puuttuu');
    }
    
    // Tarkista evästebanneri
    const banner = document.getElementById('onetrust-consent-sdk') || 
                  document.querySelector('[id*="onetrust"]') ||
                  document.querySelector('[class*="onetrust"]');
    
    if (banner) {
        console.log('✅ Evästebanneri-elementti löytyi');
        test.details.banner = true;
        test.details.bannerVisible = banner.style.display !== 'none';
    } else {
        console.log('❌ Evästebanneri-elementti ei löytynyt');
        test.details.banner = false;
        test.issues.push('Evästebanneri-elementti puuttuu');
    }
    
    // Tarkista OnetrustActiveGroups
    if (typeof OnetrustActiveGroups !== 'undefined') {
        console.log('✅ OnetrustActiveGroups löytyi:', OnetrustActiveGroups);
        test.details.activeGroups = OnetrustActiveGroups;
    } else {
        console.log('❌ OnetrustActiveGroups ei löytynyt');
        test.details.activeGroups = null;
        test.issues.push('OnetrustActiveGroups puuttuu');
    }
    
    // Määritä kokonaisstatus
    if (test.issues.length === 0) {
        test.status = 'success';
    } else if (test.details.oneTrust) {
        test.status = 'partial';
    } else {
        test.status = 'failed';
    }
    
    console.log('');
    return test;
}

// Testaa GA4:n läsnäolo
function testGA4Presence() {
    console.log('📊 TESTAA GA4 LÄSNÄOLO');
    console.log('-'.repeat(40));
    
    const test = {
        name: 'GA4 Presence',
        status: 'unknown',
        details: {},
        issues: []
    };
    
    // Tarkista gtag-funktio
    if (typeof gtag === 'function') {
        console.log('✅ gtag-funktio löytyi');
        test.details.gtag = true;
    } else {
        console.log('❌ gtag-funktio ei löytynyt');
        test.details.gtag = false;
        test.issues.push('gtag-funktio puuttuu');
    }
    
    // Etsi GA4 Measurement ID:t
    const ga4Pattern = /G-[A-Z0-9]{10}/g;
    const htmlContent = document.documentElement.outerHTML;
    const ga4Ids = htmlContent.match(ga4Pattern) || [];
    
    if (ga4Ids.length > 0) {
        console.log('✅ GA4 Measurement ID löytyi:', [...new Set(ga4Ids)]);
        test.details.measurementIds = [...new Set(ga4Ids)];
    } else {
        console.log('❌ GA4 Measurement ID ei löytynyt');
        test.details.measurementIds = [];
        test.issues.push('GA4 Measurement ID puuttuu');
    }
    
    // Tarkista GA4-skriptit
    const ga4Scripts = Array.from(document.scripts).filter(script => 
        script.src && script.src.includes('googletagmanager.com/gtag/js')
    );
    
    if (ga4Scripts.length > 0) {
        console.log('✅ GA4-skripti löytyi');
        test.details.scripts = ga4Scripts.map(s => s.src);
    } else {
        console.log('❌ GA4-skripti ei löytynyt');
        test.details.scripts = [];
        test.issues.push('GA4-skripti puuttuu');
    }
    
    // Määritä status
    test.status = test.issues.length === 0 ? 'success' : 
                 test.details.gtag ? 'partial' : 'failed';
    
    console.log('');
    return test;
}

// Testaa GTM:n läsnäolo
function testGTMPresence() {
    console.log('🏷️ TESTAA GOOGLE TAG MANAGER');
    console.log('-'.repeat(40));
    
    const test = {
        name: 'GTM Presence',
        status: 'unknown',
        details: {},
        issues: []
    };
    
    // Tarkista google_tag_manager
    if (typeof google_tag_manager !== 'undefined') {
        console.log('✅ google_tag_manager löytyi');
        test.details.gtm = true;
    } else {
        console.log('❌ google_tag_manager ei löytynyt');
        test.details.gtm = false;
        test.issues.push('GTM ei ole ladattu');
    }
    
    // Etsi GTM Container ID:t
    const gtmPattern = /GTM-[A-Z0-9]{7}/g;
    const htmlContent = document.documentElement.outerHTML;
    const gtmIds = htmlContent.match(gtmPattern) || [];
    
    if (gtmIds.length > 0) {
        console.log('✅ GTM Container ID löytyi:', [...new Set(gtmIds)]);
        test.details.containerIds = [...new Set(gtmIds)];
    } else {
        console.log('❌ GTM Container ID ei löytynyt');
        test.details.containerIds = [];
        test.issues.push('GTM Container ID puuttuu');
    }
    
    // Määritä status
    test.status = test.issues.length === 0 ? 'success' : 
                 test.details.gtm || gtmIds.length > 0 ? 'partial' : 'failed';
    
    console.log('');
    return test;
}

// Testaa Consent Mode
function testConsentMode() {
    console.log('🔒 TESTAA CONSENT MODE');
    console.log('-'.repeat(40));
    
    const test = {
        name: 'Consent Mode',
        status: 'unknown',
        details: {},
        issues: []
    };
    
    // Tarkista gtag ja consent-komennot
    if (typeof gtag === 'function') {
        try {
            // Yritä hakea consent-tiloja (toimii vain jos GA4 on oikein konfiguroitu)
            const measurementIds = test.details.measurementIds || 
                                 (window.cookieProTestResults?.tests?.ga4?.details?.measurementIds) || 
                                 [];
            
            if (measurementIds.length > 0) {
                // Käytä ensimmäistä löydettyä ID:tä
                const consentState = gtag('get', measurementIds[0], 'consent');
                console.log('✅ Consent-tilat haettu:', consentState);
                test.details.consentState = consentState;
                
                // Tarkista ovatko consent-tilat järkeviä
                if (consentState && typeof consentState === 'object') {
                    const hasAnalyticsStorage = 'analytics_storage' in consentState;
                    const hasAdStorage = 'ad_storage' in consentState;
                    
                    if (hasAnalyticsStorage && hasAdStorage) {
                        console.log('✅ Consent Mode on konfiguroitu oikein');
                        test.details.properlyConfigured = true;
                    } else {
                        console.log('⚠️ Consent Mode puutteellisesti konfiguroitu');
                        test.details.properlyConfigured = false;
                        test.issues.push('Consent Mode puutteellisesti konfiguroitu');
                    }
                } else {
                    console.log('❌ Consent-tiloja ei voitu hakea');
                    test.details.properlyConfigured = false;
                    test.issues.push('Consent-tiloja ei voitu hakea');
                }
            } else {
                console.log('❌ Ei GA4 Measurement ID:tä consent-testausta varten');
                test.issues.push('Ei GA4 Measurement ID:tä');
            }
        } catch (error) {
            console.log('❌ Virhe consent-tilojen haussa:', error.message);
            test.details.error = error.message;
            test.issues.push('Virhe consent-tilojen haussa');
        }
    } else {
        console.log('❌ gtag-funktio ei ole saatavilla');
        test.issues.push('gtag-funktio puuttuu');
    }
    
    // Tarkista onko consent-koodia HTML:ssä
    const htmlContent = document.documentElement.outerHTML;
    const hasConsentCode = /gtag\s*\(\s*['""]consent['""]/.test(htmlContent);
    
    if (hasConsentCode) {
        console.log('✅ Consent-koodi löytyi HTML:stä');
        test.details.consentCodeInHTML = true;
    } else {
        console.log('❌ Consent-koodia ei löytynyt HTML:stä');
        test.details.consentCodeInHTML = false;
        test.issues.push('Consent-koodi puuttuu HTML:stä');
    }
    
    // Määritä status
    test.status = test.issues.length === 0 ? 'success' : 
                 test.details.consentCodeInHTML ? 'partial' : 'failed';
    
    console.log('');
    return test;
}

// Testaa DataLayer
function testDataLayer() {
    console.log('📋 TESTAA DATALAYER');
    console.log('-'.repeat(40));
    
    const test = {
        name: 'DataLayer',
        status: 'unknown',
        details: {},
        issues: []
    };
    
    // Tarkista dataLayer
    if (typeof window.dataLayer !== 'undefined' && Array.isArray(window.dataLayer)) {
        console.log('✅ dataLayer löytyi, sisältää', window.dataLayer.length, 'tapahtumaa');
        test.details.exists = true;
        test.details.eventCount = window.dataLayer.length;
        
        // Analysoi dataLayer-sisältö
        const events = window.dataLayer.filter(item => item.event);
        const consentEvents = events.filter(item => 
            item.event && item.event.includes('consent')
        );
        
        console.log('   - Tapahtumia yhteensä:', events.length);
        console.log('   - Consent-tapahtumia:', consentEvents.length);
        
        test.details.totalEvents = events.length;
        test.details.consentEvents = consentEvents.length;
        
        if (consentEvents.length > 0) {
            console.log('✅ Consent-tapahtumia löytyi dataLayerista');
        } else {
            console.log('⚠️ Consent-tapahtumia ei löytynyt dataLayerista');
            test.issues.push('Consent-tapahtumia ei löytynyt dataLayerista');
        }
    } else {
        console.log('❌ dataLayer ei löytynyt tai ei ole array');
        test.details.exists = false;
        test.issues.push('dataLayer puuttuu');
    }
    
    // Määritä status
    test.status = test.issues.length === 0 ? 'success' : 
                 test.details.exists ? 'partial' : 'failed';
    
    console.log('');
    return test;
}

// Testaa nykyiset evästeet
function testCurrentCookies() {
    console.log('🍪 TESTAA NYKYISET EVÄSTEET');
    console.log('-'.repeat(40));
    
    const test = {
        name: 'Current Cookies',
        status: 'unknown',
        details: {},
        issues: []
    };
    
    const cookies = document.cookie.split(';').map(c => c.trim()).filter(c => c);
    console.log('Evästeitä yhteensä:', cookies.length);
    
    // Etsi tärkeitä evästeitä
    const importantCookies = {
        ga: cookies.filter(c => c.startsWith('_ga')),
        gid: cookies.filter(c => c.startsWith('_gid')),
        optanon: cookies.filter(c => c.includes('OptanonConsent') || c.includes('OptanonAlertBoxClosed')),
        other: cookies.filter(c => 
            !c.startsWith('_ga') && 
            !c.startsWith('_gid') && 
            !c.includes('Optanon')
        )
    };
    
    console.log('   - GA evästeet:', importantCookies.ga.length);
    console.log('   - Optanon evästeet:', importantCookies.optanon.length);
    console.log('   - Muut evästeet:', importantCookies.other.length);
    
    if (importantCookies.ga.length > 0) {
        console.log('✅ Google Analytics evästeet löytyi');
        console.log('     ', importantCookies.ga.map(c => c.split('=')[0]).join(', '));
    } else {
        console.log('❌ Google Analytics evästeitä ei löytynyt');
        test.issues.push('GA evästeet puuttuvat');
    }
    
    if (importantCookies.optanon.length > 0) {
        console.log('✅ Optanon evästeet löytyi');
        console.log('     ', importantCookies.optanon.map(c => c.split('=')[0]).join(', '));
    } else {
        console.log('❌ Optanon evästeitä ei löytynyt');
        test.issues.push('Optanon evästeet puuttuvat');
    }
    
    test.details.totalCookies = cookies.length;
    test.details.gaCookies = importantCookies.ga.length;
    test.details.optanonCookies = importantCookies.optanon.length;
    test.details.otherCookies = importantCookies.other.length;
    
    // Määritä status
    test.status = test.issues.length === 0 ? 'success' : 
                 importantCookies.optanon.length > 0 ? 'partial' : 'failed';
    
    console.log('');
    return test;
}

// Luo yhteenveto testeistä
function createSummary(tests) {
    const summary = {
        totalTests: Object.keys(tests).length,
        passed: 0,
        partial: 0,
        failed: 0,
        overallStatus: 'unknown'
    };
    
    Object.values(tests).forEach(test => {
        if (test.status === 'success') summary.passed++;
        else if (test.status === 'partial') summary.partial++;
        else if (test.status === 'failed') summary.failed++;
    });
    
    // Määritä kokonaisstatus
    if (summary.failed === 0 && summary.partial === 0) {
        summary.overallStatus = 'excellent';
    } else if (summary.passed >= summary.failed) {
        summary.overallStatus = 'good';
    } else if (summary.partial > 0) {
        summary.overallStatus = 'needs_work';
    } else {
        summary.overallStatus = 'critical';
    }
    
    return summary;
}

// Luo suositukset
function createRecommendations(tests) {
    const recommendations = [];
    
    // CookiePro-suositukset
    if (tests.cookiepro.status === 'failed') {
        recommendations.push({
            priority: 'critical',
            title: 'CookiePro puuttuu kokonaan',
            description: 'Asenna ja konfiguroi CookiePro',
            action: 'Lisää CookiePro-skripti sivustolle'
        });
    } else if (tests.cookiepro.status === 'partial') {
        recommendations.push({
            priority: 'high',
            title: 'CookiePro osittain konfiguroitu',
            description: 'Tarkista CookiePro-asetukset',
            action: 'Korjaa puuttuvat CookiePro-komponentit'
        });
    }
    
    // Consent Mode -suositukset
    if (tests.consent.status === 'failed') {
        recommendations.push({
            priority: 'critical',
            title: 'Consent Mode puuttuu',
            description: 'Tämä on todennäköisesti pääongelma!',
            action: 'Implementoi Consent Mode v2 välittömästi'
        });
    }
    
    // GA4-suositukset
    if (tests.ga4.status === 'failed') {
        recommendations.push({
            priority: 'high',
            title: 'GA4 ei ole konfiguroitu',
            description: 'Google Analytics 4 puuttuu',
            action: 'Asenna ja konfiguroi GA4'
        });
    }
    
    // Evästeet
    if (tests.cookies.details.gaCookies === 0 && tests.cookies.details.optanonCookies > 0) {
        recommendations.push({
            priority: 'high',
            title: 'GA evästeet puuttuvat vaikka Optanon on käytössä',
            description: 'Evästeet on hylätty tai Consent Mode ei toimi',
            action: 'Tarkista Consent Mode -implementointi'
        });
    }
    
    return recommendations;
}

// Näytä tulokset
function displayResults(results) {
    console.log('🎯 TESTITULOSTEN YHTEENVETO');
    console.log('='.repeat(60));
    
    const summary = results.summary;
    console.log(`Testejä yhteensä: ${summary.totalTests}`);
    console.log(`✅ Onnistui: ${summary.passed}`);
    console.log(`⚠️ Osittain: ${summary.partial}`);
    console.log(`❌ Epäonnistui: ${summary.failed}`);
    
    // Kokonaisarvio
    const statusEmojis = {
        excellent: '🟢 ERINOMAINEN',
        good: '🟡 HYVÄ',
        needs_work: '🟠 TARVITSEE TYÖTÄ',
        critical: '🔴 KRIITTINEN'
    };
    
    console.log(`\n📊 KOKONAISARVIO: ${statusEmojis[summary.overallStatus]}`);
    
    // Suositukset
    if (results.recommendations.length > 0) {
        console.log('\n🔧 SUOSITUKSET:');
        console.log('-'.repeat(40));
        
        results.recommendations.forEach((rec, index) => {
            const priorityEmoji = {
                critical: '🚨',
                high: '⚠️',
                medium: 'ℹ️',
                low: '💡'
            };
            
            console.log(`${index + 1}. ${priorityEmoji[rec.priority]} ${rec.title}`);
            console.log(`   ${rec.description}`);
            console.log(`   Toimenpide: ${rec.action}\n`);
        });
    }
    
    // Debuggausohje
    console.log('🔍 DEBUGGAUS:');
    console.log('-'.repeat(40));
    console.log('Testitulokset on tallennettu muuttujaan: window.cookieProTestResults');
    console.log('Voit tutkia yksityiskohtaisia tuloksia kirjoittamalla:');
    console.log('  window.cookieProTestResults.tests.consent.details');
    console.log('  window.cookieProTestResults.tests.cookiepro.issues');
    console.log('');
}

// Apufunktioita manuaaliseen testaukseen
function checkConsentState(measurementId) {
    if (typeof gtag === 'function' && measurementId) {
        return gtag('get', measurementId, 'consent');
    }
    console.log('gtag-funktio tai measurementId puuttuu');
    return null;
}

function simulateConsentAccept() {
    console.log('🧪 Simuloidaan evästehyväksyntä...');
    if (typeof gtag === 'function') {
        gtag('consent', 'update', {
            'analytics_storage': 'granted',
            'ad_storage': 'granted',
            'ad_user_data': 'granted',
            'ad_personalization': 'granted'
        });
        console.log('✅ Consent-tilat päivitetty "granted"-tilaan');
    } else {
        console.log('❌ gtag-funktio ei ole saatavilla');
    }
}

// Käynnistä testaus automaattisesti
console.log('🚀 Hotel Haven CookiePro Testaustyökalu ladattu!');
console.log('Suorita testaus komennolla: testCookieProImplementation()');
console.log('Tarkista consent-tilat: checkConsentState("G-XXXXXXXXXX")');
console.log('Simuloi hyväksyntä: simulateConsentAccept()');

// Vie funktiot globaaliin scopeen
window.testCookieProImplementation = testCookieProImplementation;
window.checkConsentState = checkConsentState;
window.simulateConsentAccept = simulateConsentAccept;
