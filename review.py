import requests
from bs4 import BeautifulSoup
import nltk
from nltk import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
#from textblob import TextBlob

url = 'https://www.lifewire.com/how-to-edit-videos-on-android-4770052'
r = requests.get(url)
s = BeautifulSoup(r.content, 'html.parser')

"""
print(s.prettify())
for string in s.stripped_strings:
    print(repr(string))
"""

for tag in s.find_all('ol'): 
    #print('{0}:{1}'.format(tag.name,tag.text))
    t=tag.text
    #print(t)

ol_read = [tag.text for tag in s.find_all('ol')]
ol = [m+'' for m in ol_read]
ol_list = "".join(ol)
with open('D:\instruction.txt', 'w') as file:
    file.write(ol_list)

file = open("D:\instruction.txt").read()

tokens = nltk.sent_tokenize(file)
print (tokens)

with open('D:\outfile.txt', 'w') as outfile:
    outfile.write("\n".join(tokens))

count = len(open('D:\outfile.txt').readlines())
print("\n Number of lines:",count,"\n")

file = open("D:\outfile.txt").read()

tokens = word_tokenize(file)
words = [word for word in tokens if word.isalpha()]
print(words,"\n")

'''stop_words = set(stopwords.words('english'))
words = [w for w in words if not w in stop_words]
print(words,"\n")'''

p=nltk.pos_tag(words) 
print(p,"\n")

for word, tag in p:
    if tag in ('NN'):
        print (word, tag)

for word, tag in p:
    if tag in ('NNP'):
        print (word, tag)

for word, tag in p:
    if tag in ('VB'):
        print (word, tag)

