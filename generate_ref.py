import json
import os
import argparse

__author__ = "Igor Kim"
__credits__ = ["Igor Kim"]
__maintainer__ = "Igor Kim"
__email__ = "igor.skh@gmail.com"
__date__ = "08/2019"
__license__ = "MIT"


def generate_tbs_ref_table(file_h, n_header, n_content):
    i_tbs_result = {}
    for line in file_h:
        elements = line.strip().split()
        n_elements = len(elements)
        if n_elements == n_content:
            i_tbs = elements[0]
            tbs_list = list(map(int, elements[1:]))
            if i_tbs not in i_tbs_result:
                i_tbs_result[i_tbs] = []
            i_tbs_result[i_tbs].extend(tbs_list)
        elif n_elements == n_header:
            # do something with the n_prbs
            pass
    return i_tbs_result


def check_length(ref_table, n_total):
    all_correct = True
    for i_tbs in ref_table:
        if len(ref_table[i_tbs]) != n_total:
            print("Wrong length on I_TBS = %s" % i_tbs)
            all_correct = False
            break
    return all_correct


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file",
                        default="samples/ts_136213v121200p.txt",
                        type=str, help="Path to reference text file")
    parser.add_argument("-n", "--header", default=10,
                        type=int, help="Header line length")
    parser.add_argument("-c", "--content", default=11,
                        type=int, help="Content line length")
    args = parser.parse_args()

    fname = args.file
    fname_base = os.path.basename(os.path.splitext(fname)[0])

    ref_table = generate_tbs_ref_table(open(fname), args.header, args.content)
    if check_length(ref_table, args.header*args.content):
        print("Length checked: OK")

    if not os.path.exists("generated"):
        os.mkdir("generated")
    json.dump(ref_table, open("generated/%s.json" % fname_base, "w"))
