import os

# Prompt the user to enter the directory path
directory = input("Enter the directory path where the files are located: ")

# Validate the directory path
if not os.path.isdir(directory):
    print("Invalid directory path. Please try again.")
    exit()

# Iterate over all files in the directory
for filename in os.listdir(directory):
    # Check if the file is a regular file
    if os.path.isfile(os.path.join(directory, filename)):
        file_name, file_ext = os.path.splitext(filename)
        new_file_name = file_name[:13].replace('.', ' ') + file_ext
        new_file_path = os.path.join(directory, new_file_name)
        old_file_path = os.path.join(directory, filename)

        # Rename the file
        os.rename(old_file_path, new_file_path)
        print(f'Renamed {filename} to {new_file_name}')
