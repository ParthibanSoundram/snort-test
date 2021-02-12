import os

# Getting the current work directory (cwd)
thisdir = "/home/parthiban/Desktop/SNORT/sagan_rules"

# r=root, d=directories, f = files
for r, d, f in os.walk(thisdir):
    for file in f:
        if file.endswith(".rules"):
            rules_file_name = os.path.join(r, file).split("/")[-1]
            print(f"include $RULE_PATH/{rules_file_name}")