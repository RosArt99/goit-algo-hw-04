import os
import sys
from log import show_tree, print_root

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <path_to_directory>")
        return

    path = sys.argv[1]

    if not os.path.exists(path):
        print(f"Error: path '{path}' not found.")
        return

    print_root(path)
    show_tree(path)

if __name__ == "__main__":
    main()

