import requests
from player import Player

class PlayerReader:
    def __init__(self, url):
        json_f = requests.get(url).json()
        self._players = self._create_players(json_f)

    def _create_players(self, json_f):
        plrs = []
        for dct in json_f:
            player = Player(
                dct['name'], dct['assists'],
                dct['goals'], dct['team'], dct['nationality']
            )
            plrs.append(player)
        return plrs

    def get_players(self):
        return self._players