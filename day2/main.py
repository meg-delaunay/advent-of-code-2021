import csv
import json
import os
import math
import sys

# horiz, depth, aim
coords = (0,0,0)

filename = sys.argv[1]
with open(filename) as input_file:
    input_reader = csv.reader(input_file, delimiter='\n', quotechar='|')

    for row in input_reader:
        instruction = row[0].split()

        if instruction[0] == 'forward':
            coords = (coords[0]+int(instruction[1]), coords[1]+(coords[2]*int(instruction[1])), coords[2])
        elif instruction[0] == 'up':
            coords = (coords[0], coords[1], coords[2]-int(instruction[1]))
        elif instruction[0] == 'down':
            coords = (coords[0], coords[1], coords[2]+int(instruction[1]))

print(coords)
print(coords[0] * coords[1])