from inspect import Attribute
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from urllib.error import HTTPError
from urllib.error import URLError


# html = urlopen('http://pythonscraping.com/pages/page1.html')
# html = urlopen('https://en.wikipedia.org/wiki/Machine_learning')
# bs= BeautifulSoup(html.read(), 'html.parser')
# print(bs.h2)

# try:
#     html = urlopen('https://en.wikipedia.org/wiki/Artificial_intelligence')
# except HTTPError as e:
#     print('There was an error. Try again')
# else:
#     bs= BeautifulSoup(html.read(), 'html.parser')
#     print(bs.h1)

# try:
#     html = urlopen('https://www.pythonscrapingthisurldoesnotexist.com')
# except HTTPError as e:
#     print('There was an error. Try again')
# except URLError as e:
#     print('The server could not be found!')
# else:
#     bs= BeautifulSoup(html.read(), 'html.parser')
#     print(bs.h1)


# try:
#     badContent = bs.nonExistingTag.anotherTag
# except AttributeError as e:
#     print('Tag was not found')
# else:
#     if badContent == None:
#         print('tag was not found')
#     else:
#         print(badContent)

def tags(url):
    
    try:
        html= urlopen(url)
    except HTTPError as e:
        return None
    try:
        pp= bs(html.read(), 'html.parser')
        title = pp.h1
    except AttributeError as e:
        return None
    return title
    
title= tags('https://en.wikipedia.org/wiki/Artificial_intelligence')
if title == None:
    print('Title cannot be found')
else:
    print(title)