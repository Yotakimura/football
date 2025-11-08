from __future__ import annotations

import streamlit as st

import pages_overview
import pages_players
import pages_video
import pages_analytics
import pages_scouts

st.set_page_config(page_title="JP Prospect Scout", page_icon="⚾", layout="wide")

PAGES = {
    "Overview": pages_overview.main,
    "Prospect Database": pages_players.main,
    "Video Library": pages_video.main,
    "Analytics Sandbox": pages_analytics.main,
    "Scout Workspace": pages_scouts.main,
}

st.sidebar.title("JP Prospect Scout")
selection = st.sidebar.radio("Navigate", list(PAGES.keys()))

PAGES[selection]()
