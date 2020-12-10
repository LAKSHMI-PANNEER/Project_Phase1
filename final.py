from bs4 import BeautifulSoup
import requests
import nltk
from nltk import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter

#url scrapping
url = 'https://www.lifewire.com/how-to-edit-videos-on-android-4770052'
print("From URL:",url,"\n")
r = requests.get(url)
s = BeautifulSoup(r.content, 'html.parser')
print(s.prettify())
for string in s.stripped_strings:
    print(repr(string))
for tag in s.find_all('ol'): 
    print('{0}:{1}'.format(tag.name,tag.text))

ol_read = [tag.text for tag in s.find_all('ol')]
ol = [m+'' for m in ol_read]
ol_list = "".join(ol)
with open('D:\instructions.txt', 'w') as file:
    file.write(ol_list)

#instructions-count
file = open("D:\instructions.txt").read()
sent = nltk.sent_tokenize(file)
print ("Instructions:",sent,"\n")
ls=len(sent)
print ("Number of Instructions =",ls,"\n")

with open('D:\out.txt', 'w') as outfile:
    outfile.write("\n".join(sent))

#words-count
file1 = open("D:\out.txt").read()
tokens = nltk.word_tokenize(file1)
words = [word for word in tokens if word.isalpha()]
print("Tokens:",words,"\n")
lw=len(words)
print("Number of Words =",lw,"\n")
def avg():
    sentences = sent_tokenize(file)
    counts = (len(nltk.word_tokenize(sentence)) for sentence in sentences)
    return sum(counts)/float(len(sentences))
output = avg()
print("Average number of Words per Instruction = {:.2f}".format(output),"\n")

#instruction or not
with open('D:\out.txt', 'r') as outfile:
    o=outfile.readlines()    
for i in range(len(o)):
    tokens = nltk.word_tokenize(o[i])
    words = [word for word in tokens if word.isalpha()]
    p=nltk.pos_tag(words)
    first_word = o[i].split()
    first = first_word[:1]
    n=nltk.pos_tag(first)
    
    for word, tag in n:
        if tag in ('VB'):
            i
            print (o[i])
            print("Line No-",i," => Instruction")
        else:
            i
            print (o[i])
            print("Line No-",i," => Not an Instruction")

#verbs and nouns
p=nltk.pos_tag(words) 
print("POS Tagging:",p,"\n")
tcounts = Counter(tag for word,tag in p)
print("Tags-Count:",tcounts,"\n")

obj = list(filter(lambda x:x[1]=='NN',p))
print("Objects:",obj,"\n")
lb=len(obj)
print("Number of Objects =",lb,"\n")

op = list(filter(lambda x:x[1]=='VB',p))
print("Operations:",op,"\n")
lp=len(op)
print("Number of Operations =",lp,"\n")

tp=573
fp=427
fn=0
    
p=tp/(tp+fp)
print("Precision = ",p)

r=tp/(tp+fn)
print("Recall = ",r)

f=(2*p*r)/(p+r)
print("F1 score = ",f)    

