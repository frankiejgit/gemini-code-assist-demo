import streamlit as st
import pandas as pd
import requests
import plotly.express as px

API_URL = "http://127.0.0.1:5000"

st.set_page_config(page_title="Environmental Sensor Dashboard", layout="wide")
st.title("🌱 Environmental Research: Sensor Health Portal")

# Sidebar
st.sidebar.header("Station Lookup")

# Fetch Stations
try:
    response = requests.get(f"{API_URL}/stations")
    if response.status_code == 200:
        stations = response.json()
        station_map = {s['name']: s['id'] for s in stations}
        selected_name = st.sidebar.selectbox("Select Sensor Station", list(station_map.keys()))
        selected_id = station_map[selected_name]
    else:
        st.error("Failed to fetch sensor stations.")
        st.stop()
except requests.exceptions.ConnectionError:
    st.error(f"Cannot connect to API at {API_URL}. Is api/main.py running?")
    st.stop()

if selected_id:
    # Fetch Details
    s_data = requests.get(f"{API_URL}/stations/{selected_id}").json()
    status_data = requests.get(f"{API_URL}/anomaly/{selected_id}").json()
    readings_data = requests.get(f"{API_URL}/readings/{selected_id}").json()

    # Key Metrics
    col1, col2, col3 = st.columns(3)
    col1.metric("Station Name", s_data['name'])
    col2.metric("Model", s_data['model'])
    col3.metric("Severity Level", status_data['severity_level'], f"Score: {status_data['anomaly_score']}")

    # Reading Analysis
    st.subheader("Sensor Reading History")
    if readings_data:
        df = pd.DataFrame(readings_data)
        
        # Simple stats
        valid = df[df['status'] == 'valid'].shape[0]
        anomalies = df[df['status'] == 'anomaly'].shape[0]
        st.write(f"**Data Quality Summary:** {valid} Valid Readings / {anomalies} Anomalies Detected")

        # Chart
        fig = px.bar(df, x='metric', y='value', color='status', title="Measurement Value by Metric Type")
        st.plotly_chart(fig, use_container_width=True)
        
        # Table
        st.dataframe(df)
    else:
        st.info("No readings found for this station.")
