
import streamlit as st
import pandas as pd

st.set_page_config(page_title="IPL Match Predictor", layout="centered")
st.title("🏏 IPL Match Predictor: MI vs RCB")

# Sample data of past head-to-head matches
matches_data = {
    'Team1': ['MI'] * 20 + ['RCB'] * 14,
    'Team2': ['RCB'] * 34,
    'Winner': ['MI'] * 20 + ['RCB'] * 14
}

df = pd.DataFrame(matches_data)

# Count the number of wins
win_counts = df['Winner'].value_counts()
mi_wins = win_counts.get('MI', 0)
rcb_wins = win_counts.get('RCB', 0)

# Input for venue
venue = st.selectbox("Select Match Venue:", ["Wankhede Stadium, Mumbai", "Chinnaswamy Stadium, Bengaluru", "Neutral Ground"])

# Determine home advantage
home_advantage = 'MI' if 'Mumbai' in venue else 'RCB' if 'Bengaluru' in venue else None

# Last match winner (can be dynamic)
recent_winner = st.radio("Who won the most recent encounter?", ["MI", "RCB"])

# Score system
scores = {'MI': 0, 'RCB': 0}
if home_advantage:
    scores[home_advantage] += 1
scores['MI' if mi_wins > rcb_wins else 'RCB'] += 1
scores[recent_winner] += 1

# Final prediction
predicted_winner = 'MI' if scores['MI'] > scores['RCB'] else 'RCB'

# Display Results
st.subheader("📊 Match Stats")
st.write(f"**Total MI Wins:** {mi_wins}")
st.write(f"**Total RCB Wins:** {rcb_wins}")
st.write(f"**Venue:** {venue} (Advantage: {home_advantage if home_advantage else 'None'})")
st.write(f"**Last Match Winner:** {recent_winner}")

st.markdown("---")
st.success(f"🎯 **Predicted Winner: {predicted_winner}**")
