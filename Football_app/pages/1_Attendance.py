{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4cc39955-beae-439f-9586-60e60819fbdc",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}


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
