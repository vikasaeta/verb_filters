import random
import re
import nltk
import sys
sys.path.insert(0,'..')
import filter_lines as fl

#filters the cases where the "verb" is in reality an adjective (like "A Complete List of John Grisham ' s Books by Year .")
def completeIsAdjective(my_split, my_tokens, tagged_tokens, formlist):
    if  (my_split[2].lower() in formlist) and (tagged_tokens[int(my_split[5])-1][1] in ['PRP$'] or tagged_tokens[int(my_split[5])-1][0].lower() in ['a','the']):        
        print(my_split[7])
        return(True)
    else:
        return (False)
    
lineList = [line for line in open(r'results_complete.tsv', 'r', encoding='utf-8')]

f = open(r"sample_complete.tsv", "w",encoding='utf-8')

filtered_lines = []
for s in range (1,len(lineList)):
    my_split = lineList[s].split('\t')
    my_tokens = my_split[7].split(' ')
    tagged_tokens = nltk.pos_tag(my_tokens)
    formlist = ['complete']
    
    if not (fl.isGerund(my_split) or completeIsAdjective(my_split, my_tokens,tagged_tokens, formlist) or fl.hasGerundAfter(my_split, my_tokens) or fl.isIntransitive(my_split, tagged_tokens)):
        filtered_lines.append(lineList[s])


sampleNumbers = random.sample(range(1, len(filtered_lines)), 100)
for s in range (len(filtered_lines)):
    if s in sampleNumbers:
        f.write(filtered_lines[s])
    
f.close()