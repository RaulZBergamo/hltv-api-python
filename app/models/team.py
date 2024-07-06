from models.player import Player

class Team:

    def __init__(self, id: str, name: str, logo: str, players: list[Player] = None):
        self.name = name
        self.logo = logo
        self.players = players

    def add_player(self, player):
        self.players.append(player)

    def __str__(self):
        return f"Team Name: {self.name}\nLogo: {self.logo}\nPlayers: {', '.join([player.name for player in self.players])}"