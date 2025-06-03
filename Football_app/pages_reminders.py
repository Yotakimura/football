{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "43c846d7-0fa8-424c-a05f-05aa9162c376",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}


import streamlit as st
import smtplib
from email.message import EmailMessage

def send_email(subject, body, to_email, smtp_server, smtp_port, smtp_user, smtp_pass):
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = smtp_user
    msg["To"] = to_email
    msg.set_content(body)
    with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
        server.login(smtp_user, smtp_pass)
        server.send_message(msg)

def main():
    st.header("Automated Reminders (Email)")

    st.info("Set up your SMTP credentials in Streamlit secrets for security.")

    subject = st.text_input("Email Subject", "Practice Reminder")
    body = st.text_area("Email Body", "Don't forget about practice!")
    to_email = st.text_input("Send to (comma-separated emails)")

    if st.button("Send Reminder"):
        smtp_server = st.secrets["SMTP_SERVER"]
        smtp_port = st.secrets["SMTP_PORT"]
        smtp_user = st.secrets["SMTP_USER"]
        smtp_pass = st.secrets["SMTP_PASS"]
        for email in [e.strip() for e in to_email.split(",")]:
            try:
                send_email(subject, body, email, smtp_server, smtp_port, smtp_user, smtp_pass)
                st.success(f"Email sent to {email}")
            except Exception as e:
                st.error(f"Failed to send email to {email}: {e}")

    st.markdown("""
    **To use this feature:**
    1. Set your SMTP credentials in `.streamlit/secrets.toml`:
    ```
    SMTP_SERVER = "smtp.yourprovider.com"
    SMTP_PORT = 465
    SMTP_USER = "you@example.com"
    SMTP_PASS = "your_password"
    ```
    2. Enter the email addresses and content, then click send.
    """)