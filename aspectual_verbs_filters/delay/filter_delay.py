import random
import re
import nltk
import sys
sys.path.insert(0,'..')
import filter_lines as fl

# filers cases where the word "delayed" is an adjective like "It could be delayed onset muscle soreness ."
def delayedIsAdjective(my_split, my_tokens):
    if (my_split[2].lower() == 'delayed') and (my_tokens[int(my_split[5])+1] not in   ['the','a','an','this','that','these','those','my','your','his','her','its','our','their','much','many','most','some','any','enough','all','both','half','either','neither','each','every','other','another','such','one','until',',','.','further','by','construction','production','implementation','work','completion','due','because','for','to','in']) and (my_tokens[int(my_split[5])-1] not in ['which','they','he', 'she', 'it','we','who','further','war','War']) : 
        if (len(my_tokens) > int(my_split[5])+3) and not (my_tokens[int(my_split[5])+2] == "'" and my_tokens[int(my_split[5])+3] == 's'):
            if not my_tokens[int(my_split[5])+2] in ['until','for','by']:
                print(my_split[7])
                return(True)
    elif (my_split[2].lower() == 'delayed') and int(my_split[5]) == 0:
                print(my_split[7])
                return (True)
    return(False)
        

lineList = [line for line in open(r'results_delay.tsv', 'r', encoding='utf-8')]

f = open(r"sample_delay.tsv", "w",encoding='utf-8')

filtered_lines = []
for s in range (1,len(lineList)):
    my_split = lineList[s].split('\t')
    my_tokens = my_split[7].split(' ')
    tagged_tokens = nltk.pos_tag(my_tokens)
    formlist = ['delayed']
    
    if not (fl.isGerund(my_split) or fl.isAdjective(my_split, my_tokens,tagged_tokens, formlist) or fl.hasGerundAfter(my_split, my_tokens) or delayedIsAdjective(my_split, my_tokens)):
        filtered_lines.append(lineList[s])


sampleNumbers = random.sample(range(1, len(filtered_lines)), 100)
for s in range (len(filtered_lines)):
    if s in sampleNumbers:
        f.write(filtered_lines[s])
    
f.close()