"""
This module represents a Player entity.

Classes:
    Player: Represents a player with a name, trophies, age, team, and social media links.
"""

from typing import Dict, Any

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

    def __init__(self, **kwargs: Dict[str, Any]) -> None:
        self.player_id = kwargs["player_id"]
        self.name = kwargs["name"]
        self.team = kwargs["team"]
        self.age = kwargs["age"]

        self.trophies = kwargs.get("trophies", [])

        if not isinstance(self.trophies, list):
            raise TypeError("Trophies must be a list")
        
        self.social = kwargs.get("social", [])

        if not isinstance(self.social, list):
            raise TypeError("Social must be a list")
        
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
