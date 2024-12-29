import cv2
import numpy as np
import time


if __name__ == "__main__":
    image = cv2.imread("../assets/lion-king.jpg", cv2.IMREAD_GRAYSCALE)
    kernel = np.array([[1, 0, -1], 
                       [1, 0, -1], 
                       [1, 0, -1]], dtype=np.int32)

    start_time = time.time()
    convolved_image = cv2.filter2D(image, ddepth=-1, kernel=kernel)
    end_time = time.time()

    print(f"Convolution Time (Python): {end_time - start_time:.6f} seconds")
    cv2.imwrite("output_python.jpg", convolved_image)
