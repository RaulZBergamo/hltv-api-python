class Player():

    def __init__(self, id: str, name: str, trophies: list[str], age: str, team: str, social: list[str]) -> None:
        self.name = name
        self.trophies = trophies
        self.age = age
        self.team = team
        self.social = social

    def __str__(self) -> str:
        return f"Player Name: {self.name}\nTrophies: {', '.join(self.trophies)}\nAge: {self.age}\nTeam: {self.team}\nSocial: {', '.join(self.social)}"
        