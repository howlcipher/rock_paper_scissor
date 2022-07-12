from unicodedata import name


class user():
    def __init__(self, id, name, wins, losses, draws, games_played, rock_chosen, paper_chosen, scissors_chosen):
        self.id = id
        self.name = name
        self.wins = wins
        self.losses = losses
        self.draws = draws
        self.games_played = games_played
        self.rock_chosen = rock_chosen
        self.paper_chosen = paper_chosen
        self.scissors_chosen = scissors_chosen

class human(user):
    def __init__(self, id, name, wins, losses, draws, games_played, rock_chosen, paper_chosen, scissors_chosen):
        super().__init__(id, name, wins, losses, draws, games_played, rock_chosen, paper_chosen, scissors_chosen)
        pass

class computer(user):
    def __init__(self, id, wins, losses, draws, games_played, rock_chosen, paper_chosen, scissors_chosen, name = 'Computer'):
        super().__init__(id, name, wins, losses, draws, games_played, rock_chosen, paper_chosen, scissors_chosen)
        pass
    
thuman = human(1, 'test', 1, 2, 3, 6, 1, 2, 3)
tcomputer = computer(2, 1, 2, 3, 6, 1, 2, 3)

print('hu-name', thuman.name)
print('comp-name', tcomputer.name)