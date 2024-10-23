#!/bin/bash

source_dir=$(cat config/appconfig.json | jq -r '.source_dir')
save_folder=$(cat config/appconfig.json | jq -r '.save_folder')
captions_folder=$(cat config/appconfig.json | jq -r '.captions_folder')

# Create the directories
mkdir -p "$source_dir" "$save_folder" "$captions_folder"

source .venv/bin/activate
python3 main.py