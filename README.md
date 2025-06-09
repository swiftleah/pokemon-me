# 🧠 Terminal-Based Pokémon Personality Quiz

## How Matching Works:

- Your answers are converted into a stat profile, containing 6 different values relating to Pokémon characteristics.
- Uses Cosine Similarity & Euclidean Distance with 70% and 30% weight respectively.
- You might notice that even if the user's stats have different absolute values - they might still be matched with the same Pokémon. That's because Cosine Similarity focuses on the direction of the vector, not the magnitude. Euclidean Distance helps balance that by factoring in how far apart the actual values are.

## Features

- 6 personality-based questions
- Uses both cosine similarity and euclidean distance for matching
- Compares your answers with real Pokémon base stats
- Returns your best-matched Pokémon with its name, base stats, type(s), and a link to its Pokédex!

## Use the quiz:

- git clone https://github.com/swiftleah/pokemon-me.git
- pip install -r requirements.txt
- python quiz.py
