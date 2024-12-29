import cv2
import numpy as np
import time


def apply_convolution(image, kernel):
    rows, cols = image.shape
    output = np.zeros((rows, cols), dtype=np.uint8)

    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            pixel_sum = 0
            for ki in range(-1, 2):
                for kj in range(-1, 2):
                    pixel_sum += kernel[ki + 1][kj + 1] * image[i + ki, j + kj]
            output[i, j] = min(max(pixel_sum, 0), 255)

    return output


if __name__ == "__main__":
    image = cv2.imread("../../assets/lion-king.jpg", cv2.IMREAD_GRAYSCALE)
    kernel = np.array([[1, 0, -1], 
                       [1, 0, -1], 
                       [1, 0, -1]], dtype=np.int32)

    start_time = time.time()
    convolved_image = apply_convolution(image, kernel)
    end_time = time.time()

    print(f"Convolution Time (Python): {end_time - start_time:.6f} seconds")
    cv2.imwrite("output_python.jpg", convolved_image)
