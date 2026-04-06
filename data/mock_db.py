import random
import datetime

STATIONS = [
    {"id": 1, "name": "North Hill Station", "model": "Gen-1", "calibration_age_days": 1200, "status": "active"},
    {"id": 2, "name": "River Basin Delta", "model": "Gen-2", "calibration_age_days": 45, "status": "active"},
    {"id": 3, "name": "Urban Canyon West", "model": "Gen-1", "calibration_age_days": 10, "status": "maintenance_required"},
    {"id": 4, "name": "Forest Canopy Alpha", "model": "Gen-3", "calibration_age_days": 967, "status": "active"}
]

def get_mock_readings(station_id):
    """Generates random sensor reading history for a given station."""
    readings = []
    # Deterministic seed for demo consistency
    random.seed(station_id) 
    
    num_readings = random.randint(5, 50)
    for _ in range(num_readings):
        value = round(random.uniform(5.0, 150.0), 2)
        is_anomaly = random.random() < 0.1  # 10% chance of anomaly
        readings.append({
            "timestamp": (datetime.datetime.now() - datetime.timedelta(days=random.randint(0, 30))).strftime("%Y-%m-%d %H:%M:%S"),
            "metric": random.choice(["PM2.5", "CO2", "NO2", "Temperature"]),
            "value": value,
            "status": "anomaly" if is_anomaly else "valid",
            "variance": round(random.uniform(0.1, 5.0), 2) if is_anomaly else 0.0
        })
    return readings

if __name__ == "__main__":
    for station in STATIONS:
        print(get_mock_readings(station["id"]))
