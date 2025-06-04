import streamlit as st
import datetime

def main():
# --- Injury Tracking ---
st.header("Injury Tracking")
if "injuries" not in st.session_state:
    st.session_state["injuries"] = []

with st.form("injury_form"):
    player = st.text_input("Player Name")
    injury = st.text_input("Injury Description")
    status = st.selectbox("Status", ["Active", "Rehab", "Cleared"])
    notes = st.text_area("Notes")
    return_date = st.date_input("Expected Return Date", value=datetime.date.today())
    privacy = st.selectbox("Who can see?", ["Coach/Medical Staff Only", "All Coaches"])
    submit = st.form_submit_button("Add Injury")
    if submit and player and injury:
        st.session_state["injuries"].append({
            "player": player,
            "injury": injury,
            "status": status,
            "notes": notes,
            "return_date": return_date,
            "privacy": privacy,
            "date": datetime.datetime.now()
        })

st.subheader("Injury List")
for inj in st.session_state["injuries"]:
    st.write(f"**Player:** {inj['player']} | **Status:** {inj['status']} | **Return:** {inj['return_date']} | **Privacy:** {inj['privacy']}")
    st.write(f"_{inj['injury']}_")
    if inj["notes"]:
        st.write(f"Notes: {inj['notes']}")
    st.markdown("---")

# --- Wellness Check-ins ---
st.header("Wellness Check-ins")
if "wellness" not in st.session_state:
    st.session_state["wellness"] = []

with st.form("wellness_form"):
    player_name = st.text_input("Player Name", key="wellness_name")
    sleep = st.slider("Hours of Sleep (last night)", 0, 12, 8)
    soreness = st.slider("Soreness Level (1=none, 10=worst)", 1, 10, 1)
    mood = st.selectbox("Mood", ["Great", "Good", "Okay", "Bad"])
    notes = st.text_area("Any notes or concerns?", key="wellness_notes")
    submit_wellness = st.form_submit_button("Submit Check-in")
    if submit_wellness and player_name:
        st.session_state["wellness"].append({
            "player": player_name,
            "sleep": sleep,
            "soreness": soreness,
            "mood": mood,
            "notes": notes,
            "date": datetime.datetime.now()
        })

st.subheader("Recent Wellness Check-ins")
for w in st.session_state["wellness"][-10:][::-1]:
    st.write(f"**Player:** {w['player']} | **Sleep:** {w['sleep']}h | **Soreness:** {w['soreness']} | **Mood:** {w['mood']} | {w['date'].strftime('%Y-%m-%d')}")
    if w["notes"]:
        st.write(f"Notes: {w['notes']}")
    st.markdown("---")

# (Optional) Detect red flags
red_flags = [w for w in st.session_state["wellness"] if w["sleep"] < 5 or w["soreness"] > 7 or w["mood"] == "Bad"]
if red_flags:
    st.error("🚩 Red Flags Detected in Recent Check-ins!")
    for w in red_flags[-5:][::-1]:
        st.write(f"{w['player']} on {w['date'].strftime('%Y-%m-%d')}: Sleep={w['sleep']}, Soreness={w['soreness']}, Mood={w['mood']}")
