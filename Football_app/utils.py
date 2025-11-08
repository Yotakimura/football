from __future__ import annotations

from datetime import datetime
import json
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


def _parse_timestamp(value: str | None) -> datetime:
    """Convert an ISO 8601 timestamp string to a datetime object."""
    if not value:
        return datetime.utcnow()
    try:
        return datetime.fromisoformat(value)
    except ValueError:
        return datetime.utcnow()


def load_video_library() -> list[dict]:
    """Seed the session with example video submissions."""
    data_file = DATA_PATH / "sample_videos.json"
    if not data_file.exists():
        return []

    entries = json.loads(data_file.read_text(encoding="utf-8"))
    for entry in entries:
        entry["timestamp"] = _parse_timestamp(entry.get("timestamp"))
        entry.setdefault("video_bytes", None)
    return entries


def load_scout_notes() -> list[dict]:
    """Seed the session with example scouting notes."""
    data_file = DATA_PATH / "sample_scout_notes.json"
    if not data_file.exists():
        return []

    entries = json.loads(data_file.read_text(encoding="utf-8"))
    for entry in entries:
        entry["timestamp"] = _parse_timestamp(entry.get("timestamp"))
    return entries


def initialize_player_state() -> None:
    """Ensure player and video state containers exist."""
    if "players" not in st.session_state:
        st.session_state.players = load_player_data()

    if "video_library" not in st.session_state:
        st.session_state.video_library = load_video_library()

    if "scout_notes" not in st.session_state:
        st.session_state.scout_notes = load_scout_notes()


def get_level_options(df: pd.DataFrame) -> List[str]:
    levels = ["All"]
    levels.extend(sorted(df["level"].dropna().unique()))
    return levels


def get_position_options(df: pd.DataFrame) -> List[str]:
    positions = ["All"]
    positions.extend(sorted(df["position"].dropna().unique()))
    return positions
