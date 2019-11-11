import random
import re
import nltk
import sys 
sys.path.insert(0,'..')
import filter_lines as fl



lineList = [line for line in open(r'results_can_not_bear.tsv', 'r', encoding='utf-8')]

f = open(r"sample_can_not_bear.tsv", "w",encoding='utf-8')

filtered_lines = []
for s in range (1,len(lineList)):
    my_split_orig = lineList[s].split('\t')
    my_split = my_split_orig[:2]+my_split_orig[3:4]+my_split_orig[5:7]+my_split_orig[9:11]+my_split_orig[13:]
    
    my_tokens = my_split[7].split(' ')
    tagged_tokens = nltk.pos_tag(my_tokens)
    
    
    if not (fl.isGerund (my_split) or fl.hasGerundAfter(my_split, my_tokens) or fl.hasToAfterVerb(my_split, my_tokens) or my_split[1].lower() in ['fruit','child','relevance','witness','light'] or my_tokens[int(my_split[5])+1].lower() in ['off']):
        filtered_lines.append(lineList[s])
    
    
    


sampleNumbers = random.sample(range(1, len(filtered_lines)), 100)
for s in range (len(filtered_lines)):
    if s in sampleNumbers:
        f.write(filtered_lines[s])
        
 
    
f.close()