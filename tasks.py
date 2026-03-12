from crewai import Task

# Notice the third argument here: 'reporter'
def create_tasks(planner, analyst, reporter):
    
# Task 1: Research and Plan
    research_task = Task(
        description="""1. Use the tavily_search tool to find the latest live score and match 
        summary for {goal}.
        2. Identify the ACTUAL WINNER and ACTUAL LOSER team names.
        3. Extract top 2 performers from BOTH teams. You MUST include their REAL NAMES and specific stats (e.g., Virat Kohli: 82 runs, Pathum Nissanka: 75 runs).
        4. Analyze the CRITICAL REASONS for the result (e.g., turning points, player mistakes, or strategy brilliance).
        Note: The current real-world time is {current_time}.""",
        expected_output="""A detailed raw data report containing:
        - Actual team names and final scores.
        - Winner and Loser team names.
        - Actual player names and their specific match stats.
        - In-depth reasoning for the match outcome.""",
        agent=planner
    )

    # Task 2: Validate and Schedule
    validation_task = Task(
        description="""1. Review the analysis data from the Lead Planner to ensure all real names (teams/players) are present.
        2. Use the check_resource tool to verify if 'MatchStats_DB' is ONLINE.
        3. Create a realistic execution schedule starting at {current_time}.""",
        expected_output="""A confirmation of database status and an execution timeline.""",
        agent=analyst
    )

    # Task 3: Deep Executive Report
    reporting_task = Task(
        description="""Synthesize the data into a premium Sports Analysis Report.
        CRITICAL: Do NOT use placeholders like 'Team A' or 'Player 1'. Use the ACTUAL names found by the planner.
        Format it as a single cohesive report with clear sections.""",
        expected_output="""A beautifully formatted Markdown report containing:
        1. 🏏 MATCH SUMMARY (Winner Team, actual scores, and match status)
        2. 🌟 TOP PERFORMERS (Actual player names and their stats for both teams)
        3. 🔍 WHY THEY WON/LOST (Deep technical analysis of tactical reasons and turning points)
        4. 🗄️ EXECUTION LOG (DB status and timeline)""",
        agent=reporter,
        context=[research_task, validation_task]
    )

    return [research_task, validation_task, reporting_task]