# Python training - numpy
## Library import


import cv2
import matplotlib.pyplot as plt
import numpy as np

## Image import and format processing"""

image = cv2.imread("../images/chroma.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

landscape = cv2.imread("../images/landscape.jpg")
landscape = cv2.cvtColor(landscape, cv2.COLOR_BGR2RGB)
width_height = (image.shape[1], image.shape[0])
landscape = cv2.resize(landscape, width_height)

plt.subplot(121)
plt.imshow(image)
plt.subplot(122)
plt.imshow(landscape)

"""## Ndarrays shape"""

print(image.shape)

"""## Image channel split"""

# rgb(78, 253, 0)

r = image[:, :, 0]
g = image[:, :, 1]
b = image[:, :, 2]

plt.subplot(221)
plt.imshow(r, cmap="gray")
plt.subplot(222)
plt.imshow(g, cmap="gray")
plt.subplot(223)
plt.imshow(b, cmap="gray")
plt.subplot(224)
plt.imshow(image)

"""## Image thresholding"""

r_mask = (r < 77) | (r >= 79)
g_mask = (g < 250) | (g >= 255)
b_mask = b != 0

plt.subplot(221)
plt.imshow(r_mask, cmap="gray")
plt.subplot(222)
plt.imshow(g_mask, cmap="gray")
plt.subplot(223)
plt.imshow(b_mask, cmap="gray")
plt.subplot(224)
plt.imshow(image)

"""## Image masks creation"""

rgb_mask = r_mask & g_mask & b_mask
negative_rgb_mask = np.invert(rgb_mask)

plt.subplot(121)
plt.imshow(rgb_mask, cmap="gray")
plt.subplot(122)
plt.imshow(negative_rgb_mask, cmap="gray")

"""## Image masking"""

masked_image = image * rgb_mask[:, :, None]

masked_landscape = landscape * negative_rgb_mask[:, :, None]

plt.subplot(121)
plt.imshow(masked_image)
plt.subplot(122)
plt.imshow(masked_landscape)

"""## Results"""

new_image = masked_image + masked_landscape

plt.imshow(new_image)
