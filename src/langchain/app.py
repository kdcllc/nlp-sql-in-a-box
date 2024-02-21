import pyodbc
import os
from dotenv import load_dotenv
from langchain.agents import create_sql_agent
from langchain.agents.agent_types import AgentType
from langchain.sql_database import SQLDatabase

from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain_openai import AzureOpenAI

from util import get_connection_string

# connect to the Azure SQL database
from sqlalchemy import create_engine

load_dotenv()

openai_api_key = os.getenv("AZURE_OPENAI_API_KEY")
openai_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")

openai_version = os.getenv("AZURE_OPENAI_VERSION", "2023-12-01-preview")
openai_model = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME", "gpt-35-turbo-instruct")

print(openai_endpoint)
connectionString= get_connection_string()

db_engine = create_engine(connectionString)

db = SQLDatabase(db_engine, view_support=True, schema="dbo")

# test the connection
print(db.dialect)
print(db.get_usable_table_names())
db.run("select convert(varchar(25), getdate(), 120)")

# requires gpt-35-turbo-instruct to be deployed
azurellm = AzureOpenAI(
    openai_api_type="azure",
    azure_endpoint=openai_endpoint,
    api_key=openai_api_key,
    azure_deployment=openai_model,
    api_version=openai_version,
    temperature=0.0,
)

toolkit = SQLDatabaseToolkit(db=db, llm=azurellm)

agent_executor = create_sql_agent(
    llm=azurellm,
    toolkit=toolkit,
    verbose=True,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
)

agent_executor.invoke({"input": "count the rows in the ExplorationProduction table."})

if __name__ == "__main__":
    print("Running the app")
