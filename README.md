# NLP to SQL in-a-box examples

![I stand with Israel](./docs/IStandWithIsrael.png)

Welcome to the **NLP2SQL** repository, where you can find different approaches and tools for natural language processing (NLP) translations to SQL.

With **NLP2SQL**, you can use the state-of-the-art technologies of Azure Open AI, Semantic Kernel, and LangChan to turn your natural language queries into SQL commands that can run on any SQL Server database. This will make your data analysis easier and faster, without the hassle of learning SQL syntax.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## Hire me

Please send [email](mailto:kingdavidconsulting@gmail.com) if you consider to **hire me**.

[![buymeacoffee](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/vyve0og)

## Give a Star! :star

If you like or are using this project to learn or start your solution, please give it a star. Thanks!

## Prerequisites

* An [Azure subscription](https://azure.microsoft.com/en-us/free/).
* Install latest version of [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-windows?view=azure-cli-latest)
* Install [ODBC Driver for SQL Server](https://learn.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server) 

## Deploy to Azure

1. Clone this repository locally: 

    ```
    git clone https://github.com/kdcllc/nlp-sql-in-a-box
    ```
2. Deploy resources:

- Azure SQL Server/Database
- Azure OpenAI Endpoint and deploy models
- Azure Key Vault (Optional) to store secrets

## Post Deployment

Once your resources have been deployed you will need to do the following to get the app up and running:

1. Add your client IP4 address in the Azure SQL Server Firewall rules:       
    * If you don't know how to add your IP Address to your SQL Server follow this link -> [Create a server-level firewall rule in Azure portal](https://learn.microsoft.com/en-us/azure/azure-sql/database/firewall-create-server-level-portal-quickstart)

2. [Create fake data](./src/datasetup/)

## Bash Scripts

### `add-env-file.sh` add secret from Azure Key Vault to `.env` file for local testing only

This bash script is used to create a `.env` file and populate it with secrets from an Azure Key Vault.

The script prompts the user to input the name of the `.env` file and the name of the Azure Key Vault. It then retrieves the secrets for a predefined list of environment variables from the Key Vault and writes them to the `.env` file.

The environment variables retrieved by this script are:

* AZURE-OPENAI-DEPLOYMENT-NAME
* AZURE-OPENAI-ENDPOINT
* AZURE-OPENAI-API-KEY
* SERVER-NAME
* DATABASE-NAME
* SQLADMIN-USER
* SQL-PASSWORD

To run the script, you need to make it executable with the command `chmod +x add-env-file.sh` and then execute it with `./add-env-file.sh`.

### `add-secrets-kv.sh` adds secrets to Azure Key Valut

This bash script is used to add secrets from environment variables in a `.env` file to an Azure Key Vault.

The script prompts the user to input the name of the Azure Key Vault. It then retrieves the values of a predefined list of environment variables from the `.env` file and adds them as secrets to the Key Vault.

The environment variables handled by this script are:

* AZURE_OPENAI_DEPLOYMENT_NAME
* AZURE_OPENAI_ENDPOINT
* AZURE_OPENAI_API_KEY
* SERVER_NAME
* DATABASE_NAME
* SQLADMIN_USER
* SQL_PASSWORD

Before running the script, you need to make it executable with the command `chmod +x add-secrets-kv.sh`. Then, you can execute it with `./add-secrets-kv.sh`.

Please note that the script requires the user to be logged into Azure CLI. If the user is not logged in, the script will output "User is not logged in".

### `version.sh` to pin version only of the listed main packages

This bash script reads a `requirements.txt` file and prints each Python package name along with its installed version.

The script accepts an optional argument which is the path to the `requirements.txt` file. If no argument is provided, it defaults to using a file named `requirements.txt` in the current directory.

The script checks if the specified `requirements.txt` file exists, and whether Python and pip are installed on the system. It then reads each line of the `requirements.txt` file, skipping lines that are empty or contain '-r'. For each package listed in the file, it uses pip to find the installed version of the package and prints the package name and version in the format `package==version`.

To run the script, you need to make it executable with the command `chmod +x version.sh` and then execute it with `./version.sh` or `./version.sh <path_to_requirements.txt>`.

Please note that this script requires Python and pip to be installed on your system.

### `create-venv.sh` run this script to quickly create and install python environment

This bash script creates a Python virtual environment and installs the packages listed in a `requirements.txt` file.

The script accepts two optional arguments:

1. The path to the `requirements.txt` file. If no argument is provided, it defaults to a file named `requirements.txt` in the current directory.
2. The name for the virtual environment. If no argument is provided, it defaults to `.venv`.

The script first checks if the provided `requirements.txt` file exists. It then creates a virtual environment with the specified name (or `.venv` if no name is provided), activates the environment, and installs the packages listed in the `requirements.txt` file.

To run the script, you need to make it executable with the command `chmod +x create-venv.sh`. Then, you can execute it with `./create-venv.sh` or `./create-venv.sh <path_to_requirements.txt> <environment_name>`.

Please note that this script requires Python 3 and pip to be installed on your system.

### `delete-venv.sh` run this script to quickly remove python environment

This bash script deletes a Python virtual environment.

The script accepts one optional argument:

1. The name of the virtual environment to be deleted. If no argument is provided, it defaults to `.venv`.

The script first deactivates the virtual environment (if it's active) and then removes the directory associated with the environment.

To run the script, you need to make it executable with the command `chmod +x delete-venv.sh`. Then, you can execute it with `./delete-venv.sh` or `./delete-venv.sh <environment_name>`.

Please note that this script requires the virtual environment to be in the same directory from where the script is being run.


## Sample questions

* How many locations are there?
* How many wells are there were water cut is more than 95?


## References

* [Revolutionizing SQL Queries with Azure Open AI and Semantic Kernel](https://techcommunity.microsoft.com/t5/analytics-on-azure-blog/revolutionizing-sql-queries-with-azure-open-ai-and-semantic/ba-p/3913513)

* [NL2SQL with LangChain and Azure SQL Database](https://devblogs.microsoft.com/azure-sql/nl2sql-with-langchain-and-azure-sql-database/)

* [SQL-AI-samples (LangChain) repo](https://github.com/Azure-Samples/SQL-AI-samples/tree/main/AzureSQLDatabase/LangChain)

* [LangChain SQL Database Toolkit](https://python.langchain.com/docs/integrations/toolkits/sql_database)
