import sys
import os
import random
import shutil
from PIL import Image

# Set the paths to your folders containing the PNG files
folders = {
    'backgrounds': '/grbackground',
    'body': '/body',
    'hair': '/hair',
    'hat': '/hat',
    'glasses': '/sunglass',
    'beard': '/beard',
    'smoke': '/smoke',
    'hoodie': '/hoodie',
    'breclet': '/chain',
    'jacket': '/jacket',
    'socks': '/socks',
    'shoe': '/shoes'
  
     
}

# Set the output folder path
output_folder = '/output/'

# Get the number of unique artworks from the command-line argument
num_artworks = int(sys.argv[1]) if len(sys.argv) > 1 else 10

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Create a list of available PNG files for each body part
png_files = {}
for folder_name, folder_path in folders.items():
    png_files[folder_name] = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith('.png')]

# Generate unique artwork
generated_artworks = set()
for _ in range(num_artworks):
    # Generate a random combination of PNG files
    artwork = {}
    for folder_name, files in png_files.items():
        artwork[folder_name] = random.choice(files)

    # Create a unique identifier for the artwork based on the chosen files
    artwork_id = '-'.join([os.path.basename(file).split('.')[0] for file in artwork.values()])

    # Check if the artwork has already been generated
    if artwork_id not in generated_artworks:
        generated_artworks.add(artwork_id)

        # Create a new image with a transparent background with specific size of 1080x1080
        canvas = Image.new('RGBA', (1080, 1080), (0, 0, 0, 0))

        # Paste each body part onto the canvas
        for file_path in artwork.values():
            part_image = Image.open(file_path).convert('RGBA')
            canvas.paste(part_image, (0, 0), mask=part_image)

        # Save the merged image
        image_path = os.path.join(output_folder, f"{artwork_id}.png")
        canvas.save(image_path)

print(f"{num_artworks} unique artworks generated in the '{output_folder}' folder.")
