# -*- coding: utf-8 -*-
import random
import re
import nltk
import stanfordnlp
stanfordnlp.download('en')   # This downloads the English models for the neural pipeline
nlp = stanfordnlp.Pipeline() # This sets up a default neural pipeline in English

#builds lists of dependency relations and governers of the tokens in the sentence
def dep_lists(my_split):    
    doc = nlp(my_split[7])
    dep_rels = []
    governors = []    
    for word in doc.sentences[0].words:
        dep_rels.append(word.dependency_relation)
        governors.append(word.governor)    
    return(dep_rels,governors)
    
#filters cases like "I want him to go ."    
def verbHasXcomp(my_split):
    want_index = int(my_split[5])+1    
    dep_rels,governors = dep_lists(my_split)
    if 'xcomp' in dep_rels[want_index:]:        
        for x in range(want_index,len(dep_rels)):
            if dep_rels[x] == 'xcomp' and governors[x] == want_index:
                print(my_split[7])
                return(True)
    return(False)

# filters the cases where the "dobj" is in reality a gerund, e.g. "And Isaac pitched his tent there and his servants began digging a well ."
def isGerund(my_split):
    if(my_split[1].endswith('ing') and (my_split[1].lower() not in ['everything','anything','something','nothing'])and (int(my_split[3]) - int(my_split[5]) == 1)):        
        return(True)
    else:        
        return(False)
# filters the cases where the verb is followed by 'to + infinitive'        
def hasToAfterVerb(my_split, my_tokens):
    if my_tokens[int(my_split[5])+1] == 'to':    
        return(True)
    else:
        return(False)
#filters the cases  where the sentence contains a certain pattern (can be used for filtering different sorts of parsing errors). For example, hasPattern(my_split[7].lower(), "start[^\s]+\sto\s") filters out things like "Then they continued north")    
def hasPattern(string, pattern):
    my_pattern = re.compile(pattern)    
    if my_pattern.search(string):
        return(True)
    else:
        return(False)
        
#filters the cases where the "verb" is in reality an adjective (or a noun), e.g. "In 1926 , the discovery of oil <...> helped spur the city ' s continuing growth ."
def isAdjectiveOrNoun(my_split, my_tokens, tagged_tokens, formlist):    
          
    if  (my_split[2].lower() in formlist) and (tagged_tokens[int(my_split[5])-1][1] in ['DT','PRP$','JJ','JJR','JJS']):        
        
        return(True)  
    elif  (my_split[2].lower() in formlist) and (int(my_split[5]) > 2) and my_tokens[int(my_split[5])-2] == "'" and my_tokens[int(my_split[5])-1] == 's':        
        
        return(True)  
    elif (my_split[2].lower() in formlist) and (tagged_tokens[int(my_split[5])][1].startswith('NN')):
        
        return(True)  
    return (False)

#filters the cases where the verb is intransitive, and therefore the "dobj" is wrong  (e.g. "The former editor-in-chief of the magazine quit because of Berm u dez ' s behaviour")  
def isIntransitive(my_split,tagged_tokens):
    if int(my_split[5])-int(my_split[3])<0 and (tagged_tokens[int(my_split[5])+1][1] in ['IN','RP'] or tagged_tokens[int(my_split[5])+1][0] in [',','.']):            
        return(True)    
    else:
        return (False)
#filters the cases where the verb is followed by a gerund, e.g. "they would discontinue distributing newscasts from CNN Radio".        
def hasGerundAfter (my_split, my_tokens):
    if (my_tokens[int(my_split[5])+1].endswith('ing') and (my_tokens[int(my_split[5])+1].lower() not in ['everything','anything','something','nothing'])):        
        return(True)
    else:
        return (False)
#filters the cases where the verb is in reality a phrasal verb (and not the one we are looking for), e.g. "the Draka nation started off as a British settler colony"       
def isPhrasalVerb(my_split,tagged_tokens):
    if len(tagged_tokens) > (int(my_split[5])+1) and int(my_split[5])-int(my_split[3])>0 and (tagged_tokens[int(my_split[5])+1][1] in ['RP']):            
        return(True)    
    else:
        return (False)
#filters the cases where the verb is followed by an ordinal number (like "Newport improved in the second half of the season to finish tenth in the league .")        
def hasOrdNumAfter(my_split, tagged_tokens):
    if ((tagged_tokens[int(my_split[5]) +1][1]=='CD' and tagged_tokens[int(my_split[5]) +1][0].endswith(('st','nd','rd'))) or tagged_tokens[int(my_split[5]) +1][0] in ['first','second','third','fourth','fifth','sixth','seventh','eighth','ninth','tenth','eleventh','twelfth','thirteenth','fourteenth','fifteenth','sixteenth','seventeenth','eighteenth','nineteenth','twentieth'])and not tagged_tokens[int(my_split[5]) +2][1].startswith(('NN','JJ')):         
        return(True)
    else:
        return(False)
#filters the cases where the "dobj" is in reality an xcomp in the form of an ordinal number (like "the team managing to finish only tenth")      
def dobjIsOrdinalNumber(my_split, tagged_tokens):
    if ((tagged_tokens[int(my_split[3])][1]=='CD' and tagged_tokens[int(my_split[3])][0].endswith(('st','nd','rd'))) or (tagged_tokens[int(my_split[3])][0] in ['first','second','third','fourth','fifth','sixth','seventh','eighth','ninth','tenth','eleventh','twelfth','thirteenth','fourteenth','fifteenth','sixteenth','seventeenth','eighteenth','nineteenth','twentieth'])) and (tagged_tokens[int(my_split[5]) +1][1] not in ['DT','PRP$']):         
        return(True)
    else:
        return(False)
        
def dobjTooFarFromVerb(my_split):
    if int(my_split[3]) - int(my_split[5]) >=10:        
        return(True)
    else:
        return(False)