from crewai import Agent, LLM
from crewai_tools import TavilySearchTool
from sports_analysis import check_resource
import os
print(os.getenv("GROQ_API_KEY"))
search_tool = TavilySearchTool()
search_tool.name = "tavily_search"

local_llm = LLM(
    model="groq/llama-3.3-70b-versatile", # Switched to a lighter model to avoid TPM rate limits
    temperature=0.3
)

planner_agent = Agent(
    role='Lead Sports Planner',
    goal='Research real-time sports data and plan analysis steps.',
    backstory="Expert sports strategist using live match statistics.",
    llm=local_llm,
    tools=[search_tool],
    allow_delegation=False,
    verbose=True,
    max_iter=5
)

analyst_agent = Agent(
    role='Resource Validator',
    goal='Validate tool availability and prepare execution schedule.',
    backstory="Technical feasibility expert.",
    llm=local_llm,
    tools=[check_resource],
    allow_delegation=False,
    verbose=True,
    max_iter=3
)

reporter_agent = Agent(
    role="Chief Sports Editor",
    goal="Combine analysis into a final markdown report.",
    backstory="Expert editor merging sports data and execution plans.",
    llm=local_llm,
    allow_delegation=False,
    verbose=True

)
