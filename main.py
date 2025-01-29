import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread
from skimage.color import rgb2gray
from PIL import Image

def add_stripes(image_array, stripe_width):
    height, width = image_array.shape
    striped_image = image_array.copy()

    for i in range(0, width, 2 * stripe_width):
        striped_image[:, i:i + stripe_width] = 0  # פסים שחורים

    return striped_image

image_array = imread('costarica.jpg')

if image_array.ndim == 3:
    image_array = rgb2gray(image_array)

image_array = (image_array * 255).astype(np.uint8)

striped_image = add_stripes(image_array, stripe_width=20)

image_pil = Image.fromarray(striped_image, mode='L')
image_pil.save('striped_costarica.jpeg')

plt.imshow(striped_image, cmap='gray')
plt.title('Striped Costa Rica')
plt.axis('off')
plt.show()
