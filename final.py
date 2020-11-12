import requests
from bs4 import BeautifulSoup
import nltk
from nltk import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

url = 'https://www.t-mobile.com/support/devices/mobile-internet/syncup-and-internet-of-things/using-your-timex-familyconnect-smartwatch-for-kids'
r = requests.get(url)
s = BeautifulSoup(r.content, 'html.parser')

"""prints whole html content"""
print(s.prettify())

"""prints whole text content w/o html tags"""
for string in s.stripped_strings:
    print(repr(string))

"""prints ordered list(instructions)"""
for tag in s.find_all('ol'): 
    print('{0}:{1}'.format(tag.name,tag.text))
    t=tag.text
    print(t)

"""stores instructions in txt file"""
ol_read = [tag.text for tag in s.find_all('ol')]
ol = [m+'' for m in ol_read]
ol_list = "".join(ol)
with open('D:\instructions.txt', 'w') as file:
    file.write(ol_list)

"""counts no of lines in txt file"""
count = len(open('D:\instructions.txt').readlines())
print(count)

file = open("D:\instructions.txt").read()

sentences = sent_tokenize(file)
print(sentences[0],"\n")

tokens = word_tokenize(file)
words = [word for word in tokens if word.isalpha()]
print(words,"\n")

stop_words = set(stopwords.words('english'))
words = [w for w in words if not w in stop_words]
print(words,"\n")

p=nltk.pos_tag(words) 
print(p)

