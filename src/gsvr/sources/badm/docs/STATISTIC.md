# Enum: STATISTIC



URI: [STATISTIC](STATISTIC)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| 10th Percentile | None | Quantile at 10% of distribution |
| 1st Percentile | None | Quantile at 1% of distribution |
| 25th Percentile | None | Quantile at 25% of distribution |
| 5th Percentile | None | Quantile at 5% of distribution |
| 75th Percentile | None | Quantile at 75% of distribution |
| 90th Percentile | None | Quantile at 90% of distribution |
| 95th Percentile | None | Quantile at 95% of distribution |
| 99th Percentile | None | Quantile at 99% of distribution |
| Maximum | None | Maximum value |
| Mean | None | Average (mean) value of sample population |
| Measurement Uncertainty | None | Report uncertainty as a plus or minus value in the measurement units |
| Median - 50th Percentile | None | Median - Quantile at 50% of distribution |
| Minimum | None | Minimum value |
| Single observation | None | Single observation that is not a calculated statistic of replicates either to... |
| Standard Deviation | None | Standard deviation may be reported from a sample population that consists of ... |




## Slots

| Name | Description |
| ---  | --- |
| [PFCURVE_MP_STATISTIC](PFCURVE_MP_STATISTIC.md) | Water retention (pF) curve matric potential statistic |
| [PFCURVE_SWC_STATISTIC](PFCURVE_SWC_STATISTIC.md) | Water retention (pF) curve soil water content (SWC) statistic |
| [SOIL_CHEM_BD_STATISTIC](SOIL_CHEM_BD_STATISTIC.md) | Soil bulk density statistic |
| [SOIL_CHEM_CN_RATIO_STATISTIC](SOIL_CHEM_CN_RATIO_STATISTIC.md) | Soil C/N ratio statistic |
| [SOIL_CHEM_C_ORG_STATISTIC](SOIL_CHEM_C_ORG_STATISTIC.md) | Soil organic carbon concentration statistic |
| [SOIL_CHEM_K_STATISTIC](SOIL_CHEM_K_STATISTIC.md) | Soil potassium concentration statistic |
| [SOIL_CHEM_NH4_STATISTIC](SOIL_CHEM_NH4_STATISTIC.md) | Soil ammonium concentration statistic |
| [SOIL_CHEM_NO3_STATISTIC](SOIL_CHEM_NO3_STATISTIC.md) | Soil nitrate concentration statistic |
| [SOIL_CHEM_N_TOT_STATISTIC](SOIL_CHEM_N_TOT_STATISTIC.md) | Soil total nitrogen concentration statistic |
| [SOIL_CHEM_PH_H2O_STATISTIC](SOIL_CHEM_PH_H2O_STATISTIC.md) | Soil pH by H2O statistic |
| [SOIL_CHEM_PH_SALT_STATISTIC](SOIL_CHEM_PH_SALT_STATISTIC.md) | Soil pH by CaCl2 or other salt statistic |
| [SOIL_CHEM_P_STATISTIC](SOIL_CHEM_P_STATISTIC.md) | Soil phosphorus concentration statistic |
| [SOIL_DEPTH_ORG_STATISTIC](SOIL_DEPTH_ORG_STATISTIC.md) | Soil depth of organic horizon statistic |
| [SOIL_DEPTH_STATISTIC](SOIL_DEPTH_STATISTIC.md) | Soil depth statistic |
| [SOIL_STOCK_C_ORG_STATISTIC](SOIL_STOCK_C_ORG_STATISTIC.md) | Soil organic carbon stock statistic |
| [SOIL_STOCK_K_STATISTIC](SOIL_STOCK_K_STATISTIC.md) | Soil potassium stock statistic |
| [SOIL_STOCK_NH4_STATISTIC](SOIL_STOCK_NH4_STATISTIC.md) | Soil ammonium stock statistic |
| [SOIL_STOCK_NO3_STATISTIC](SOIL_STOCK_NO3_STATISTIC.md) | Soil nitrate stock statistic |
| [SOIL_STOCK_N_TOT_STATISTIC](SOIL_STOCK_N_TOT_STATISTIC.md) | Soil total nitrogen stock statistic |
| [SOIL_STOCK_P_STATISTIC](SOIL_STOCK_P_STATISTIC.md) | Soil phosphorus stock statistic |
| [SOIL_TEX_CLAY_STATISTIC](SOIL_TEX_CLAY_STATISTIC.md) | Clay content statistic |
| [SOIL_TEX_FIELD_CAP_STATISTIC](SOIL_TEX_FIELD_CAP_STATISTIC.md) | Field capacity statistic |
| [SOIL_TEX_ROCK_STATISTIC](SOIL_TEX_ROCK_STATISTIC.md) | Rock content (>2mm) statistic |
| [SOIL_TEX_SAND_STATISTIC](SOIL_TEX_SAND_STATISTIC.md) | Sand content statistic |
| [SOIL_TEX_SAT_STATISTIC](SOIL_TEX_SAT_STATISTIC.md) | Soil water saturation point statistic |
| [SOIL_TEX_SILT_STATISTIC](SOIL_TEX_SILT_STATISTIC.md) | Silt content statistic |
| [SOIL_TEX_WATER_HOLD_CAP_STATISTIC](SOIL_TEX_WATER_HOLD_CAP_STATISTIC.md) | Soil water holding capacity statistic |
| [SOIL_TEX_WILT_STATISTIC](SOIL_TEX_WILT_STATISTIC.md) | Wilting point statistic |
| [SWC_STATISTIC](SWC_STATISTIC.md) | Soil water content statistic |
| [WTD_STATISTIC](WTD_STATISTIC.md) | Water table depth statistic |






## Identifier and Mapping Information







### Schema Source


* from schema: TEMP




## LinkML Source

<details>
```yaml
name: STATISTIC
from_schema: TEMP
rank: 1000
permissible_values:
  10th Percentile:
    text: 10th Percentile
    description: Quantile at 10% of distribution
  1st Percentile:
    text: 1st Percentile
    description: Quantile at 1% of distribution
  25th Percentile:
    text: 25th Percentile
    description: Quantile at 25% of distribution
  5th Percentile:
    text: 5th Percentile
    description: Quantile at 5% of distribution
  75th Percentile:
    text: 75th Percentile
    description: Quantile at 75% of distribution
  90th Percentile:
    text: 90th Percentile
    description: Quantile at 90% of distribution
  95th Percentile:
    text: 95th Percentile
    description: Quantile at 95% of distribution
  99th Percentile:
    text: 99th Percentile
    description: Quantile at 99% of distribution
  Maximum:
    text: Maximum
    description: Maximum value
  Mean:
    text: Mean
    description: Average (mean) value of sample population
  Measurement Uncertainty:
    text: Measurement Uncertainty
    description: Report uncertainty as a plus or minus value in the measurement units.
      For example, enter 1.5 for +/- 1.5 units. Uncertainty may be reported from the
      instrument's specifications, determined empirically, or estimated by the tower
      team. Please describe such details in Approach. For uncertainty values that
      are better described by a range, a percent, or other, please enter information
      in Comments.
  Median - 50th Percentile:
    text: Median - 50th Percentile
    description: Median - Quantile at 50% of distribution
  Minimum:
    text: Minimum
    description: Minimum value
  Single observation:
    text: Single observation
    description: Single observation that is not a calculated statistic of replicates
      either to get a robust estimate or for spatial variability analysis. For example
      a single biomass observation may be the vegetation harvested in a single 1 x
      1 meter area.
  Standard Deviation:
    text: Standard Deviation
    description: Standard deviation may be reported from a sample population that
      consists of individual or aggregated samples (observations). If the distinction
      is important, specify in STATISTIC_METHOD or Comments.

```
</details>
