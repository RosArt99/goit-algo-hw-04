import os
from colorama import Fore, Style, init

init(autoreset=True)

def show_tree(path, indent=""):
    try:
        items = sorted(os.listdir(path))
    except PermissionError:
        print(indent + Fore.RED + "[Permission Denied]")
        return

    for item in items:
        full_path = os.path.join(path, item)
        if os.path.isdir(full_path):
            print(indent + Fore.BLUE + f"{item}/")
            show_tree(full_path, indent + "    ")
        else:
            print(indent + Fore.LIGHTYELLOW_EX + f"{item}")

def print_root(path):
    print(Fore.MAGENTA + f"{os.path.basename(path)}/")
