"""Streamlit entry point for the High School Football Team Manager app."""

import streamlit as st

from pages_attendance import main as attendance_main
from pages_script_builder import main as script_builder_main
from pages_reminders import main as reminders_main
from pages_communication import main as communication_main
from pages_health import main as health_main
from pages_calendar import main as calendar_main

PAGES = {
    "Practice Attendance": attendance_main,
    "Practice Script Builder": script_builder_main,
    "Automated Reminders": reminders_main,
    "Communication Hub": communication_main,
    "Health & Wellness": health_main,
    "Calendar & Scheduling": calendar_main,
}


def run() -> None:
    """Render the selected page."""
    st.set_page_config(page_title="High School Football Team Manager", layout="wide")
    st.title("High School Football Team Manager")

    page_label = st.sidebar.radio("Navigation", list(PAGES.keys()))
    PAGES[page_label]()


if __name__ == "__main__":
    run()
