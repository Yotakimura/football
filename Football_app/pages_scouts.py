from __future__ import annotations

from datetime import datetime

import pandas as pd
import streamlit as st

from utils import initialize_player_state


def render_pipeline(df: pd.DataFrame) -> None:
    st.subheader("Recruitment Pipeline")
    status_counts = df["availability_status"].value_counts().rename_axis("Status").reset_index(name="Prospects")
    st.dataframe(status_counts, use_container_width=True)

    with st.expander("Full Contact Sheet"):
        st.dataframe(
            df[["name", "position", "school", "contact_email", "availability_status"]]
            .rename(columns={"contact_email": "Contact"})
            .sort_values("name"),
            use_container_width=True,
        )


def note_input(df: pd.DataFrame) -> None:
    st.subheader("Scout Notes")
    with st.form("scout_note"):
        player = st.selectbox("Select Prospect", df["name"].tolist())
        organization = st.text_input("Organization")
        evaluator = st.text_input("Evaluator")
        priority = st.select_slider("Priority", options=["Monitor", "Follow Up", "High"])
        notes = st.text_area("Evaluation Summary")

        submitted = st.form_submit_button("Log Note")
        if submitted:
            if not notes.strip():
                st.error("Enter an evaluation summary before submitting.")
                return

            entry = {
                "player": player,
                "organization": organization or "Unknown",
                "evaluator": evaluator or "Anonymous",
                "priority": priority,
                "notes": notes,
                "timestamp": datetime.utcnow(),
            }
            st.session_state.scout_notes.insert(0, entry)
            st.success("Note recorded.")

    if not st.session_state.scout_notes:
        st.info("No notes yet. Capture observations to build a shared view of each prospect.")
        return

    for note in st.session_state.scout_notes:
        with st.expander(f"{note['player']} – {note['priority']} priority"):
            st.markdown(note["notes"])
            st.caption(
                f"Logged {note['timestamp'].strftime('%Y-%m-%d %H:%M')} | "
                f"{note['organization']} – {note['evaluator']}"
            )


def main() -> None:
    initialize_player_state()
    st.header("Scout Workspace")
    st.caption("Coordinate outreach and share evaluations with trusted partners")

    df = st.session_state.players.copy()
    render_pipeline(df)

    st.markdown("---")
    note_input(df)
