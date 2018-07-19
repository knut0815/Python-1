#! /usr/bin/env python
import os
import sys

# initialize
dict_drug = {}
#tok = []

# create dictionary
with open(sys.argv[1], 'r') as f:
    next(f)
    for line in f:
        tok = str.strip(line).split(',')
        drug = tok[3]
        prescriber = tok[2]+ ' ' + tok[1]
        cost = int(tok[4])
        if drug in dict_drug:
            if prescriber in dict_drug[drug]:
                dict_drug[drug][prescriber] += cost
            else:
                dict_drug[drug][prescriber] = cost
        else:
            dict_drug[drug] = {}
            dict_drug[drug][prescriber] = cost

# generate output list
output = [None]*len(dict_drug)
item = 0
for drug in dict_drug:
    num_prescriber = len(dict_drug[drug])
    total_cost = 0
    for prescriber in dict_drug[drug]:
        total_cost += dict_drug[drug][prescriber]
        output[item] = drug, num_prescriber, total_cost
    item += 1

# sort output list
output.sort(key=lambda x: x[0], reverse = False)
output.sort(key=lambda x: x[2], reverse = True)

# print to file
sys.stdout = open(sys.argv[2],'w')
#print('drug_name,num_prescriber,total_cost',file=sys.stdout)
#print('\n'.join([','.join([format(j) for j in i]) for i in output]),file=sys.stdout)
sys.stdout.write('drug_name,num_prescriber,total_cost\n')
sys.stdout.write('\n'.join([','.join([format(j) for j in i]) for i in output]))
f.close()

