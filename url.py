import requests
from bs4 import BeautifulSoup

url ='https://support.google.com/edu/classroom/answer/7080036?hl=en&ref_topic=9050121'

reqs = requests.get(url)

soup = BeautifulSoup(reqs.text,'html.parser')

for tag in soup.find_all("ol"): 
    print("{0}: {1}".format(tag.name, tag.text))
    t=tag.text
    print(t)


