class Player:
    def __init__(self, name, assists, goals, team, nationality):
        self.name = name
        self.assists = assists
        self.goals = goals
        self.team = team
        self.nationality = nationality
    
    def __str__(self):
        return f'{self.name:22}{self.team} {self.goals:2d} + {self.assists:2d} = {self.goals+self.assists:2d}'
