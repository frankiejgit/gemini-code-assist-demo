import sys
import os

# Add the parent directory to sys.path so we can import 'data' and 'api' modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask, jsonify, request
from data.mock_db import PLAYERS, get_mock_wagers
from api.logic import calculate_risk_score, determine_risk_level

app = Flask(__name__)

@app.route('/players', methods=['GET'])
def get_players():
    return jsonify(PLAYERS)

@app.route('/players/<int:player_id>', methods=['GET'])
def get_player_detail(player_id):
    player = next((p for p in PLAYERS if p['id'] == player_id), None)
    if player:
        return jsonify(player)
    return jsonify({"error": "Player not found"}), 404

@app.route('/wagers/<int:player_id>', methods=['GET'])
def get_wagers(player_id):
    wagers = get_mock_wagers(player_id)
    return jsonify(wagers)

@app.route('/risk/<int:player_id>', methods=['GET'])
def get_risk(player_id):
    player = next((p for p in PLAYERS if p['id'] == player_id), None)
    if not player:
        return jsonify({"error": "Player not found"}), 404
        
    wagers = get_mock_wagers(player_id)
    score = calculate_risk_score(player, wagers)
    level = determine_risk_level(score)
    
    return jsonify({
        "player_id": player_id,
        "risk_score": score,
        "risk_level": level
    })

if __name__ == '__main__':
    print("Starting Flask API on port 5000...")
    app.run(port=5000, debug=True)