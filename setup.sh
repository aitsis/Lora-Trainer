#!/bin/bash

python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

source_dir=$(cat config/appconfig.json | jq -r '.source_dir')
save_folder=$(cat config/appconfig.json | jq -r '.save_folder')
captions_folder=$(cat config/appconfig.json | jq -r '.captions_folder')

# Create the directories
mkdir -p "$source_dir" "$save_folder" "$captions_folder"