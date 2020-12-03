from bs4 import BeautifulSoup
import requests
import nltk
from nltk import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from collections import Counter

urls = ['https://support.google.com/photos/answer/6128838',
'https://support.google.com/photos/answer/6128843?co=GENIE.Platform%3DAndroid&hl=en',
'https://support.google.com/photos/answer/6128850',
'https://support.google.com/photos/answer/6128858?visit_id=637213412787536629-872446421&rd=1',
'https://support.google.com/photos/answer/6131416',
'https://support.google.com/photos/answer/6131416?visit_id=637176625396538486-1031873361&hl=en&rd=1&co=GENIE.Platform%3DDesktop',
'https://support.google.com/photos/answer/6153599?co=GENIE.Platform%3DAndroid&hl=en',
'https://support.google.com/photos/answer/6193313?co=GENIE.Platform%3DAndroid&hl=en&oco=0',
'https://support.google.com/photos/answer/6280921?hl=en',
'https://support.google.com/photos/answer/7362432',
'https://support.google.com/photos/answer/7378811?co=GENIE.Platform%3DAndroid&hl=en',
'https://support.google.com/photos/answer/7378942?hl=en&ref_topic=7378810&co=GENIE.Platform%3DAndroid',
'https://support.google.com/photos/answer/7539151?hl=en-GB&ref_topic=6128848',
'https://support.google.com/photos/answer/9284827?hl=en&ref_topic=6156061',
'https://support.google.com/photos/answer/9343965?hl=en',
'https://support.google.com/photos/answer/9380189?co=GENIE.Platform%3DAndroid&hl=en',
'https://support.google.com/photos/answer/9454489?hl=en-GB&ref_topic=6128848',
'https://support.google.com/photos/answer/9454489?hl=ur&ref_topic=6128848',
'https://support.google.com/photos/thread/29507038?hl=en',
'https://www.androidcentral.com/how-set-google-photos',
'https://www.lifewire.com/how-to-delete-google-photos-4690368',
'https://www.lifewire.com/how-to-transfer-photos-from-phone-to-computer-4173057',
'https://www.lifewire.com/how-to-frame-photo-like-polaroid-1701563',
'https://www.lifewire.com/how-to-retrieve-google-backup-photos-4690013',
'https://www.lifewire.com/recover-deleted-photos-on-android-4165361',
'https://www.lifewire.com/save-instagram-photos-4125398',
'https://www.wikihow.com/Assign-a-Photo-to-a-Contact-on-Your-Android-Phone'
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
