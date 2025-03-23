import os

# Get user input for the text to replace and the new text
original_text = input("Enter the text you want to replace: ")
new_text = input("Enter the new text: ")

# Get the current directory
current_directory = os.getcwd()

# Loop through all files in the directory
for filename in os.listdir(current_directory):
    if original_text in filename:
        new_filename = filename.replace(original_text, new_text)
        old_path = os.path.join(current_directory, filename)
        new_path = os.path.join(current_directory, new_filename)
        os.rename(old_path, new_path)
        print(f'Renamed: "{filename}" → "{new_filename}"')

print("Renaming process completed!")
