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
