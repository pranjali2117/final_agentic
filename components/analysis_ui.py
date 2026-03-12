import streamlit as st
from datetime import datetime
from database import add_history, get_history
from crewai import Crew, Process

def home_page(st_user, create_tasks_fn, planner_agent, analyst_agent, reporter_agent):
    st.title(f"Welcome, {st_user[1]}! 🏏")
    st.markdown("Enter any sports match to get a deep AI analysis report.")
    
    user_goal = st.text_input("Enter Sports Analysis Request", placeholder="Example: India vs Australia 2023 World Cup Final", label_visibility="collapsed")
    
    if st.button("🚀 Start Deep Analysis", key="start_analysis_btn"):
        if not user_goal:
            st.warning("Please enter a query.")
            return

        with st.status("⚙️ Sportlytics AI Analyzing...", expanded=True) as status:
            try:
                now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                tasks = create_tasks_fn(planner_agent, analyst_agent, reporter_agent)
                crew = Crew(agents=[planner_agent, analyst_agent, reporter_agent], tasks=tasks, process=Process.sequential, verbose=True)
                
                result = crew.kickoff(inputs={"goal": user_goal, "current_time": now})
                final_report = result.raw if hasattr(result, "raw") else str(result)
                
                add_history(st_user[0], user_goal, final_report)
                
                status.update(label="✅ Analysis Complete", state="complete")
                
                st.divider()
                st.subheader("📊 Sportlytics Deep Report")
                st.markdown(final_report)
                
                st.download_button(label="📥 Download Report", data=final_report, file_name=f"Sportlytics_{user_goal.replace(' ', '_')}.md", mime="text/markdown")
                
            except Exception as e:
                st.error(f"Run Error: {e}")

def history_page(st_user):
    st.title("📂 Your Analysis History")
    history = get_history(st_user[0])
    if not history:
        st.info("You haven't performed any analysis yet.")
    else:
        for query, result, timestamp in history:
            with st.expander(f"🔍 {query} - {timestamp}"):
                st.markdown(result)
                st.download_button(label="📥 Download This Report", data=result, file_name=f"Sportlytics_{query.replace(' ', '_')}.md", mime="text/markdown", key=f"dl_{timestamp}")
