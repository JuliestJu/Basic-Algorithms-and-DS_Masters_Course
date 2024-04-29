import argparse
import os
import shutil

def parse_args():
    parser = argparse.ArgumentParser(description="Recursively copy files to a new directory sorted by file extension.")
    parser.add_argument("source", type=str, help="The source directory to copy files from.")
    parser.add_argument("-d", "--destination", type=str, help="The destination directory to copy files to.", default="dist")
    args = parser.parse_args()
    return args.source, args.destination

def recurse_dir(path, dest):
    try:
        for item in os.listdir(path):
            full_path = os.path.join(path, item)
            if os.path.isdir(full_path):
                recurse_dir(full_path, dest)  # Recursively traverse into directories
            elif os.path.isfile(full_path):
                copy_file(full_path, dest)  # Handle file copying
    except PermissionError:
        print(f"Permission denied: {path}")

def copy_file(file_path, dest):
    extension = os.path.splitext(file_path)[1].lstrip('.').lower()
    if extension == '':
        extension = 'no_extension'  # Handling files without an extension
    dest_dir = os.path.join(dest, extension)
    os.makedirs(dest_dir, exist_ok=True)  # Create target directory if it doesn't exist
    shutil.copy(file_path, dest_dir)
    print(f"Copied {file_path} to {dest_dir}")

def main():
    source, destination = parse_args()
    recurse_dir(source, destination)

if __name__ == "__main__":
    main()