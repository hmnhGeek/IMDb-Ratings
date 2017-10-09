'''
    AUTHOR: Himanshu Sharma
'''

import requests, bs4
import warnings
import numpy as np
warnings.filterwarnings("ignore", category=UserWarning, module='bs4')

# define the base url of IMDb
base_url = "https://www.imdb.com"

# create a soup of this url.
soup = bs4.BeautifulSoup(requests.get(base_url).text)

for div in soup.findAll('div', attrs = {'class':'sub_nav'}):
    a = div.findAll('a')

    top_rated = a[5]
    break

# Now we have the top_rated movies url.
def find_movies(lower = 8.0, upper = 10.0):
    
    top_rated_url = base_url + top_rated.attrs['href']
    sub_soup = bs4.BeautifulSoup(requests.get(top_rated_url).text)

    # find all the <td> tags with the given class. Then inside this for loop,
    # find the <strong> tags which carries the imdb rating. Append these <strong>
    # tags inside rankings list.
    ratings = []
    for td in sub_soup.findAll('td', attrs = {'class':'ratingColumn imdbRating'}):
        strong = td.findAll('strong')
        ratings.append(strong)

    # find all the <td> tags with the given class. Then inside this for loop,
    # find the <a> tags which carries the movie name. Append these <a>
    # tags inside movies list.
    movies = []
    for td in sub_soup.findAll('td', attrs = {'class':'titleColumn'}):
        a = td.findAll('a')
        movies.append(a)

    # although len(movies) will always be equal to len(ratings), but still in case
    # if they are not equal, take the min among them to make sure no index error is raised.
    minLen = min(len(movies), len(ratings)) 

    for i in range(minLen):
        # note that rankings[i] is list of <strong> tags and so to access the attributes
        # of this tag [0] element is to be taken.
        if float(ratings[i][0].text) in np.arange(lower, upper+0.1, 0.1):
            print movies[i][0].text
        
