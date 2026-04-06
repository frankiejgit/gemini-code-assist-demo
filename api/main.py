import sys
import os

# Add the parent directory to sys.path so we can import 'data' and 'api' modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask, jsonify, request
from data.mock_db import STATIONS, get_mock_readings
from api.logic import calculate_anomaly_score, determine_severity_level

app = Flask(__name__)

@app.route('/stations', methods=['GET'])
def get_stations():
    return jsonify(STATIONS)

@app.route('/stations/<int:station_id>', methods=['GET'])
def get_station_detail(station_id):
    station = next((s for s in STATIONS if s['id'] == station_id), None)
    if station:
        return jsonify(station)
    return jsonify({"error": "Station not found"}), 404

@app.route('/readings/<int:station_id>', methods=['GET'])
def get_readings(station_id):
    readings = get_mock_readings(station_id)
    return jsonify(readings)

@app.route('/anomaly/<int:station_id>', methods=['GET'])
def get_anomaly_status(station_id):
    station = next((s for s in STATIONS if s['id'] == station_id), None)
    if not station:
        return jsonify({"error": "Station not found"}), 404
        
    readings = get_mock_readings(station_id)
    score = calculate_anomaly_score(station, readings)
    level = determine_severity_level(score)
    
    return jsonify({
        "station_id": station_id,
        "anomaly_score": score,
        "severity_level": level
    })

if __name__ == '__main__':
    print("Starting Sensor Data API on port 5000...")
    app.run(port=5000, debug=True)
