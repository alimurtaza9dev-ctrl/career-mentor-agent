# 🤖 Career Mentor Agent

An AI-powered career guidance assistant built with **Python**, **Streamlit**, and the **GitHub Copilot SDK**.

Career Mentor Agent provides conversational career guidance to help users explore career paths, build learning roadmaps, discover certifications and projects, and prepare for interviews.

## 🚀 Live Demo

👉 [Try Career Mentor Agent](https://career-mentor-agentbranchmainmainfileapppy-njkahyn6mdbqz4phstd.streamlit.app/)

## ✨ Features

- 💬 Conversational career guidance
- 🗺️ Learning roadmap generation
- 🎓 Certification suggestions
- 💻 Portfolio project recommendations
- 🎯 Interview preparation
- 🧠 AI-powered career advice
- 💾 Conversation history during the session
- 🌙 Streamlit light and dark themes
- ⚡ Fast interactive chat interface

## 🛠️ Technologies

| Technology | Purpose |
|------------|---------|
| Python | Application development |
| Streamlit | Web interface |
| GitHub Copilot SDK | AI agent integration |
| GPT-5.4 | AI-powered responses |
| AsyncIO | Asynchronous operations |
| Git & GitHub | Version control and collaboration |

## 🏗️ Architecture

```text
                    ┌─────────────────┐
                    │      User       │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │    Streamlit    │
                    │   Chat UI       │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │  Conversation   │
                    │     History     │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │  System Prompt  │
                    │ Career Mentor   │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ GitHub Copilot  │
                    │      SDK        │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │     GPT-5.4     │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Career Guidance │
                    │    Response     │
                    └─────────────────┘



📸 Application Preview
Career Mentor Agent

AI Career Guidance

📁 Project Structure

career-mentor-agent/
│
├── app.py
├── prompts.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── screenshots/
    ├── career-mentor-home.png
    └── career-mentor-response.png

🤖 Agent Capabilities

The Career Mentor Agent can help users with:

Career path exploration
Skill development planning
Learning roadmaps
Certification guidance
Portfolio project ideas
Interview preparation
AI and Machine Learning career guidance
Technology and skill recommendations

💡 Example Questions

You can ask the Career Mentor Agent questions such as:

What skills should I learn to become a Data Scientist?

🎓 Microsoft Frontier Program

This project was developed as part of the Microsoft Frontier Program – Day 4 Agent-a-Thon.

The project provided hands-on experience with:

AI agent development
GitHub Copilot SDK
Python asynchronous programming
Streamlit application development
Authentication and secrets management
Git and GitHub
Cloud deployment

Create a 6-month roadmap for becoming a Machine Learning Engineer.

Which Python projects should I build for my portfolio?

What certifications are useful for a beginner in AI and Machine Learning?

How should I prepare for a Data Science internship interview?

⚙️ Installation
1. Clone the repository
git clone https://github.com/alimurtaza9dev-ctrl/career-mentor-agent.git
cd career-mentor-agent
2. Create a virtual environment
python -m venv .venv
3. Activate the virtual environment
Windows
.venv\Scripts\activate
4. Install dependencies
pip install -r requirements.txt
5. Run the application
streamlit run app.py

The application will open in your browser.

🔐 Configuration

The application uses GitHub Copilot authentication.

For cloud deployment, configure the required authentication credential through the deployment platform's Secrets management system.

Example:

COPILOT_GITHUB_TOKEN = "YOUR_TOKEN"

🌐 Deployment

The application is deployed using Streamlit Community Cloud.

The deployment process includes:

GitHub repository
Streamlit application
Python dependencies
Secure authentication through Streamlit Secrets

Never commit authentication tokens, API keys, passwords, or other sensitive credentials to GitHub.
