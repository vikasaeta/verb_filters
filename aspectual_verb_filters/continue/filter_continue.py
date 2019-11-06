import random
import re
import nltk
import sys
sys.path.insert(0,'..')
import filter_lines as fl


# filters the cases where the verb continue is intransitive. like "At this point , the route continues southeast through more woods before heading into farmland and turning south ."
def continueIsIntransitive(my_split,tagged_tokens):    
   if (fl.isIntransitive(my_split,tagged_tokens) and tagged_tokens[int(my_split[5])+1][0] != 'that') or tagged_tokens[int(my_split[5])-1][0] == 'road':
        return(True)
   elif fl.hasPattern(my_split[7].lower(),'continu[a-z]+\s[a-z]*(west|east|north|south)[a-z]*\s'):
        print(my_split[7])
        return (True)
   else:
        return (False)
        

lineList = [line for line in open(r'results_continue.tsv', 'r', encoding='utf-8')]

f = open(r"sample_continue.tsv", "w",encoding='utf-8')

filtered_lines = []
for s in range (1,len(lineList)):
    my_split = lineList[s].split('\t')
    my_tokens = my_split[7].split(' ')
    tagged_tokens = nltk.pos_tag(my_tokens)
    formlist = ['continued','continuing']
    
    if not (fl.isGerund(my_split) or fl.isAdjective(my_split, my_tokens,tagged_tokens, formlist) or continueIsIntransitive(my_split, tagged_tokens) or fl.hasPattern(my_split[7].lower(), "continu[^\s]+\sto\s") or fl.hasGerundAfter(my_split, my_tokens) or fl.isPhrasalVerb(my_split, tagged_tokens)):
        filtered_lines.append(lineList[s])


sampleNumbers = random.sample(range(1, len(filtered_lines)), 100)
for s in range (len(filtered_lines)):
    if s in sampleNumbers:
        f.write(filtered_lines[s])
    
f.close()