import streamlit as st
import os
import sys
import re
from datetime import datetime

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

# ---------------- CALLBACK ---------------- #

def streamlit_callback(step_output):
    raw_text = str(step_output)

    if "Failed to parse" in raw_text:
        return

    thought = re.search(r"thought=['\"](.*?)['\"]", raw_text, re.DOTALL)
    output = re.search(r"output=['\"](.*?)['\"]", raw_text, re.DOTALL)

    if thought:
        clean = thought.group(1).replace('\\n', '\n').strip()
        if clean:
            st.markdown("### 🤔 Agent Strategy")
            st.info(clean)

    if output:
        clean = output.group(1).replace('\\n', '\n').strip()
        if clean not in ["{}", "{", "None", ""]:
            st.markdown("### ⚡ Task Output")
            st.success(clean)

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="Sports Analyst",
    page_icon="🏏",
    layout="wide"
)

# ---------------- HEADER ---------------- #

st.title("🏏 Sports Analysis Assistant")

st.markdown(
"""
This application uses a **multi-agent AI system** to analyze sports data and produce insights.

**Planner Agent:**  
The planner interprets your request, determines what sports information is needed, and creates a structured plan for the other agents to follow during the analysis process.
"""
)

st.divider()

# ---------------- USER INPUT ---------------- #

st.subheader("🔎 Enter Sports Analysis Request")

user_goal = st.text_input(
    "",
    placeholder="Example: India vs New Zealand latest match statistics and analysis"
)

start_button = st.button("🚀 Start Analysis", use_container_width=True)

# ---------------- EXECUTION ---------------- #

if start_button:

    if not user_goal:
        st.warning("Please enter a sports query first.")
        st.stop()

    planner_agent.step_callback = streamlit_callback
    analyst_agent.step_callback = streamlit_callback
    reporter_agent.step_callback = streamlit_callback

    with st.status("⚙️ Running AI agents...", expanded=True) as status:

        try:
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            tasks = create_tasks(
                planner_agent,
                analyst_agent,
                reporter_agent
            )

            crew = Crew(
                agents=[planner_agent, analyst_agent, reporter_agent],
                tasks=tasks,
                process=Process.sequential,
                verbose=True
            )

            result = crew.kickoff(
                inputs={
                    "goal": user_goal,
                    "current_time": now
                }
            )

            status.update(
                label="✅ Analysis Complete",
                state="complete"
            )

            st.divider()

            # ---------- FINAL REPORT ---------- #

            st.subheader("📊 Final Sports Analysis Report")

            final_report = result.raw if hasattr(result, "raw") else str(result)

            with st.container(border=True):
                st.markdown(final_report.strip("`"))

        except Exception as e:
            st.error(f"Run Error: {e}")

st.markdown("---")
st.caption("Created by D707")