from bs4 import BeautifulSoup
import requests
import nltk
from nltk import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from collections import Counter

urls = [
'https://support.google.com/chrome/a/answer/7131624',
'https://support.google.com/chrome/a/answer/9490493?hl=en&ref_topic=4386754',
'https://support.google.com/chrome/answer/114662?hl=en&co=GENIE.Platform=Android',
'https://support.google.com/chrome/answer/114662?hl=en-GB&co=GENIE.Platform%3DAndroid',
'https://support.google.com/chrome/answer/95759?co=GENIE.Platform%3DAndroid&oco=1',
'https://support.google.com/chrome/answer/1385029?hl=en-GB&co=GENIE.Platform%3DAndroid',
'https://support.google.com/chrome/answer/142065',
'https://support.google.com/chrome/answer/142065?hl=en-GB&ref_topic=7437824',
'https://support.google.com/chrome/answer/142893?hl=en&co=GENIE.Platform%3DAndroid',
'https://support.google.com/chrome/answer/173424?hl=en&ref_topic=7439724&co=GENIE.Platform%3DAndroid',
'https://support.google.com/chrome/answer/185277?co=GENIE&co=GENIE.Platform%3DAndroid&hl=en',
'https://support.google.com/chrome/answer/2391819?co=GENIE.Platform%3DAndroid',
'https://support.google.com/chrome/answer/2392284?hl=bn',
'https://support.google.com/chrome/answer/2392709?co=GENIE.Platform%3DAndroid&hl=en',
'https://support.google.com/chrome/answer/2392709?co=GENIE.Platform%3DAndroid&hl=en-GB',
'https://support.google.com/chrome/answer/2765944?co=GENIE.Platform%3DAndroid&hl=en',
'https://support.google.com/chrome/answer/2765944?hl=en-gb&co=GENIE.Platform%3DAndroid',
'https://support.google.com/chrome/answer/2790761?co=GENIE.Platform%253DAndroid&hl=en',
'https://support.google.com/chrome/answer/3220216?co=GENIE...hl=en&co=GENIE.Platform%3DAndroid&hl=en',
'https://support.google.com/chrome/answer/6204307',
'https://support.google.com/chrome/answer/6362090?hl=en&ref_topic=7437724',
'https://support.google.com/chrome/answer/7440301?co=GENIE.Platform%3DAndroid&hl=en',
'https://support.google.com/chrome/answer/9281740?hl=en-EN&ref_topic=7437824&co=GENIE.Platform%3DAndroid',
'https://support.google.com/chrome/answer/95346?hl=en&ref_topic=14660&visit_id=637176604000229475-3948958844&rd=1&co=GENIE.Platform%3DAndroid',
'https://support.google.com/chrome/answer/95414?co=GENIE.Platform%3DAndroid&hl=en',
'https://support.google.com/chrome/answer/95417?co=GENIE.Platform%3DAndroid&hl=en',
'https://support.google.com/chrome/answer/95464?hl=is&co=GENIE.Platform%3DAndroid',
'https://support.google.com/chrome/answer/95589',
'https://support.google.com/chrome/answer/95647?%20hl=fr&hlrm=en&co=GENIE.Platform%3DAndroid',
'https://support.google.com/chrome/a/answer/1360534',
'https://support.google.com/chrome/a/answer/3523633?hl=en&ref_topic=2935995'
]

print("Task Category: CHROME")
print("Number of URLs:",len(urls),"\n")

for url in urls:
    print("From URL:",url,"\n")
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "lxml")
    text = [tag.text for tag in soup.find_all("ol")]
    #print("\n",text,"\n")

    ol_read = [tag.text for tag in soup.find_all('ol')]
    ol = [m+'' for m in ol_read]
    ol_list = "".join(ol)
    with open('D:\instructions.txt', 'w') as file:
        file.write(ol_list)

    file = open("D:\instructions.txt").read()
    
    sent = nltk.sent_tokenize(file)
    #print ("Instructions:",sent,"\n")
    ls=len(sent)
    print ("1. Number of Instructions =",ls,"\n")
        
    with open('D:\out.txt', 'w') as outfile:
        outfile.write("\n".join(sent))
        
    file1 = open("D:\out.txt").read()

    tokens = nltk.word_tokenize(file1)
    words = [word for word in tokens if word.isalpha()]
    #print("Tokens:",words,"\n")
    lw=len(words)
    print("2. Number of Tokens =",lw,"\n")

    def avg():
        sentences = sent_tokenize(file)
        counts = (len(nltk.word_tokenize(sentence)) for sentence in sentences)
        return sum(counts)/float(len(sentences))
    output = avg()
    print("3. Average number of Tokens per Instruction = {:.2f}".format(output),"\n")

    utokens=len(set(words))/float(len(words))
    print("4. Lexical diversity =",utokens,"\n")

    fd = nltk.FreqDist(words)
    print("5. Frequency Distribution:")
    print(fd,"\n")

    p=nltk.pos_tag(words) 
    #print("POS Tagging:",p,"\n")
    
    op = list(filter(lambda x:x[1]=='VB',p))
    #print("Operations:",op,"\n")
    lp=len(op)
    print("6. Number of Operations =",lp,"\n")
    out1=lp/lw
    print("7. Average number of Operations = {:.2f}".format(out1),"\n")

    obj = list(filter(lambda x:x[1]=='NN',p))
    #print("Objects:",obj,"\n")
    lb=len(obj)
    print("8. Number of Objects =",lb,"\n")
    out1=lb/lw
    print("9. Average number of Objects = {:.2f}".format(out1),"\n")

    print("-------------------------------------------------------")
