# Japanese Baseball Prospect Scouting Platform (Prototype)

This repository contains a Streamlit-based prototype for a scouting and data-sharing
platform designed to connect Japanese high school and college baseball players with
U.S. organizations. The application focuses on transparency, objective evaluation,
and secure collaboration during the earliest stages of the product roadmap.

## Key Features

- **Player Profiles** – Filterable roster with academic, athletic, and contact details.
- **Video Library** – Upload highlight clips or link to external streaming platforms.
- **Analytics Sandbox** – Explore example metrics and visualizations for scouting.
- **Scout Workspace** – Track outreach, record evaluations, and monitor prospect status.

## Getting Started

1. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```

2. Launch the prototype locally

   ```bash
   streamlit run Football_app/app.py
   ```

3. Explore each module using the sidebar navigation.
   - The prototype seeds the session with example prospects, highlight submissions, and scout notes so you can evaluate the end-to-end workflow immediately.

## Roadmap

Future iterations will incorporate computer-vision powered video breakdowns, automated
stat-sheet ingestion (via OCR and speech-to-text), private access controls for scouts, and
advanced analytics packages for partner organizations.
