import logging
from flask import Flask
from services.match_service import MatchService

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def init() -> tuple[dict[str, str], int, dict[str, str]]:
    return ({ "message": "Health check ok" }, 200, { "Content-Type": "application/json" })

@app.route('/matches/all', methods=['GET'])
def matches() -> tuple[dict[str, str], int, dict[str, str]]:
    MatchService().get_matches()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)