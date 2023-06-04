"""
import os
import re

def rename_files_with_series_number():
    directory_path = input("Enter the directory path: ")
    series_number = input("Enter the series number: ")

    files = os.listdir(directory_path)

    for file in files:
        if re.search(r'E(\d+)', file) and not re.search(r'S\d+E(\d+)', file):
            # Extract episode number
            episode_number = re.search(r'E(\d+)', file).group(1)

            # Create new filename with series number
            new_filename = re.sub(r'E(\d+)', f'S{series_number}E{episode_number}', file)

            # Rename the file
            os.rename(os.path.join(directory_path, file), os.path.join(directory_path, new_filename))
            print(f"Renamed {file} to {new_filename}")


# Example usage
rename_files_with_series_number()


import os
import re

def rename_files_with_series_number():
    directory_path = input("Enter the directory path: ")

    files = os.listdir(directory_path)

    series_number = input("Enter the correct series number: ")

    for file in files:
        if re.search(r'E(\d+)', file) and not re.search(r'S\d{2}E(\d+)', file):
            # Extract episode number
            episode_number = re.search(r'E(\d+)', file).group(1)

            # Create new filename with corrected series number
            new_filename = re.sub(r'S(\d)E', f'S{series_number.zfill(2)}E', file)

            # Rename the file
            os.rename(os.path.join(directory_path, file), os.path.join(directory_path, new_filename))
            print(f"Renamed {file} to {new_filename}")


# Example usage
rename_files_with_series_number()

"""

import os
import re

def rename_files_with_series_number():
    directory_path = input("Enter the directory path: ")

    files = os.listdir(directory_path)

    series_number = input("Enter the correct series number: ")

    for file in files:
        if re.search(r'E(\d+)|E(\d+)$', file) and not re.search(r'S\d{2}E(\d+)', file):
            # Extract episode number
            episode_number = re.search(r'E(\d+)|E(\d+)$', file).group(1) or re.search(r'E(\d+)|E(\d+)$', file).group(2)

            # Check if series number is a single digit preceded by 'S'
            series_match = re.search(r'S(\d)', file)
            if series_match:
                series_number = series_match.group(1).zfill(2)

            # Ensure two-digit episode number
            episode_number = episode_number.zfill(2)

            # Create new filename with corrected series number and episode number
            new_filename = re.sub(r'S\d{1}E(\d+)|E(\d+)', f'S{series_number}E{episode_number}', file)

            # Rename the file
            os.rename(os.path.join(directory_path, file), os.path.join(directory_path, new_filename))
            print(f"Renamed {file} to {new_filename}")


# Example usage
rename_files_with_series_number()
