import os
import re
import sys

directory = input("Enter the directory path: ")
series_name = input("Enter the series name: ")
pattern = r"s(\d{2})e(\d{2})"

if not os.path.isdir(directory):
    print("Invalid directory path. Please try again.")
    sys.exit(1)

for filename in os.listdir(directory):
    file_name, file_ext = os.path.splitext(filename)
    match = re.search(pattern, filename, re.IGNORECASE)

    if match:
        season_number = match.group(1)
        episode_number = match.group(2)
    
        new_file_name = f"{series_name} S{season_number}E{episode_number}{file_ext}"
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_file_name))
        print(f"Renamed {file_name} to {new_file_name}.")
