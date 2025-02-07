#author: Vinay

import sys
import csv
import logging
import webbrowser
from pathlib import Path
from PyPDF2 import PdfReader
import google.generativeai as genai
from browser_use.controller.service import Controller

# 🔹 Configure Gemini AI
genai.configure(api_key="YOUR_GEMINI_API_KEY")  # Replace with your Gemini API Key

# 🔹 Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 🔹 Define file paths (adjust to your system)
CV_PATH = Path("/path/to/your/resume.pdf")  # Update with your resume path
CSV_PATH = Path("/path/to/your/job_listings.csv")  # Update with your job listings CSV path

# 🔹 Ensure the CV file exists
if not CV_PATH.exists():
    raise FileNotFoundError(f"CV file not found at {CV_PATH}")

# 🔹 Initialize Controller
controller = Controller()
logger.info("Controller initialized successfully!")

# 🔹 Action: Read CV
@controller.action("Read my CV for job applications")
def read_cv():
    pdf = PdfReader(CV_PATH)
    text = ''.join(page.extract_text() for page in pdf.pages if page.extract_text())
    logger.info(f"Extracted {len(text)} characters from CV")
    return text

# 🔹 Action: Read job listings
@controller.action("Read job listings from CSV")
def read_jobs():
    if not CSV_PATH.exists():
        raise FileNotFoundError(f"Job listings file not found: {CSV_PATH}")

    jobs = []
    with open(CSV_PATH, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            jobs.append(row)

    logger.info(f"Loaded {len(jobs)} job listings")
    return jobs

# 🔹 Function: Use Gemini AI to analyze job fit
def analyze_job_fit(resume_text, job_description):
    model = genai.GenerativeModel("gemini-pro")
    prompt = f"""
    You are a job matching assistant. Analyze the following resume and job description. 
    Give a score from 0 to 100 based on how well the resume fits the job.
    
    Resume: {resume_text}
    
    Job Description: {job_description}
    
    Output format: "Fit Score: [score]"
    """
    
    response = model.generate_content(prompt)
    fit_score = response.text.split("Fit Score:")[-1].strip() if "Fit Score:" in response.text else "N/A"
    
    return fit_score

# 🔹 Function: Process job applications
def apply_for_jobs():
    resume_text = read_cv()
    jobs = read_jobs()
    filtered_jobs = []

    for job in jobs:
        job_description = f"{job['Title']} at {job['Company']} in {job['Location']}"
        fit_score = analyze_job_fit(resume_text, job_description)
        
        if fit_score != "N/A" and int(fit_score) > 69:  # Apply only if score > 69
            job["Fit Score"] = fit_score
            filtered_jobs.append(job)
            logger.info(f"✅ Matched Job: {job['Title']} at {job['Company']} (Score: {fit_score})")

    return filtered_jobs

# 🔹 Function: Open job links in browser
def open_job_links(jobs):
    for job in jobs:
        print(f"🔹 Applying to: {job['Title']} at {job['Company']} ({job['Location']})")
        webbrowser.open(job["Link"])

# 🔹 Main execution
if __name__ == "__main__":
    matched_jobs = apply_for_jobs()
    if matched_jobs:
        print("\n🎯 Opening job applications...\n")
        open_job_links(matched_jobs)
    else:
        print("❌ No suitable job matches found.")
