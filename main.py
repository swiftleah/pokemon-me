import requests
from bs4 import BeautifulSoup
import time
import json

# Top 50 "OG" Pokemons
pokemonNames = [
    "bulbasaur", "ivysaur", "venusaur", "charmander", "charmeleon", "charizard",
    "squirtle", "wartortle", "blastoise", "pikachu", "raichu",
    "jigglypuff", "meowth", "psyduck", "gengar", "snorlax",
    "eevee", "vaporeon", "jolteon", "flareon", "machop", "machoke", "machamp",
    "growlithe", "arcanine", "mew", "mewtwo", "articuno", "zapdos", "moltres",
    "lugia", "ho-oh", "celebi", "cyndaquil", "typhlosion", "totodile", "mudkip",
    "torchic", "blaziken", "turtwig", "chimchar", "piplup", "lucario",
    "gardevoir", "garchomp", "togepi", "ditto", "scyther", "dragonite", "alakazam"
]

baseURL = "https://pokemondb.net/pokedex/"
pokemonData = []

for name in pokemonNames:
    url = baseURL + name
    print(f"Fetching {name}...")

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    pokeName = soup.find("h1").text.strip()

    # Types (Fire, Electric, etc.)
    typeTags = soup.select(".vitals-table td a.type-icon")
    types = list(set(tag.text for tag in typeTags))

    base_stats = {}

    # Stats
    resp_scroll_div = soup.find("div", class_="resp-scroll")
    vitals_table = resp_scroll_div.find("table", class_="vitals-table")

    for row in vitals_table.tbody.find_all("tr"):
        stat_name = row.find("th").text.strip()
        stat_value_cell = row.find("td", class_="cell-num")

        if stat_name in ["HP", "Attack", "Defense", "Sp. Atk", "Sp. Def", "Speed"]:
            base_stats[stat_name] = int(stat_value_cell.text.strip())

    try:
        description = soup.select_one("#dex-flavor .resp-scroll p").text.strip()
    except:
        description = "No description available."

    pokemonData.append({
        "name": pokeName,
        "types": types,
        "base_stats": base_stats,
        "description": description,
        "url": url
    })

    time.sleep(1)

    with open("main_pokemon_data.json", "w") as f:
        json.dump(pokemonData, f, indent=2)
