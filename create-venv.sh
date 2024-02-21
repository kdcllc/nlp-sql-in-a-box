#!/bin/bash

#----------------------------------------------------
# Path: create-venv.sh
# Author: King David Consulting LLC
# Description: This script creates a virtual environment and installs the packages from requirements.txt
# chmod +x create-venv.sh
# command: ./create-venv.sh <requirements.txt> <.venv>
#----------------------------------------------------

echo "Creating Python virtual environment and installing packages from requirements.txt"

# if requirements.txt file name is not provided, use default name requirements.txt
if [ -z "$1" ]; then
    requirements="requirements.txt"
else
    requirements=$1
fi

# if name for the environment is not provided, use default name .venv
if [ -z "$2" ]; then
    name=".venv"
else
    name=$2
fi

# Create environment
python3 -m venv $name

# Activate environment
source $name/bin/activate

# Install requirements
pip install -r $requirements

echo "Environment $name has been created and packages have been installed."