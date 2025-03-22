import os
import shutil

def copy_and_rename_files(tag):
    # List of ideologies
    ideologies = [
    "AN",
    "ML",
    "RS",
    "PL",
    "CL",
    "AC",
    "NA",
    "NF"
]

    
    # Iterate through the ideologies
    for ideology in ideologies:
        # Original file name
        original_file = f"TAG_{ideology}.tga"
        
        # Check if the original file exists
        if not os.path.isfile(original_file):
            print(f"File {original_file} does not exist. Skipping.")
            continue
        
        # New file name
        new_file = f"{tag}_{ideology}.tga"
        
        # Copy and rename the file
        shutil.copy(original_file, new_file)
        print(f"Copied {original_file} to {new_file}")

if __name__ == "__main__":
    # Get the tag from user input
    tag = input("Enter the 3-letter tag: ").strip().upper()
    
    # Call the function
    copy_and_rename_files(tag)
