# RPM Differential Analysis

Color-coded visualizations showing where each configuration has better or worse RPM compared to qualifying baseline.

## Files

- `config_1_rpm_differential.png` - Config 1 RPM vs Qualifying RPM
- `config_2_rpm_differential.png` - Config 2 RPM vs Qualifying RPM
- `config_3_rpm_differential.png` - Config 3 RPM vs Qualifying RPM
- `config_4_rpm_differential.png` - Config 4 RPM vs Qualifying RPM
- `config_5_rpm_differential.png` - Config 5 RPM vs Qualifying RPM
- `config_6_rpm_differential.png` - Config 6 RPM vs Qualifying RPM

## What These Show

Each differential map displays:
- **Single track line** color-coded by RPM advantage/disadvantage
- **Color scheme**:
  - **Bright Green** = Configuration has higher RPM (advantage)
  - **Bright Yellow** = Equal/neutral RPM (within 5% difference)
  - **Bright Red** = Qualifying has higher RPM (disadvantage)
- **RPM analysis stats** (bottom left):
  - Max config advantage (highest RPM gain)
  - Max qualifying advantage (highest RPM loss)
  - Average RPM difference across lap
- **Color legend** (bottom right)

## How to Read

**Green zones** indicate where the configuration is outperforming qualifying:
- Better acceleration
- Higher corner exit speed
- Superior engine power delivery

**Red zones** indicate where qualifying was better:
- Configuration losing power
- Less effective acceleration
- Potential setup issues

**Yellow zones** indicate neutral areas:
- Similar performance
- Minimal RPM difference

## Analysis Method

RPM differences are calculated by:
1. GPS-matching points between qualifying and configuration laps
2. Calculating RPM differential at each matched position
3. Color-coding based on magnitude and direction of difference

## Use Cases

These maps help identify:
- **Strengths**: Where does this config excel?
- **Weaknesses**: Where is power being lost?
- **Track zones**: Which corners/straights benefit most from the setup?
- **Setup optimization**: What component changes affect which track sections?

## Component Impact

Compare differential maps between configurations to understand:
- How flywheel changes affect acceleration zones
- How carburetor changes affect mid-corner RPM
- How exhaust changes affect straightaway performance
