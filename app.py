from langchain_tavily import TavilySearch
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

# LLM model
llm = ChatGroq(model="openai/gpt-oss-20b")

# Search tool
search_tool = TavilySearch(topic="general", max_results=3)

def generate_insights(company_name, product_name, company_url, company_competitors):
    # Search query
    search_query = f"site:{company_url} company strategy, leadership, competitors, business model"
    search_results = search_tool.invoke(search_query)
    
    messages = [
        SystemMessage("You are a sales assistant that provides concise, structured insights."),
        HumanMessage(content=f"""
Company Info from Tavily: {search_results}

Company: {company_name}
Product: {product_name}
Competitors: {company_competitors}

Generate a **one-page summary** including:
1. Company strategy related to {product_name}
2. Possible competitors or partnerships (including {company_competitors})
3. Leadership and decision-makers relevant to this area
Format output in clear sections with bullet points.
""")
    ]

    model_response = llm.invoke(messages)
    return model_response.content

# ================= Streamlit UI =================
st.title("Sales Agent Prototype")
st.subheader("Generate a report for a prospective client")

company_name = st.text_input("Company Name")
company_url = st.text_input("Company URL")
product_name = st.text_input("Product Name")
company_competitors = st.text_input("Company Competitors (comma-separated)")

if st.button("Generate Report"):
    if company_name and company_url:
        with st.spinner("Generating report..."):
            result = generate_insights(company_name, product_name, company_url, company_competitors)
            st.divider()
            st.text(result)
    else:
        st.warning("Please enter at least the company name and URL.")
