from __future__ import annotations

import altair as alt
import pandas as pd
import streamlit as st

from utils import initialize_player_state


def build_velocity_chart(df: pd.DataFrame) -> alt.Chart:
    pitching_df = df.dropna(subset=["fastball_velocity_kmh"])
    if pitching_df.empty:
        return alt.Chart(pd.DataFrame({"name": [], "fastball_velocity_kmh": []}))

    return (
        alt.Chart(pitching_df)
        .mark_bar(color="#002d62")
        .encode(
            x=alt.X("fastball_velocity_kmh", bin=alt.Bin(maxbins=10), title="Fastball Velocity (km/h)"),
            y=alt.Y("count()", title="Number of Pitchers"),
        )
    )


def build_hitting_chart(df: pd.DataFrame) -> alt.Chart:
    hitting_df = df.dropna(subset=["batting_avg"]).sort_values("batting_avg", ascending=False)
    if hitting_df.empty:
        return alt.Chart(pd.DataFrame({"name": [], "batting_avg": []}))

    return (
        alt.Chart(hitting_df)
        .mark_bar(color="#e4002b")
        .encode(
            x=alt.X("name", sort="-y", title="Player"),
            y=alt.Y("batting_avg", title="Batting Average"),
            tooltip=["name", "level", "position", "batting_avg", "obp"],
        )
    )


def main() -> None:
    initialize_player_state()
    st.header("Analytics Sandbox")
    st.caption("A preview of the data products scouts will receive")

    df = st.session_state.players.copy()

    cols = st.columns(2)
    with cols[0]:
        st.subheader("Pitching Velocity Distribution")
        chart = build_velocity_chart(df)
        if chart.data.empty:
            st.info("Add pitchers with velocity data to populate this chart.")
        else:
            st.altair_chart(chart, use_container_width=True)

    with cols[1]:
        st.subheader("Top Hitters by Average")
        hitting_chart = build_hitting_chart(df.head(15))
        if hitting_chart.data.empty:
            st.info("Add hitters with batting data to populate this chart.")
        else:
            st.altair_chart(hitting_chart, use_container_width=True)

    st.markdown("---")
    st.subheader("KPI Snapshot")
    col1, col2, col3 = st.columns(3)
    col1.metric("Average Fastball", f"{df['fastball_velocity_kmh'].dropna().mean():.1f} km/h" if df['fastball_velocity_kmh'].dropna().any() else "–")
    col2.metric("Median Batting AVG", f"{df['batting_avg'].dropna().median():.3f}" if df['batting_avg'].dropna().any() else "–")
    col3.metric("Prospects per Prefecture", df['prefecture'].nunique())

    st.markdown(
        """
        _Upcoming modules will include swing/throw biomechanics, pitch movement tracking, and
        longitudinal player development dashboards._
        """
    )
