import requests
from bs4 import BeautifulSoup

url = "https://support.google.com/plus/answer/6320398?co=GENIE.Platform%3DAndroid&hl=en"
r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')

#print(soup.prettify())
#print(soup.find_all('div'))

#s=soup.find('ol').get_text()

#print(s.prettify())
#print(s)

for string in soup.stripped_strings:
    print(repr(string))









