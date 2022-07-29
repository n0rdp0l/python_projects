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

    
zipped = list(zip(names, links))
df = pd.DataFrame(zipped, columns=['Name', 'Link'])

age = ["all","sub18","18-29","30-44","44+"]
gender = ["_m", "_f"]
colnames = age
colnames.extend([i+gender[0] for i in age])
colnames.extend([i+gender[1] for i in age[:5]])
colnames.extend(["top_1000", "US", "non_US"])

Ratings_df = pd.DataFrame(columns=colnames)
Voters_df = pd.DataFrame(columns=colnames)

for name, link in zip(movie_links['Name'], movie_links['Link']):
    html = requests.get('https://www.imdb.com' + link + "ratings/").text
    soup2 = BeautifulSoup(html, 'lxml')


    grid =  soup2.find_all('td', class_ = 'ratingTable') 
    ratings = []
    voters = []
    for cell in grid:

        rating = cell.find('div', class_ = 'bigcell').text.replace(' ','')
        voter = cell.find('a', href = True).text.replace(' ','').replace('\n', '')

        ratings.append(rating)
        voters.append(voter) 

    r_temp = pd.DataFrame([ratings], columns=colnames, index=[name])
    v_temp = pd.DataFrame([voters], columns=colnames, index=[name])

    Ratings_df = pd.concat([Ratings_df, r_temp])
    Voters_df =  pd.concat([Voters_df, v_temp])

print("Uncomment last two lines to create csv documents of the dataframes")

# Voters_df.to_csv('Number_of_Voters.csv') #uncomment to create document
# Ratings_df.to_csv('Ratings.csv') #uncomment to create document
