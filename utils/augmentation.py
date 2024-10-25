import cv2
import os
import albumentations as A
import random
import string
from pathlib import Path
from utils.logger import log_info

# Function to load images from a directory
def load_images_from_folder(folder):
    return [
        (cv2.imread(os.path.join(folder, filename)), filename) 
        for filename in os.listdir(folder) 
        if cv2.imread(os.path.join(folder, filename)) is not None
    ]

# Function to generate a random prefix
def generate_random_prefix(length=5):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

# Define your optimized augmentation pipeline
def create_augmentation_pipeline():
    return [
        ("original", None),  # Original image (no augmentation)
        ("flip_horizontal", A.HorizontalFlip(p=1.0)),
        ("flip_vertical", A.VerticalFlip(p=1.0)),
        ("rotate", A.Rotate(limit=(-30, 30), p=1.0)),  # Combined rotation
        ("crop", A.RandomCrop(width=430, height=430, p=1.0)),
        ("color_jitter", A.HueSaturationValue(hue_shift_limit=10, sat_shift_limit=20, val_shift_limit=20, p=0.5)),
        ("channel_shuffle", A.ChannelShuffle(p=0.5)),
    ]

# Function to apply augmentations and save images
def apply_and_save_augmentations(images, augmentations, save_folder):
    os.makedirs(save_folder, exist_ok=True)  # Create directory if not exists
    
    for index, (img, filename) in enumerate(images, start=1):
        for name, augmentation in augmentations:
            prefix = generate_random_prefix(5)  # Random prefix for filenames
            
            if augmentation:  # Only apply valid augmentations
                try:
                    augmented = augmentation(image=img)['image']
                except Exception as e:
                    print(f"Error applying {name} to {filename}: {e}")
                    continue
            else:  # Original image
                augmented = img
            
            new_filename = f'{prefix}_{name}_{filename}'
            cv2.imwrite(os.path.join(save_folder, new_filename), augmented)
        log_info(f"Applied augmentation ({index} / {len(images)})")

# Main function
def dataAugmentation(source_dir, save_folder):
    images = load_images_from_folder(source_dir)
    augmentations = create_augmentation_pipeline()
    apply_and_save_augmentations(images, augmentations, save_folder)
