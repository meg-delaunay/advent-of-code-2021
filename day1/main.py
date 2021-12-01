import csv
import json
import os
import math
import sys

depths = []

filename = sys.argv[1]
with open(filename) as input_file:
    input_reader = csv.reader(input_file, delimiter='\n', quotechar='|')

    for row in input_reader:
        #print(row[0])
        depths.append(int(row[0]))

number_depths = len(depths)

groups = []

for i in range(0, len(depths)-2): 
    group_mems = [depths[i], depths[i+1], depths[i+2]]
    sums = depths[i] + depths[i+1] + depths[i+2]
    groups.append(sums)

print(groups)

current_depth = 99999999999
increases = 0
for i in range(0, len(groups)):
    if groups[i] > current_depth:
        print(current_depth, groups[i])
        increases += 1
    
    current_depth = groups[i]

print(increases)