import random
import re
import nltk
import sys
sys.path.insert(0,'..')
import filter_lines as fl




lineList = [line for line in open(r'results_give_up.tsv', 'r', encoding='utf-8')]

f = open(r"sample_give_up.tsv", "w",encoding='utf-8')

filtered_lines = []
for s in range (1,len(lineList)):
    my_split = lineList[s].split('\t')    
    
    
    
    if not fl.hasPattern(my_split[10].lower(), "(giv|gav)[^\s]+\sup\s[^\s]+ing"):#like "Your doctor or pharmacist can help you to give up smoking ."
        filtered_lines.append(lineList[s])
    
    

sampleNumbers = random.sample(range(1, len(filtered_lines)), 100)
for s in range (len(filtered_lines)):
    if s in sampleNumbers:
        f.write(filtered_lines[s])
    
f.close()