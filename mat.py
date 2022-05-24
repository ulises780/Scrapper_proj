from unicodedata import name
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

# page = urlopen('https://www.pythonscraping.com/pages/warandpeace.html')
page = urlopen('http://www.pythonscraping.com/pages/page3.html')
file = soup(page.read(), 'html.parser')

print(file.h1)

# nameList= file.find_all('span', {'class': 'green', ''})
# for name in nameList:
#     print(name.get_text())

# p = file.find_all(['h1', 'h2', 'h3'])
# print(p)

# p = file.find_all('span', {'class': 'red'})
# for pp in p:
#     print(pp.get_text())

# prince = file.find_all(text= 'the prince')
# print(len(prince))

