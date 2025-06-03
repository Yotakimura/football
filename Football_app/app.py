{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2fbafddf-1ed6-4e77-ab23-7dc1f8926735",
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
from pages import attendance, script_builder, reminders

PAGES = {
    "Practice Attendance": attendance.main,
    "Practice Script Builder": script_builder.main,
    "Automated Reminders": reminders.main,
}

st.title("High School Football Team Manager")

page = st.sidebar.radio("Navigation", list(PAGES.keys()))
PAGES[page]()