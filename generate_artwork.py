import os
import random
from multiprocessing import Pool
from functools import partial
import sys
from PIL import Image, ImageDraw, ImageFont
import time
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

# Get the number of unique artworks
num_artworks = int(sys.argv[1]) if len(sys.argv) > 1 else 10

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Create a list of available PNG files for each body part
png_files = {}
for folder_name, folder_path in folders.items():
    png_files[folder_name] = [os.path.join(folder_path, file) for file in os.listdir(
        folder_path) if file.endswith('.png')]

# Generate unique artwork
generated_artworks = set()


def generate_artwork(folders, png_files, artwork_id):
    # Generate a random combination of PNG files
    artwork = {}
    for folder_name, files in png_files.items():
        artwork[folder_name] = random.choice(files)

    # Create a unique identifier for the artwork based on the chosen files
    artwork_id = f"a{artwork_id}"

    # Check if the artwork has already been generated
    if artwork_id not in generated_artworks:
        generated_artworks.add(artwork_id)

        # Create a new image with a transparent background with a specific size of 1080x1080
        canvas = Image.new('RGBA', (1080, 1080), (255, 255, 255))

        # Paste each body part onto the canvas
        for file_path in artwork.values():
            part_image = Image.open(file_path).convert('RGBA')
            canvas.paste(part_image, (0, 0), mask=part_image)

        # Remove the alpha channel to make the background fully opaque
        canvas = canvas.convert('RGB')

        # Save the merged image
        image_path = os.path.join(output_folder, f"{artwork_id}.png")
        canvas.save(image_path)

# Function to be used for parallel execution


def generate_and_save_artwork(artwork_id):
    generate_artwork(folders.copy(), png_files.copy(), artwork_id)


# Main execution with multiprocessing
if __name__ == "__main__":
    start_time = time.time()  # Record the start time

    with Pool(processes=os.cpu_count()) as pool:
        # Use partial function to pass additional arguments to generate_and_save_artwork
        partial_generate_and_save = partial(generate_and_save_artwork)
        pool.map(partial_generate_and_save, range(num_artworks))

    end_time = time.time()  # Record the end time
    elapsed_time = end_time - start_time

    print(f"{num_artworks} unique artworks generated in the '{output_folder}' folder.")
    print(f"Processing time: {elapsed_time:.2f} seconds")
