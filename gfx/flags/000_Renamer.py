import os

# Get the current directory
current_directory = os.getcwd()

# Loop through all files in the directory
for filename in os.listdir(current_directory):
    if "original" in filename:
        new_filename = filename.replace("original","new thing")
        old_path = os.path.join(current_directory, filename)
        new_path = os.path.join(current_directory, new_filename)
        os.rename(old_path, new_path)
        print(f'Renamed: "{filename}" → "{new_filename}"')

print("Renaming process completed!")
