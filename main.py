import streamlit as st
from dotenv import load_dotenv
from logic.resume_analyzer import analyze_resume_and_role, generate_improved_resume

load_dotenv()

st.set_page_config(page_title="ResuMatch AI", layout="wide")

st.title("📄 ResuMatch AI - Resume Gap Analyzer & Enhancer")

resume_file = st.file_uploader("Upload your resume (PDF or DOCX)", type=["pdf", "docx"])
job_role = st.text_area("Paste the job role/description you're targeting", height=200)

if st.button("Analyze Resume"):
    if not resume_file or not job_role:
        st.warning("Please upload a resume and paste the job role.")
    else:
        with st.spinner("Analyzing resume..."):
            gaps, suggestions = analyze_resume_and_role(resume_file, job_role)
        # st.subheader("🛠️ Identified Gaps")
        # st.markdown(gaps)

        st.subheader("✨ Suggested Resume Improvements")
        st.markdown(suggestions)

        if st.button("Generate AI-Improved Resume"):
            with st.spinner("Generating enhanced resume..."):
                improved = generate_improved_resume(resume_file, job_role)
            st.download_button("Download Enhanced Resume", improved, file_name="enhanced_resume.txt")
