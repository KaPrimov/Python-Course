import os
import sys


def find_file(start_dir, filename: str) -> str:

    for dirpath, _, filenames in os.walk(start_dir):
        if filename in filenames:
            return os.path.join(dirpath, filename)
    return None

    # if found:
    #     return os.path.join('path', filename)
    # else:
    #     return None
if len(sys.argv) >= 2:
    found_filename = find_file('./', sys.argv[1])
    if found_filename:
        print("Full path to the file: ", found_filename)
    else:
        print("File not found")
else:
    print("Please provide name as first parameter")

