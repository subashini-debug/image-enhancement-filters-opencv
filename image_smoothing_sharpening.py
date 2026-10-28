# Image Smoothing and Sharpening Using OpenCV
# Developed By: Subashini K
# Register Number: 212225240160

import cv2
import matplotlib.pyplot as plt
import numpy as np

# Read image and convert to RGB
image1 = cv2.imread("city.jpg")
image2 = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)

# 1. Averaging Filter
kernel = np.ones((11, 11), np.float32) / 169
image3 = cv2.filter2D(image2, -1, kernel)

plt.figure(figsize=(9, 9))
plt.subplot(1, 2, 1)
plt.imshow(image2)
plt.title("Original Image")
plt.axis("off")
plt.subplot(1, 2, 2)
plt.imshow(image3)
plt.title("Average Filter Image")
plt.axis("off")
plt.show()

# 2. Weighted Average Filter
kernel1 = np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]]) / 16
image2 = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
image3 = cv2.filter2D(image2, -1, kernel1)

plt.figure(figsize=(9, 9))
plt.subplot(1, 2, 1)
plt.imshow(image2)
plt.title("Original Image")
plt.axis("off")
plt.subplot(1, 2, 2)
plt.imshow(image3)
plt.title("Weighted Average Filter Image")
plt.axis("off")
plt.show()

# 3. Gaussian Blur
gaussian_blur = cv2.GaussianBlur(image2, (33, 33), 0, 0)

plt.figure(figsize=(9, 9))
plt.subplot(1, 2, 1)
plt.imshow(image2)
plt.title("Original Image")
plt.axis("off")
plt.subplot(1, 2, 2)
plt.imshow(gaussian_blur)
plt.title("Gaussian Blur")
plt.axis("off")
plt.show()

# 4. Median Blur
median = cv2.medianBlur(image2, 13)

plt.figure(figsize=(9, 9))
plt.subplot(1, 2, 1)
plt.imshow(image2)
plt.title("Original Image")
plt.axis("off")
plt.subplot(1, 2, 2)
plt.imshow(median)
plt.title("Median Blur")
plt.axis("off")
plt.show()

# 5. Laplacian Sharpening Kernel
kernel2 = np.array([[-1, -1, -1], [2, -2, 1], [2, 1, -1]])
image3 = cv2.filter2D(image2, -1, kernel2)

plt.figure(figsize=(9, 9))
plt.subplot(1, 2, 1)
plt.imshow(image2)
plt.title("Original Image")
plt.axis("off")
plt.subplot(1, 2, 2)
plt.imshow(image3)
plt.title("Laplacian Kernel")
plt.axis("off")
plt.show()

# 6. Laplacian Operator
laplacian = cv2.Laplacian(image2, cv2.CV_64F)

plt.figure(figsize=(9, 9))
plt.subplot(1, 2, 1)
plt.imshow(image2)
plt.title("Original Image")
plt.axis("off")
plt.subplot(1, 2, 2)
plt.imshow(laplacian)
plt.title("Laplacian Operator")
plt.axis("off")
plt.show()
