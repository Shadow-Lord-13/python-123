import os

def main():
    try:       
        folder_path = input("Please enter the folders(With spaces in between: ").split()
        for folder in folder_path:
            files, error_message = list_files(folder)
            if files:
                print(f"===== Listing files for folder - {folder}")
                for file in files:
                    print(file)
            else:
                print(f"===== Error while fetching files from folder - {folder}: {error_message}")
    except Exception as e:
        print(f"Error: {e}")

def list_files(folder_path):
    try:
        files = os.listdir(folder_path)
        return files, None
    except FileNotFoundError:
        return None, "Folder not found"
    except PermissionError:
        return None, "Permission denied"
    
if __name__ == "__main__":
    main()