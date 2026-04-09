#!/usr/bin/env python3
"""Remove green screen background from penguin sprite images."""
from PIL import Image
import sys

def remove_green(input_path, output_path, threshold=100):
    img = Image.open(input_path).convert("RGBA")
    pixels = img.load()
    w, h = img.size
    
    for y in range(h):
        for x in range(w):
            r, g, b, a = pixels[x, y]
            # If the pixel is predominantly green (green screen)
            if g > threshold and g > r * 1.4 and g > b * 1.4:
                pixels[x, y] = (0, 0, 0, 0)  # Make transparent
    
    img.save(output_path, "PNG")
    print(f"Saved: {output_path}")

remove_green("assets/penguin_stand_1775693270487.png", "assets/penguin_stand.png")
remove_green("assets/penguin_duck_1775693283846.png", "assets/penguin_duck.png")
print("Done!")
