import random
import re
import nltk
import sys 
sys.path.insert(0,'..')
import filter_lines as fl




lineList = [line for line in open(r'results_fancy.tsv', 'r', encoding='utf-8')]

f = open(r"sample_fancy.tsv", "w",encoding='utf-8')

filtered_lines = []
for s in range (1,len(lineList)):
    my_split = lineList[s].split('\t')
    my_tokens = my_split[7].split(' ')
    tagged_tokens = nltk.pos_tag(my_tokens)
    formlist = ['fancied','fancy','fancies']
    
    
    if not (fl.isGerund (my_split) or fl.hasGerundAfter(my_split, my_tokens) or fl.isAdjectiveOrNoun(my_split, my_tokens, tagged_tokens, formlist) or fl.isPhrasalVerb(my_split,tagged_tokens) or my_tokens[int(my_split[3])+1].lower() == 'to' or my_tokens[int(my_split[5])+1].lower() == 'up' or fl.hasPattern(my_split[7], "too\sfancy")):
        filtered_lines.append(lineList[s])
    
    


sampleNumbers = random.sample(range(1, len(filtered_lines)), 50)
for s in range (len(filtered_lines)):
    if s in sampleNumbers:
        f.write(filtered_lines[s])
    
f.close()