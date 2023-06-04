import os
import re
import sys

def rename_files(directory, series_name, pattern):
    for root, dirs, files in os.walk(directory):
        for filename in files:
            file_name, file_ext = os.path.splitext(filename)
            match = re.search(pattern, filename, re.IGNORECASE)

            if match:
                season_number = match.group(1)
                episode_number = match.group(2)
                
                new_file_name = f"{series_name} S{season_number}E{episode_number}{file_ext}"
                current_path = os.path.join(root, filename)
                new_path = os.path.join(root, new_file_name)
                os.rename(current_path, new_path)
                print(f"Renamed {filename} to {new_file_name}.")

directory = input("Enter the directory path: ")
series_name = input("Enter the series name: ")
pattern = r"s(\d{2})e(\d{2})"

if not os.path.isdir(directory):
    print("Invalid directory path. Please try again.")
    sys.exit(1)

rename_files(directory, series_name, pattern)
