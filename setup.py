import sys
import os


from crewai import Crew, Process
from agents import planner_agent, analyst_agent
from tasks import create_tasks

# 1. Setup the tasks using our agents
my_tasks = create_tasks(planner_agent, analyst_agent)

# 2. Define the Crew
sports_crew = Crew(
    agents=[planner_agent, analyst_agent],
    tasks=my_tasks,
    process=Process.sequential,
    verbose=True
)

# 3. Dynamic User Input
print("\n" + "="*50)
user_goal = input("Enter your sports analysis goal: ")
print("="*50 + "\n")

# 4. Kickoff the Crew with your custom prompt
print(f"### INITIATING DEEPSEEK SPORTS PLANNER FOR: {user_goal} ###")

# The 'user_goal' is passed into the '{goal}' placeholder in your tasks
result = sports_crew.kickoff(inputs={'goal': user_goal})

print("\n\n" + "="*50)
print("## FINAL AGENT REPORT ##")
print("="*50 + "\n")
print(result)