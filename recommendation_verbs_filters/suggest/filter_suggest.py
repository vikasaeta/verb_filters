import random
import re
import nltk
import sys
sys.path.insert(0,'..')
import filter_lines as fl


#filters the sentences where the "dobj" is in reality the subject of a subordinate clause, e.g. "Although this page suggests the whole thing is a load of rubbish ."
def dobjIsSubj(my_tokens,tagged_tokens,my_split):    
    if len(my_tokens) > int(my_split[3])+1  and (tagged_tokens[int(my_split[3])+1][1].startswith('VB') or (tagged_tokens[int(my_split[3])+1][1].startswith('RB') and tagged_tokens[int(my_split[3])+2][1].startswith('VB'))):
        print(my_split[7])
        return (True)
    else:
        return (False)    
    
lineList = [line for line in open(r'results_suggest.tsv', 'r', encoding='utf-8')]

f = open(r"sample_suggest.tsv", "w",encoding='utf-8')

filtered_lines = []
for s in range (1,len(lineList)):
    my_split = lineList[s].split('\t')
    my_tokens = my_split[7].split(' ')
    tagged_tokens = nltk.pos_tag(my_tokens)
    formlist = ['suggested']
    
    if not (dobjIsSubj(my_tokens,tagged_tokens,my_split) or fl.hasSubjunctiveAfterDobj(my_tokens,tagged_tokens,my_split) or (fl.hasInfinitiveAfterDobj(my_tokens,tagged_tokens,my_split) and my_tokens[int(my_split[5])+1] not in ['a','an']) or fl.dobjIsGerund(my_split) or fl.isAdjective(my_split, my_tokens,tagged_tokens, formlist) or (fl.hasPattern(my_split[7].lower(), "suggest[^\s]+\sto\s") and tagged_tokens[int(my_split[5])+2][1].startswith('VB')) or fl.hasGerundAfter(my_split, my_tokens) or my_tokens[int(my_split[5])+1] == ','):
        filtered_lines.append(lineList[s])
    
 

sampleNumbers = random.sample(range(1, len(filtered_lines)), 100)
for s in range (len(filtered_lines)):
    if s in sampleNumbers:
        f.write(filtered_lines[s])
    
    
f.close()