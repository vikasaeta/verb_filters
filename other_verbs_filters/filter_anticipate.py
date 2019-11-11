import random
import re
import nltk
import sys 
sys.path.insert(0,'..')
import filter_lines as fl
# import stanfordnlp
# stanfordnlp.download('en')   # This downloads the English models for the neural pipeline
# nlp = stanfordnlp.Pipeline() # This sets up a default neural pipeline in English
# doc = nlp("I want this man to leave .")
# doc.sentences[0].print_dependencies()
# pprint(vars(doc.sentences[0]))
# print(doc.sentences[0].words[6])


# def dep_lists(my_split):
    # print(my_split)
    # print(my_split[7])
    # doc = nlp(my_split[7])
    # dep_rels = []
    # governors = []
    # print (doc.sentences[0])
    # print(doc.sentences[0].words)
    # for word in doc.sentences[0].words:
        # dep_rels.append(word.dependency_relation)
        # governors.append(word.governor)
    # print(dep_rels)
    # print(governors)
    # return(dep_rels,governors)
    
    
# def verbHasXcomp(my_split):
    # want_index = int(my_split[5])+1
    # print(want_index)
    # dep_rels,governors = dep_lists(my_split)
    # if 'xcomp' in dep_rels[want_index:]:        
        # for x in range(want_index,len(dep_rels)):
            # if dep_rels[x] == 'xcomp' and governors[x] == want_index:
                # print(my_split[7])
                # return(True)
    # return(False)
        
    
    
# example = "47900868	article	wants	5	5	3	3	Our side only wants the article to reflect that ."
# my_split = example.split('\t')
# print(my_split)
# print(verbHasXcomp(my_split))
def dobjTooFarFromVerb(my_split):
    if int(my_split[3]) - int(my_split[5]) >=10:
        # print(my_split)
        return(True)
    else:
        return(False)

lineList = [line for line in open(r'results_anticipate.tsv', 'r', encoding='utf-8')]

f = open(r"sample_anticipate.tsv", "w",encoding='utf-8')

filtered_lines = []
for s in range (1,len(lineList)):
    my_split = lineList[s].split('\t')
    # my_split = my_split_orig[:3]+my_split_orig[4:8]+my_split_orig[10:]
    # print(my_split)
    my_tokens = my_split[7].split(' ')
    tagged_tokens = nltk.pos_tag(my_tokens)
    formlist = ['anticipated']
    
   
    # if not (fl.isGerund (my_split) or fl.hasGerundAfter(my_split, my_tokens)  or fl.isAdjectiveOrNoun(my_split, my_tokens, tagged_tokens, formlist) or fl.hasToAfterVerb(my_split, my_tokens) or (my_tokens[int(my_split[3])+1].lower() == 'to' and tagged_tokens[int(my_split[3])+2][1] == 'VB') or tagged_tokens[int(my_split[3])+1][1].startswith('VB') or tagged_tokens[int(my_split[5])+1][1].startswith('VB') or fl.isIntransitive(my_split,tagged_tokens) or (my_tokens[int(my_split[5])][0].isupper() and int(my_split[5]) > 0) or fl.hasPattern(my_split[7].lower(), "wanted\sposter")):
    if not (fl.dobjIsGerund (my_split) or fl.hasGerundAfter(my_split, my_tokens) or tagged_tokens[int(my_split[3])+1][1].startswith('VB') or fl.isAdjective(my_split, my_tokens, tagged_tokens, formlist) or fl.hasPattern(my_split[7].lower(), "\s(much|most)\santicipated")):
        # if not verbHasXcomp(my_split):
        # if not verbHasXcomp(my_split):
            filtered_lines.append(lineList[s])
    else:
        print(my_split[7])
    


sampleNumbers = random.sample(range(1, len(filtered_lines)), 100)
for s in range (len(filtered_lines)):
    if s in sampleNumbers:
        f.write(filtered_lines[s])
# n = 0
# sampled_numbers = []
# while n < 100:        
    # s = random.randint(1, len(filtered_lines))
    # if not s in sampled_numbers:
        # sampled_numbers.append(s)        
        # my_split_orig = filtered_lines[s].split('\t')
        # my_split = my_split_orig[:3]+my_split_orig[4:8]+my_split_orig[10:]
        # if not fl.verbHasXcomp(my_split):
                # f.write(filtered_lines[s]) 
                # n = n+1    
    
f.close()