from models.team import Team
from datetime import date

class Match:
    
    def __init__(self, id: str, home_team: Team, away_team: Team, home_score: int, away_sore: int, state: str, date: date, tournament: str) -> None:
        self.id = id
        self.home_team = home_team
        self.away_team = away_team
        self.home_score = home_score
        self.away_score = away_sore
        self.state = state
        self.date = date
        self.tournament = tournament
        
    def __repr__(self) -> str:
        return f"Match ID: {self.id}\nHome Team: {self.home_team}\nAway Team: {self.away_team}\nHome Score: {self.home_score}\nAway Score: {self.away_score}\nState: {self.state}\nDate: {self.date}\nTournament: {self.tournament}"