from fake_useragent import UserAgent

CONFIG = {
    "BASE_URL": "https://www.hltv.org",
    "CDN": "https://img-cdn.hltv.org",
    "RSS": "rss",
    "RESULTS": "results",
    "MATCHES": "matches",
    "PLAYERS": "stats/players",
    "TEAMS": "ranking/teams",
    "TEAM": "team",
}

MAPS = {
    "trn": "Train",
    "mrg": "Mirage",
    "d2": "Dust 2",
    "inf": "Inferno",
    "vtg": "Vertigo",
    "ovp": "Overpass",
    "nuke": "Nuke",
    "anc": "Ancient",
}

# Generate a random user agent string
USER_AGENT = UserAgent().random