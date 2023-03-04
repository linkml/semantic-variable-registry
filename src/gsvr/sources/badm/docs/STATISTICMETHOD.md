# Enum: STATISTICMETHOD



URI: [STATISTICMETHOD](STATISTICMETHOD)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| Aggregate of individual observations | None | The statistic is aggregated from individual observations located within the s... |
| Aggregate of sample aggregates | None | The statistic is aggregated from aggregated individual observations located i... |
| Expert estimate | None | Estimate made by expert familiar with site |




## Slots

| Name | Description |
| ---  | --- |
| [PFCURVE_MP_STATISTIC_METHOD](PFCURVE_MP_STATISTIC_METHOD.md) | Water retention (pF) curve matric potential statistic method |
| [PFCURVE_SWC_STATISTIC_METHOD](PFCURVE_SWC_STATISTIC_METHOD.md) | Water retention (pF) curve soil water content (SWC) statistic method |
| [SOIL_CHEM_BD_STATISTIC_METHOD](SOIL_CHEM_BD_STATISTIC_METHOD.md) | Soil bulk density statistic method |
| [SOIL_CHEM_CN_RATIO_STATISTIC_METHOD](SOIL_CHEM_CN_RATIO_STATISTIC_METHOD.md) | Soil C/N ratio statistic method |
| [SOIL_CHEM_C_ORG_STATISTIC_METHOD](SOIL_CHEM_C_ORG_STATISTIC_METHOD.md) | Soil organic carbon concentration statistic method |
| [SOIL_CHEM_K_STATISTIC_METHOD](SOIL_CHEM_K_STATISTIC_METHOD.md) | Soil potassium concentration statistic method |
| [SOIL_CHEM_NH4_STATISTIC_METHOD](SOIL_CHEM_NH4_STATISTIC_METHOD.md) | Soil ammonium concentration statistic method |
| [SOIL_CHEM_NO3_STATISTIC_METHOD](SOIL_CHEM_NO3_STATISTIC_METHOD.md) | Soil nitrate concentration statistic method |
| [SOIL_CHEM_N_TOT_STATISTIC_METHOD](SOIL_CHEM_N_TOT_STATISTIC_METHOD.md) | Soil total nitrogen concentration statistic method |
| [SOIL_CHEM_PH_H2O_STATISTIC_METHOD](SOIL_CHEM_PH_H2O_STATISTIC_METHOD.md) | Soil pH by H2O statistic method |
| [SOIL_CHEM_PH_SALT_STATISTIC_METHOD](SOIL_CHEM_PH_SALT_STATISTIC_METHOD.md) | Soil pH by CaCl2 or other salt statistic method |
| [SOIL_CHEM_P_STATISTIC_METHOD](SOIL_CHEM_P_STATISTIC_METHOD.md) | Soil phosphorus concentration statistic method |
| [SOIL_DEPTH_ORG_STATISTIC_METHOD](SOIL_DEPTH_ORG_STATISTIC_METHOD.md) | Soil depth of organic horizon statistic method |
| [SOIL_DEPTH_STATISTIC_METHOD](SOIL_DEPTH_STATISTIC_METHOD.md) | Soil depth statistic method |
| [SOIL_STOCK_C_ORG_STATISTIC_METHOD](SOIL_STOCK_C_ORG_STATISTIC_METHOD.md) | Soil organic carbon stock statistic method |
| [SOIL_STOCK_K_STATISTIC_METHOD](SOIL_STOCK_K_STATISTIC_METHOD.md) | Soil potassium stock statistic method |
| [SOIL_STOCK_NH4_STATISTIC_METHOD](SOIL_STOCK_NH4_STATISTIC_METHOD.md) | Soil ammonium stock statistic method |
| [SOIL_STOCK_NO3_STATISTIC_METHOD](SOIL_STOCK_NO3_STATISTIC_METHOD.md) | Soil nitrate stock statistic method |
| [SOIL_STOCK_N_TOT_STATISTIC_METHOD](SOIL_STOCK_N_TOT_STATISTIC_METHOD.md) | Soil total nitrogen stock statistic method |
| [SOIL_STOCK_P_STATISTIC_METHOD](SOIL_STOCK_P_STATISTIC_METHOD.md) | Soil phosphorus stock statistic method |
| [SOIL_TEX_CLAY_STATISTIC_METHOD](SOIL_TEX_CLAY_STATISTIC_METHOD.md) | Clay content statistic method |
| [SOIL_TEX_FIELD_CAP_STATISTIC_METHOD](SOIL_TEX_FIELD_CAP_STATISTIC_METHOD.md) | Field capacity statistic method |
| [SOIL_TEX_ROCK_STATISTIC_METHOD](SOIL_TEX_ROCK_STATISTIC_METHOD.md) | Rock content (>2mm) statistic method |
| [SOIL_TEX_SAND_STATISTIC_METHOD](SOIL_TEX_SAND_STATISTIC_METHOD.md) | Sand content statistic method |
| [SOIL_TEX_SAT_STATISTIC_METHOD](SOIL_TEX_SAT_STATISTIC_METHOD.md) | Soil water saturation point statistic method |
| [SOIL_TEX_SILT_STATISTIC_METHOD](SOIL_TEX_SILT_STATISTIC_METHOD.md) | Silt content statistic method |
| [SOIL_TEX_WATER_HOLD_CAP_STATISTIC_METHOD](SOIL_TEX_WATER_HOLD_CAP_STATISTIC_METHOD.md) | Soil water holding capacity statistic method |
| [SOIL_TEX_WILT_STATISTIC_METHOD](SOIL_TEX_WILT_STATISTIC_METHOD.md) | Wilting point statistic method |
| [SWC_STATISTIC_METHOD](SWC_STATISTIC_METHOD.md) | Soil water content statistic method |
| [WTD_STATISTIC_METHOD](WTD_STATISTIC_METHOD.md) | Water table depth statistic method |






## Identifier and Mapping Information







### Schema Source


* from schema: TEMP




## LinkML Source

<details>
```yaml
name: STATISTIC_METHOD
from_schema: TEMP
rank: 1000
permissible_values:
  Aggregate of individual observations:
    text: Aggregate of individual observations
    description: The statistic is aggregated from individual observations located
      within the site. Observations may be grouped into sample areas (e.g., plots)
      within the site but those groupings are ignored. Statistics generated from individual
      observations directly yield information on the site generally. The statistic
      may represent spatial characteristics of the measurement within the site (e.g.,
      spatial heterogeneity) and/or characteristics due to other factors (e.g., population
      variability).
  Aggregate of sample aggregates:
    text: Aggregate of sample aggregates
    description: The statistic is aggregated from aggregated individual observations
      located in sample areas within the site. For example, individual observations
      are made in 5 sample plots within a site. "Aggregate of sample aggregates" is
      used if a plot statistic (e.g., Mean) is first calculated, and then the plot
      values are aggregated to calculate the site statistic. Statistics generated
      by this approach are often used to highlight the spatial characteristics within
      the site (i.e., the spatial heterogeneity of measurement within the site).
  Expert estimate:
    text: Expert estimate
    description: Estimate made by expert familiar with site

```
</details>
