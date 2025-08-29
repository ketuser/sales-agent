# sales-agent

Sales Agent Prototype built with GPT models, LangChain, Tavily Search, and Streamlit. 
Helps sales reps gain insights into accounts by summarizing company strategy, identifying competitors, and highlighting leadership, generating a structured one-page report.

# Sales Agent Prototype

## Overview

The Sales Agent Prototype is an AI-powered assistant that helps sales representatives gain insights into prospective accounts.
It generates a one-page report that includes:

  - Company Strategy
  - Competitors & Partnerships
  - Leadership Insights
  - Source References

Built with LangChain, Tavily Search, and Groq GPT models, deployed via Streamlit for easy use.

## Live Demo

Try the app here: Sales Agent on Streamlit

## Features

  - Input Form: Company name, URL, product, competitors.
  - Web Search: Uses Tavily to fetch relevant strategy/leadership data.
  - LLM Summaries: GPT-based one-pager with structured insights.
  - Streamlit UI: Clean, responsive, user-friendly.
  - Environment Ready: .env file support with API keys.

## Project Structure

  sales-agent/
│── app.py              # Streamlit app
│── requirements.txt     # Dependencies
│── .env.example         # Example env file (API keys)
│── README.md            # Documentation
│── docs/                # Report & screenshots

## Installation & Setup
  
  1. Clone the Repository
     git clone https://github.com/yourusername/sales-agent.git
     cd sales-agent
  
  2. Create Virtual Environment
     python -m venv .venv
     source .venv/bin/activate   # Mac/Linux
     .\.venv\Scripts\activate    # Windows

  3. Install Dependencies
     pip install -r requirements.txt

  4. Configure Environment Variables
     Create a .env file with your API keys:
     OPENAI_API_KEY=your_openai_api_key_here
     TAVILY_API_KEY=your_tavily_api_key_here

  5. Run the App Locally
     streamlit run app.py

## Deployment

Deploy on Streamlit Cloud

  1. Connect your GitHub repo.
  2. Choose main branch and app.py.
  3. Add secrets (OPENAI_API_KEY, TAVILY_API_KEY) in App Settings → Secrets.

The app will be available at:
  https://sales-agent.streamlit.app

## Example Output (One-Pager)

Company Strategy
  - Microsoft invests heavily in Azure Cloud.
  - Focus on AI, hybrid cloud, and cybersecurity.

Competitors & Partnerships
  - AWS, Google Cloud are primary competitors.
  - Partnerships with OpenAI, Accenture for enterprise cloud adoption.

Leadership
  - Satya Nadella (CEO) → AI-first strategy.
  - Scott Guthrie (EVP Cloud) → Hybrid adoption push.

Sources
  - Microsoft Press Release 2025
  - Microsoft Careers Portal

## Development Timeline

  - Day 1: Setup environment, Streamlit UI, model connection.
  - Day 2: Integrations, prompt engineering, documentation, deployment.

## Future Improvements

  - Export one-pager to PDF.
  - CRM integration (e.g., Salesforce).
  - Alert system for new press releases/job postings.

##  Author

Anatoly Lunev
📍 Brooklyn, NY
🌐 LinkedIn | GitHub

## License

This project is licensed under the MIT License.

