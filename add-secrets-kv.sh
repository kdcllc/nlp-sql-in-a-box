#!/bin/bash

#----------------------------------------------------
# Path: add-secrets-kv.sh
# Author: King David Consulting LLC
# Description: This script adds secrets from environment variables in .env file to a key vault
# chmod +x add-secrets-kv.sh
# command: ./add-secrets-kv.sh
#----------------------------------------------------

echo "This script adds secrets from environment variables in .env file to a key vault"

# ask for key vault name
echo "Enter the name of the key vault you want ro use to create secrets from environment variables in .env file"
read key_vault_name

# Check if user is logged in to Azure CLI
if az account show &> /dev/null
then
    echo "User is logged in"
else
    echo "User is not logged in"
fi

# Load the .env file
set -a
source .env
set +a

# Environment variables
env_vars="AZURE_OPENAI_DEPLOYMENT_NAME AZURE_OPENAI_ENDPOINT AZURE_OPENAI_API_KEY SERVER_NAME DATABASE_NAME SQLADMIN_USER SQL_PASSWORD"

# Create the secrets in the key vault
for var in $env_vars
do
    value=$(printenv $var)
    # Replace underscores with hyphens in the variable name
    var_with_hyphens=${var//_/-}
    az keyvault secret set --vault-name $key_vault_name --name $var_with_hyphens --value $value
done