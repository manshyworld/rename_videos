import os
import re

# Specify the directory path where the files are located
directory = input("path:")

# Retrieve a list of files in the directory
file_list = os.listdir(directory)

# Regular expression pattern to match the first number in a file name
pattern = r"\d+"

# Variable to store the extracted episode number
ep = None

# Find the first number in each file name
for file_name in file_list:
    match = re.search(pattern, file_name)
    if match:
        ep = int(match.group())
        break

# Rename the files
if ep is not None:
    season = 1
    if 62 <= ep <= 77:
        season = 2
    elif ep <= 91:
        season = 3
    elif ep <= 130:
        season = 4
    elif ep <= 143:
        season = 5
    elif ep <= 195:
        season = 6
    elif ep <= 228:
        season = 7
    elif ep <= 263:
        season = 8
    elif ep <= 336:
        season = 9
    elif ep <= 381:
        season = 10
    elif ep <= 407:
        season = 11
    elif ep <= 421:
        season = 12
    elif ep <= 456:
        season = 13
    elif ep <= 516:
        season = 14
    elif ep <= 578:
        season = 15
    elif ep <= 628:
        season = 16
    elif ep <= 746:
        season = 17
    elif ep <= 782:
        season = 18
    elif ep <= 891:
        season = 19
    elif 892 <= ep:
        season = 20
    
    for file_name in file_list:
        # Extract the file extension from the original file name
        file_extension = os.path.splitext(file_name)[1]

        # Extract the episode number from the file name
        match = re.search(pattern, file_name)
        if match:
            ep = int(match.group())

        new_file_name = f"One Piece S{season:02d}E{ep:04d}{file_extension}"
        os.rename(os.path.join(directory, file_name), os.path.join(directory, new_file_name))
        ep += 1
