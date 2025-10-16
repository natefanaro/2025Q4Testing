# Racing Session Data - Public Release

## Overview
This directory contains processed racing telemetry data from two events:
- **Test Day**: October 4, 2025 (10 sessions) - Configuration testing
- **Race 23**: September 27, 2025 (5 sessions) - Competitive racing data

## Data Processing Notes

### Filtering Applied
- **First lap exclusion**: All first laps removed from analysis (warm-up period)
- **Valid lap filtering**: Only laps between 15-45 seconds included in statistics
- **RPM validation**: Laps with 0 RPM excluded as invalid data
- **In/out lap removal**: Cool-down and pit entry/exit laps filtered out

### Metrics Explained
- **Best Lap**: Fastest valid racing lap (excludes first lap)
- **Peak RPM**: Highest RPM achieved during valid racing laps
- **Low/Avg RPM**: Minimum and average RPM from racing data only
- **Top Speed**: Maximum GPS speed from valid lap segments
- **Peak Lateral G**: Highest cornering G-force recorded
- **Valid Laps**: Count of laps meeting filtering criteria
- **Total Laps**: Raw lap count including all recorded laps

### Sessions Overview
**Test Day (TD) Sessions**: Configuration testing with various setups
- Session 1 (11:11 AM): Baseline configuration - 11 valid laps
- Sessions 2-10: Various configuration changes - 4-5 valid laps each
- Best overall lap: 19.101 seconds (Session 8, 1:06 PM)

**Race 23 (R23) Sessions**: Competitive racing event
- Practice: 25 valid laps of race preparation
- Q1-Q3: Qualifying sessions (5 laps each)
- Race: 25 valid racing laps
- Best race lap: 19.141 seconds
