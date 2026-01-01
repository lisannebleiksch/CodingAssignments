# Winc Academy Assignment: Files

__winc_id__: ae539110d03e49ea8738fd413ac44ba8  
__human_name__: files  

## Goal
You will practice working with files and folders in Python. You will:

- Create and clean a folder programmatically
- Extract a ZIP file using the standard library
- List files inside a folder
- Read text files and search for specific content
- Return a value found in the files

A `data.zip` file is already in this project folder. Your code must use it.

## What you get
The starter code already contains imports and these paths:

- `my_zip_file` points to `data.zip` in the current working directory
- `my_cache_dir` points to a folder named `cache` in the current working directory

## Assignment
Implement these functions so that the script can find and return the password hidden inside the extracted files.

### 1) `clean_cache()`
Create an empty folder named `cache` in the current directory.

Requirements:
- If `cache` already exists, delete it including all its contents
- Create a new empty `cache` folder

Hints:
- Use `os.path.exists`
- Use `shutil.rmtree` to remove an existing folder
- Use `os.mkdir` to create the folder

### 2) `cache_zip(zip_file_path, cache_dir_path)`
Extract the contents of `data.zip` into the `cache` folder.

Requirements:
- Use `zipfile.ZipFile` in read mode
- Extract all files to `cache_dir_path`

Hints:
- `ZipFile(..., "r")`
- `.extractall(cache_dir_path)`

### 3) `cached_files()`
Return a list of file paths for all files inside the `cache` folder.

Requirements:
- Return full paths, not just file names
- The return type is a list of strings

Hints:
- `os.listdir(cache_dir)`
- `os.path.join(cache_dir, filename)`

### 4) `find_password(all_cache_files)`
Search through the extracted files and return the password.

Requirements:
- `all_cache_files` is a list of file paths as returned by `cached_files()`
- Open each file in text mode
- Scan the lines for one that contains the word `"password"`
- When found, extract and return only the password value

Expected format in a file:
- A line that looks like `password: <value>`

## What "good" looks like
- Running the script creates a fresh `cache` folder
- The zip contents end up inside `cache`
- `cached_files()` returns correct full paths
- `find_password()` returns a string that is the password and nothing else
- No hardcoded paths to your own machine
