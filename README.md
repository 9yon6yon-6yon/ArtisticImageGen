# Artistic Image Generation

![Banner](/banner.png)

This repository contains a script for generating unique artworks by combining different body parts.

## Folder Arrangement

The folders should be arranged as follows:

1. backgrounds/
2. body/
3. hair/
4. hat/
5. glasses/
6. beard/
7. smoke/
8. hoodie/
9. breclet/
10. socks/
11. shoe/
12. jacket/

Each folder should contain PNG files representing the respective body part. Make sure the PNG files have `transparent` backgrounds and make sure the files are 1080x1080 px of size, If different size is given then change the code of `generate_artwork.py` at `line 56`:
   
    canvas = Image.new('RGBA', (1080, 1080), (0, 0, 0, 0))#1080,1080 is the width and height of the image

## Prerequisites

- Python 3.x
- PIL (Python Imaging Library)

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/9yon6yon-6yon/ArtisticImageGen.git
cd ArtisticImageGen
pip install -r requirements.txt
```
Modify the folders dictionary in the generate_artwork.py file to specify the paths to your folders containing the PNG files and the path to the output file.

Run the script:

```bash
python generate_artwork.py <num_artworks>
```
Replace `<num_artworks>` with the desired number of unique artworks to generate.
The generated artworks will be saved in the `output/` folder.

<hr>
Feel free to customize and modify the content according to your specific requirements.
