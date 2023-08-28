# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 15:22:57 2018

@author: khanhle
"""
import re
import sys

in_file = sys.argv[1]
out_file = sys.argv[2]
ngram = sys.argv[3]
ng = int(ngram)
#label = sys.argv[4]

fout = open(out_file,'w')

spe_character = []
j = 0
with open(in_file) as f:
    for line in f:
        if j != 0:
            sequence = line.split('\t')[-1]
            label = line.split('\t')[1]
            print(sequence)
            fout.write(label + '\t' + ' '.join([sequence[i:i+ng] for i in range(len(sequence)-ng)]) + '\n')
            # fout.write(' '.join([sequence[i:i+ng] for i in range(len(sequence)-ng+1)]) + '\n')
        j += 1
'''
with open(in_file) as f:
    for line in f:
        if (line.startswith('>') == False) and (any(x in line for x in spe_character) == False):
            sequence = ''.join(line).replace('\n','')
            print(sequence)
            fout.write(label + '\t' + ' '.join([sequence[i:i+ng] for i in range(len(sequence)-ng+1)]) + '\n')
            # fout.write(' '.join([sequence[i:i+ng] for i in range(len(sequence)-ng+1)]) + '\n')
'''
fout.close()
