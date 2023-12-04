import os
import re

def rename_images_to_digits(folder_path):
    # Get a list of all files in the folder
    files = os.listdir(folder_path)

    for file_name in files:
        # Check if the file name contains any digits
        if any(char.isdigit() for char in file_name):
            # Generate the new file name by removing non-digit characters
            new_file_name = re.sub(r'\D', '', file_name)

            # Construct the full paths for the old and new file names
            old_path = os.path.join(folder_path, file_name)
            new_path = os.path.join(folder_path, new_file_name+'.jpg')

            # Rename the file
            os.rename(old_path, new_path)
            print(f'Renamed: {file_name} to {new_file_name}')
        else:
            print(f'Skipped: {file_name} (no digits)')

# Replace 'your_folder_path' with the path to your image folder
folder_path = './'
rename_images_to_digits(folder_path)