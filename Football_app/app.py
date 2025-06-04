import streamlit as st
import pages_attendance
import pages_script_builder
import pages_reminders
import pages_communication
import pages_health
import pages_calendar # <-- Add this import

PAGES = {
    "Practice Attendance": pages_attendance.main,
    "Practice Script Builder": pages_script_builder.main,
    "Automated Reminders": pages_reminders.main,
    "Communication Hub": pages_communication.main,
    "Health & Wellness": pages_health.main,
    "Calendar & Scheduling": pages_calendar.main, # <-- Add this line
}

st.title("High School Football Team Manager")

page = st.sidebar.radio("Navigation", list(PAGES.keys()))
PAGES[page]()
