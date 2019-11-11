import random
import re
import nltk
import sys 
sys.path.insert(0,'..')
import filter_lines as fl




lineList = [line for line in open(r'results_regret.tsv', 'r', encoding='utf-8')]

f = open(r"sample_regret.tsv", "w",encoding='utf-8')

filtered_lines = []
for s in range (1,len(lineList)):
    my_split = lineList[s].split('\t')
    my_tokens = my_split[7].split(' ')
    tagged_tokens = nltk.pos_tag(my_tokens)
    formlist = ['regret','regretted'] 
    
    if not (fl.isGerund (my_split) or fl.hasGerundAfter(my_split, my_tokens) or fl.isAdjectiveOrNoun(my_split, my_tokens, tagged_tokens, formlist) or fl.hasToAfterVerb(my_split, my_tokens)):
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