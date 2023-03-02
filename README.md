## IMDB Top 250 Movies Cast Graph Scraper
This is a Python project that scrapes the top 250 movies from IMDB and extracts the cast information for each movie. The goal of the project is to create a graph connecting the cast members of these movies, which can be used to visualize the connections between different actors and actresses.

## Scraper Details
The scraper uses the requests and beautifulsoup4 Python packages to extract the top 250 movies from the IMDB website. It then goes through each movie and extracts the cast information using the BeautifulSoup library.

The cast information is stored in a JSON format, where each movie is represented by an object with the following properties:

title: The title of the movie
year: The release year of the movie
cast: A list of cast members, where each member is represented by an object with the following properties:
name: The name of the cast member
character: The character played by the cast member
The output JSON file can be used to create a graph using tools like networkx and matplotlib. The graph can be used to visualize the connections between different actors and actresses in the top 250 movies from IMDB.
