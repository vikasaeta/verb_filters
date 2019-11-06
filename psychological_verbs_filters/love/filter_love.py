import random
import re
import nltk
import sys 
sys.path.insert(0,'..')
import filter_lines as fl


#filters out phrases like 'Sunny is a much loved figure in the campus community .'
def lovedAsNounModifyer(my_split, my_tokens, tagged_tokens):            
    if  (my_split[2].lower() == 'loved') and ((tagged_tokens[int(my_split[5])-2][1] in ['DT','PRP$','CC'] and (tagged_tokens[int(my_split[5])-1][1].startswith('RB') or tagged_tokens[int(my_split[5])-1][0].lower() in ['well','most','much'] ) and (tagged_tokens[int(my_split[5])+1][1].startswith(('NN','JJ')))) or tagged_tokens[int(my_split[5])+1][0].lower in ['one','ones']):        
        # print(my_split[7])
        return(True)  
    else:  
        return (False)

lineList = [line for line in open(r'results_love.tsv', 'r', encoding='utf-8')]

f = open(r"sample_love.tsv", "w",encoding='utf-8')

filtered_lines = []
for s in range (1,len(lineList)):
    my_split = lineList[s].split('\t')
    my_tokens = my_split[7].split(' ')
    tagged_tokens = nltk.pos_tag(my_tokens)
    formlist = ['love','loves']
    
    if not (fl.hasPattern(my_split[7],'\slove\slife') or lovedAsNounModifyer(my_split, my_tokens, tagged_tokens) or fl.isGerund (my_split) or fl.hasGerundAfter(my_split, my_tokens) or fl.isAdjectiveOrNoun(my_split, my_tokens, tagged_tokens, formlist) or fl.hasToAfterVerb(my_split, my_tokens) or (fl.hasPattern(my_split[7], "would\shave\sloved") and my_tokens[int(my_split[3])+1] == 'to')):
        filtered_lines.append(lineList[s])
    
    


sampleNumbers = random.sample(range(1, len(filtered_lines)), 100)
for s in range (len(filtered_lines)):
    if s in sampleNumbers:
        f.write(filtered_lines[s])
    
f.close()