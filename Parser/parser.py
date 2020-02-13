import requests
from bs4 import BeautifulSoup as BS 

r = requests.get('https://tlgrm.ru/channels/blogs')
html = BS(r.content, 'html.parser')

for el in html.select('.channel-card__info'):
	title = el.select('.channel-card__title > a')
	print (title[0].text )
