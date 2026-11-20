"""Streamlit Community Cloud portfolio adapter for face-detector.

This does not replace the original implementation.
"""
from pathlib import Path

import streamlit as st

TITLE = "Face Landmark Tracker"
ICON = "👁️"
DESC = "OpenCV and MediaPipe code for eye, mouth and head-roll landmark indicators."
CATEGORY = "Desktop computer vision"
NOTICE = "Webcam landmark processing remains in the original local OpenCV application. This Streamlit portfolio entry does not perform inference."
GITHUB = "https://github.com/mohsinattasial/face-detector"
VERCEL = "https://mohsin-face-landmarks.vercel.app"
LOCAL_COMMAND = "python detector.py"
FEATURES = ["MediaPipe face mesh","Eye and mouth ratios","Head-roll estimate"]

st.set_page_config(page_title=TITLE + " | Mohsin Atta", page_icon=ICON, layout="wide")
st.caption("Mohsin Atta · GitHub Portfolio · Streamlit Cloud edition")
st.title(ICON + " " + TITLE)
st.write(DESC)
st.caption(CATEGORY)

left, right = st.columns(2)
with left:
    st.link_button("GitHub source code", GITHUB, use_container_width=True)
with right:
    st.link_button("Existing browser version", VERCEL, use_container_width=True)

st.info(NOTICE)
with st.expander("Original project and features", expanded=False):
    for feature in FEATURES:
        st.write("• " + feature)
    st.code(LOCAL_COMMAND, language="bash")

st.subheader("Project overview")
st.write("This page is a deployable portfolio presentation of the original repository. Use the GitHub link above to inspect the code and run it in its intended local environment.")

st.divider()
st.caption("© 2026 Mohsin Atta · Educational portfolio · MIT-licensed original code where applicable")
