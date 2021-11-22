class Player:
    def __init__(self, name, assists, goals, team):
        self.name = name
        self.assists = assists
        self.goals = goals
        self.team = team
    
    def __str__(self):
        return f'{self.name} team {self.team} goals {self.goals} assists {self.assists}'
