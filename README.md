# LTE Transport Block Size Table Generator
This script parses a transport block size Table 7.1.7.2.1-1 from [3GPP TS 36.213](https://portal.3gpp.org/desktopmodules/Specifications/SpecificationDetails.aspx?specificationId=2427).

## Generator Input Format
As input script accepts text copied directly from a PDF file, just from the begging of the table to the end. [Sample](samples/ts_136213v121300p.txt) is located in [samples](samples/).

## Check Correctness
The script [compare.py](compare.py) can be used to check correctness of a table stored in a json format. An [example](samples/cpp_tbs.json) is located in [samples](samples/).

## Usage
In order to generate reference JSON file for the TBS table:
```
python3 generate_ref.py -f samples/ts_136213v121300p.txt
```

Generated JSON file will be located in `generated/`.

In order to compare another file with a reference:
```
python3 generate_ref.py -f generated/ts_136213v121300p.json -c samples/cpp_tbs.json
```

This will generated an html report in `generated/report.html` showing in which rows which columns are different.

## Copyright
Except for the content of the `samples/` folder the code is licensed under the [MIT License](LICENSE.md).