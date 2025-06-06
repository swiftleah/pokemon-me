from questions import questions

# Initial stat scores & traits
def run_quiz():
    stat_scores = {
        "HP": 0,
        "Attack": 0,
        "Defense": 0,
        "Sp. Atk": 0,
        "Sp. Def": 0,
        "Speed": 0
    }

    print("Welcome to the Pokémon Personality Quiz!")
    print("Answer the following questions to find your Pokémon match <3\n")

    # print questions
    for idx, question in enumerate(questions):
        print(f"\nQuestion {idx + 1}: {question['question']}")

        # print answer options
        for i, option in enumerate(question["answers"]):
            print(f"{i + 1}. {option}")

        # safe input
        while True:
            try:
                choice = int(input("Choose 1-5: "))
                if 1 <= choice <= len(question["answers"]):
                    break
                else:
                    print("Please enter a number between 1 and 5.")
            except ValueError:
                print("Please enter a valid number.")


        stat = question["stat"]
        # grab weight based on answer from user
        weight = question["weights"][choice - 1]
        stat_scores[stat] += weight


    print("\nYour base stat profile:")
    for stat, score in stat_scores.items():
        print(f"{stat}: {score}")

if __name__ == "__main__":
    run_quiz()