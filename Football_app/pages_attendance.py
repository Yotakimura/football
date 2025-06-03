import streamlit as st
import pandas as pd
from datetime import date

ATTENDANCE_FILE = "attendance.csv"

def load_attendance():
    try:
        return pd.read_csv(ATTENDANCE_FILE)
    except FileNotFoundError:
        return pd.DataFrame(columns=["Date", "Player", "Present"])

def save_attendance(df):
    df.to_csv(ATTENDANCE_FILE, index=False)

def main():
    st.header("Practice Attendance Tracker")

    players = st.text_area("Enter player names (one per line):").splitlines()
    today = date.today().strftime("%Y-%m-%d")

    if players:
        st.subheader(f"Attendance for {today}")
        attendance = {player: st.checkbox(player) for player in players}

        if st.button("Submit Attendance"):
            df = load_attendance()
            for player in players:
                df = pd.concat([df, pd.DataFrame([{"Date": today, "Player": player, "Present": attendance[player]}])], ignore_index=True)
            save_attendance(df)
            st.success("Attendance submitted!")

    st.subheader("Attendance History")
    df = load_attendance()
    st.dataframe(df)

    st.download_button(
        "Export as CSV",
        df.to_csv(index=False).encode("utf-8"),
        "attendance_history.csv",
        "text/csv"
    )
