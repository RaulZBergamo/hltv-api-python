"""
Módulo de configuração para a API HLTV.

Este módulo contém as configurações utilizadas pela API HLTV. Ele define as URLs base, caminhos para recursos específicos, mapeamento de abreviações de mapas e gera um agente de usuário aleatório.

Variáveis:
- CONFIG: Um dicionário que contém as configurações principais, como a URL base, CDN, RSS, resultados, partidas, jogadores e equipes.
- MAPS: Um dicionário que mapeia as abreviações dos mapas para seus nomes completos.
- USER_AGENT: Uma string que representa um agente de usuário aleatório gerado pelo pacote fake_useragent.

Exemplo de uso:
    from app.config import CONFIG, MAPS, USER_AGENT

    print(CONFIG["BASE_URL"])  # Imprime a URL base da API HLTV
    print(MAPS["d2"])  # Imprime o nome completo do mapa com a abreviação "d2"
    print(USER_AGENT)  # Imprime o agente de usuário aleatório gerado

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
