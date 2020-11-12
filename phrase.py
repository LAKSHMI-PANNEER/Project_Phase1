import requests
from bs4 import BeautifulSoup
import re
import nltk
import string
from nltk import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

url ='https://support.google.com/edu/classroom/answer/7080036?hl=en&ref_topic=9050121'

reqs = requests.get(url)

soup = BeautifulSoup(reqs.text,'html.parser')

for tag in soup.find_all("ol"): 
    t=tag.text
    print(t)

#sentence
sentences = sent_tokenize(t)
print(sentences[0],"\n")

#words without punctuation
tokens = word_tokenize(t)
words = [word for word in tokens if word.isalpha()]
print(words[:100],"\n")

#removing stop words
stop_words = set(stopwords.words('english'))
words = [w for w in words if not w in stop_words]
print(words[:100])
