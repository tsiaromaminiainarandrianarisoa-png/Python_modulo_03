import random

def data_alchemist() -> None:
    print("=== Game Data Alchemist ===\n")
    players = ['Alice', 'bob', 'Charlie', 'dylan', 'Emma', 'Gregory', 'john', 'kevin', 'Liam']
    print(f"Initial list of players: {players}")
    all_players = [player.capitalize() for player in players]
    capitalized_players = [player for player in players if player == player.capitalize()]
    print(f"New list with all names capitalized: {all_players}")
    print(f"New list of capitalized names only: {capitalized_players}")
    score_attribute = {player: (random.randrange(1000)) for player in all_players}
    print(f"\nScore dict: {score_attribute}")
    average = (sum(score_attribute.values()))/len(score_attribute)
    print(f"Score average is {round(average, 2)}")
    high_score = { player: score for player, score in score_attribute.items() if score_attribute[player] > average}
    print(f"High score: {high_score}")

if __name__ == "__main__":
    data_alchemist()
