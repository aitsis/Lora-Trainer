import os
import torch
from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    Trainer,
    TrainingArguments,
)
from accelerate import Accelerator
from datasets import load_dataset
from pathlib import Path
from config import ConfigHandler

config = ConfigHandler("config/appconfig.json")

lora_save_path = config.get_key("lora_save_folder")
logging_path = config.get_key("loging_folder")

# Generate directories if they don't exist
lora_save_dir = Path(lora_save_path) if Path(lora_save_path).is_absolute() else Path.cwd() / lora_save_path
loging_dir = Path(logging_path) if Path(logging_path).is_absolute() else Path.cwd() / logging_path

if not os.path.exists(lora_save_dir):
    os.makedirs(lora_save_dir)
if not os.path.exists(loging_dir):
    os.makedirs(loging_dir)