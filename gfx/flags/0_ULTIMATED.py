import os
import shutil
from PIL import Image

# Welcome message
print("Welcome to HOI4 Flags Tool!")
print("Type 'help' for a list of commands or 'exit' to quit.")

# Helper functions
def create_tag_file(tag):
    base_file = "TAG.tga"
    if not os.path.isfile(base_file):
        print(f"Base file {base_file} does not exist. Exiting.")
        return
    new_file = f"{tag}.tga"
    shutil.copy(base_file, new_file)
    print(f"Copied {base_file} to {new_file}")

def copy_and_rename_files(tag):
    ideologies = ["AN", "ML", "RS", "PL", "CL", "AC", "NA", "NF"]
    for ideology in ideologies:
        original_file = f"TAG_{ideology}.tga"
        if not os.path.isfile(original_file):
            print(f"File {original_file} does not exist. Skipping.")
            continue
        new_file = f"{tag}_{ideology}.tga"
        shutil.copy(original_file, new_file)
        print(f"Copied {original_file} to {new_file}")

def resize_all_files(tag=None):
    medium_dir = "medium"
    small_dir = "small"
    os.makedirs(medium_dir, exist_ok=True)
    os.makedirs(small_dir, exist_ok=True)
    
    # Fetch .tga files
    files = [file for file in os.listdir() if file.lower().endswith(".tga")]
    
    if tag and tag != "ALL":
        files = [file for file in files if file.upper().startswith(tag.upper())]
    
    if not files:
        print("No .tga files found to resize.")
        return
    
    for file in files:
        try:
            img = Image.open(file)
            resized_img_medium = img.resize((41, 26))
            output_file_medium = os.path.join(medium_dir, file)
            resized_img_medium.save(output_file_medium)
            print(f"Resized and saved {file} to {output_file_medium} (Medium)")
            
            resized_img_small = img.resize((10, 7))
            output_file_small = os.path.join(small_dir, file)
            resized_img_small.save(output_file_small)
            print(f"Resized and saved {file} to {output_file_small} (Small)")
        
        except Exception as e:
            print(f"Error processing {file}: {e}")

    print("Resizing operation finished successfully.")

def rename_files(original_prefix, new_prefix):
    # Get the current directory
    current_directory = os.getcwd()

    # Loop through all files in the directory
    files_renamed = False
    for filename in os.listdir(current_directory):
        if filename.upper().startswith(original_prefix.upper()):
            new_filename = filename.replace(original_prefix, new_prefix)
            old_path = os.path.join(current_directory, filename)
            new_path = os.path.join(current_directory, new_filename)
            os.rename(old_path, new_path)
            print(f'Renamed: "{filename}" → "{new_filename}"')
            files_renamed = True

    if not files_renamed:
        print(f"No files found starting with '{original_prefix}' to rename.")

    print("Renaming process completed!")

def rename_text_in_files():
    # Get user input for the text to replace and the new text
    original_text = input("Enter the text you want to replace: ")
    new_text = input("Enter the new text: ")

    # Get the current directory
    current_directory = os.getcwd()

    # Loop through all files in the directory
    files_renamed = False
    for filename in os.listdir(current_directory):
        if original_text in filename:
            new_filename = filename.replace(original_text, new_text)
            old_path = os.path.join(current_directory, filename)
            new_path = os.path.join(current_directory, new_filename)
            os.rename(old_path, new_path)
            print(f'Renamed: "{filename}" → "{new_filename}"')
            files_renamed = True

    if not files_renamed:
        print(f"No files found containing '{original_text}' to rename.")

    print("Renaming process completed!")

def print_joe():
    copypasta = """
Joe Biden is a Dengist economic reformer in the American Soviet Socialist Union.
His policies are a perfect blend of socialist planning and market-oriented reforms,
bringing prosperity to the proletariat while maintaining the revolutionary spirit.
Long live Comrade Biden!
"""
    print(copypasta)

# Main loop
while True:
    command = input("> ").strip().lower()
    
    if command == "exit":
        print("Exiting HOI4 Flags Tool. Goodbye!")
        break
    
    elif command == "help":
        print("""
Commands:
- exit: Exit the tool.
- help: Show this help message.
- copy <TAG>: Create a unique copy of TAG.tga with the specified tag.
- copy all <TAG>: Copy and rename all ideology files with the specified tag.
- downsize <TAG> or downsize all: Resize all .tga files to medium (41x26) and small (10x7) sizes. Optionally specify a tag.
- rename: Rename files by replacing part of the filename.
- rename <OLD_PREFIX> to <NEW_PREFIX>: Rename files that start with the old prefix to the new prefix.
""")
    
    elif command.startswith("copy"):
        parts = command.split()
        if len(parts) < 2:
            print("Error: Missing TAG. Usage: copy <TAG> or copy all <TAG>")
        elif parts[1] == "all":
            if len(parts) < 3:
                print("Error: Missing TAG. Usage: copy all <TAG>")
            else:
                tag = parts[2].upper()
                copy_and_rename_files(tag)
        else:
            tag = parts[1].upper()
            create_tag_file(tag)
    
    elif command == "downsize all":
        resize_all_files()  # Downsize all files
    elif command.startswith("downsize"):
        parts = command.split()
        if len(parts) < 2:
            print("Error: Missing tag or 'all'. Usage: downsize <TAG> or downsize all")
        else:
            tag = parts[1].upper()
            resize_all_files(tag)  # Only resize files starting with this tag
    
    elif command == "rename":
        rename_text_in_files()  # Trigger the text replacement renaming functionality

    elif command.startswith("rename "):
        parts = command.split()
        if len(parts) == 4 and parts[2] == "to":
            original_prefix = parts[1].upper()
            new_prefix = parts[3].upper()
            try:
                # Trigger the renaming by prefix functionality
                rename_files(original_prefix, new_prefix)
            except Exception as e:
                print(f"Error during renaming: {e}")
        else:
            print("Error: Invalid rename command. Usage: rename <OLD_PREFIX> to <NEW_PREFIX>")

    elif command in ["printjoe", "joe", "biden", "liberal", "brandon", "joebiden"]:
        print_joe()
    
    else:
        print("Error: Unknown command. Type 'help' for a list of commands.")
