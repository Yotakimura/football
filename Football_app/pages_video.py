from __future__ import annotations

from datetime import datetime

import streamlit as st

from utils import initialize_player_state


def render_video_gallery() -> None:
    if not st.session_state.video_library:
        st.info("No videos uploaded yet. Use the form below to share highlights.")
        return

    for entry in st.session_state.video_library:
        with st.expander(f"{entry['player_name']} – {entry['title']}", expanded=False):
            st.write(entry["description"] or "No description provided.")
            if entry.get("video_bytes"):
                st.video(entry["video_bytes"])
            if entry.get("external_url"):
                st.markdown(f"[Watch externally]({entry['external_url']})")
            st.caption(f"Uploaded {entry['timestamp'].strftime('%Y-%m-%d %H:%M')} by {entry['submitted_by']}")


def upload_video_form() -> None:
    st.subheader("Submit Highlight Footage")
    with st.form("upload_video"):
        player_name = st.text_input("Player Name")
        title = st.text_input("Title", value="Bullpen Session")
        description = st.text_area("Context / Notes")
        submitted_by = st.text_input("Submitted By (coach/player)")
        video_file = st.file_uploader("Upload MP4/MOV", type=["mp4", "mov", "m4v"])
        external_url = st.text_input("External Video URL (YouTube, Bilibili, etc.)")

        submitted = st.form_submit_button("Add to Library")
        if submitted:
            if not player_name.strip():
                st.error("Player name is required.")
                return
            if not video_file and not external_url:
                st.error("Upload a file or provide an external link.")
                return

            video_entry = {
                "player_name": player_name,
                "title": title or "Highlight",
                "description": description,
                "submitted_by": submitted_by or "Unknown",
                "timestamp": datetime.utcnow(),
                "video_bytes": video_file.read() if video_file else None,
                "external_url": external_url,
            }
            st.session_state.video_library.insert(0, video_entry)
            st.success("Video added to the shared library.")


def main() -> None:
    initialize_player_state()
    st.header("Video Upload & Library")
    st.caption("Centralize highlight footage for invited scouts")

    render_video_gallery()
    st.markdown("---")
    upload_video_form()
