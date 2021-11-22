import requests
from time import strftime, localtime
from player import Player

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    response = requests.get(url).json()

    # print("JSON-muotoinen vastaus:")
    # print(response)

    players = []

    for player_dict in response:
        if player_dict['nationality'] == 'FIN':
            player = Player(
                player_dict['name'], player_dict['assists'],
                player_dict['goals'], player_dict['team']
            )

            players.append(player)

    print(f"Players from FIN {strftime('%Y-%m-%d %H:%M:%S', localtime())}")

    plrs_sorted = sorted(players, key=lambda player: (player.goals+player.assists, player.goals), reverse=True)

    for player in plrs_sorted:
        print(player)

if __name__ == "__main__":
    main()
