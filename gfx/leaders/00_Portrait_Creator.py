import os
import shutil

def print_help():
    print("""
User Manual:
-------------
This program helps you create a portrait file by copying and renaming the background.dds file.

How to use:
1. Enter a code in the format: TAG_First_Last (e.g., ABK_John_Doe)
   - The program will create a folder named after the tag if it does not exist (e.g., ABK).
   - It will copy the `background.dds` file into that folder and rename it to `Portrait_TAG_First_Last.dds`.

2. If you type "exit", the program will stop.

3. If you type "help", this manual will be displayed again.

Error Handling:
- "Error: Invalid Code": When the code is blank or doesn't contain an underscore.
- "Error: Couldn't find background.dds": If the background.dds file is missing.
- "Error: TAG_First_Last already exists": If the portrait file already exists in the folder.

Enjoy!
    """)

# Opening message
print(""" Welcome to the WAFD Portrait Creator ! - Type 'Help' if you need it, or type 'Exit' to close.
""")

while True:
    # Ask the user for the code
    code = input(" Command : ").strip()

    if code.lower() == "exit":
        print("Exiting program.")
        break  # Exit the loop

    if code.lower() == "help":
        print_help()
        continue  # Restart the loop

    # Validate the code format (it must contain at least one underscore "_")
    if "_" not in code:
        print("Error: Invalid Code. Expected format: TAG_First_Last")
        continue  # Restart the loop

    # Extract the prefix (e.g., ABK)
    parts = code.split("_")
    prefix = parts[0]

    # Define file names
    source_file = "background.dds"
    destination_folder = os.path.join(os.getcwd(), prefix)
    destination_file = os.path.join(destination_folder, f"Portrait_{code}.dds")

    # Check if the source file exists
    if not os.path.exists(source_file):
        print(f"Error: Couldn't find {source_file}")
        continue  # Restart the loop

    # Create the folder if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Check if the destination file already exists
    if os.path.exists(destination_file):
        print(f"Error: {destination_file} already exists")
        continue  # Restart the loop

    # Copy and rename the file
    shutil.copy(source_file, destination_file)
    print(f"Portrait created: {destination_file}")
