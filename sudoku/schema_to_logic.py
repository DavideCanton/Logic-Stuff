import sys
import re
import numpy as np

PATTERN = re.compile(r"sudoku_value\(\s*(\d)\s*,\s*(\d)\s*,\s*(\d)\s*\)")

def to_logic(path):
    with open(path) as f:
        for i, line in enumerate(f):
            for j, c in enumerate(line):
                if c.isdigit():
                    print("initial_pos({}, {}, {}).".format(i,j,c))
                    
def to_txt(path):
    m = np.zeros((9, 9), dtype=np.uint8)
    
    with open(path) as f:
        for line in f:            
            for match in PATTERN.finditer(line):
                i, j, v = [int(match.group(i)) for i in (1, 2, 3)]
                m[i, j] = v
                
    for i in range(9):
        for j in range(9):
            print(m[i, j], end="")
        print()
            

if __name__ == "__main__":
    args = sys.argv
    if args[1] == "-l":
        to_logic(args[2])
    elif args[1] == "-s":
        to_txt(args[2])
    else:
        exit("Parametro non valido!")