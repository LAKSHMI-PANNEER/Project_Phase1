import nltk
from nltk import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

file = open("D:\instruction.txt").read()

tokens = word_tokenize(file)
words = [word for word in tokens if word.isalpha()]
print(words,"\n")

'''
stop_words = set(stopwords.words('english'))
words = [w for w in words if not w in stop_words]
print(words,"\n")
'''

p=nltk.pos_tag(words) 
#print(p)

op = list(filter(lambda x:x[1]=='VB',p))
print(op,"\n")

obj = list(filter(lambda x:x[1]=='NN',p))
print(obj)
