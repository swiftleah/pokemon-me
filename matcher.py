# Logic to find most similar pokemon character based on stats
# cosine similarity

from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import json

# load pokemon stats json file
with open("main_pokemon_data.json", "r") as file:
    pokemon_data = json.load(file)

# temp dummy data
# user_stats = {
#     "HP": 5,
#     "Attack": 3,
#     "Defense": 4,
#     "Sp. Atk": 2,
#     "Sp. Def": 2,
#     "Speed": 1
# }

# convert stats to vector
def stats_to_vector(stats_dict):
    return [
        stats_dict["HP"],
        stats_dict["Attack"],
        stats_dict["Defense"],
        stats_dict["Sp. Atk"],
        stats_dict["Sp. Def"],
        stats_dict["Speed"]
    ]

def find_best_match(user_stats):
    user_vector = np.array([stats_to_vector(user_stats)])


    most_similar = None
    # set lowest similarity possible (perpendicular vectors = -1)
    highest_similarity = -1

    for pokemon in pokemon_data:
        pokemon_vector = np.array([stats_to_vector(pokemon["base_stats"])])
        similarity = cosine_similarity(user_vector, pokemon_vector)[0][0]

        if similarity > highest_similarity:
            highest_similarity = similarity
            most_similar_pokemon = pokemon

    # Beautify terminal result layout
    name = most_similar_pokemon["name"]
    stats = most_similar_pokemon["base_stats"]
    types = ", ".join(most_similar_pokemon["types"])
    url = most_similar_pokemon["url"]
    
    print("\n🎉 Based on your answers, the Pokémon you're most like is...\n")
    print("╭" + "─" * 34 + "╮")
    print(f"│{'✨  ' + name + '  ✨':^32}│")
    print("╰" + "─" * 34 + "╯\n")

    print(f"🧬 Type(s): {types}")
    print("📊 Base Stats:")
    for stat_name, value in stats.items():
        print(f"   - {stat_name}: {value}")

    print(f"\n🔗 More Info: {url}")


    return most_similar_pokemon