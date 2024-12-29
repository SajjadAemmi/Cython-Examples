import tensorflow as tf
import numpy as np
import time


def create_random_tensor(rows, cols):
    # Create a tensor with random values
    data = np.random.rand(rows, cols) * 10.0  # Random float between 0 and 10
    tensor = tf.constant(data, dtype=tf.float32)
    return tensor


def print_tensor(tensor):
    print(tensor.numpy())


def main():
    # Start clock
    start_time = time.time()

    # Create two random tensors
    rows = 20000
    cols = 20000
    tensor1 = create_random_tensor(rows, cols)

    # Calculate and print process time in seconds
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Process time: {elapsed_time} seconds")


if __name__ == "__main__":
    main()
