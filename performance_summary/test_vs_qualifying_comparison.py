#!/usr/bin/env python3

import csv

def create_qualifying_comparison_csvs():
    """Create CSV files comparing test configurations to Race 23 qualifying only"""

    # Race 23 Qualifying data (excluding Practice and Race)
    race23_qualifying = {
        'Q1': {'best_lap': '0:19.563', 'sessions': 'Q1'},
        'Q2': {'best_lap': '0:19.457', 'sessions': 'Q2'},
        'Q3': {'best_lap': '0:19.573', 'sessions': 'Q3'}
    }

    # Best qualifying lap for comparison
    best_qualifying = '0:19.457'  # Q2 best

    # Test day configuration data
    test_configs = [
        {'config': 1, 'sessions': '1-3', 'best_lap': '0:19.298', 'flywheel': 'V2 High-Performance', 'carburetor': 'V1', 'exhaust': 'V1 Stock'},
        {'config': 2, 'sessions': '4-5', 'best_lap': '0:19.403', 'flywheel': 'V2 High-Performance', 'carburetor': 'V1', 'exhaust': 'V1 Stock'},
        {'config': 3, 'sessions': '6', 'best_lap': '0:19.236', 'flywheel': 'V2 High-Performance', 'carburetor': 'V1', 'exhaust': 'V2 Thick Wall'},
        {'config': 4, 'sessions': '7-8', 'best_lap': '0:19.101', 'flywheel': 'V2 High-Performance', 'carburetor': 'V2', 'exhaust': 'V2 Thick Wall'},
        {'config': 5, 'sessions': '9', 'best_lap': '0:19.280', 'flywheel': 'V1 Stock', 'carburetor': 'V2', 'exhaust': 'V2 Thick Wall'},
        {'config': 6, 'sessions': '10', 'best_lap': '0:19.673', 'flywheel': 'V1 Stock', 'carburetor': 'V2', 'exhaust': 'V1 Stock'}
    ]

    def lap_to_seconds(lap_str):
        """Convert lap time string to seconds"""
        minutes, seconds = lap_str.split(':')
        return int(minutes) * 60 + float(seconds)

    def calculate_difference(test_time, qualifying_time):
        """Calculate time difference and percentage"""
        test_sec = lap_to_seconds(test_time)
        qual_sec = lap_to_seconds(qualifying_time)
        diff = test_sec - qual_sec
        percent = (diff / qual_sec) * 100
        return diff, percent

    # 1. Test Configurations vs Best Qualifying (Q2)
    with open('public/performance_summary/test_vs_best_qualifying.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([
            'Configuration', 'Test_Sessions', 'Test_Best_Lap', 'Q2_Best_Lap',
            'Time_Difference', 'Percent_Difference', 'Performance_vs_Qualifying',
            'Flywheel', 'Carburetor', 'Exhaust'
        ])

        for config in test_configs:
            diff, percent = calculate_difference(config['best_lap'], best_qualifying)
            status = 'FASTER' if diff < 0 else 'SLOWER'
            diff_str = f"{diff:+.3f}s"
            percent_str = f"{percent:+.2f}%"

            writer.writerow([
                f"Config {config['config']}", config['sessions'], config['best_lap'],
                best_qualifying, diff_str, percent_str, status,
                config['flywheel'], config['carburetor'], config['exhaust']
            ])

    # 2. Test Configurations vs All Qualifying Sessions
    with open('public/performance_summary/test_vs_all_qualifying.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([
            'Configuration', 'Test_Best_Lap', 'vs_Q1', 'vs_Q2', 'vs_Q3',
            'Best_Qualifying_Comparison', 'Flywheel', 'Carburetor', 'Exhaust'
        ])

        for config in test_configs:
            vs_q1_diff, vs_q1_pct = calculate_difference(config['best_lap'], race23_qualifying['Q1']['best_lap'])
            vs_q2_diff, vs_q2_pct = calculate_difference(config['best_lap'], race23_qualifying['Q2']['best_lap'])
            vs_q3_diff, vs_q3_pct = calculate_difference(config['best_lap'], race23_qualifying['Q3']['best_lap'])

            # Best comparison
            best_diff = min(vs_q1_diff, vs_q2_diff, vs_q3_diff)
            best_status = 'FASTER than all qualifying' if best_diff < 0 else f"{best_diff:+.3f}s vs best qualifying"

            writer.writerow([
                f"Config {config['config']}", config['best_lap'],
                f"{vs_q1_diff:+.3f}s", f"{vs_q2_diff:+.3f}s", f"{vs_q3_diff:+.3f}s",
                best_status, config['flywheel'], config['carburetor'], config['exhaust']
            ])

    # 3. Component Impact Analysis vs Qualifying
    with open('public/performance_summary/component_impact_vs_qualifying.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([
            'Component_Type', 'Component_Version', 'Best_Lap_Achieved', 'vs_Best_Qualifying',
            'Configurations_Using', 'Impact_Rating'
        ])

        # Analyze flywheel impact
        v2_flywheel_configs = [c for c in test_configs if c['flywheel'] == 'V2 High-Performance']
        v1_flywheel_configs = [c for c in test_configs if c['flywheel'] == 'V1 Stock']

        v2_best = min([lap_to_seconds(c['best_lap']) for c in v2_flywheel_configs])
        v1_best = min([lap_to_seconds(c['best_lap']) for c in v1_flywheel_configs])

        v2_vs_qual = v2_best - lap_to_seconds(best_qualifying)
        v1_vs_qual = v1_best - lap_to_seconds(best_qualifying)

        writer.writerow([
            'Flywheel', 'V2 High-Performance', f"0:{v2_best:06.3f}", f"{v2_vs_qual:+.3f}s",
            'Configs 1,2,3,4', 'High Performance'
        ])
        writer.writerow([
            'Flywheel', 'V1 Stock', f"0:{v1_best:06.3f}", f"{v1_vs_qual:+.3f}s",
            'Configs 5,6', 'Lower Performance'
        ])

        # Analyze carburetor impact
        v2_carb_configs = [c for c in test_configs if c['carburetor'] == 'V2']
        v1_carb_configs = [c for c in test_configs if c['carburetor'] == 'V1']

        v2_carb_best = min([lap_to_seconds(c['best_lap']) for c in v2_carb_configs])
        v1_carb_best = min([lap_to_seconds(c['best_lap']) for c in v1_carb_configs])

        v2_carb_vs_qual = v2_carb_best - lap_to_seconds(best_qualifying)
        v1_carb_vs_qual = v1_carb_best - lap_to_seconds(best_qualifying)

        writer.writerow([
            'Carburetor', 'V2', f"0:{v2_carb_best:06.3f}", f"{v2_carb_vs_qual:+.3f}s",
            'Configs 4,5,6', 'Peak Performance'
        ])
        writer.writerow([
            'Carburetor', 'V1', f"0:{v1_carb_best:06.3f}", f"{v1_carb_vs_qual:+.3f}s",
            'Configs 1,2,3', 'Good Performance'
        ])

        # Analyze exhaust impact
        v2_exhaust_configs = [c for c in test_configs if c['exhaust'] == 'V2 Thick Wall']
        v1_exhaust_configs = [c for c in test_configs if c['exhaust'] == 'V1 Stock']

        v2_exhaust_best = min([lap_to_seconds(c['best_lap']) for c in v2_exhaust_configs])
        v1_exhaust_best = min([lap_to_seconds(c['best_lap']) for c in v1_exhaust_configs])

        v2_exhaust_vs_qual = v2_exhaust_best - lap_to_seconds(best_qualifying)
        v1_exhaust_vs_qual = v1_exhaust_best - lap_to_seconds(best_qualifying)

        writer.writerow([
            'Exhaust', 'V2 Thick Wall', f"0:{v2_exhaust_best:06.3f}", f"{v2_exhaust_vs_qual:+.3f}s",
            'Configs 3,4,5', 'High Performance'
        ])
        writer.writerow([
            'Exhaust', 'V1 Stock', f"0:{v1_exhaust_best:06.3f}", f"{v1_exhaust_vs_qual:+.3f}s",
            'Configs 1,2,6', 'Standard Performance'
        ])

    # 4. Qualifying Session Breakdown
    with open('public/performance_summary/qualifying_session_breakdown.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([
            'Session', 'Session_Type', 'Best_Lap', 'Configs_Faster_Than_This',
            'Fastest_Test_Config', 'Time_Gap_to_Fastest_Test'
        ])

        fastest_test = min([lap_to_seconds(c['best_lap']) for c in test_configs])
        fastest_config = next(c for c in test_configs if lap_to_seconds(c['best_lap']) == fastest_test)

        for session, data in race23_qualifying.items():
            session_time = lap_to_seconds(data['best_lap'])
            configs_faster = [c for c in test_configs if lap_to_seconds(c['best_lap']) < session_time]
            gap_to_fastest = session_time - fastest_test

            writer.writerow([
                f"Race 23 {session}", "Qualifying", data['best_lap'],
                f"{len(configs_faster)}/6 configs", f"Config {fastest_config['config']}",
                f"{gap_to_fastest:+.3f}s"
            ])

    print("Created qualifying comparison CSV files:")
    print("1. test_vs_best_qualifying.csv")
    print("2. test_vs_all_qualifying.csv")
    print("3. component_impact_vs_qualifying.csv")
    print("4. qualifying_session_breakdown.csv")

if __name__ == "__main__":
    create_qualifying_comparison_csvs()