import os

def main():
    try:
        folders = input("Please enter the folder names: ").split()
        for folder in folders:
            files, error_message = list_files_in_folder(folder)
            if files:
                print(f"===== Listing files in folder - {folder}")
                for file in files:
                    print(file)
            else:
                print(f"===== Error {folder} not found: {error_message}")
    except Exception as e:
        print(f"Error: {e}")

def list_files_in_folder(folder):
    try:
        files = os.listdir(folder)
        return files, None
    except FileNotFoundError:
        return None, "Folder does not exist"
    except PermissionError:
        return None, "Permission Denied!!!"
    
if __name__ == "__main__":
    main()