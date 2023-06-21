import os
import re

# Ask for the directory path
dir_path = input("Enter the directory path: ")

# Ask for the starting episode number
start_episode = int(input("Enter the starting episode number: "))

# Get a list of files in the directory
files = os.listdir(dir_path)

# Filter files that match the pattern 'One Piece E' followed by three digits
pattern = r'One Piece E(\d{3})'
matching_files = [file for file in files if re.match(pattern, file)]

# Sort the files in reverse order
matching_files.sort(reverse=True)

# Iterate over the files and rename them
for file in matching_files:
    # Extract the episode number from the file name
    episode_num = int(re.search(pattern, file).group(1))
    
    # Increment the episode number by 1
    new_episode_num = episode_num + 1
    
    # Generate the new file name
    new_file_name = re.sub(pattern, f'One Piece E{new_episode_num:03}', file)
    
    # Get the full paths of the old and new files
    old_file_path = os.path.join(dir_path, file)
    new_file_path = os.path.join(dir_path, new_file_name)
    
    # Rename the file
    os.rename(old_file_path, new_file_path)
    print(f'Renamed "{old_file_path}" to "{new_file_path}"')

    # Check if the current episode number matches the starting episode
    if episode_num == start_episode:
        break
