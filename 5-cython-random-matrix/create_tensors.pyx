import numpy as np
cimport numpy as np
import tensorflow as tf


cpdef create_random_tensor(int rows, int cols):
    cdef np.ndarray data = np.random.rand(rows, cols) * 10.0
    return tf.constant(data, dtype=tf.float32)
