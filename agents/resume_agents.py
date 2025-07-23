from crewai import Agent, LLM
from groq import Groq
import os



groq_llm = LLM(
    model="groq/llama3-8b-8192",
    api_key=os.getenv("GROQ_API_KEY"),
)



analyzer_agent = Agent(
    role="Resume Gap Analyzer",
    goal="Identify skill, keyword, and experience mismatches between the resume and job description",
    backstory="You are an expert career consultant helping candidates align their resumes with job requirements.",
    verbose=True,
    llm=groq_llm,
)

editor_agent = Agent(
    role="Resume Enhancer",
    goal="Rewrite or enhance resume sections to align with job description and ATS systems",
    backstory="You specialize in optimizing resumes to maximize interview chances.",
    verbose=True,
    llm=groq_llm,
)
