from __future__ import annotations

from pathlib import Path
from typing import List

import pandas as pd
import streamlit as st

DATA_PATH = Path(__file__).resolve().parent / "data"


def load_player_data() -> pd.DataFrame:
    """Load the baseline player dataset for the session."""
    data_file = DATA_PATH / "sample_players.csv"
    df = pd.read_csv(data_file)
    df["age"] = df["age"].astype(int)
    df["availability_status"] = df["availability_status"].fillna("Unknown")
    return df


def initialize_player_state() -> None:
    """Ensure player and video state containers exist."""
    if "players" not in st.session_state:
        st.session_state.players = load_player_data()

    if "video_library" not in st.session_state:
        st.session_state.video_library = []

    if "scout_notes" not in st.session_state:
        st.session_state.scout_notes = []


def get_level_options(df: pd.DataFrame) -> List[str]:
    levels = ["All"]
    levels.extend(sorted(df["level"].dropna().unique()))
    return levels


def get_position_options(df: pd.DataFrame) -> List[str]:
    positions = ["All"]
    positions.extend(sorted(df["position"].dropna().unique()))
    return positions
