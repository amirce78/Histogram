from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

def shrink(img: 'np.ndarray', shrink_min= 100, shrink_max= 150) -> 'Image.Image':
    img_np = np.asarray(img, dtype= np.uint8)
    min_graylevel = np.amin(img_np)
    max_graylevel = np.amax(img_np)
    img_result = ((shrink_max - shrink_min) / (max_graylevel - min_graylevel)) * (img - min_graylevel) + shrink_min
    return Image.fromarray(img_result)

def stretch(img: 'np.ndarray', stretch_min= 0, stretch_max= 255) -> 'Image.Image':
    img_np = np.asarray(img, dtype= np.uint8)
    min_graylevel = np.amin(img_np)
    max_graylevel = np.amax(img_np)
    img_result = ((img - min_graylevel) / (max_graylevel - min_graylevel)) * (stretch_max - stretch_min) + stretch_min
    return Image.fromarray(img_result)

def histogram(img: 'Image.Image') -> 'np.ndarray':
    return np.histogram(np.asarray(img, dtype=np.uint8), bins=256, range=(0, 255))[0]

img = Image.open(fp= "./image.png").convert('P') # Convert Image into GrayScale
shrinked_img = shrink(img, shrink_min= 100, shrink_max= 150)
stretched_img = stretch(shrinked_img, stretch_min= 0, stretch_max= 255)

plt.subplot(2, 3, 1)
plt.title("Original")
plt.axis('off')
plt.imshow(img)

plt.subplot(2, 3, 2)
plt.title("Histogram Shrinking [100:150]")
plt.axis('off')
plt.imshow(shrinked_img)

plt.subplot(2, 3, 3)
plt.title("Histogram Stretching [0:255]")
plt.axis('off')
plt.imshow(stretched_img)

plt.subplot(2, 3, 4)
plt.title("Original")
plt.stem(histogram(img), markerfmt=" ")

plt.subplot(2, 3, 5)
plt.title("Histogram Shrinking [100:150]")
plt.stem(histogram(shrinked_img), markerfmt=" ")

plt.subplot(2, 3, 6)
plt.title("Histogram Stretching [0:255]")
plt.stem(histogram(stretched_img), markerfmt=" ")

plt.show()