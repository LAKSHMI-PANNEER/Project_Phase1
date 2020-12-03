import requests
from bs4 import BeautifulSoup

url = "https://www.lifewire.com/how-to-edit-videos-on-android-4770052"

r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')

#print(soup.prettify())

for string in soup.stripped_strings:
    print(repr(string))









