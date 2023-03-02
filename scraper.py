import requests
from bs4 import BeautifulSoup
import re
import json

html_text = requests.get('https://www.imdb.com/chart/top/?ref_=nv_mv_250', headers={'Accept-Language': 'en-US,en;q=0.8'}).text
soup = BeautifulSoup(html_text, 'lxml')
movies = soup.find_all('td', class_='titleColumn')
to_json = []
for index, movie in enumerate(movies):
    title = movie.find('a')
    year = movie.find('span')
    link = title['href']

    print(f"Ranking: {index+1}\tTítulo: {title.text}\tYear: {year.text[1:-1]}\tLink: https://www.imdb.com{link}")
    page = requests.get(f"https://www.imdb.com{link}fullcredits/", headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(page.text, 'html.parser')
    tmp = soup.find('table', class_='cast_list')
    info = tmp.find_all('td', class_='primary_photo')
    actors = []
    for i in info:
        actors_name = re.search('title="(.*?)"', str(i)).group(1)
        actors.append(actors_name)
    to_json.append({'Ranking': index+1, 'Title': title.text, 'Year': year.text[1:-1], 'Link': f"https://www.imdb.com{link}", 'Actors': actors})
    
json.dump(to_json, open('top250movies.json', 'w'), indent=4)