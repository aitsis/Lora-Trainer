import os
import uuid
from utils.logger import log_info

def rename(target_dir, source_file, index):
    new_name = str(index) + ".png"
    target_path = os.path.join(target_dir, new_name)
    
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    
    if os.path.exists(target_path):
        index += 1
        return rename(target_dir, source_file, index)
    
    os.rename(source_file, target_path)
    log_info(f"Renamed {source_file} to {new_name}")

def rename_images(target_dir):
    # Step 1: Rename all files to random temporary names
    temp_names = {}
    for filename in os.listdir(target_dir):
        file_path = os.path.join(target_dir, filename)
        if os.path.isfile(file_path):
            temp_name = str(uuid.uuid4()) + ".tmp"
            temp_path = os.path.join(target_dir, temp_name)
            os.rename(file_path, temp_path)
            temp_names[temp_name] = filename  # Store original name for logging if needed
    
    # Step 2: Apply index-based renaming
    index = 1
    for temp_name in temp_names:
        temp_path = os.path.join(target_dir, temp_name)
        if os.path.isfile(temp_path):
            rename(target_dir, temp_path, index)
            index += 1
