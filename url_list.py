from bs4 import BeautifulSoup
import requests
import nltk
from nltk import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from collections import Counter

urls = ['https://www.lifewire.com/android-file-transfer-any-device-4173383',
'https://www.lifewire.com/backup-android-phone-4177052',
'https://www.lifewire.com/block-text-messages-every-phone-and-carrier-4172380',
'https://www.lifewire.com/change-android-settings-4135692',
'https://www.lifewire.com/change-google-assistant-voice-4169323',
'https://www.lifewire.com/changing-android-ringtone-1616828',
'https://www.lifewire.com/check-updates-for-android-1616953',
'https://www.lifewire.com/clear-cache-android-4157780',
'https://www.lifewire.com/close-apps-on-android-4164116'
]

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
    print("7. Average number of Operations per Instruction = {:.2f}".format(out1),"\n")

    obj = list(filter(lambda x:x[1]=='NN',p))
    #print("Objects:",obj,"\n")
    lb=len(obj)
    print("8. Number of Objects =",lb,"\n")
    out1=lb/lw
    print("9. Average number of Objects per Instruction = {:.2f}".format(out1),"\n")

    print("-------------------------------------------------------")
