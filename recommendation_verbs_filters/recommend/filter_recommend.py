import random
import re
import nltk
import sys
sys.path.insert(0,'..')
import filter_lines as fl


    
lineList = [line for line in open(r'results_recommend.tsv', 'r', encoding='utf-8')]

f = open(r"sample_recommend.tsv", "w",encoding='utf-8')

filtered_lines = []
for s in range (1,len(lineList)):
    my_split = lineList[s].split('\t')
    my_tokens = my_split[7].split(' ')
    tagged_tokens = nltk.pos_tag(my_tokens)
    formlist = ['recommended']
    
    if not (fl.hasSubjunctiveAfterDobj(my_tokens,tagged_tokens,my_split) or fl.hasInfinitiveAfterDobj(my_tokens,tagged_tokens,my_split) or fl.dobjIsGerund(my_split) or fl.isAdjective(my_split, my_tokens,tagged_tokens, formlist) or fl.hasPattern(my_split[7].lower(), "recommend[^\s]+\sto\s") or fl.hasGerundAfter(my_split, my_tokens) or (my_tokens[int(my_split[5])].lower() =='recommended' and (my_tokens[int(my_split[5])-1].lower() in ['maximum','CODATA','a','the'] or my_tokens[int(my_split[5])+1].lower() in ['practice','value']))):
        filtered_lines.append(lineList[s])
    


sampleNumbers = random.sample(range(1, len(filtered_lines)), 100)
for s in range (len(filtered_lines)):
    if s in sampleNumbers:
        f.write(filtered_lines[s])
    
    
f.close()