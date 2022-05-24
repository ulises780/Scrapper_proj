from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
# from urllib.error import HTTPError

# html = urlopen('https://en.wikipedia.org/wiki/One_Piece')
html = urlopen('https://www.pythonscraping.com/pages/page3.html')

bs= soup(html, 'html.parser')


footer= bs.find_all(['div'])
print(footer[2])

# for child in bs.find('table', {'id': 'giftList'}).children:
#     print(child)


# for descendant in bs.find('table', {'id': 'giftList'}).descendants:
#     print(descendant)

# for sibling in bs.find({'table': 'giftList'}).tr.next_siblings:
#     print(sibling)