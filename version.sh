#!/bin/bash

#----------------------------------------------------
# Path: version.sh
# Author: King David Consulting LLC
# Description: This script reads the requirements.txt file and prints the package name and its version
# chmod +x version.sh
# command: ./version.sh <requirements.txt>
#----------------------------------------------------

# input the name of requirements.txt file if not provided use default
if [ -z "$1" ]; then
    file="requirements.txt"
else
    file=$1
fi

echo "Using: $file"

# Check if $file exists
if [ ! -f $file ]; then
    echo "$file not found"
    exit 1
fi

# Check if python is installed
if ! [ -x "$(command -v python)" ]; then
    echo "python is not installed"
    exit 1
fi

# Check if pip is installed
if ! [ -x "$(command -v pip)" ]; then
    echo "pip is not installed"
    exit 1
fi

# Read requirements.txt and get package names
while IFS= read -r line
do
    # Skip lines that contain '-r' or are empty
    if [[ $line =~ "-r" ]] || [[ -z "$line" ]]; then
        continue
    fi
    package=$(echo $line | cut -d'=' -f1)
    version=$(pip show $package | grep Version | cut -d' ' -f2)
    echo "$package==$version"
done < $file