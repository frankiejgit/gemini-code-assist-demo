# Demo Guide: Gemini Code Assist for Environmental Research

**Goal:** Demonstrate the power of AI assistance for software engineers and researchers focusing on **Modernization**, **Documentation**, and **Cross-Language Interoperability**.

## Repository Overview
```text
gemini-code-assist-demo/
├── api/
│   ├── main.py            # Flask API (Station data endpoints)
│   ├── logic.py           # Anomaly detection logic (Explain Code target)
│   └── models.py          # TODO (Code generation target)
├── ui/
│   └── app.py             # Environmental Sensor Dashboard (Streamlit)
├── data/
│   ├── mock_db.py         # Mock Sensor Data Generator
│   └── sensor_readings.csv # Legacy batch data format (Java target)
└── legacy-java-service/
    └── StationDataProcessor.java # Legacy Java 8 Ingestion Engine
```

## Pre-Demo Setup

1. **Environment Setup**:
   ```bash
   # Create a virtual environment and install dependencies
   uv init
   uv venv
   source .venv/bin/activate
   uv pip install -r requirements.txt
   ```

2. **Start Services**:
   *   **Terminal 1**: `python api/main.py` (API starts on port 5000)
   *   **Terminal 2**: `streamlit run ui/app.py` (Dashboard opens in browser)

3. **Optional (Context Cleanup)**:
   *   Add `INSTRUCTIONS.md` to a `.aiexclude` file to ensure Gemini doesn't read the demo prompts.

---

## 🎬 Demo Flow

### Phase 1: Java Modernization (The "Legacy Tech Debt" Use Case)
**Goal:** Transform decades-old Java 8 boilerplate into modern Java 21+.

1. **Open**: `legacy-java-service/StationDataProcessor.java`.
2. **Action**: Highlight the `processAnomalies` method and the `StationAnomaly` class.
3. **Prompt**:
   ```text
   Refactor this data ingestion logic to use modern Java 21 features. 
   1. Replace StationAnomaly with a Java Record.
   2. Use try-with-resources for the BufferedReader.
   3. Use Java Streams and Lambdas to parse the CSV lines and sort the results.
   4. Use 'var' for local variables.
   ```
4. **Talk Track**:
   > "Stable but 'clunky' Java apps are common for historical data batching. Gemini can instantly modernize this code—removing manual resource management and anonymous classes—so we can focus on the data, not the boilerplate."

### Phase 2: Documentation (The "Scientific Compliance" Use Case)
**Goal:** Automate researcher-grade documentation for complex formulas.

1. **Open**: `api/logic.py`.
2. **Action**: Highlight the `calculate_anomaly_score` function.
3. **Prompt**:
   ```text
   Generate deep technical documentation for this anomaly detection logic. Explain the scientific thresholds and thresholds used (like calibration age). Suggest extracting magic numbers into descriptive constants.
   ```
4. **Talk Track**:
   > "Researchers must document exactly how 'Anomaly Scores' are derived for peer review. Gemini identifies hidden logic and 'magic numbers,' automatically documenting the scientific intent behind our raw code."

### Phase 3: Explain Code (The "Onboarding" Use Case)
**Goal:** Instantly understand system-wide behaviors.

1. **Open**: Chat Panel.
2. **Prompt**:
   ```text
   Explain the risk assessment flow in this project. How does a sensor's 'calibration_age_days' affect the final severity level across the Python and Java modules?
   ```
3. **Talk Track**:
   > "When a new researcher joins, they shouldn't spend days tracing code. Gemini instantly explains that sensors older than 365 days are penalized, providing high-level clarity on cross-module business rules."

### Phase 4: Velocity (The "Cross-Language Porting" Use Case)
**Goal:** Port a Python research algorithm into a Java production engine.

1. **Action**: Open `api/logic.py` and `StationDataProcessor.java` in a **Split View**.
2. **Prompt**:
   ```text
   I've updated the 'calculate_anomaly_score' in Python. Please port this logic into the Java 'calculateLegacyAnomalyScore' method. Ensure the Java implementation is idiomatic and maintains the same scientific rules.
   ```
3. **Talk Track**:
   > "The biggest bottleneck in research is moving logic from a Python notebook into a production-scale Java engine. Gemini acts as an instant translator, ensuring our production system is always in sync with our latest research."

### Phase 5: Code Generation (The "Modern Framework" Use Case)
**Goal:** Generate Pydantic models for a modernized API.

1. **Open**: `api/models.py`.
2. **Prompt**:
   ```text
   Look at the station data structures in data/mock_db.py and generate Pydantic v2 models in api/models.py to represent a SensorStation and a Reading.
   ```
3. **Talk Track**:
   > "Finally, as we modernize our stack, we need strong typing. Gemini can look at our mock data and generate all the Pydantic models we need to move from Flask to FastAPI, eliminating manual data entry."
