from os import link
from bitarray import test
from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.imdb.com/chart/top/?ref_=nv_mv_250').text
soup = BeautifulSoup(html_text, 'lxml')
movies = soup.find_all('td', class_ = 'titleColumn')
for movie in movies:
    name = [a.text for a in movie.find_all('a', href = True)]
    link = [a['href'] for a in movie.find_all('a', href = True)]
    print(link)
    print(name)
