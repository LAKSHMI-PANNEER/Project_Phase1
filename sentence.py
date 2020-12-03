import requests
from bs4 import BeautifulSoup
import nltk
from nltk import sent_tokenize

url = 'https://www.lifewire.com/how-to-edit-videos-on-android-4770052'
r = requests.get(url)
s = BeautifulSoup(r.content, 'html.parser')

"""
print(s.prettify())
for string in s.stripped_strings:
    print(repr(string))
"""

for tag in s.find_all('ol'): 
    t=tag.text
    print(t)
    
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
print("\n Number of instructions = ", count)
