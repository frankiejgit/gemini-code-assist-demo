# Demo Instructions for Gemini Code Assist

**Goal:** Demonstrate the capabilities of AI coding assistance for software engineers and platform administrators. Focus on **Onboarding Speed**, **Developer Velocity**, and **Modernization**.

**Repo Structure:**
```text
hard-rock-admin-demo/
├── api/
│   ├── main.py            # currently Flask (Refactor target)
│   ├── logic.py           # Risk calculation logic (Explain Code target)
│   └── models.py          # Empty/TODO (Code generation target)
├── ui/
│   └── app.py             # Streamlit Dashboard
├── data/
│   └── mock_db.py         # Mock Data Generator
└── requirements.txt       # Dependencies
```

## Pre-Demo Setup

1. Clone this repository
```
git clone https://github.com/frankiejgit/digital-casino-code-assist.git
cd code-assist-player-risk-demo
```

2. Create a virtual environment using `uv`
```
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies
```
uv pip install -r requirements.txt
```

4. Opemm a terminal in VS Code (or your IDE of choice) and start the backend API 
```
python api/main.py
```

5. In a new terminal window, start the Streamlit UI
```
streamlit run ui/app.py
```

6. __IMPORTANT - Hiding Context:__

Before the demo, you must ensure Gemini does not read this instruction file. You have two options:
- Option A: Delete this INSTRUCTIONS.md file entirely.
- Option B (recommended): Create a file named .aiexclude in the root and add INSTRUCTIONS.md to it.

## Demo Flow

### Content & Explanation (The "Onboarding" Use Case)

__Goal:__ Show how Gemini understands business/code logic instantly.

1. Open api/logic.py.
2. Highlight the entire calculate_risk_score function.
3. Prompt:
```
Explain this risk calculation logic in plain English. What specific behaviors trigger a high risk score?
```

Talk Track:
> "Normally, a new developer would have to hunt down a senior engineer to understand this legacy logic. Gemini acts as an instant mentor, explaining that 'Losses', 'Velocity', and 'Account Age' are the key drivers here."

### Documentation (The "Compliance" Use Case)
__Goal:__ Automate the creation of missing documentation.

1. Open the Chat panel (ensure no specific text is highlighted).
2. Prompt:
```
Generate a professional README.md for this project. Include an overview of the Flask backend, the Streamlit frontend, and instructions on how to install requirements and run the app.
```

Talk Track:
> "Developers are often tasked with documentation, a tedious yet important task. Gemini can handle this in seconds, ensuring our project is handoff-ready and compliant while developers can focus on the main goal of their work: building and innovating."

### Velocity (The "New Feature" Use Case)
__Goal:__ Add a missing API endpoint to handle VIP logic.

1. Open api/main.py.
2. Scroll to the bottom of the file (before the if __name__ block).
3. Prompt:
```
I need to add a new endpoint /vip_check/{player_id}. If a player has wagered over $15,000 lifetime, return status 'VIP', otherwise 'Standard'. Use the existing get_mock_wagers function to calculate this.
```

Talk Track:
> "Notice that Gemini didn't just paste generic code. It found our existing helper function get_mock_wagers and used it correctly. This is context-aware coding."

### Modernization (The "Refactor" Use Case)
__Goal:__ Migrate legacy Flask code to modern FastAPI.

__Part A: Generate Models__
1. Open api/models.py (It is currently empty).
2. Prompt:
```
Look at data/mock_db.py and create Pydantic models in api/models.py to represent a Player and a Wager.
```
3. Action: Accept/Insert the code.

__Part B: The Refactor__

1. Open api/main.py.
2. Prompt:
```
Refactor this entire file to use FastAPI instead of Flask. Use the logic in api/logic.py and the Pydantic models we just created in api/models.py. Keep the same endpoints.
```

Talk Track:
> "This is the most powerful part. Migrating frameworks usually takes weeks of copy-pasting. Gemini handles the syntax translation (changing @app.route to @app.get, etc.), allowing your senior engineers to focus on architecture rather than boilerplate."