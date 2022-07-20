from bitarray import test
from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.imdb.com/chart/top/?ref_=nv_mv_250').text
soup = BeautifulSoup(html_text, 'lxml')
movies = soup.find_all('td', class_ = 'titleColumn')
link = movies.find('a')
print(link)