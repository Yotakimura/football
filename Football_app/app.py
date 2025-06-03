import streamlit as st
import pages_attendance
import pages_script_builder
import pages_reminders

PAGES = {
    "Practice Attendance": pages_attendance.main,
    "Practice Script Builder": pages_script_builder.main,
    "Automated Reminders": pages_reminders.main,
}

st.title("High School Football Team Manager")

page = st.sidebar.radio("Navigation", list(PAGES.keys()))
PAGES[page]()
