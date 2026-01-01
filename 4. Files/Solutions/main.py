import os
import shutil
import zipfile

# Get the directory where this script is located (not where it's run from)
# this is different for your main.py because its in another folder and this file is in a subfolder
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# data.zip is in the parent folder (files/), not in Solutions/
my_zip_file = os.path.join(SCRIPT_DIR, "..", "data.zip")
my_cache_dir = os.path.join(SCRIPT_DIR, "..", "cache")


def clean_cache():
    # creates an empty folder named cache in the current directory
    if os.path.exists(my_cache_dir):
        shutil.rmtree(my_cache_dir)
    os.mkdir(my_cache_dir)

def cache_zip(zip_file_path, cache_dir_path):
    # zip_file_path = my_zip_file
    # cache_dir_path = my_cache_dir
    #use class ZipFile in r (read) modus to read the zip
    with zipfile.ZipFile(zip_file_path, "r") as my_zip:
        my_zip.extractall(cache_dir_path)

# Returns list of file paths in cache
def cached_files():
    all_cache_files = []
    for filename in os.listdir(my_cache_dir):
        filepath = os.path.join(my_cache_dir, filename)
        all_cache_files.append(filepath)
    return all_cache_files

def find_password(all_cache_files):
    for file_path in all_cache_files:
        with open(file_path, "r") as file:
            for line in file:
                if "password" in line:
                    return line.split(": ")[1].strip()

if __name__ == "__main__":
    clean_cache()
    cache_zip(zip_file_path=my_zip_file, cache_dir_path=my_cache_dir)
    password = find_password(cached_files())
    print(f"Password found: {password}")
