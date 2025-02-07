# Automated-job-apply
# AI-Powered Job Application Agent

## 🚀 Overview

This project is an AI-powered agent that automates the job application process. It reads your resume, analyzes job descriptions from a CSV file, and applies to jobs that match your profile based on a custom “fit score” powered by **Google Gemini AI**.

## 🛠️ Tools & Libraries Used

- **PyPDF2**: To extract text from PDF resumes.
- **Google Gemini AI**: For generating job fit scores based on resume and job descriptions.
- **csv**: To manage and read job listings stored in CSV format.
- **webbrowser**: For automating the opening of job application links in your browser.
- **Logging**: To track the process and display real-time updates.

## 💡 Features

- **Resume Parsing**: Automatically extracts text from your resume in PDF format.
- **Job Listings Management**: Loads job listings from a CSV file.
- **AI-Powered Job Fit**: Uses **Google Gemini AI** to compare your resume to job descriptions and assign a “fit score”.
- **Job Application Automation**: Automatically applies to jobs based on the fit score (only applies if the score is above 50).
- **Real-Time Logging**: Keep track of all job applications with logs.

Download the requirements
pip install -r requirements.txt

Replace the CV_PATH and CSV_PATH in main.py with the paths to your resume and job listings CSV file.
Set up your Google Gemini API key and replace it in the code.

🎯 How It Works

The script reads your CV file and extracts the text.
It loads job listings from a CSV file.
It uses Google Gemini AI to calculate a fit score between your CV and each job listing.
It filters jobs that have a fit score greater than 69.
It opens the job application links in your default web browser.


## 📦 Installation

Follow these steps to get the project up and running:


1. Clone the repository:

   ```bash
   git clone https://github.com/Vinay-M-T/Automated-job-apply.git

2.Create a virtual environment (recommended):
    python -m venv venv

3.Activate the virtual environment:
    For Windows:
    venv\Scripts\activate

    For macOS/Linux:
    source venv/bin/activate

4.Install the necessary dependencies:
pip install -r requirements.txt

________________________________________________

PyPDF2==2.11.0
google-generativeai==0.5.0  # Adjust version based on your needs
requests==2.26.0
browser-use==0.1.0  # Add any other necessary libraries
