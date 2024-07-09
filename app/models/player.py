"""
This module represents a Player entity.

Classes:
    Player: Represents a player with a name, trophies, age, team, and social media links.
"""

from typing import List

class Player():
    """
    This class represents a Player entity.

    Attributes:
        player_id (str): The unique identifier of the player.
        name (str): The name of the player.
        trophies (list[str]): A list of trophies won by the player.
        age (str): The age of the player.
        team (str): The team the player belongs to.
        social (list[str]): A list of social media links of the player.

    Methods:

        add_trophy() -> None: Adds a new Trophy.
        
        add_social() -> None: Adds a new Social.
    """

    def __init__(
        self,
        player_id: str,
        name: str,
        trophies: List[str], 
        age: str,
        team: str, 
        social: List[str]
    ) -> None:
        self.player_id = player_id
        self.name = name
        self.trophies = trophies
        self.age = age
        self.team = team
        self.social = social

    def add_trophy(self, trophy: str) -> None:
        """
        Adds a new trophy to the player's list of trophies.

        Parameters:
            trophy (str): The name of the trophy to add.
        """
        self.trophies.append(trophy)

    def add_social(self, social: str) -> None:
        """
        Adds a new social to the player's list of socials.

        Parameters:
            social (str): The link of the social to add.
        """
        self.social.append(social)

    def __repr__(self) -> str:
        return f"""
        {self.name}:
        Age: {self.age},
        Team: {self.team},
        Trophies: {', '.join(self.trophies)},
        Social: {', '.join(self.social)}
        """
