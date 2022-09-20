#imports.
from difflib import diff_bytes
import os
import numpy as np

from PIL import Image
from imagehash import whash #whash is wavelet hash.

threshold = 1

if __name__ == "__main__":
    images = [Image.open(f"imgs/{x}") for x in os.listdir("imgs")]
    hashes = np.array([whash(img) for img in images])
    threshold
    diffs = [] #will be a 2d matrix in a little while.
    for i, ele in enumerate(hashes):
        diffs.append(np.array(hashes) - ele) #vectorization!
    
    diffs = np.array(diffs)
    diffs_mat = np.vstack(diffs) #vertical stack to make matrix.
    print(diffs)

    duplicate_x, duplicate_y = np.where(diffs_mat < threshold)
    
    indexes = [(x, y) for (x, y) in zip(duplicate_x, duplicate_y) if x != y]
    for d1, d2 in indexes:
        print(f"{hashes[d1]}, {hashes[d2]} are duplicates.")
        




