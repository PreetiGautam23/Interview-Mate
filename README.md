# InterviewMate – Agentic AI Interview Trainer

An AI-powered Interview Trainer Agent built on **IBM watsonx Orchestrate**, using **IBM Granite models** and a **RAG-based knowledge store**, that helps students and job seekers prepare for placements.

Built as part of the **IBM SkillsBuild x AICTE University Engagement Program (2026)** — IBM Cloud / Agentic AI track.

## Problem Statement

Job seekers, especially students and freshers, often struggle to prepare effectively for job interviews, role-specific questions, and behavioral rounds. Information about industry expectations, HR guidelines, and interview patterns is scattered across recruitment portals and unreliable sources. Without personalized, real-time coaching, many candidates walk into interviews underprepared and lose confidence.

## What InterviewMate Does

- **Role-Specific Question Generation** – generates tailored technical + behavioral questions based on job role, experience level, and resume
- **RAG-Based Retrieval** – fetches role-specific questions, industry expectations, and HR guidelines from a curated knowledge base
- **Mock Interview & Feedback** – evaluates a candidate's answers and gives model answers with improvement tips
- **Progress Dashboard** – readiness score and category-wise weak areas across mock sessions

## Tech Stack

| Component | Technology |
|---|---|
| LLM inference | IBM watsonx.ai — direct API (`ibm-watsonx-ai` SDK) |
| Model | `ibm/granite-4-h-small` (falls back to Meta/Mistral models if Granite isn't available in your region) |
| Front-end | Python Streamlit |
| Retrieval | RAG-lite — the interview knowledge base is injected into the system prompt |
| Hosting | IBM Cloud Lite (watsonx.ai project) + Streamlit Community Cloud (free) for the live app |

## Repository Contents

| File | Description |
|---|---|
| `app_streamlit.py` | The working Streamlit app — calls watsonx.ai directly using Project ID, Region URL, API Key, and Model ID |
| `requirements.txt` | Python dependencies |
| `app.json` | Reference agent definition (matches the watsonx Orchestrate ADK schema, in case Orchestrate is also used) |
| `Interview_Question_Bank_KnowledgeBase.md` | The knowledge document used for RAG (interview questions, HR guidelines) |
| `problemstatement.pdf` | Original AICTE / IBM SkillsBuild problem statement this project responds to |
| `InterviewMate_Agentic_AI_Project_Submission_updated.pptx` | Full project presentation with architecture, screenshots, and evaluation-criteria mapping |
| `screenshots/` | Screenshots of the app running (terminal, browser UI, sample conversations) |

## How to Get Your Credentials

1. Sign up at [IBM Cloud](https://cloud.ibm.com) and create a **watsonx.ai** project (Lite plan is free)
2. In the project, go to **Manage → General** to copy your **Project ID**
3. Go to **IBM Cloud IAM → API keys** and create an **API key**
4. Note your **region URL** based on where your project is provisioned:
   - Dallas: `https://us-south.ml.cloud.ibm.com`
   - London: `https://eu-gb.ml.cloud.ibm.com`
   - Frankfurt: `https://eu-de.ml.cloud.ibm.com`
   - Tokyo: `https://jp-tok.ml.cloud.ibm.com`
5. Pick a **Model ID** available in your region — `ibm/granite-4-h-small` if Granite is available, otherwise a Meta/Mistral model shown in your project's model catalog

## How to Run Locally

```bash
pip install -r requirements.txt
export WATSONX_API_KEY="your-api-key"
export WATSONX_URL="https://us-south.ml.cloud.ibm.com"
export WATSONX_PROJECT_ID="your-project-id"
export WATSONX_MODEL_ID="ibm/granite-4-h-small"
streamlit run app_streamlit.py
```

## How to Deploy for Free (Streamlit Community Cloud)

1. Push this repo to GitHub (public)
2. Go to [share.streamlit.io](https://share.streamlit.io) → sign in with GitHub → "New app"
3. Select this repo and `app_streamlit.py` as the entry point
4. Under **Advanced settings → Secrets**, paste:
   ```
   WATSONX_API_KEY = "your-api-key"
   WATSONX_URL = "https://us-south.ml.cloud.ibm.com"
   WATSONX_PROJECT_ID = "your-project-id"
   WATSONX_MODEL_ID = "ibm/granite-4-h-small"
   ```
5. Deploy — you'll get a free live link to put in your PPT and submission form

## Author

Preeti — B.Tech (IT), Madhav Institute of Technology and Science (MITS), Gwalior
IBM SkillsBuild Virtual Internship, 2026
