import numpy as np
cimport numpy as np

# Specify the type of input arrays
cpdef convolve_2d(np.ndarray[np.float32_t, ndim=2] image, 
                np.ndarray[np.float32_t, ndim=2] kernel):
    cdef int img_h = image.shape[0]
    cdef int img_w = image.shape[1]
    cdef int kernel_h = kernel.shape[0]
    cdef int kernel_w = kernel.shape[1]
    
    cdef int output_h = img_h - kernel_h + 1
    cdef int output_w = img_w - kernel_w + 1

    cdef np.ndarray[np.float32_t, ndim=2] output = np.zeros((output_h, output_w), dtype=np.float32)
    cdef int i, j, ki, kj
    cdef float pixel_sum

    # Perform the convolution using nested loops
    for i in range(output_h):
        for j in range(output_w):
            pixel_sum = 0.0
            for ki in range(kernel_h):
                for kj in range(kernel_w):
                    pixel_sum += image[i + ki, j + kj] * kernel[ki, kj]
            output[i, j] = pixel_sum
    
    return output
