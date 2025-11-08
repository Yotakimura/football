from __future__ import annotations

import streamlit as st

from utils import initialize_player_state


def main() -> None:
    initialize_player_state()

    st.title("Japanese Baseball Prospect Scouting Platform")
    st.caption("Prototype environment for cross-border talent discovery")

    st.markdown(
        """
        ### Mission
        Build a transparent scouting bridge that surfaces Japanese high school and college talent for
        U.S. organizations that have limited coverage in the region. This prototype consolidates
        trusted data, curated video, and collaboration tools so that every prospect has an equal
        opportunity to be evaluated on merit.
        """
    )

    st.markdown("---")

    col1, col2, col3 = st.columns(3)
    col1.metric("Prospects Tracked", len(st.session_state.players))
    col2.metric("Video Submissions", len(st.session_state.video_library))
    col3.metric("Scout Notes Logged", len(st.session_state.scout_notes))

    st.markdown("---")

    st.subheader("Prototype Scope")
    st.markdown(
        """
        - **Player Profiles**: searchable roster with academic, athletic, and contact information.
        - **Video Hub**: upload highlight clips and share streaming-ready links.
        - **Analytics Sandbox**: surface baseline metrics and identify standout skills.
        - **Scout Workspace**: capture evaluations and monitor recruitment pipeline.
        """
    )

    st.info(
        "Future integrations will leverage computer vision for pitch tracking, speech-to-text for "
        "rapid stat ingestion, and secure sharing controls for invited scouts."
    )

    st.markdown("---")

    st.subheader("Implementation Roadmap")
    st.markdown(
        """
        1. Expand data ingestion via CSV, image OCR, and stat APIs.
        2. Layer in machine learning models for objective pitch and swing grading.
        3. Deploy private cloud infrastructure with access tiers for teams and agents.
        4. Monetize through premium analytics bundles and verified player promotions.
        """
    )
