import os
import re

def rename_subtitles(folder_path):
    video_extensions = ['.mp4', '.avi', '.mov', '.wmv', '.flv', '.mkv', '.mpg', '.mpeg', '.webm', '.3gp', '.rmvb', '.vob']  # Add more extensions if needed
    subtitle_extension = ".srt"
    pattern = r"s(\d{2})e(\d{2})"  # Regular expression pattern to match episode number (e.g., s01e01)

    # Get a list of video files in the folder
    video_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f)) and os.path.splitext(f)[1].lower() in video_extensions]

    # Iterate through each video file
    for video_file in video_files:
        video_name = os.path.splitext(video_file)[0]  # Remove the extension
        match = re.search(pattern, video_name, re.IGNORECASE)  # Match episode number using regex

        if match:
            season_number = match.group(1)  # Get the matched season number
            episode_number = match.group(2)  # Get the matched episode number
            subtitle_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f)) and os.path.splitext(f)[1].lower() == subtitle_extension]

            # Iterate through subtitle files
            for subtitle_file in subtitle_files:
                subtitle_name = os.path.splitext(subtitle_file)[0]  # Remove the extension
                subtitle_match = re.search(pattern, subtitle_name, re.IGNORECASE)  # Match episode number in subtitle file name

                if subtitle_match and subtitle_match.group(1) == season_number and subtitle_match.group(2) == episode_number:
                    new_subtitle_file = video_name + subtitle_extension

                    # Rename the subtitle file
                    os.rename(os.path.join(folder_path, subtitle_file), os.path.join(folder_path, new_subtitle_file))

                    print(f"Renamed '{subtitle_file}' to '{new_subtitle_file}'.")

# Example usage
folder_path = input("enter directory: ")
rename_subtitles(folder_path)
