# Logic to find most similar pokemon character based on stats
# cosine similarity

from sklearn.metrics.pairwise import cosine_similarity
from scipy.spatial.distance import euclidean
import numpy as np
import json

# load pokemon stats json file
with open("main_pokemon_data.json", "r") as file:
    pokemon_data = json.load(file)


# define order
STAT_ORDER = ["HP", "Attack", "Defense", "Sp. Atk", "Sp. Def", "Speed"]

# normalize stats into ratios
def normalize_stats(stats_dict):
    '''
    -divide stats by combined total
    -include safe protocol for combined total of 0
    '''
    total = sum(stats_dict.values())
    if total == 0:
        return {stat: 0 for stat in STAT_ORDER}
    return {stat: stats_dict[stat] / total for stat in STAT_ORDER}


# calculate cosine similarity & euclidean distance between user_stat vector & pokemon stat vector
def calculate_similarities(user_vector, pokemon_vector):
    user_vec = np.array(user_vector).reshape(1, -1)
    poke_vec = np.array(pokemon_vector).reshape(1, -1)

    cosine_sim = cosine_similarity(user_vec, poke_vec)[0][0]
    euclidean_dist = euclidean(user_vector, pokemon_vector)

    return cosine_sim, euclidean_dist

# 3. Match function
def find_best_match(user_stats):
    user_norm_stats = normalize_stats(user_stats)
    user_vector = [user_norm_stats[stat] for stat in STAT_ORDER]

    best_pokemon = None
    best_score = -float("inf")

    # Weight tuning (1.0 = full cosine, 0.0 = full euclidean)
    weight_cosine = 0.7
    weight_euclid = 0.3

    for pokemon in pokemon_data:
        poke_norm_stats = normalize_stats(pokemon["base_stats"])
        poke_vector = [poke_norm_stats[stat] for stat in STAT_ORDER]

        cos_sim, euc_dist = calculate_similarities(user_vector, poke_vector)
        combined_score = weight_cosine * cos_sim + weight_euclid * (-euc_dist)

        if combined_score > best_score:
            best_score = combined_score
            best_pokemon = pokemon

    return best_pokemon