def calculate_anomaly_score(station_data, readings):
    """
    Calculates an anomaly score (0-100) based on sensor behavior.
    
    Args:
        station_data (dict): Station profile
        readings (list): List of sensor reading dictionaries
    """
    if not readings:
        return 0

    total_anomalies = sum(1 for r in readings if r['status'] == 'anomaly')
    total_readings = len(readings)
    
    # Base score from anomaly frequency
    anomaly_rate = (total_anomalies / total_readings) if total_readings > 0 else 0
    anomaly_score = min(100, int(anomaly_rate * 200)) # Scale up for visibility
    
    # Calibration age risk factor (sensors need calibration every 365 days)
    if station_data.get('calibration_age_days', 0) > 365:
        anomaly_score += 20
        
    # Frequent fluctuation penalty
    if len(readings) > 40:
        anomaly_score += 10

    # Cap at 100
    return min(100, anomaly_score)

def determine_severity_level(score):
    if score > 80:
        return "Critical"
    elif score > 50:
        return "High"
    elif score > 20:
        return "Moderate"
    return "Stable"