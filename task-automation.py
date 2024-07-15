import os
import shutil

def organize_files(directory):
    # Change to the specified directory
    os.chdir(directory)

    # Create folders for each file type
    for filename in os.listdir(directory):
        if os.path.isfile(filename):  # Check if it's a file
            file_extension = filename.split('.')[-1] if '.' in filename else 'no_extension'
            # Create a folder for the file extension if it doesn't exist
            if not os.path.exists(file_extension):
                os.makedirs(file_extension)
            # Move the file into the corresponding folder
            shutil.move(filename, os.path.join(file_extension, filename))

    print("Files organized successfully!")

if __name__ == "__main__":
    path = input("Enter the directory path to organize: ")
    if os.path.exists(path):
        organize_files(path)
    else:
        print("The specified directory does not exist.")
