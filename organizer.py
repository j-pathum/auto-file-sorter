import os
import shutil

# 1. Define the directory to clean
# Change this path to whatever folder you want to organize
TARGET_FOLDER = './test_folder' 

# 2. Define the mappings: Extension -> Folder Name
EXTENSIONS = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx', '.csv'],
    'Archives': ['.zip', '.rar', '.tar', '.gz'],
    'Audio': ['.mp3', '.wav', '.flac'],
    'Video': ['.mp4', '.mkv', '.mov', '.avi'],
    'Programs': ['.exe', '.msi', '.dmg', '.apk']
}

def create_folders():
    """Creates the category folders if they don't exist."""
    for folder_name in EXTENSIONS.keys():
        folder_path = os.path.join(TARGET_FOLDER, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"Created folder: {folder_name}")

def move_file(filename):
    """Moves a single file to its correct destination."""
    # Get the file extension
    _, extension = os.path.splitext(filename)
    
    # Find which category this extension belongs to
    found_category = False
    for folder_name, ext_list in EXTENSIONS.items():
        if extension.lower() in ext_list:
            source = os.path.join(TARGET_FOLDER, filename)
            destination = os.path.join(TARGET_FOLDER, folder_name, filename)
            
            # Move the file
            try:
                shutil.move(source, destination)
                print(f"Moved: {filename} -> {folder_name}/")
                found_category = True
            except Exception as e:
                print(f"Error moving {filename}: {e}")
            break
    
    # If no category found, skip or move to 'Misc' (Optional)
    if not found_category:
        print(f"Skipped: {filename} (Unknown type)")

def main():
    print(f"--- Organizing: {TARGET_FOLDER} ---")
    
    # Check if target folder exists
    if not os.path.exists(TARGET_FOLDER):
        print("Error: Target folder does not exist.")
        return

    create_folders()

    # Loop through all files in the target directory
    for filename in os.listdir(TARGET_FOLDER):
        # Skip folders, only move files
        if os.path.isfile(os.path.join(TARGET_FOLDER, filename)):
            # Don't move this script itself if it's inside the folder!
            if filename != "organizer.py": 
                move_file(filename)
                
    print("--- Organization Complete ---")

if __name__ == "__main__":
    main()
