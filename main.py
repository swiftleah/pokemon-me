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
    types = [tag.text for tag in typeTags]

    # Stats
    statRows = soup.select("table.vitals-table tr") 
    stats = {}
    for row in statRows:
        # find all <td> elements in this row
        cells = row.find_all("td")
        # only process rows with 2 <td> (stat value & extra info)
        if len(cells) == 2:
            # get name of stat from <th>
            statName = row.find("th").text.strip()
            # get value of stat from first <td> element
            statValue = cells[0].text.strip()
            if statName in ["HP", "Attack", "Defense", "Sp. Atk", "Sp. Def", "Speed"]:
                # save stat in dict stats with stat name as key
                stats[statName] = int(statValue)

    try:
        description = soup.select_one("#dex-flavor .resp-scroll p").text.strip()
    except:
        description = "No description available."

    pokemonData.append({
        "name": pokeName,
        "types": types,
        "base_stats": stats,
        "description": description,
        "url": url
    })

    time.sleep(1)

with open("main_pokemon_data.json", "w") as f:
    json.dump(pokemonData, f, indent=2)
