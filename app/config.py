"""
Módulo de configuração para a API HLTV.

Este módulo contém as configurações utilizadas pela API HLTV. 
Ele define as URLs base, caminhos para recursos específicos. 
E mapeamento de abreviações de mapas e gera um agente de usuário aleatório.

Variáveis:
- CONFIG: Um dicionário que contém as configurações principais.
- MAPS: Um dicionário que mapeia as abreviações dos mapas para seus nomes completos.
- USER_AGENT: Representa um agente de usuário aleatório gerado pelo pacote fake_useragent.

"""

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

USER_AGENT = UserAgent().random
