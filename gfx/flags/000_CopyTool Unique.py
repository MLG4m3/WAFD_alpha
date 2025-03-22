import os
import shutil

def create_tag_file(tag):
    # Base file to copy from
    base_file = "TAG.tga"
    
    # Check if the base file exists
    if not os.path.isfile(base_file):
        print(f"Base file {base_file} does not exist. Exiting.")
        return
    
    # New file name
    new_file = f"{tag}.tga"
    
    # Copy and rename the file
    shutil.copy(base_file, new_file)
    print(f"Copied {base_file} to {new_file}")

if __name__ == "__main__":
    # Get the tag from user input
    tag = input("Enter the 3-letter tag: ").strip().upper()
    
    # Call the function
    create_tag_file(tag)
