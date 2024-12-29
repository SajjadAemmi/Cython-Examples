import time
from create_tensors import create_random_tensor


def print_tensor(tensor):
    print(tensor.numpy())


def main():
    start_time = time.time()

    # Create two random tensors
    rows = 10000
    cols = 10000
    tensor1 = create_random_tensor(rows, cols)

    # Optionally print tensors (this can be commented out if not needed)
    # print_tensor(tensor1)
    # print_tensor(tensor2)

    # Calculate and print process time
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Process time: {elapsed_time} seconds")


if __name__ == "__main__":
    main()
