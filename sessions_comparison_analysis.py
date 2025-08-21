#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hotel Haven - Sessioiden vertailu MCP vs GA4 UI
Testataan onko ero vain revenue-mittareissa vai kaikissa mittareissa
"""

def sessions_comparison_analysis():
    """Vertaa sessioita MCP:n ja GA4:n välillä"""
    
    print("📊 SESSIOIDEN VERTAILU - MCP vs GA4 UI")
    print("=" * 80)
    print()
    
    # MCP:n päivittäiset luvut toukokuu 2025
    daily_data = [
        {"date": "2025-05-31", "sessions": 1391, "totalUsers": 1249, "newUsers": 1023},
        {"date": "2025-05-30", "sessions": 1169, "totalUsers": 1023, "newUsers": 826},
        {"date": "2025-05-29", "sessions": 1154, "totalUsers": 1044, "newUsers": 828},
        {"date": "2025-05-28", "sessions": 1845, "totalUsers": 1654, "newUsers": 1391},
        {"date": "2025-05-27", "sessions": 1225, "totalUsers": 1098, "newUsers": 865},
        {"date": "2025-05-26", "sessions": 1132, "totalUsers": 1044, "newUsers": 823},
        {"date": "2025-05-25", "sessions": 1148, "totalUsers": 1050, "newUsers": 866},
        {"date": "2025-05-24", "sessions": 1003, "totalUsers": 892, "newUsers": 712},
        {"date": "2025-05-23", "sessions": 1093, "totalUsers": 950, "newUsers": 706},
        {"date": "2025-05-22", "sessions": 1139, "totalUsers": 1033, "newUsers": 822},
        {"date": "2025-05-21", "sessions": 1099, "totalUsers": 994, "newUsers": 777},
        {"date": "2025-05-20", "sessions": 1051, "totalUsers": 934, "newUsers": 721},
        {"date": "2025-05-19", "sessions": 1298, "totalUsers": 1176, "newUsers": 971},
        {"date": "2025-05-18", "sessions": 765, "totalUsers": 683, "newUsers": 558},
        {"date": "2025-05-17", "sessions": 802, "totalUsers": 709, "newUsers": 555},
        {"date": "2025-05-16", "sessions": 1036, "totalUsers": 883, "newUsers": 692},
        {"date": "2025-05-15", "sessions": 1006, "totalUsers": 882, "newUsers": 699},
        {"date": "2025-05-14", "sessions": 1000, "totalUsers": 862, "newUsers": 665},
        {"date": "2025-05-13", "sessions": 1028, "totalUsers": 918, "newUsers": 713},
        {"date": "2025-05-12", "sessions": 1026, "totalUsers": 916, "newUsers": 721},
        {"date": "2025-05-11", "sessions": 765, "totalUsers": 685, "newUsers": 553},
        {"date": "2025-05-10", "sessions": 888, "totalUsers": 772, "newUsers": 613},
        {"date": "2025-05-09", "sessions": 970, "totalUsers": 861, "newUsers": 681},
        {"date": "2025-05-08", "sessions": 923, "totalUsers": 822, "newUsers": 643},
        {"date": "2025-05-07", "sessions": 1077, "totalUsers": 952, "newUsers": 761},
        {"date": "2025-05-06", "sessions": 1022, "totalUsers": 905, "newUsers": 699},
        {"date": "2025-05-05", "sessions": 1043, "totalUsers": 926, "newUsers": 738},
        {"date": "2025-05-04", "sessions": 1043, "totalUsers": 944, "newUsers": 762},
        {"date": "2025-05-03", "sessions": 1003, "totalUsers": 879, "newUsers": 699},
        {"date": "2025-05-02", "sessions": 1082, "totalUsers": 949, "newUsers": 751},
        {"date": "2025-05-01", "sessions": 963, "totalUsers": 848, "newUsers": 675}
    ]
    
    # MCP:n kanavittaiset luvut
    channel_data = [
        {"channel": "Organic Search", "sessions": 8354, "totalUsers": 5836},
        {"channel": "Paid Social", "sessions": 7509, "totalUsers": 6884},
        {"channel": "Paid Search", "sessions": 6780, "totalUsers": 5381},
        {"channel": "Direct", "sessions": 4203, "totalUsers": 3377},
        {"channel": "Referral", "sessions": 2242, "totalUsers": 1735},
        {"channel": "Email", "sessions": 1370, "totalUsers": 1087},
        {"channel": "Cross-network", "sessions": 1260, "totalUsers": 1036},
        {"channel": "Organic Social", "sessions": 618, "totalUsers": 580},
        {"channel": "Unassigned", "sessions": 487, "totalUsers": 465},
        {"channel": "Mobile Push Notifications", "sessions": 73, "totalUsers": 62},
        {"channel": "Paid Other", "sessions": 30, "totalUsers": 27},
        {"channel": "Paid Video", "sessions": 23, "totalUsers": 23}
    ]
    
    # Laske kokonaisluvut
    total_sessions = sum(day["sessions"] for day in daily_data)
    total_users = sum(day["totalUsers"] for day in daily_data)
    total_new_users = sum(day["newUsers"] for day in daily_data)
    
    channel_total_sessions = sum(ch["sessions"] for ch in channel_data)
    channel_total_users = sum(ch["totalUsers"] for ch in channel_data)
    
    print("📅 MCP KOKONAISLUVUT TOUKOKUU 2025:")
    print("-" * 40)
    print(f"Sessiot (päivittäin aggregoitu):    {total_sessions:,}")
    print(f"Sessiot (kanavittain aggregoitu):   {channel_total_sessions:,}")
    print(f"Käyttäjät (päivittäin):            {total_users:,}")
    print(f"Käyttäjät (kanavittain):           {channel_total_users:,}")
    print(f"Uudet käyttäjät:                   {total_new_users:,}")
    print()
    
    # Tarkista konsistenssi
    session_diff = abs(total_sessions - channel_total_sessions)
    user_diff = abs(total_users - channel_total_users)
    
    print("🔍 MCP SISÄINEN KONSISTENSSI:")
    print("-" * 35)
    print(f"Sessiot - päivittäin vs kanavittain: {session_diff:,} ({(session_diff/total_sessions)*100:.2f}%)")
    print(f"Käyttäjät - päivittäin vs kanavittain: {user_diff:,} ({(user_diff/total_users)*100:.2f}%)")
    print()
    
    if session_diff == 0 and user_diff == 0:
        print("✅ MCP DATA ON KONSISTENTTIA")
    elif session_diff < total_sessions * 0.01:  # alle 1% ero
        print("✅ MCP DATA ON LÄHES KONSISTENTTIA (alle 1% ero)")
    else:
        print("⚠️ MCP DATASSA ON EROJA")
    
    print()
    print("🎯 VERTAILUN TARKOITUS:")
    print("-" * 30)
    print()
    print("TESTAAMME ONKO ERO:")
    print("• 🎯 VAIN ECOMMERCE-MITTAREISSA (revenue, conversions)")
    print("• 🌐 KAIKISSA MITTAREISSA (sessions, users)")
    print()
    print("JOS ERO ON VAIN ECOMMERCE-MITTAREISSA:")
    print("→ Ongelma on spesifisti ecommerce-datan käsittelyssä")
    print()
    print("JOS ERO ON KAIKISSA MITTAREISSA:")
    print("→ Ongelma on yleisempi (aikavyöhyke, property, suodattimet)")
    print()
    
    print("📋 GA4 UI TARKISTUSOHJE:")
    print("-" * 30)
    print()
    print("Tarkista GA4:stä seuraavat luvut toukokuulle 2025:")
    print()
    print("1. 📊 YLEISKATSAUS (Reports > Acquisition > Overview):")
    print("   • Sessions")
    print("   • Users")
    print("   • New users")
    print()
    print("2. 📈 KANAVITTAINEN JAKAUTUMA:")
    print("   • Sessions by default channel grouping")
    print("   • Users by default channel grouping")
    print()
    print("3. 🔍 EXPLORE-RAPORTTI:")
    print("   • Dimension: Session default channel group")
    print("   • Metrics: Sessions, Users")
    print("   • Date range: 1.5.2025 - 31.5.2025")
    print()
    
    print("MCP:N LUVUT VERTAILUA VARTEN:")
    print("-" * 40)
    print()
    print("KOKONAISLUVUT:")
    print(f"• Sessions: {total_sessions:,}")
    print(f"• Users: {total_users:,}")
    print(f"• New Users: {total_new_users:,}")
    print()
    
    print("TOP 5 KANAVAA (Sessions):")
    sorted_channels = sorted(channel_data, key=lambda x: x["sessions"], reverse=True)[:5]
    for i, ch in enumerate(sorted_channels, 1):
        print(f"{i}. {ch['channel']}: {ch['sessions']:,} sessions, {ch['totalUsers']:,} users")
    
    print()
    print("🔍 MITÄ ETSIMME:")
    print("-" * 20)
    print()
    print("SKENAARIO A: LUVUT TÄSMÄÄVÄT (±5%)")
    print("→ Ongelma on vain ecommerce-datassa")
    print("→ Revenue/conversion -mittarit ovat ongelma")
    print("→ Sessions/users -mittarit toimivat")
    print()
    print("SKENAARIO B: LUVUT EIVÄT TÄSMÄÄ")
    print("→ Ongelma on yleisempi")
    print("→ Kaikki mittarit kärsivät samasta ongelmasta")
    print("→ Todennäköisesti aikavyöhyke/property/suodatin -ongelma")
    print()
    print("Kerro GA4:n luvut niin voimme verrata!")

if __name__ == "__main__":
    sessions_comparison_analysis()
