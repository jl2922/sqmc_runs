#!/usr/bin/python

import sys

template_filename = sys.argv[1]
print 'Template:', template_filename

template_file = open(template_filename, "r")
template = template_file.read()
template_file.close()

# eps1_list = [0.00005, 0.0001, 0.0002, 0.0005, 0.001]
# eps1_list = [0.00005, 0.0001, 0.0002]
eps1_list = [0.0002, 0.0005, 0.0010, 0.0020]
# eps2_list = [0.0000001, 0.0000002, 0.0000005, 0.000001, 0.000002, 0.000005]
eps2_list = [0.000005]
cutoff_list = [2.85, 3.50, 4.50, 4.75]

bash_script = open("submit_inputs.sh", "w")
bash_script.write("#!/bin/bash\n")

for eps1 in eps1_list:
    for eps2 in eps2_list:
        for cutoff in cutoff_list:
            eps1_str = "%.5f" % eps1
            eps2_str = "%.7f" % eps2
            cutoff_str = "%.2f" % cutoff

            input_str = template
            input_str = input_str.replace("{{eps1}}", eps1_str, 1)
            input_str = input_str.replace("{{eps2}}", eps2_str, 1)
            input_str = input_str.replace("{{cutoff}}", cutoff_str, 1)

            input_filename = "i_heg_e38_eps1_%s_eps2_%s_cut_%s" % (eps1_str, eps2_str, cutoff_str)
            print input_filename

            input_file = open(input_filename, "w")
            input_file.write(input_str)
            input_file.close()

            bash_script.write("../submit_2k.sh %s\n" % input_filename)

