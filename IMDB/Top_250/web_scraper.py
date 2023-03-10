# import necessary modules
from os import link
from bitarray import test
import requests
from bs4 import BeautifulSoup
import pandas as pd

# retrieve the html content from the given imdb url
html_text = requests.get('https://www.imdb.com/chart/top/?ref_=nv_mv_250').text

# parse the html content using BeautifulSoup
soup = BeautifulSoup(html_text, 'lxml')

# extract all the movie titles and links from the html content
movies = soup.find_all('td', class_ = 'titleColumn')
names = []
links = []
for movie in movies:
    name = movie.find('a', href = True).text
    link =  movie.find('a', href = True)['href']
    names.append(name)
    links.append(link)

# create a dataframe with the movie names and links
zipped = list(zip(names, links))
df = pd.DataFrame(zipped, columns=['Name', 'Link'])

# create column names for the ratings and voters dataframes
age = ["all","sub18","18-29","30-44","44+"]
gender = ["_m", "_f"]
colnames = age
colnames.extend([i+gender[0] for i in age])
colnames.extend([i+gender[1] for i in age[:5]])
colnames.extend(["top_1000", "US", "non_US"])

# create empty dataframes for the ratings and voters
Ratings_df = pd.DataFrame(columns=colnames)
Voters_df = pd.DataFrame(columns=colnames)

# loop through each movie in the dataframe
for name, link in zip(df['Name'], df['Link']):
    
    # retrieve the html content for the ratings page of the movie
    html = requests.get('https://www.imdb.com' + link + "ratings/").text
    soup2 = BeautifulSoup(html, 'lxml')

    # extract the ratings and voters data for the movie
    grid =  soup2.find_all('td', class_ = 'ratingTable') 
    ratings = []
    voters = []
    for cell in grid:
        rating = cell.find('div', class_ = 'bigcell').text.replace(' ','')
        voter = cell.find('a', href = True).text.replace(' ','').replace('\n', '')
        ratings.append(rating)
        voters.append(voter) 

    # create temporary dataframes for the ratings and voters data of the movie
    r_temp = pd.DataFrame([ratings], columns=colnames, index=[name])
    v_temp = pd.DataFrame([voters], columns=colnames, index=[name])

    # append the temporary dataframes to the ratings and voters dataframes
    Ratings_df = pd.concat([Ratings_df, r_temp])
    Voters_df =  pd.concat([Voters_df, v_temp])

# print a message to remind the user to uncomment the last two lines of the code
# to create csv files for the ratings and voters dataframes
print("Uncomment last two lines to create csv documents of the dataframes")


# Voters_df.to_csv('Number_of_Voters.csv') #uncomment to create document
# Ratings_df.to_csv('Ratings.csv') #uncomment to create document
