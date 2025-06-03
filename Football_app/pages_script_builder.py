import streamlit as st
import pandas as pd
import json
from datetime import date

SCRIPTS_FILE = "practice_scripts.json"

def load_scripts():
    try:
        with open(SCRIPTS_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_scripts(scripts):
    with open(SCRIPTS_FILE, "w") as f:
        json.dump(scripts, f)

def main():
    st.header("Practice Script Builder")

    scripts = load_scripts()
    script_names = list(scripts.keys())

    st.subheader("Load or Create Practice Script")
    selected_script = st.selectbox("Choose script to load or enter a new name:", [""] + script_names)
    if selected_script and selected_script in scripts:
        script = scripts[selected_script]
    else:
        script = []

    if st.button("Load Script") and selected_script in scripts:
        st.session_state['script'] = script

    if 'script' not in st.session_state:
        st.session_state['script'] = script

    st.subheader("Add Drill")
    drill = st.text_input("Drill Name")
    group = st.text_input("Group (e.g., Offense, Defense, WRs)")
    time = st.number_input("Time (minutes)", min_value=1, max_value=60, value=10)
    if st.button("Add Drill"):
        st.session_state['script'].append({"Drill": drill, "Group": group, "Time": time})

    st.subheader("Current Practice Script")
    df = pd.DataFrame(st.session_state['script'])
    st.dataframe(df)

    script_name = st.text_input("Save Script As", value=selected_script if selected_script else f"Practice_{date.today()}")
    if st.button("Save Script"):
        scripts[script_name] = st.session_state['script']
        save_scripts(scripts)
        st.success("Script saved!")

    if st.button("Clear Script"):
        st.session_state['script'] = []

    if st.button("Export Script as CSV") and not df.empty:
        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button("Download CSV", csv, f"{script_name}.csv", "text/csv")
