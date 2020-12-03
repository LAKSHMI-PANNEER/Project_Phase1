from bs4 import BeautifulSoup
import requests
import nltk
from nltk import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from collections import Counter

url = 'https://www.lifewire.com/how-to-edit-videos-on-android-4770052'
print("From URL:",url,"\n")
r = requests.get(url)
s = BeautifulSoup(r.content, 'html.parser')

'''
print(s.prettify())
for string in s.stripped_strings:
    print(repr(string))
for tag in s.find_all('ol'): 
    print('{0}:{1}'.format(tag.name,tag.text))
'''

ol_read = [tag.text for tag in s.find_all('ol')]
ol = [m+'' for m in ol_read]
ol_list = "".join(ol)
with open('D:\instructions.txt', 'w') as file:
    file.write(ol_list)

file = open("D:\instructions.txt").read()

sent = nltk.sent_tokenize(file)
print ("Instructions:",sent,"\n")
ls=len(sent)
print ("Number of Instructions =",ls,"\n")
    
with open('D:\out.txt', 'w') as outfile:
    outfile.write("\n".join(sent))
with open('D:\out.txt', 'r') as outfile:
    o=outfile.readlines()
    
for i in range(len(o)):
    print ("Line No-",i) 
    print (o[i])

file1 = open("D:\out.txt").read()

tokens = nltk.word_tokenize(file1)
words = [word for word in tokens if word.isalpha()]
print("\nTokens:",words,"\n")
lw=len(words)
print("Number of Tokens =",lw,"\n")

def avg():
    sentences = sent_tokenize(file)
    counts = (len(nltk.word_tokenize(sentence)) for sentence in sentences)
    return sum(counts)/float(len(sentences))
output = avg()
print("Average number of Tokens per Instruction = {:.2f}".format(output),"\n")

utokens=len(set(words))/float(len(words))
print("Lexical diversity =",utokens,"\n")

fd = nltk.FreqDist(words)
print("Frequency Distribution:")
print(fd,"\n")
    
'''
stop_words = set(stopwords.words('english'))
words = [w for w in words if not w in stop_words]
print(words,"\n")
'''

p=nltk.pos_tag(words) 
print("POS Tagging:",p,"\n")
tcounts = Counter(tag for word,tag in p)
print("Tags-Count:",tcounts,"\n")

print("Objects:")
for word, tag in p:
    if tag in ('NN'):
        print (word)
'''for word, tag in p:
    if tag in ('NNP'):
        print (word)'''
obj = list(filter(lambda x:x[1]=='NN',p))
lb=len(obj)
print("\nNumber of Objects =",lb,"\n")
out1=lb/lw
print("Average number of Objects per Instruction = {:.2f}".format(out1),"\n")

print("Operations:") 
for word, tag in p:
    if tag in ('VB'):
        print (word)
op = list(filter(lambda x:x[1]=='VB',p))
lp=len(op)
print("\nNumber of Operations =",lp,"\n")
out2=lp/lw
print("Average number of Operations per Instruction = {:.2f}".format(out2),"\n")
