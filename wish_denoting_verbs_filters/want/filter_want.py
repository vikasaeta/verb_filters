import random
import re
import nltk
import sys 
sys.path.insert(0,'..')
import filter_lines as fl


lineList = [line for line in open(r'results_want.tsv', 'r', encoding='utf-8')]

f = open(r"sample_want.tsv", "w",encoding='utf-8')

filtered_lines = []
for s in range (1,len(lineList)):
    my_split = lineList[s].split('\t')
    my_tokens = my_split[7].split(' ')
    tagged_tokens = nltk.pos_tag(my_tokens)
    formlist = ['want','wanted']
    
    
    if not (fl.isGerund (my_split) or fl.hasGerundAfter(my_split, my_tokens)  or fl.isAdjectiveOrNoun(my_split, my_tokens, tagged_tokens, formlist) or fl.hasToAfterVerb(my_split, my_tokens) or (my_tokens[int(my_split[3])+1].lower() == 'to' and tagged_tokens[int(my_split[3])+2][1] == 'VB') or tagged_tokens[int(my_split[3])+1][1].startswith('VB') or tagged_tokens[int(my_split[5])+1][1].startswith('VB') or fl.isIntransitive(my_split,tagged_tokens) or (my_tokens[int(my_split[5])][0].isupper() and int(my_split[5]) > 0) or fl.hasPattern(my_split[7].lower(), "wanted\sposter")):
        
            filtered_lines.append(lineList[s])
    
    



n = 0
sampled_numbers = []
while n < 100:        
    s = random.randint(1, len(filtered_lines))
    if not s in sampled_numbers:
        sampled_numbers.append(s)        
        my_split = filtered_lines[s].split('\t')
        if not fl.verbHasXcomp(my_split):
                f.write(filtered_lines[s]) 
                n = n+1    
    
f.close()