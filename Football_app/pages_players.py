from __future__ import annotations

import pandas as pd
import streamlit as st

from utils import get_level_options, get_position_options, initialize_player_state


PLAYER_TABLE_COLUMNS = [
    "name",
    "level",
    "position",
    "school",
    "prefecture",
    "fastball_velocity_kmh",
    "batting_avg",
    "obp",
    "availability_status",
]


def render_player_table(df: pd.DataFrame) -> None:
    if df.empty:
        st.warning("No players match the current filters.")
        return

    st.dataframe(
        df[PLAYER_TABLE_COLUMNS]
        .rename(
            columns={
                "fastball_velocity_kmh": "FB Velo (km/h)",
                "batting_avg": "AVG",
                "obp": "OBP",
                "availability_status": "Availability",
            }
        )
        .sort_values("name"),
        use_container_width=True,
    )


def add_player_form() -> None:
    st.subheader("Add a Prospect")
    with st.form("add_player"):
        left, right = st.columns(2)
        with left:
            name = st.text_input("Full Name")
            age = st.number_input("Age", min_value=15, max_value=24, value=18)
            level = st.selectbox("Level", ["High School", "College"])
            position = st.text_input("Primary Position")
            school = st.text_input("School / Club")
            prefecture = st.text_input("Prefecture")
        with right:
            bats = st.selectbox("Bats", ["R", "L", "Switch"], index=0)
            throws = st.selectbox("Throws", ["R", "L"], index=0)
            fastball_velocity = st.number_input("Fastball Velocity (km/h)", min_value=0, max_value=170, value=0)
            batting_avg = st.number_input("Batting Average", min_value=0.0, max_value=1.0, value=0.0, format="%.3f")
            obp = st.number_input("On-base Percentage", min_value=0.0, max_value=1.0, value=0.0, format="%.3f")
            era = st.number_input("ERA", min_value=0.0, max_value=15.0, value=0.0, format="%.2f")
            innings = st.number_input("Innings Pitched", min_value=0.0, max_value=200.0, value=0.0)
        top_metrics = st.text_area("Key Metrics / Notes")
        video_url = st.text_input("Highlight Video URL")
        contact_email = st.text_input("Contact Email")
        availability = st.text_input("Availability Status", value="Open for conversations")

        submitted = st.form_submit_button("Save Prospect")
        if submitted:
            if not name.strip():
                st.error("Player name is required.")
                return

            new_player = pd.DataFrame(
                [
                    {
                        "name": name,
                        "age": int(age),
                        "level": level,
                        "position": position,
                        "school": school,
                        "prefecture": prefecture,
                        "bats": bats,
                        "throws": throws,
                        "fastball_velocity_kmh": fastball_velocity or None,
                        "batting_avg": batting_avg or None,
                        "obp": obp or None,
                        "era": era or None,
                        "innings_pitched": innings or None,
                        "top_metrics": top_metrics,
                        "video_url": video_url,
                        "contact_email": contact_email,
                        "availability_status": availability,
                    }
                ]
            )
            st.session_state.players = pd.concat([st.session_state.players, new_player], ignore_index=True)
            st.success(f"Added {name} to the prospect list.")


def main() -> None:
    initialize_player_state()
    st.header("Prospect Database")
    st.caption("Filter and manage the current roster of prospects")

    base_df = st.session_state.players.copy()

    with st.expander("Filter Prospects", expanded=True):
        col1, col2, col3 = st.columns(3)
        with col1:
            selected_level = st.selectbox("Level", get_level_options(base_df))
        with col2:
            selected_position = st.selectbox("Position", get_position_options(base_df))
        with col3:
            prefecture_filter = st.text_input("Prefecture contains", value="")

        filtered = base_df
        if selected_level != "All":
            filtered = filtered[filtered["level"] == selected_level]
        if selected_position != "All":
            filtered = filtered[filtered["position"].str.contains(selected_position, case=False, na=False)]
        if prefecture_filter:
            filtered = filtered[filtered["prefecture"].str.contains(prefecture_filter, case=False, na=False)]

    render_player_table(filtered)

    st.markdown("---")
    add_player_form()
