# InterviewMate – Agentic AI Interview Trainer

An AI-powered Interview Trainer built using **IBM watsonx.ai**, **IBM Granite Foundation Models**, **Python Streamlit**, and a **RAG-based knowledge base**. The application helps students and job seekers prepare for placement interviews by generating personalized interview questions, evaluating responses, and providing constructive feedback.

This project was developed as part of the **IBM SkillsBuild x AICTE University Engagement Program (2026)**.

---

## 📌 Problem Statement

Students and freshers often struggle to prepare effectively for placement interviews due to a lack of personalized guidance, role-specific practice, and constructive feedback.

InterviewMate solves this problem by providing an AI-powered interview coach that:
- Generates role-specific interview questions.
- Evaluates candidate responses.
- Provides improvement suggestions.
- Helps candidates build confidence before real interviews.

---

## 🚀 Features

- 🎯 Role-specific interview question generation
- 🤖 AI-powered interview coaching using IBM Granite Models
- 📝 Answer evaluation with personalized feedback
- 📊 Readiness scoring
- 📚 Knowledge-base assisted interview guidance (RAG-lite)
- 💻 Modern Streamlit web application
- ☁️ Live deployment using Streamlit Community Cloud

---

## 🛠 Tech Stack

| Component | Technology |
|------------|------------|
| AI Platform | IBM watsonx.ai |
| Foundation Model | IBM Granite 4 H Small |
| SDK | ibm-watsonx-ai |
| Frontend | Python Streamlit |
| Programming Language | Python |
| Knowledge Base | Markdown (RAG-lite) |
| Version Control | GitHub |
| Deployment | Streamlit Community Cloud |

---

## 🏗 System Architecture

```
                User
                  │
                  ▼
          Streamlit Web App
                  │
                  ▼
       IBM watsonx.ai API (SDK)
                  │
                  ▼
      IBM Granite Foundation Model
                  │
                  ▼
     Interview Knowledge Base (RAG)
                  │
                  ▼
      Personalized Interview Response
```

---

## 📂 Repository Structure

```
InterviewMate/
│
├── app_streamlit.py
├── requirements.txt
├── Interview_Question_Bank_KnowledgeBase.md
├── architecture_diagram.png
├── app.json
├── README.md
└── .gitignore
```

---

## 📄 Repository Contents

| File | Description |
|------|-------------|
| app_streamlit.py | Main Streamlit application |
| requirements.txt | Python dependencies |
| Interview_Question_Bank_KnowledgeBase.md | Knowledge base for interview preparation |
| architecture_diagram.png | System architecture diagram |
| app.json | Project configuration |
| README.md | Project documentation |

---

## ⚙️ How It Works

1. User enters interview requirements.
2. The application sends the prompt to IBM watsonx.ai.
3. IBM Granite Foundation Model generates interview questions.
4. The knowledge base provides additional interview context.
5. AI evaluates candidate responses and provides suggestions.
6. Interview readiness score is displayed.

---

## ☁️ IBM Cloud Setup

1. Create an IBM Cloud account.
2. Create a **watsonx.ai Project (Lite Plan)**.
3. Copy your **Project ID**.
4. Generate an **IBM Cloud API Key**.
5. Note your **Region URL**.
6. Select a supported IBM Granite model.

---

## ▶️ Run Locally

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

**Windows**

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Set Environment Variables (PowerShell)

```powershell
$env:WATSONX_API_KEY="your_api_key"
$env:WATSONX_URL="https://eu-de.ml.cloud.ibm.com"
$env:WATSONX_PROJECT_ID="your_project_id"
$env:WATSONX_MODEL_ID="ibm/granite-4-h-small"
```

### Run the Application

```bash
streamlit run app_streamlit.py
```

---

## 🌐 Deploy on Streamlit Community Cloud

1. Push the repository to GitHub.
2. Open Streamlit Community Cloud.
3. Create a New App.
4. Select:
   - Repository: **Interview-Mate**
   - Branch: **main**
   - Main File: **app_streamlit.py**
5. Under **Advanced Settings → Secrets**, add:

```toml
WATSONX_API_KEY="your_api_key"
WATSONX_URL="https://eu-de.ml.cloud.ibm.com"
WATSONX_PROJECT_ID="your_project_id"
WATSONX_MODEL_ID="ibm/granite-4-h-small"
```

6. Click **Deploy**.

---

## 💬 Sample Prompt

```
Hi, my name is Preeti.

I am preparing for Infosys.

Role: Software Developer

Language: Java

Difficulty: Medium

Please start my mock interview.
```

---

## 🔮 Future Enhancements

- Resume upload support
- PDF interview report generation
- Voice-based interview simulation
- Multi-round interview support
- User authentication
- Performance analytics dashboard

---

## 🔗 Live Demo

**Streamlit Application**

https://interview-mate-3jnbwasegzzs8dzckcxaws.streamlit.app/

**GitHub Repository**

https://github.com/PreetiGautam23/Interview-Mate

---



