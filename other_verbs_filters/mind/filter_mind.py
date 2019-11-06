import random
import re
import nltk
import sys
sys.path.insert(0,'..')
import filter_lines as fl

  
def containsPattern(my_split):
    pattern_list = ["(bring|brought|call|cam|com|spr(i|a|u)ng)[a-z]*\sto\smind","never mind","\sin\smind","mind\s[a-z']+\sown\s","'\ss\smind","mind\s(read|control)", "mind\s(to|my|his|her|your|our|their)\s","mind a bit","mind you","mind \."]
    for pattern in pattern_list:
        if fl.hasPattern(my_split[7].lower(),pattern):
            
            return(True)
    return (False) 
 
lineList = [line for line in open(r'results_mind.tsv', 'r', encoding='utf-8')]

f = open(r"sample_mind.tsv", "w",encoding='utf-8')

filtered_lines = []
for s in range (1,len(lineList)):
    my_split = lineList[s].split('\t')
    my_tokens = my_split[7].split(' ')
    tagged_tokens = nltk.pos_tag(my_tokens)
    formlist = ['mind']
    
    
    if not (containsPattern(my_split) or fl.dobjIsGerund(my_split) or fl.hasGerundAfter(my_split, my_tokens) or my_tokens[int(my_split[3])+1].lower().endswith('ing')  or my_split[1].lower() in ('business','time') or fl.isAdjective(my_split, my_tokens,tagged_tokens, formlist) or fl.isIntransitive(my_split,tagged_tokens) or my_split[1].lower().endswith('ing')):    
        filtered_lines.append(lineList[s])
    
 

sampleNumbers = random.sample(range(1, len(filtered_lines)), 100)
for s in range (len(filtered_lines)):
    if s in sampleNumbers:
        f.write(filtered_lines[s])
    
    
f.close()