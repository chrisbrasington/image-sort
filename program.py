#!/usr/bin/env python3
import os
import shutil
import sys

if len(sys.argv) != 3:
    print("Usage: python program.py <input_directory> <output_directory>")
    sys.exit(1)

input_directory = sys.argv[1]
output_directory = sys.argv[2]

print(input_directory)
print(output_directory)

# Create subdirectories if they don't exist
os.makedirs(output_directory, exist_ok=True)

# Initialize a dictionary to store user-modified paths
user_modified_paths = {}

# Initialize an array to store unique paths
unique_paths = []

# Loop through images in the input directory
for filename in os.listdir(input_directory):
    if filename.endswith(('.jpg', '.jpeg', '.png', '.gif')):
        # open with feh
        os.system(f"feh {os.path.join(input_directory, filename)}")

    image_path = os.path.join(input_directory, filename)

    # Ask the user for a file path to move the image to
    while True:
        print(f"Image: {filename}")
        print("Select a path or enter a new path:")
        for i, path in enumerate(unique_paths):
            print(f"{i+1} - {path}")
        user_input = input("Enter path: ")
        if user_input.isdigit() and int(user_input) <= len(unique_paths):
            selected_path = unique_paths[int(user_input)-1]
        else:
            selected_path = user_input
            unique_paths.append(selected_path)
        if os.path.exists(selected_path):
            break
        else:
            print("Invalid path. Please try again.")

    # Move the image to the selected path
    shutil.move(image_path, os.path.join(selected_path, filename))
    user_modified_paths[filename] = selected_path

# Display all the prior paths
print("Prior paths:")
for i, path in enumerate(unique_paths):
    print(f"{i+1} - {path}")

# Update user-modified paths
with open('user_modified_paths.txt', 'w') as file:
    for filename, path in user_modified_paths.items():
        file.write(f"{filename}:{path}\n")
