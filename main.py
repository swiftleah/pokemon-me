import requests
from bs4 import BeautifulSoup

url = "https://pokemondb.net/pokedex/national"

response = requests.get(url)
print(response)