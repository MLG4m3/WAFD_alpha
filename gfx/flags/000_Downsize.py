import os
from PIL import Image

def resize_and_save_files(medium_dir, small_dir):
    # List all .tga files in the current directory
    files = [file for file in os.listdir() if file.lower().endswith(".tga")]
    
    if not files:
        print("No .tga files found in the current directory.")
        return
    
    # Resize and save images for medium directory (41x26)
    for file in files:
        img = Image.open(file)
        resized_img = img.resize((41, 26))
        output_file = os.path.join(medium_dir, file)
        resized_img.save(output_file)
        print(f"Resized and saved {file} to {output_file} (Medium)")

    # Resize and save images for small directory (10x7)
    for file in files:
        img = Image.open(file)
        resized_img = img.resize((10, 7))
        output_file = os.path.join(small_dir, file)
        resized_img.save(output_file)
        print(f"Resized and saved {file} to {output_file} (Small)")

def main():
    medium_dir = "medium"
    small_dir = "small"
    
    # Create output directories if they don't exist
    os.makedirs(medium_dir, exist_ok=True)
    os.makedirs(small_dir, exist_ok=True)
    
    # Process all .tga files
    resize_and_save_files(medium_dir, small_dir)

if __name__ == "__main__":
    main()