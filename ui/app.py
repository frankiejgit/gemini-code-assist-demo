import streamlit as st
import pandas as pd
import requests
import plotly.express as px

API_URL = "http://127.0.0.1:5000"

st.set_page_config(page_title="Player Risk Admin", layout="wide")
st.title("🎸 Digital Casino: Player Risk Portal")

# Sidebar
st.sidebar.header("Player Lookup")

# Fetch Players
try:
    response = requests.get(f"{API_URL}/players")
    if response.status_code == 200:
        players = response.json()
        player_map = {p['name']: p['id'] for p in players}
        selected_name = st.sidebar.selectbox("Select Player", list(player_map.keys()))
        selected_id = player_map[selected_name]
    else:
        st.error("Failed to fetch players.")
        st.stop()
except requests.exceptions.ConnectionError:
    st.error(f"Cannot connect to API at {API_URL}. Is api/main.py running?")
    st.stop()

if selected_id:
    # Fetch Details
    p_data = requests.get(f"{API_URL}/players/{selected_id}").json()
    risk_data = requests.get(f"{API_URL}/risk/{selected_id}").json()
    wagers_data = requests.get(f"{API_URL}/wagers/{selected_id}").json()

    # Key Metrics
    col1, col2, col3 = st.columns(3)
    col1.metric("Player Name", p_data['name'])
    col2.metric("Tier", p_data['tier'])
    col3.metric("Risk Level", risk_data['risk_level'], f"Score: {risk_data['risk_score']}")

    # Wager Analysis
    st.subheader("Wager History")
    if wagers_data:
        df = pd.DataFrame(wagers_data)
        
        # Simple stats
        wins = df[df['result'] == 'win'].shape[0]
        losses = df[df['result'] == 'loss'].shape[0]
        st.write(f"**Win/Loss Record:** {wins} Wins / {losses} Losses")

        # Chart
        fig = px.bar(df, x='game', y='amount', color='result', title="Betting Volume by Game")
        st.plotly_chart(fig, use_container_width=True)
        
        # Table
        st.dataframe(df)
    else:
        st.info("No wagers found for this player.")