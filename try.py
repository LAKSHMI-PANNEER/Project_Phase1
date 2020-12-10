
import nltk
from nltk import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from collections import Counter

text = open("D:\out.txt", "r") 

sentences = nltk.sent_tokenize(text)                        
words = [nltk.word_tokenize(sent)for sent in sentences]    
tagged_sent = [nltk.pos_tag(sent)for sent in words]
nouns= []
for word,pos in tagged_sent:
    if pos in ['NN',"NNP"]:
        nouns.append(word)
freq_nouns=nltk.FreqDist(nouns)
print (freq_nouns)


