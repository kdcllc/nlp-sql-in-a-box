import asyncio
from math import e
import pyodbc
import os
from dotenv import load_dotenv
from langchain.agents import create_sql_agent
from langchain.agents.agent_types import AgentType
from langchain.sql_database import SQLDatabase

from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain_openai import AzureChatOpenAI

from util import get_connection_string
import streamlit as st

# connect to the Azure SQL database
from sqlalchemy import create_engine

load_dotenv()

openai_api_key = os.getenv("AZURE_OPENAI_API_KEY")
openai_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")

openai_version = os.getenv("AZURE_OPENAI_VERSION", "2023-12-01-preview")
openai_model = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME", "gpt-35-turbo")

def create_agent(openai_api_key, openai_endpoint, openai_version, openai_model):
    connectionString= get_connection_string()

    db_engine = create_engine(connectionString)
    db = SQLDatabase(db_engine, view_support=True, schema="dbo")

    from langchain_community.agent_toolkits import SQLDatabaseToolkit

    llm = AzureChatOpenAI(
    openai_api_type="azure",
    azure_endpoint=openai_endpoint,
    api_key=openai_api_key,
    azure_deployment=openai_model,
    api_version=openai_version,
    temperature=0.0,
)

    from langchain.prompts.chat import ChatPromptTemplate

    final_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", 
         """
          You are a helpful AI assistant expert in querying SQL Database to find answers to user's question about ExplorationProduction (WellID, WellName, Location, ProductionDate, ProductionVolume, Operator, FieldName, Reservoir, Depth, APIGravity, WaterCut, GasOilRatio).
         """
         ),
        ("user", "{question}\n ai: "),
    ]
)

    toolkit = SQLDatabaseToolkit(db=db, llm=llm)

    agent = create_sql_agent(
    llm=llm,
    toolkit=toolkit,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    # comment out to see the full conversation logic
    #verbose=True
)
    
    return final_prompt,agent



async def stream(agent, query):
    async for chunk in agent.astream(final_prompt.format(
        question=query
  )
):
    # Agent Action
        if "actions" in chunk:
            for action in chunk["actions"]:
                yield f"Calling Tool: `{action.tool}` with input `{action.tool_input}`"
    # Observation
        elif "steps" in chunk:
            for step in chunk["steps"]:
                yield f"Tool Result: `{step.observation}`"
    # Final result
        elif "output" in chunk:
            yield f'Final Output: {chunk["output"]}'
        else:
            raise ValueError()
        yield "---"

st.title("SQL Query Generator with GPT")
st.write("Enter your message to generate SQL and view results.")

# Input field for the user to type a message
user_message = st.text_input("Enter your message:")

if user_message:

    final_prompt, agent = create_agent(openai_api_key, openai_endpoint, openai_version, openai_model)
    try:
        st.write("Query Results:")

        async def run_query():
            async for result in stream(agent, user_message):
                st.text(result)

        asyncio.run(run_query())

    except Exception as e:
        st.write(f"An error occurred: {e}")

if __name__ == "__main__":
    print("Running the app")
