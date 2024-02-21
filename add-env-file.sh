#!/bin/bash

#----------------------------------------------------
# Path: add-env-file.sh
# Author: King David Consulting LLC
# Description: This script creates a .env file and adds secrets from a key vault to it
# chmod +x add-env-file.sh
# command: ./add-env-file.sh
#----------------------------------------------------

echo "This script creates a .env file and adds secrets from a key vault to it"

# Prompt the user for the key vault name
echo "Please enter the .env name to store secrets:"
read env_name

echo "Please enter the key vault name:"
read key_vault_name

# Environment variables
env_vars="AZURE-OPENAI-DEPLOYMENT-NAME AZURE-OPENAI-ENDPOINT AZURE-OPENAI-API-KEY SERVER-NAME DATABASE-NAME SQLADMIN-USER SQL-PASSWORD"

# Create $env_name file
touch $env_name

# Get the secrets from the key vault and write them to $env_name
for var in $env_vars
do
    # Replace hyphens with underscores in the variable name
    var_with_underscores=${var//-/_}
    value=$(az keyvault secret show --name $var --vault-name "$key_vault_name" --query value -o tsv)
    echo "$var_with_underscores=$value" >> $env_name
done