import os
import re

# Prompt for directory path
directory = input("Enter the directory path: ")

# Create lists to store file names and extensions
file_names = []
extensions = []

# Define a regex pattern to match video qualities, specific words, additional patterns, video codecs, web, web-dl, x264, x265, hd, cam, consecutive spaces, and [EgyBest]
pattern = re.compile(r'\b\d{3,4}p\b|HDCAM|Wecima|tube|dvd|rip|\[egybest\]|web[- ]?dl|x264|x265|h264|mpeg4|hd|bluray|cam| {2,}|\[EgyBest\]', re.IGNORECASE)

# Iterate over files in the directory
for file in os.listdir(directory):
    # Check if the current item is a file
    if os.path.isfile(os.path.join(directory, file)):
        # Split the file name and extension
        file_name, file_extension = os.path.splitext(file)

        # Remove video qualities, specific words, additional patterns, video codecs, web, web-dl, x264, x265, hd, cam, consecutive spaces, and [EgyBest] from the file name
        file_name = re.sub(pattern, ' ', file_name)

        # Replace dots with spaces in the file name
        file_name = file_name.replace(".", " ")

        # Remove extra whitespace from the modified file name
        file_name = file_name.strip()

        # Append the modified file name to the list
        file_names.append(file_name)

        # Append the extension to the list
        extensions.append(file_extension)

# Rename the files in the directory
for i, file in enumerate(os.listdir(directory)):
    # Check if the current item is a file
    if os.path.isfile(os.path.join(directory, file)):
        # Get the modified file name and extension
        modified_file_name = file_names[i]
        file_extension = extensions[i]

        # Create the new file name with the extension
        new_file_name = modified_file_name + file_extension

        # Get the absolute paths of the old and new file names
        old_file_path = os.path.join(directory, file)
        new_file_path = os.path.join(directory, new_file_name)

        # Rename the file
        os.rename(old_file_path, new_file_path)

print("File names in the directory have been renamed.")
