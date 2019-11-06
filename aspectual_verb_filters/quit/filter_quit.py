import random
import re
import nltk
import sys
sys.path.insert(0,'..')
import filter_lines as fl

lineList = [line for line in open(r'results_quit.tsv', 'r', encoding='utf-8')]

f = open(r"sample_quit.tsv", "w",encoding='utf-8')

filtered_lines = []
for s in range (1,len(lineList)):
    my_split = lineList[s].split('\t')
    my_tokens = my_split[7].split(' ')
    tagged_tokens = nltk.pos_tag(my_tokens)
    formlist = ['quit']
    
    if not (fl.isGerund(my_split) or fl.isAdjective(my_split, my_tokens,tagged_tokens, formlist) or fl.isIntransitive(my_split, tagged_tokens) or fl.hasGerundAfter(my_split, my_tokens) or fl.isPhrasalVerb(my_split, tagged_tokens) or fl.hasPattern(my_split[7].lower(), ' (a|the)[^a-zA-Z]*quit')):
        filtered_lines.append(lineList[s])


sampleNumbers = random.sample(range(1, len(filtered_lines)), 100)
for s in range (len(filtered_lines)):
    if s in sampleNumbers:
        f.write(filtered_lines[s])
    
f.close()