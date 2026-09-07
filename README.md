# 🔬 Multi-Agent Research System

> An AI-powered autonomous research assistant that searches the web, reads relevant sources, generates a structured research report, and critically evaluates the final output using specialized AI agents.

[![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![LangChain](https://img.shields.io/badge/LangChain-Framework-1C3C3C?style=for-the-badge&logo=chainlink&logoColor=white)](https://www.langchain.com/)
[![Groq](https://img.shields.io/badge/Groq-LLM%20Inference-F55036?style=for-the-badge)](https://groq.com/)
[![Tavily](https://img.shields.io/badge/Tavily-Web%20Search-000000?style=for-the-badge)](https://tavily.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Deployment-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github)](https://github.com/)

---

## 🌐 Live Demo

🚀 **Try the deployed application:**

**https://multi-agent-research-system-bejja96yqzji9rbu7hfc5k.streamlit.app/**

> The application is deployed using Streamlit Community Cloud.

---

## 📌 Overview

The **Multi-Agent Research System** is an AI research automation platform designed to transform a simple research topic into a structured, professionally written report.

Instead of relying on a single LLM prompt, the system divides the research workflow into multiple specialized agents.

Each agent performs a specific task:

```text
                    ┌─────────────────────┐
                    │    User Research    │
                    │       Topic         │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   🔎 Search Agent   │
                    │ Web Search & Source │
                    │     Discovery       │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   📖 Reader Agent   │
                    │  Source Selection & │
                    │    Web Scraping    │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   ✍️ Writer Agent   │
                    │ Research Synthesis  │
                    │   & Report Writing  │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   🧠 Critic Agent   │
                    │ Quality Evaluation  │
                    │  & Improvements     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   📄 Final Report   │
                    │  + Critical Review  │
                    └─────────────────────┘
