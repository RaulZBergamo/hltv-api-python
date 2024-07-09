"""
This module represents a Match entity.

Classes:
    Match: Represents a match with a home team, away team, score, state, date, and tournament.
"""

from typing import Dict, Any

class Match:
    """
    This class represents a Match entity.

    Attributes:
        match_id (str): The ID of the match.
        home_team (Team): The home team.
        away_team (Team): The away team.
        home_score (int): The score of the home team.
        away_score (int): The score of the away team.
        state (str): The state of the match.
        match_date (date): The date of the match.
        tournament (str): The tournament of the match.

    Methods

    is_finished() -> bool: Checks if the match has finished
    """

    def __init__(self, **kwargs: Dict[str, Any]) -> None:
        self.match_id = kwargs["match_id"]
        self.home_team = kwargs["home_team"]
        self.away_team = kwargs["away_team"]
        self.home_score = kwargs["home_score"]
        self.away_score = kwargs["away_score"]
        self.state = kwargs["state"]
        self.match_date = kwargs["match_date"]
        self.tournament = kwargs["tournament"]

    def is_finished(self) -> bool:
        """
        Checks if the match has finished.

        Returns:
            bool: True if the match is finished, False otherwise.
        """
        return self.state.lower() in ["finished", "completed"]

    def __repr__(self) -> str:
        return f"{self.home_team} {self.home_score} X {self.away_score} {self.away_team}"
