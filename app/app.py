"""
This module contains the main application logic

Endpoints

    / - GET: A health check endpoint
    /matches/all - GET: An endpoint that returns all matches from HLTV
"""

import logging
from flask import Flask
from services.match_service import MatchService

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def init() -> tuple[dict[str, str], int, dict[str, str]]:
    """
    An endpoint that returns a health check message
    """

    return ({ "message": "Health check ok" }, 200, { "Content-Type": "application/json" })

@app.route('/matches/all', methods=['GET'])
def matches() -> tuple[dict[str, str], int, dict[str, str]]:
    """
    An endpoint that returns all matches from HLTV
    """

    MatchService().get_matches()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
