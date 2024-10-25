import os
import shutil
from colorama import Fore, Style

def clear_folder(folder_path):
    if os.path.exists(folder_path):
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)  # Delete the file or symlink
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)  # Delete the directory and its contents


def mainMenu():
    os.system('clear')
    print(Fore.GREEN + "AIT DATASET PREPERATION\n")
    print(Fore.BLUE + "1 -" + Style.RESET_ALL + " Data Augmentation")
    print(Fore.BLUE + "2 -" + Style.RESET_ALL + " Rename Images")
    print(Fore.BLUE + "3 -" + Style.RESET_ALL + " Caption Images")
    print(Fore.RED + "(Q) EXIT" + Style.RESET_ALL)

def dataAugmentationMenu(source_dir, save_folder):
    print(Fore.GREEN + "DATA AUGMENTATION\n")
    print(Fore.BLUE + "1 -" + Style.RESET_ALL + " Show directory paths")
    print(Fore.GREEN + "2 - Start data augmentation")
    print(Fore.YELLOW + "(Q) Main Menu" + Style.RESET_ALL)

    while True:
        try:
            choice = int(input("\nEnter your choice: "))
        except:
            break

        if choice == 1:
            print(Fore.BLUE + "\nOriginal images directory: " + Style.RESET_ALL + str(source_dir))
            print(Fore.BLUE + "Augmented images save directory: " + Style.RESET_ALL + str(save_folder))

        elif choice == 2:
            from utils.augmentation import dataAugmentation
            clear_folder(save_folder)
            dataAugmentation(source_dir, save_folder)
            