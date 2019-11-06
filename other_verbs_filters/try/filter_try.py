import random
import re
import nltk
import sys
sys.path.insert(0,'..')
import filter_lines as fl

def dobjIsGerund(my_split):
    if(my_split[1].endswith('ing') and (my_split[1].lower() not in ['everything','anything','something','nothing'])):        
        return(True)
    else:        
        return(False)
        
def dobjTooFarFromVerb(my_split):
    if int(my_split[3]) - int(my_split[5]) >=10:
        
        return(True)
    else:
        return(False)
        
lineList = [line for line in open(r'results_try.tsv', 'r', encoding='utf-8')]

f = open(r"sample_try.tsv", "w",encoding='utf-8')

filtered_lines = []
for s in range (1,len(lineList)):
    my_split = lineList[s].split('\t')
    my_tokens = my_split[7].split(' ')
    tagged_tokens = nltk.pos_tag(my_tokens)
    formlist = ['tried','try','trying','tries']
    
    if not (my_split[2][0].isupper() or dobjTooFarFromVerb(my_split) or dobjIsGerund(my_split) or fl.hasPattern(my_split[7].lower(), "tr(i|y)[^\s]*\s(to|and)\s") or fl.hasGerundAfter(my_split, my_tokens) or fl.isAdjective(my_split, my_tokens,tagged_tokens, formlist) or fl.isPhrasalVerb(my_split,tagged_tokens) or fl.hasPattern(my_split[7], '\str(y|i)[^\s]*\s[^\s]*\s(luck|hand|best|while|lot|fortune|patience)\s') or my_tokens[int(my_split[5])+1] in ['out','again'] or my_split[1] in ['case','time','lot','fortune','day','year','patience','hand'] or tagged_tokens[int(my_split[3])+1][1] == 'RP' or tagged_tokens[int(my_split[5])+1][1].startswith('VB') or fl.isIntransitive(my_split,tagged_tokens) or 'Try Tag Rugby' in my_split[7]):
        filtered_lines.append(lineList[s])
    


sampleNumbers = random.sample(range(1, len(filtered_lines)), 100)
for s in range (len(filtered_lines)):
    if s in sampleNumbers:
        f.write(filtered_lines[s])
    
f.close()