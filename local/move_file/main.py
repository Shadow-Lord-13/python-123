import os
import shutil

def move_file(source_path, destination_folder):
    try:
        if not os.path.isfile(source_path):
            print(f"File does not exist at source folder location: {source_path}")
        
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)
            print(f"Destination folder created: {destination_folder}")

        file_name = os.path.basename(source_path)

        destination_path = os.path.join(destination_folder, file_name)

        #shutil.copy(source_path, destination_path) for move file 
        shutil.copy(source_path, destination_path)
        print(f"File moved successfully to destination path: {destination_path}")

    except Exception as e:
        print(f"Exception occured while moving the file: {e}")

if __name__ == "__main__":
    source_path = "F:/python/projects/files/source_folder/test.txt"
    destination_folder = "F:/python/projects/files/destination_folder"

    move_file(source_path, destination_folder)