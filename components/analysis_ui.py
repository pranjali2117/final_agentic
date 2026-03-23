import streamlit as st
from datetime import datetime
from database import add_history, get_history
from crewai import Crew, Process


# ---------------- HOME PAGE ---------------- #
def home_page(st_user, create_tasks_fn, planner_agent, analyst_agent, reporter_agent):

    st.title("🏟️ Sports Planning")
    st.caption(f"Welcome 👋")

    st.markdown(
        "Analyze any sports match using **AI-powered multi-agent analysis**."
    )

    st.divider()

    # Centered Input Section
    col1, col2, col3 = st.columns([1,2,1])

    with col2:
        user_goal = st.text_input(
            "Enter Match",
            placeholder="India vs Australia 2023 World Cup Final",
            label_visibility="collapsed"
        )

        start = st.button("🚀 Start Deep Analysis", use_container_width=True)

    if start:

        if not user_goal:
            st.warning("⚠️ Please enter a sports query.")
            return

        with st.status("⚙️ Sportlytics AI is analyzing...", expanded=True) as status:

            try:
                now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                tasks = create_tasks_fn(planner_agent, analyst_agent, reporter_agent)

                crew = Crew(
                    agents=[planner_agent, analyst_agent, reporter_agent],
                    tasks=tasks,
                    process=Process.sequential,
                    verbose=True
                )

                result = crew.kickoff(inputs={"goal": user_goal, "current_time": now})

                final_report = result.raw if hasattr(result, "raw") else str(result)

                add_history(st_user[0], user_goal, final_report)

                status.update(label="✅ Analysis Complete", state="complete")

                st.divider()

                st.subheader("📊 AI Match Report")

                with st.container(border=True):
                    st.markdown(final_report)

                st.download_button(
                    "📥 Download Report",
                    data=final_report,
                    file_name=f"Sportlytics_{user_goal.replace(' ', '_')}.md",
                    mime="text/markdown",
                    use_container_width=True
                )

            except Exception as e:
                st.error(f"Run Error: {e}")


# ---------------- HISTORY PAGE ---------------- #
def history_page(st_user):

    st.title("📂 Analysis History")

    history = get_history(st_user[0])

    if not history:
        st.info("No analysis performed yet.")
        return

    for query, result, timestamp in history:

        with st.container(border=True):

            st.markdown(f"### 🔎 {query}")
            st.caption(f"🕒 {timestamp}")

            with st.expander("View Report"):

                st.markdown(result)

                st.download_button(
                    "📥 Download Report",
                    data=result,
                    file_name=f"Sportlytics_{query.replace(' ', '_')}.md",
                    mime="text/markdown",
                    key=f"dl_{timestamp}",
                    use_container_width=True
                )