---
title: Sportlytics
emoji: 🏏
colorFrom: indigo
colorTo: blue
sdk: streamlit
sdk_version: 1.31.1
app_file: app.py
pinned: false
---

# 🏏 Sportlytics - AI Sports Analysis Assistant


Sportlytics is a premium, multi-agent AI application designed to provide deep, real-time sports analysis. Using specialized AI agents, it researches live match data, analyzes performance stats of teams and players, and generates professional executive reports.

## ✨ Features

- **🔐 Secure Authentication**: Signup, Login, and Password Reset (with validation).
- **🕵️ Multi-Agent System**:
    - **Planner**: Researches live data and plans the analysis.
    - **Analyst**: Validates technical feasibility and manages schedules.
    - **Reporter**: Synthesizes findings into a beautiful Markdown report.
- **📊 Deep Analysis**: Actual player names, team stats, tactical winner/loser reasoning.
- **📂 User History**: Track and view all your previous analysis reports.
- **📥 Downloadable Reports**: Export analysis as `.md` files.
- **🎨 Premium UI**: Modern Glassmorphism design with a responsive layout.

---

## 🚀 Getting Started (Local Setup)

Follow these steps to get the project running on your local machine.

### 📋 Prerequisites
- **Python 3.10+** installed.
- API Keys from:
    - [Groq Console](https://console.groq.com/) (Free tier available).
    - [Tavily AI](https://tavily.com/) (For real-time search).

### 🛠️ Installation Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/pranjali2117/final_agentic.git
   cd final_agentic
   ```

2. **Create a Virtual Environment**
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\Activate.ps1

   # Mac/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirement.txt
   ```

4. **Configure Environment Variables**
   Create a `.env` file in the root directory and add your API keys:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   TAVILY_API_KEY=your_tavily_api_key_here
   ```

### 🏃 Running the App

Start the Streamlit application with the following command:
```bash
streamlit run app.py
```

---

## 🛠️ Built With
- **Streamlit**: For the interactive web interface.
- **CrewAI**: For multi-agent orchestration.
- **Groq/Llama 3**: For fast and intelligent language processing.
- **Tavily AI**: For high-quality real-time web research.
- **SQLite**: For secure user data and history management.

---
Created with ❤️ for Sport Fans.
