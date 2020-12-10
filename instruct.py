from bs4 import BeautifulSoup
import requests
import nltk
from nltk import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from collections import Counter
from nltk import Tree
import re

url = 'https://www.lifewire.com/how-to-edit-videos-on-android-4770052'
print("From URL:",url,"\n")
r = requests.get(url)
s = BeautifulSoup(r.content, 'html.parser')

ol_read = [tag.text for tag in s.find_all('ol')]
ol = [m+'' for m in ol_read]
ol_list = "".join(ol)
with open('D:\instructions.txt', 'w') as file:
    file.write(ol_list)

file = open("D:\instructions.txt").read()

sent = nltk.sent_tokenize(file)

ls=len(sent)
    
with open('D:\out.txt', 'w') as outfile:
    outfile.write("\n".join(sent))

with open('D:\out.txt', 'r') as outfile:
    o=outfile.readlines()
    
for i in range(len(o)):
    tokens = nltk.word_tokenize(o[i])
    words = [word for word in tokens if word.isalpha()]
    p=nltk.pos_tag(words)
    #print(p)
    nes = nltk.ne_chunk(p)
    #print(nes) 
    first_word = o[i].split()
    first = first_word[:2]
    #print(first)
    n=nltk.pos_tag(first)
    #print(n)

'''
op = list(filter(lambda x:x[1]=='VB',p))
print("Operations:",op,"\n")
obj = list(filter(lambda x:x[1]=='NN',p))
print("Objects:",obj,"\n")
'''
    
    for word, tag in n:
        if tag in ('VB'):
            i
            print (o[i])
            print("Line No-",i," => Instruction")
        else:
            i
            print (o[i])
            print("Line No-",i," => Not an Instruction")

