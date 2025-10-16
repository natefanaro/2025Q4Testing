# Data Dictionary

## Column Definitions

### Session Identification
- **Session**: Session identifier (e.g., "TD Session 1", "R23 Practice")
- **Type**: Event type ("Test Day" or "Race 23")
- **Date/Time**: Session start time
- **session_number**: Numeric session identifier (1-10 for test day)
- **session_time**: Time of day session occurred

### Lap Performance
- **Best Lap**: Fastest valid lap time (format: mm:ss.sss)
- **lap_time**: Individual lap time
- **lap_number**: Sequential lap number within session
- **Avg Valid Lap**: Average of all valid racing laps (excludes first lap)

### RPM (Engine Speed)
- **Peak RPM**: Maximum RPM achieved during valid racing laps
- **Low RPM**: Minimum RPM from valid racing laps
- **Avg RPM**: Average RPM across all valid racing laps
- **rpm_min/rpm_max/rpm_avg**: Individual lap RPM statistics

### Speed Measurements
- **Top Speed (mph)**: Maximum GPS speed from valid lap segments
- **speed_min_mph/speed_max_mph/speed_avg_mph**: Individual lap speed data
- **Low Speed (mph)**: Minimum speed from valid racing segments

### Throttle Data
- **Max Throttle %**: Peak throttle application percentage
- **Min Throttle %**: Minimum throttle percentage
- **Avg Throttle %**: Average throttle across valid laps
- **max_throttle_pct/avg_throttle_pct**: Individual lap throttle statistics

### G-Force Measurements
- **Peak Lateral G**: Maximum lateral (cornering) G-force
- **max_lateral_g**: Individual lap peak lateral G-force
- **max_longitudinal_g**: Peak forward/braking G-force

### Vehicle Dynamics
- **max_steering_deg**: Maximum steering wheel angle (degrees)

### Data Quality Indicators
- **Valid Laps**: Count of laps meeting filtering criteria:
  - Excludes first lap (warm-up)
  - Lap time between 15-45 seconds
  - Non-zero RPM values
  - Excludes in/out laps
- **Total Laps**: Raw count of all recorded laps

## Data Types and Ranges

### Time Formats
- Lap times: mm:ss.sss (minutes:seconds.milliseconds)
- Session times: h:mm AM/PM format

### Numeric Ranges (Typical)
- **RPM**: 1,500 - 7,000 (kart engine range)
- **Speed**: 0 - 45 mph (track dependent)
- **Throttle**: 0 - 100% (percentage values)
- **Lateral G**: 0 - 2.0 G (cornering forces)
- **Longitudinal G**: -1.5 to +1.0 G (braking/acceleration)
- **Steering**: -180 to +180 degrees

## Special Values
- **0 values**: Often indicate sensor issues or invalid readings
- **Missing data**: Represented as empty cells in lap comparison files
- **Filtered data**: Values outside realistic ranges excluded from analysis
