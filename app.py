import streamlit as st
import os
import sys

# Local imports
from components.ui_utils import apply_custom_css, navbar
from components.auth_ui import login_page, signup_page, forgot_password_page
from components.analysis_ui import home_page, history_page

sys.path.append(os.path.dirname(__file__))

try:
    from crewai import Crew, Process
    from agents import planner_agent, analyst_agent, reporter_agent
    from tasks import create_tasks
except Exception as e:
    st.error(f"Environment Error: {e}. Try restarting VS Code.")
    st.stop()

os.environ["OTEL_SDK_DISABLED"] = "true"
os.environ["CREWAI_TELEMETRY_OPT_OUT"] = "true"

# ---------------- INITIALIZATION ---------------- #
apply_custom_css()

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'user' not in st.session_state:
    st.session_state.user = None
if 'page' not in st.session_state:
    st.session_state.page = "Login"

# ---------------- NAVIGATION & ROUTING ---------------- #
navbar()

if not st.session_state.logged_in:
    if st.session_state.page == "Signup":
        signup_page()
    elif st.session_state.page == "Forgot":
        forgot_password_page()
    else:
        login_page()
else:
    if st.session_state.page == "History":
        history_page(st.session_state.user)
    else:
        home_page(
            st.session_state.user, 
            create_tasks, 
            planner_agent, 
            analyst_agent, 
            reporter_agent
        )