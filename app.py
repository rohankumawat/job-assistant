# import libraries
import os
import streamlit as st
from langchain_openai import OpenAI
from langchain.agents import AgentType, initialize_agent, load_tools
# from langchain.prompts import PromptTemplate
# from langchain.chains import LLMChain
# from langchain_experimental.agents import create_pandas_dataframe_agent
from dotenv import load_dotenv

load_dotenv()

# initialise keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY")

# initialise OpenAI
llm = OpenAI()

'''
prompt_template = PromptTemplate(
    input_variables = ["job_title", "job_type", "job_location"],
    template = """
    Please search for {job_title} {job_type} jobs in {job_location} and provide a list of approximately 5 unique positions. Ensure that the jobs are suitable for someone with no prior professional experience in the field. For each job, include the following details:

    - Job title
    - Company name
    - Company location
    - Job description
    - Job requirements
    - Job responsibilities
    - Salary (if available)
    - Application link

    Use reputable job search websites and company career pages to find the listings. Avoid including internships, fellowships, or positions that require more than 1 year of professional experience.
    If possible, provide jobs from different companies to ensure variety.
    """,
)
'''
# template = "Give me 10 {job_type} {job_title} postings in {job_location}. Then save all of the {job_type} to an Excel file calles '{job_title}.xlsx' on my computer.",

# prompt_template.format(job_title="entry level", job_type="internship", job_location="New York City")

tools = load_tools(["google-jobs", "llm-math"], llm=llm) # "serpapi"

agent = initialize_agent(
    tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
)

agent.invoke("""Please search for entry level software engineering jobs in London and provide a list of approximately 5 unique positions. Ensure that the jobs are suitable for someone with 
    no prior professional experience in the field. For each job, include the following details:

    - Job title
    - Company name
    - Company location
    - Job description
    - Job requirements
    - Job responsibilities
    - Salary (if available)
    - Application link

    Use reputable job search websites and company career pages to find the listings. Avoid including internships, fellowships, or positions that require more than 1 year of professional experience.
    If possible, please ensure that each job listing is from a different company and provides unique opportunities compared to the others""")