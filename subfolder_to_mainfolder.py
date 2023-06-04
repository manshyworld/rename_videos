import os
import shutil

def move_movie_files_to_main_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            destination_path = os.path.join(directory, file)
            file_extension = os.path.splitext(file)[1].lower()

            if file_extension in ['.mp4', '.avi', '.mov', '.wmv', '.flv', '.mkv', '.mpg', '.mpeg', '.webm', '.3gp', '.vob', '.rmvb'] or file_extension == '.srt':
                shutil.move(file_path, destination_path)
                print(f"Moved {file_path} to {destination_path}")

# Prompt the user to enter the main directory
directory_path = input("Enter the path of the main directory: ")

# Call the function to move the movie files and subtitles
move_movie_files_to_main_directory(directory_path)
