import random
import re
import nltk
import sys
sys.path.insert(0,'..')
import filter_lines as fl

  
    
lineList = [line for line in open(r'results_miss.tsv', 'r', encoding='utf-8')]

f = open(r"sample_miss.tsv", "w",encoding='utf-8')

filtered_lines = []
for s in range (1,len(lineList)):
    my_split = lineList[s].split('\t')
    my_tokens = my_split[7].split(' ')
    tagged_tokens = nltk.pos_tag(my_tokens)
    formlist = ['missing','miss']
    
    if not (fl.dobjIsGerund(my_split) or fl.isAdjective(my_split, my_tokens,tagged_tokens, formlist) or fl.hasGerundAfter(my_split, my_tokens) or my_split[1] in ['target','fact','point','step','chance','call','opportunity','mark','issue'] or fl.isPhrasalVerb(my_split,tagged_tokens) or my_tokens[int(my_split[5])+1] == 'out' or fl.hasPattern(my_split[7], 'miss[^\s]*\s[^\s]*\s(target|call|opportunity|fact|point|step|chance|mark|issue)') or fl.hasPattern(my_split[7],'(go|went|gone|going)\smissing') or fl.isIntransitive(my_split,tagged_tokens)):    
        filtered_lines.append(lineList[s])
    
 

sampleNumbers = random.sample(range(1, len(filtered_lines)), 100)
for s in range (len(filtered_lines)):
    if s in sampleNumbers:
        f.write(filtered_lines[s])
    
    
f.close()