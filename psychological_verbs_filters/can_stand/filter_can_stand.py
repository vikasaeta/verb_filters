import random
import re
import nltk
import sys 
sys.path.insert(0,'..')
import filter_lines as fl



lineList = [line for line in open(r'results_can_stand.tsv', 'r', encoding='utf-8')]

f = open(r"sample_can_stand.tsv", "w",encoding='utf-8')

filtered_lines = []
for s in range (1,len(lineList)):
    my_split_orig = lineList[s].split('\t')
    my_split = my_split_orig[:3]+my_split_orig[4:8]+my_split_orig[10:]
    my_tokens = my_split[7].split(' ')
    tagged_tokens = nltk.pos_tag(my_tokens)
    
    
    if not (fl.isGerund (my_split) or fl.hasGerundAfter(my_split, my_tokens) or fl.hasToAfterVerb(my_split, my_tokens) or my_split[1] in ['ground','toe','shoulder'] or my_tokens[int(my_split[5])+1].lower() in ['upright','behind','on','and','up','out','in','by','against','at','between',',']):
        filtered_lines.append(lineList[s])
    else:
        print(my_split[7])
    
    



n = 0
sampled_numbers = []

while n < 100:        
    s = random.randint(1, len(filtered_lines)-1)
    if not s in sampled_numbers:
        # print(s)
        sampled_numbers.append(s)        
        my_split_orig = filtered_lines[s].split('\t')
        my_split = my_split_orig[:3]+my_split_orig[4:8]+my_split_orig[10:]
        if not fl.verbHasXcomp(my_split):
                f.write(filtered_lines[s]) 
                n = n+1            
    
f.close()