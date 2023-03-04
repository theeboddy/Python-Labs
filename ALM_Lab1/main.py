import os
from pathlib import Path
import shutil

with open("cycle_for", "r") as f1, open("label_goto", 'w') as f2, open("label", "r") as f3:
    f1_lines = f1.readlines()

    for line in f1_lines:
        f1_elem_line = line.split()

        for elem in f1_elem_line:
            if elem == 'for':
                for new_line in f3:
                    f2.write(new_line)
            else:
                f2.write(elem)
                continue
        print(line)






