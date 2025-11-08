# High School Football Team Manager

A Streamlit web application for managing a high school football program, including pages for attendance, practice scripts, reminders, communication, health tracking, and scheduling.

## Prerequisites
- Python 3.10 or newer
- (Optional) [virtualenv](https://docs.python.org/3/library/venv.html) for dependency isolation

## Local Setup
1. Clone this repository and move into the project root:
   ```bash
   git clone <your-fork-url>
   cd football
   ```
2. Create and activate a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. Install the project dependencies from the repository root:
   ```bash
   pip install -r requirements.txt
   ```

## Running the App
From the repository root, launch Streamlit and point it at the main application module:
```bash
streamlit run Football_app/app.py
```
Streamlit will host the UI at `http://localhost:8501` by default.

## Development Tips
- Streamlit auto-reloads when you save changes to files in `Football_app/`.
- To lint or reformat code, follow your preferred tooling (e.g., `ruff`, `black`).
- When opening a pull request, use **Create a merge commit** unless your team has agreed on a different merge strategy. This option preserves the branch history, which is useful for tracking changes across multiple commits.

## License
This project is distributed under the terms of the MIT License. See [`LICENSE`](LICENSE) for details.
