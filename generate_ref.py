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
parser.add_argument("-f", "--file", default="samples/ts_136213v121200p.txt", type=str, help="Path to reference text file")
args = parser.parse_args()

fname = args.file
fname_base = os.path.basename(os.path.splitext(fname)[0])
f = open(fname)
lines = f.readlines()

LEN_HEADER_IDX_LEN = 10  
LEN_CONTENT = 11
EXPECTED_LEN = LEN_CONTENT*LEN_HEADER_IDX_LEN

i_tbs_result = {}

for line in lines:
    elements = line.strip().split()
    n_elements = len(elements) 

    if n_elements == LEN_CONTENT:
        i_tbs = elements[0]
        tbs_list = list(map(int, elements[1:]))
        if not i_tbs in i_tbs_result:
            i_tbs_result[i_tbs] = []
        i_tbs_result[i_tbs].extend(tbs_list)
    elif n_elements == LEN_HEADER_IDX_LEN:
        pass

# check lengths
all_correct = True
for i_tbs in i_tbs_result:
    if len(i_tbs_result[i_tbs]) != EXPECTED_LEN:
        print("Wrong length on I_TBS = %s"%i_tbs)
        all_correct = False
if all_correct:
    print("Length checked: OK")

if not os.path.exists("generated"):
    os.mkdir("generated")
json.dump(i_tbs_result, open("generated/%s.json"%fname_base, "w"))