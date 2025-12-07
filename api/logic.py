def calculate_risk_score(player_data, wagers):
    """
    Calculates a risk score (0-100) based on betting behavior.
    
    Args:
        player_data (dict): Player profile
        wagers (list): List of wager dictionaries
    """
    if not wagers:
        return 0

    total_loss = sum(w['amount'] for w in wagers if w['result'] == 'loss')
    total_wagered = sum(w['amount'] for w in wagers)
    
    # Base risk: High losses relative to simple threshold
    risk_score = min(100, int((total_loss / 1000) * 10))
    
    # Velocity risk: High frequency betting check (simplified)
    if len(wagers) > 40:
        risk_score += 15
        
    # New account risk factor
    if player_data.get('account_age_days', 0) < 30:
        risk_score += 10

    # Cap at 100
    return min(100, risk_score)

def determine_risk_level(score):
    if score > 80:
        return "Critical"
    elif score > 50:
        return "High"
    elif score > 20:
        return "Medium"
    return "Low"