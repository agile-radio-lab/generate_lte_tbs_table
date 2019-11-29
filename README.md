[![CircleCI](https://circleci.com/gh/igorskh/generate_lte_tbs_table.svg?style=svg)](https://circleci.com/gh/igorskh/generate_lte_tbs_table)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/8228948b075c4e37afe4632813fba406)](https://www.codacy.com/app/igorskh/generate_lte_tbs_table?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=igorskh/generate_lte_tbs_table&amp;utm_campaign=Badge_Grade)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/igorskh/generate_lte_tbs_table.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/igorskh/generate_lte_tbs_table/alerts/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/igorskh/generate_lte_tbs_table.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/igorskh/generate_lte_tbs_table/context:python)

# LTE Transport Block Size Table Generator
This script parses a transport block size Table 7.1.7.2.1-1 from [3GPP TS 36.213](https://portal.3gpp.org/desktopmodules/Specifications/SpecificationDetails.aspx?specificationId=2427).

## Generator Input Format
Script accepts as input a text copied directly from a PDF version of [3GPP TS 36.213](https://www.etsi.org/deliver/etsi_ts/136200_136299/136213/12.04.00_60/ts_136213v120400p.pdf), just from the begging of the Table 7.1.7.2.1-1 to the end of the table. [Sample text file](samples/ts_136213v121300p.txt) is located in [samples](samples/) folder. The script writes output to in JSON format to [generated](generated/) folder.

## Check Correctness
The script [compare.py](compare.py) can be used to check correctness of a table stored in a json format. An [example](samples/cpp_tbs.json) is located in [samples](samples/).

## Usage
In order to generate reference JSON file for the TBS table:
```bash
python3 generate_ref.py -f samples/ts_136213v121300p.txt
```

Generated JSON file will be located in `generated/`.

In order to compare another file with a reference:
```bash
python3 compare.py -f generated/ts_136213v121300p.json -c samples/cpp_tbs.json
```

This will generated an html report in `generated/report.html` showing in which rows which columns are different.

## Copyright
Except for the content of the `samples/` folder the code is licensed under the [MIT License](LICENSE.md).
