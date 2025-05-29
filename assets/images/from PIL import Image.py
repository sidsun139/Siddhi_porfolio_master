from PIL import Image
import os

# Load the uploaded image
input_path = "C:\Users\siddh\Downloads\jack-portfolio-master\jack-portfolio-master\assets\images\Siddhi-pic.jpeg"
image = Image.open(input_path)

# Define target sizes for large, medium, and small
sizes = {
    "siddhi-lg.png": 1024,  # for large screens
    "siddhi-md.png": 768,   # for medium screens
    "siddhi-sm.png": 480    # for small screens
}

# Resize and save images
output_paths = {}
for name, width in sizes.items():
    # Maintain aspect ratio
    ratio = width / image.width
    height = int(image.height * ratio)
    resized = image.resize((width, height), Image.LANCZOS)
    output_path = f"/mnt/data/{name}"
    resized.save(output_path)
    output_paths[name] = output_path

output_paths