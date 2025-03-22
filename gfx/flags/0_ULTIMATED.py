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
    
    # Fetch .tga files based on tag (if specified)
    files = [file for file in os.listdir() if file.lower().endswith(".tga")]
    if tag and tag != "all":
        files = [file for file in files if file.upper().startswith(tag.upper())]
    
    if not files:
        print("No .tga files found to resize.")
        return
    
    for file in files:
        img = Image.open(file)
        resized_img_medium = img.resize((41, 26))
        output_file_medium = os.path.join(medium_dir, file)
        resized_img_medium.save(output_file_medium)
        print(f"Resized and saved {file} to {output_file_medium} (Medium)")
        
        resized_img_small = img.resize((10, 7))
        output_file_small = os.path.join(small_dir, file)
        resized_img_small.save(output_file_small)
        print(f"Resized and saved {file} to {output_file_small} (Small)")

    print("Resizing operation finished successfully.")

def rename_files(original, new):
    files_found = False
    # Get the current directory
    current_directory = os.getcwd()

    # Loop through all files in the directory
    for filename in os.listdir(current_directory):
        if original.lower() in filename.lower():  # Case-insensitive search
            files_found = True
            new_filename = filename.replace(original, new)
            old_path = os.path.join(current_directory, filename)
            new_path = os.path.join(current_directory, new_filename)
            os.rename(old_path, new_path)
            print(f'Renamed: "{filename}" → "{new_filename}"')

    if not files_found:
        print(f"Error: No files found containing '{original}'.")

def print_joe():
    copypasta = """
Joe Biden is a Dengist economic reform in the American Soviet Socialist Union.
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
- rename <ORIGINAL> to <NEW>: Rename files containing ORIGINAL to NEW.
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
        resize_all_files()  # Downsize all files, no specific tag
    elif command.startswith("downsize"):
        parts = command.split()
        if len(parts) < 2 or (parts[1] != "all" and len(parts) < 3):
            print("Error: Missing tag or 'all'. Usage: downsize <TAG> or downsize all")
        elif parts[1] == "all":
            resize_all_files()  # Downsize all files
        else:
            tag = parts[1].upper()
            resize_all_files(tag)  # Downsize files with specific tag
    
    elif command.startswith("rename"):
        parts = command.split()
        if "to" not in parts:
            print("Error: Missing 'to' in rename command. Usage: rename <ORIGINAL> to <NEW>")
        else:
            to_index = parts.index("to")
            original = " ".join(parts[1:to_index])
            new = " ".join(parts[to_index + 1:])
            rename_files(original, new)

    elif command in ["printjoe", "joe", "biden", "liberal", "brandon", "joebiden"]:
        print_joe()
    
    else:
        print("Error: Unknown command. Type 'help' for a list of commands.")
