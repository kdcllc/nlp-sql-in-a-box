from dotenv import load_dotenv

import pyodbc

import os
import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion

def setup_kernel():
    # Load environment variables from .env file
    load_dotenv()

    # Create a new kernel
    kernel = sk.Kernel()
    context = kernel.create_new_context()
    context['result'] = ""

    # Configure AI service used by the kernel
    deployment, api_key, endpoint = sk.azure_openai_settings_from_dot_env()

    # Add the AI service to the kernel
    kernel.add_text_completion_service("dv", AzureChatCompletion(deployment_name=deployment, endpoint=endpoint, api_key=api_key))
    plugins_directory = os.path.join(os.path.dirname(__file__),"plugins")
    print(plugins_directory)

    plugin = kernel.import_semantic_plugin_from_directory(plugins_directory, "SQLPlugin")

    return kernel, plugin

# Function to get the result from the database
def get_result_from_database(sql_query):
    server_name = os.environ.get("SERVER_NAME")
    database_name = os.environ.get("DATABASE_NAME")
    username = os.environ.get("SQLADMIN_USER")
    password = os.environ.get("SQL_PASSWORD")
    conn = pyodbc.connect('DRIVER={driver};SERVER={server_name};DATABASE={database_name};UID={username};PWD={password}'.format(driver="ODBC Driver 18 for SQL Server",server_name=server_name, database_name=database_name, username=username, password=password))
    
    cursor = conn.cursor()
    try:
        cursor.execute(sql_query)
        result = cursor.fetchall()
    except Exception as e:
        return f"No Result Found - {e}"
    cursor.close()
    conn.close()
    return result