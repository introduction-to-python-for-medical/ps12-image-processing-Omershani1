from PIL import Image
import numpy as np
from scipy.signal import convolve
from image_utils import load_image, edge_detection
from PIL import Image
from skimage.filters import median
from skimage.morphology import ball
import matplotlib.pyplot as plt

def add_stripes(image_array, stripe_width):
    if image_array.ndim != 2:
        raise ValueError(f"Expected a grayscale (2D) image, but got shape: {image_array.shape}")

    height, width = image_array.shape
    striped_image = image_array.copy()

    for i in range(0, width, 2 * stripe_width):
        striped_image[:, i:i + stripe_width] = 0  

    return striped_image

image_array = imread('costarica.jpg')

print(f"Original shape: {image_array.shape}")  

if image_array.ndim == 3:  
    image_array = rgb2gray(image_array)
    print(f"Converted to grayscale, new shape: {image_array.shape}")  

image_array = (image_array * 255).astype(np.uint8)

striped_image = add_stripes(image_array, stripe_width=20)

image_pil = Image.fromarray(striped_image, mode='L')
image_pil.save('striped_costarica.jpeg')

plt.imshow(striped_image, cmap='gray')
plt.title('Striped Costa Rica')
plt.axis('off')
plt.show()
