import time
import cv2
import numpy as np
from convolution import convolve_2d


# Create a sample image and kernel
image = cv2.imread("../assets/lion-king.jpg", cv2.IMREAD_GRAYSCALE).astype(np.float32)
kernel = np.array([[1, 0, -1],
                   [1, 0, -1],
                   [1, 0, -1]], dtype=np.float32)

# Perform the convolution
start_time = time.time()
convolved_image = convolve_2d(image, kernel)
end_time = time.time()

print(f"Convolution completed in {end_time - start_time:.6f} seconds")
cv2.imwrite("output_python.jpg", convolved_image)
