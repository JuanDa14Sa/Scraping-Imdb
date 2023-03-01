import requests
from bs4 import BeautifulSoup
import csv

html_text = requests.get('https://www.imdb.com/chart/top/?ref_=nv_mv_250').text
soup = BeautifulSoup(html_text, 'lxml')
movies = soup.find_all('td', class_='titleColumn')
titles = []
years = []
rankings = []
for index, movie in enumerate(movies):
    title = movie.find('a')
    year = movie.find('span')
    print(f"Ranking: {index+1}\tTítulo: {title.text}\tYear: {year.text[1:-1]}")
    rankings.append(index+1)
    titles.append(title.text)
    years.append(year.text[1:-1])

titles.insert(0,'Pelicula')
years.insert(0,'Fecha-Estreno')
with open('top250movies.csv', 'w', newline='') as file:
     writer = csv.writer(file)
     writer.writerows(list(zip(titles,years)))