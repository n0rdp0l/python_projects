from os import link
from bitarray import test
from bs4 import BeautifulSoup
import requests
import pandas as pd

html_text = requests.get('https://www.imdb.com/chart/top/?ref_=nv_mv_250').text
soup = BeautifulSoup(html_text, 'lxml')
movies = soup.find_all('td', class_ = 'titleColumn')
names = []
links = []
for movie in movies:
    
    name = movie.find('a', href = True).text
    link =  movie.find('a', href = True)['href']

    names.append(name)
    links.append(link)

    print(f'''
    Movie Name: {name}
    Link: {"www.imdb.com" + link}
    ''')
zipped = list(zip(names, links))
df = pd.DataFrame(zipped, columns=['Name', 'Link'])
print(df)