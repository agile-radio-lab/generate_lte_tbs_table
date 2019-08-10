__author__ = "Igor Kim"
__credits__ = ["Igor Kim"]
__maintainer__ = "Igor Kim"
__email__ = "igor.skh@gmail.com"
__date__ = "08/2019"
__license__ = "MIT"

import json
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", default="generated/ts_136213v121200p.json", type=str, help="Path to reference JSON file")
parser.add_argument("-c", "--compare", default="samples/cpp_tbs.json", type=str, help="Path to target file")
parser.add_argument("-o", "--output", default="generated/report.html", type=str, help="Path to report")
args = parser.parse_args()

fname_ref = args.file
fname_comp = args.compare

ref_table = json.load(open(fname_ref))
comp_tbs_table = json.load(open(fname_comp))

def to_html(arr, is_correct):
    res = "<tr>"
    for i, val in enumerate(arr):
        color = "black" if is_correct[i] else "red"
        res += "<td style=\"color:%s\">%d</td>"%(color, val)
    res += "</tr>"
    return res

report_html = "<table style=\"text-align:left;\">"
errors_cnt = 0
for i, tbs_list in enumerate(comp_tbs_table):
    i_tbs = str(i)
    if i_tbs in ref_table:
        len_ref = len(ref_table[i_tbs])
        len_comp = len(tbs_list)
        if len_ref != len_comp:
            report_html += "<tr><th colspan=\"%d\">I_TBS = %s, \
                inconsistent length got %d, expected %d</th></tr>"\
                    %(len_ref, i_tbs, len_comp, len_ref)
            print("Inconsistent length, I_TBS = %s"%i_tbs)
            errors_cnt += 1
            continue
    
        compare = [ref_table[i_tbs][i] == tbs_list[i] for i in range(len_ref)]
        if not all(compare):
            report_html += "<tr><th colspan=\"%d\">I_TBS = %s</th></tr>"%(len_ref, i_tbs)
            report_html += to_html(ref_table[i_tbs], compare)
            report_html += to_html(tbs_list, compare)
            print("Incorrect values found, I_TBS = %s"%i_tbs)
            errors_cnt += 1
report_html += "</table>"

print("%d error(s) found"%errors_cnt)
if errors_cnt > 0:
    print("Writting report to: %s"%args.output)
    if not os.path.exists("generated"):
        os.mkdir("generated")
    f = open(args.output, "w")
    f.write(report_html)