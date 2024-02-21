#!/bin/bash

#----------------------------------------------------
# Path: delete-venv.sh
# Author: King David Consulting LLC
# Description: This script deletes the virtual environment
# chmod +x delete-venv.sh
# command: ./delete-venv.sh <.venv>
#----------------------------------------------------

echo "Deleting Python virtual environment"

# if name for the environment is not provided, use default name .venv
if [ -z "$1" ]; then
    name=".venv"
else
    name=$1
fi

# Deactivate environment
source $name/bin/deactivate

# Remove environment directory
rm -rf $name

echo "Environment $name has been removed."