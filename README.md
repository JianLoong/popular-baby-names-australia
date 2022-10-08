# Popular Baby Names in Australia

This repository is a collection of the top 100 baby names in Australia from various open data sets.

If you have noticed some mistakes or bugs, or maybe you have any suggestions please create an issue.

This API is meant to be a read-only web API. It is intentional for files to be stored this way (json format) as it avoids using any database engine.

# Introduction

The data consists of a ranked list of the top 100 male and female baby names with frequency counts for every year since 2008. 

The aim of this API is to provide static information that will be consumed by other applications.

# Data Sets Sources

| Dataset | Source                                                                                  | License                                                                                   |
| ------- | --------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| QLD     | https://www.data.qld.gov.au/dataset/top-100-baby-names                                  |                                                                                           |
| TAS     | https://data.gov.au/dataset/ds-dga-a37db87d-6bbb-4fb1-96a4-224266b757b8/details         |                                                                                           |
| VIC     | [Data Vic Australia](https://discover.data.vic.gov.au/dataset/popular-baby-names-api  ) | [Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/) |
| NSW     | [Data NSW Australia](https://data.nsw.gov.au/data/dataset/popular-baby-names)           | [Creative Commons Attribution](https://opendefinition.org/licenses/cc-by/)                |
| SA      | [Data SA Australia](https://data.sa.gov.au/data/dataset/popular-baby-names)             | [Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/) |


# List of End Points

The current base url is [https://jianliew.me/popular-baby-names-australia/](https://jianliew.me/popular-baby-names-australia/)

| State | End Point          | Status |                                                                            |
| ----- | ------------------ | ------ | -------------------------------------------------------------------------- |
| VIC   | /data/vic/all.json | x      | [Test](https://jianliew.me/popular-baby-names-australia/data/vic/all.json) |


# Usage Example

```bash
curl https://jianliew.me/popular-baby-names-australia/data/vic/2020.json
```
