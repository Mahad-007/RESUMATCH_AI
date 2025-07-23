import pdfplumber
import docx2txt
from crewai import Task, Crew, Process
from agents.resume_agents import analyzer_agent, editor_agent

def extract_text(file):
    if file.name.endswith(".pdf"):
        with pdfplumber.open(file) as pdf:
            return "\n".join([page.extract_text() or "" for page in pdf.pages])
    elif file.name.endswith(".docx"):
        return docx2txt.process(file)
    return ""

def analyze_resume_and_role(resume_file, job_desc):
    resume = extract_text(resume_file)

    task_gaps = Task(
        description=f"Identify missing skills, experiences, or keywords.\n\nResume:\n{resume}\n\nJob Description:\n{job_desc}",
        expected_output="Bullet list of identified gaps",
        agent=analyzer_agent,
    )
    task_suggestions = Task(
        description=f"Suggest bullet-point improvements aligned with job.\n\nResume:\n{resume}\n\nJob Description:\n{job_desc}",
        expected_output="Bullet list",
        agent=analyzer_agent,
    )

    crew = Crew(
        agents=[analyzer_agent],
        tasks=[task_gaps, task_suggestions],
        process=Process.sequential,
        verbose=True,
    )
    crew.kickoff()

    return task_gaps.output.raw, task_suggestions.output.raw

def generate_improved_resume(resume_file, job_desc):
    resume = extract_text(resume_file)
    task = Task(
        description=f"Rewrite resume to align with job.\n\nResume:\n{resume}\n\nJob Description:\n{job_desc}",
        expected_output="Full improved resume",
        agent=editor_agent,
    )
    crew = Crew(
        agents=[editor_agent],
        tasks=[task],
        process=Process.sequential,
        verbose=True,
    )
    crew.kickoff()
    
    return task.output.raw
