"""
This module represents a Team entity.

Classes:
    Team: Represents a team with a name, logo, and list of players.
"""

from typing import List
from models.player import Player

class Team:
    """
    This class represents a Team entity

    Attributes:
        team_id (str): The unique identifier of the team.
        name (str): The name of the team.
        logo (str): The url to the logo of the team.
        players (List[Player]): A list of players in the team.
    """

    def __init__(self, team_id: str, name: str, logo: str, players: List[Player] = None):
        self.team_id = team_id
        self.name = name
        self.logo = logo
        self.players = players

    def add_player(self, player: str) -> None:
        """
        Adds a new player to the team's list of players.

        Parameters:
            player (str): The name of the player to add.
        """
        self.players.append(player)

    def __str__(self) -> str:
        return f"{self.name}\nPlayers: {', '.join([player.name for player in self.players])}"
