class PlayerStats:
    def __init__(self, reader):
        self._reader = reader

    def top_scorers_by_nationality(self, nationality):
        lst = [plr for plr in self._reader.get_players() if plr.nationality == nationality]
        return sorted(lst, key=lambda player: (player.goals+player.assists, player.goals), reverse=True)