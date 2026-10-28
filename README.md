# Image Smoothing and Sharpening Using OpenCV

## Aim

To write a Python program using OpenCV to apply different smoothing filters (Averaging, Weighted Averaging, Gaussian, Median) and sharpening filters (Laplacian Kernel and Laplacian Operator) for image enhancement, and display each result separately along with the original image for comparison.

---

## The program performs the following operations:

- Read and display an input image  
- Apply Averaging filter  
- Apply Weighted Averaging filter  
- Apply Gaussian filter  
- Apply Median filter  
- Apply Laplacian sharpening using kernel  
- Apply Laplacian operator  
- Display all outputs for comparison  

---

## Software Used

- Anaconda – Python 3.7 / 3.x  
- Jupyter Notebook / VS Code  
- OpenCV (`cv2`)  
- NumPy  
- Matplotlib  

---

## Algorithm

### Step 1:
Import the required libraries: OpenCV, NumPy, and Matplotlib.

### Step 2:
Read the input image (`city.jpg`).

### Step 3:
Convert the image from BGR to RGB format for display.

### Step 4:
Apply Averaging Filter using `cv2.filter2D()` with a normalized box filter kernel.

### Step 5:
Apply Weighted Averaging Filter using a custom kernel with `cv2.filter2D()`.

### Step 6:
Apply Gaussian Filter using `cv2.GaussianBlur()`.

### Step 7:
Apply Median Filter using `cv2.medianBlur()`.

### Step 8:
Apply Laplacian Sharpening using Kernel with `cv2.filter2D()`.

### Step 9:
Apply Laplacian Operator using `cv2.Laplacian()`.

### Step 10:
Display all filtered images along with the original image for comparison.

---

## Developed By

- **Name:** Subashini K  
- **Register Number:** 212225240160  

---

## Program

```python
import cv2
import matplotlib.pyplot as plt
import numpy as np
```

```python
image1 = cv2.imread("city.jpg")
image2 = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
kernel = np.ones((11, 11), np.float32) / 169
image3 = cv2.filter2D(image2, -1, kernel)
```

```python
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
```

```python
kernel1 = np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]]) / 16
image2 = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
image3 = cv2.filter2D(image2, -1, kernel1)
```

```python
plt.subplot(1, 2, 1)
plt.imshow(image2)
plt.title("Original Image")
plt.axis("off")
plt.subplot(1, 2, 2)
plt.imshow(image3)
plt.title("Weighted Average Filter Image")
plt.axis("off")
plt.show()
```

```python
gaussian_blur = cv2.GaussianBlur(image2, (33, 33), 0, 0)
```

```python
plt.subplot(1, 2, 1)
plt.imshow(image2)
plt.title("Original Image")
plt.axis("off")
plt.subplot(1, 2, 2)
plt.imshow(gaussian_blur)
plt.title("Gaussian Blur")
plt.axis("off")
plt.show()
```

```python
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
```

```python
kernel2 = np.array([[-1, -1, -1], [2, -2, 1], [2, 1, -1]])
image3 = cv2.filter2D(image2, -1, kernel2)
plt.subplot(1, 2, 1)
plt.imshow(image2)
plt.title("Original Image")
plt.axis("off")
plt.subplot(1, 2, 2)
plt.imshow(image3)
plt.title("Laplacian Kernel")
plt.axis("off")
plt.show()
```

```python
laplacian = cv2.Laplacian(image2, cv2.CV_64F)
plt.subplot(1, 2, 1)
plt.imshow(image2)
plt.title("Original Image")
plt.axis("off")
plt.subplot(1, 2, 2)
plt.imshow(laplacian)
plt.title("Laplacian Operator")
plt.axis("off")
plt.show()
```

---

## Output

### Smoothing Filters

- **Averaging filter produces blurred image:**

  ![Averaging filter](output1_average.png)

- **Weighted averaging provides smoother result with less distortion:**

  ![Weighted averaging filter](output2_weighted_average.png)

- **Gaussian filter preserves edges better while reducing noise:**

  ![Gaussian blur](output3_gaussian.png)

- **Median filter removes salt-and-pepper noise effectively:**

  ![Median blur](output4_median.png)

---

### Sharpening Filters

- **Laplacian kernel enhances edges and fine details:**

  ![Laplacian kernel](output5_laplacian_kernel.png)

- **Laplacian operator detects edges clearly:**

  ![Laplacian operator](output6_laplacian_operator.png)

---

## Result

Thus, smoothing filters and sharpening filters are successfully implemented using OpenCV.

The smoothing filters reduce noise and improve image quality, while sharpening filters enhance edges and details for better feature extraction.