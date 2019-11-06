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
        

        
def beConsidered(my_split, my_tokens):
    if (my_tokens[int(my_split[5])-1].lower() in ['be','was','were','been','am','are','is','being'] or (my_tokens[int(my_split[5])-1].lower() in ['m','s','re'] and my_tokens[int(my_split[5])-2].lower() == "'") or (my_tokens[int(my_split[5])-2].lower() in ['m','s','re','be','was','were','been','am','are','is','being'] and (my_tokens[int(my_split[5])-1].lower() == "not" or tagged_tokens[int(my_split[5])-1][1].startswith('RB'))))and my_split[2].lower() == 'considered':        
        return(True)
    else:
        return False
        
def containsPattern(my_split):
    pattern_list = ["consider[a-z]*\s(this|these|that|those|them|him|her|us|me|you|it)\s(a|an|the)\s","(what|which|whom)\s[a-zA-Z\s-]+\sconsider[^\s]*\s","consider[^\s]*\s[^\s]*(self|selves)","consider[a-zA-Z\s'-]*(to\s[a-zA-Z]*\s*be\s|\sas\s)","(ly|often|although|always|sometimes|,)\sconsidered","consider[a-z]* ``"]
    for pattern in pattern_list:
        if fl.hasPattern(my_split[7].lower(),pattern):            
            return(True)
    return (False)


    
lineList = [line for line in open(r'results_consider.tsv', 'r', encoding='utf-8')]

f = open(r"sample_consider1.tsv", "w",encoding='utf-8')

filtered_lines = []
for s in range (1,len(lineList)):
    my_split = lineList[s].split('\t')
    my_tokens = my_split[7].split(' ')
    tagged_tokens = nltk.pos_tag(my_tokens)
    formlist = ['considered']
    
 
    if not (containsPattern(my_split) or dobjIsGerund(my_split) or fl.hasGerundAfter(my_split, my_tokens) or beConsidered(my_split, my_tokens) or (my_tokens[int(my_split[5])+1].lower() == 'that' and tagged_tokens[int(my_split[5])+1][1] == 'IN') or fl.isAdjective(my_split, my_tokens,tagged_tokens, formlist) or my_split[2] in ['Considered'] or tagged_tokens[int(my_split[3])+1][1].startswith(('JJ','DT','VBN')) or (tagged_tokens[int(my_split[3])+1][1].startswith('RB') and tagged_tokens[int(my_split[3])+2][1].startswith(('JJ','VBN'))) or (not tagged_tokens[int(my_split[3])][1].startswith('NN')) or my_split[5] == "0" or my_split[1].lower() in ['matter','fact','possibility','issue','idea']):
        
        filtered_lines.append(lineList[s])
    


sampleNumbers = random.sample(range(1, len(filtered_lines)), 100)
for s in range (len(filtered_lines)):
    if s in sampleNumbers:
        f.write(filtered_lines[s])
    
f.close()

