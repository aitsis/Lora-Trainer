import sys
import os
from menu import mainMenu, dataAugmentationMenu
from pathlib import Path
from config import ConfigHandler

from utils.rename import rename_images
from utils.caption import caption_images

config = ConfigHandler("config/appconfig.json")

source_path = config.get_key("source_dir")
save_path = config.get_key("save_folder")
captions_path = config.get_key("captions_folder")

# Generate directories if they don't exist
original_images_dir = Path(source_path) if Path(source_path).is_absolute() else Path.cwd() / source_path
train_images_dir = Path(save_path) if Path(save_path).is_absolute() else Path.cwd() / save_path
captions_dir = Path(captions_path) if Path(captions_path).is_absolute() else Path.cwd() / captions_path

if not os.path.exists(original_images_dir):
    os.makedirs(original_images_dir)
if not os.path.exists(train_images_dir):
    os.makedirs(train_images_dir)
if not os.path.exists(captions_dir):
    os.makedirs(captions_dir)

if __name__ == "__main__":
    while True:
        mainMenu()
        try:
            choice = int(input("Enter your choice: "))
            os.system('clear')
        except:
            print("\nApplication Terminated.")
            sys.exit()
        if choice == 1:
            dataAugmentationMenu(original_images_dir, train_images_dir)
        if choice == 2:
            rename_images(train_images_dir)
        if choice == 3:
            caption_images(train_images_dir, captions_dir)