import random
import datetime

PLAYERS = [
    {"id": 1, "name": "Alice Highroller", "tier": "Legend", "account_age_days": 1200, "status": "active"},
    {"id": 2, "name": "Bob Casual", "tier": "Bronze", "account_age_days": 45, "status": "active"},
    {"id": 3, "name": "Charlie Risk", "tier": "Silver", "account_age_days": 10, "status": "under_review"},
]

def get_mock_wagers(player_id):
    """Generates random wager history for a given player."""
    wagers = []
    # Deterministic seed for demo consistency
    random.seed(player_id) 
    
    num_wagers = random.randint(5, 50)
    for _ in range(num_wagers):
        amount = round(random.uniform(10.0, 5000.0), 2)
        win = random.choice([True, False])
        wagers.append({
            "date": (datetime.datetime.now() - datetime.timedelta(days=random.randint(0, 30))).strftime("%Y-%m-%d"),
            "game": random.choice(["Blackjack", "Sportsbook - NFL", "Slots", "Roulette"]),
            "amount": amount,
            "result": "win" if win else "loss",
            "payout": amount * 2 if win else 0
        })
    return wagers

if __name__ == "__main__":
    for player in PLAYERS:
        print(get_mock_wagers(player["id"]))
