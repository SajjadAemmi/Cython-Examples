import time


def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def calculate_factorial_in_python():
    test_values = [20, 200, 2000, 20000, 200000]
    print("Python Results:")
    for n in test_values[:5]:
        start_time = time.process_time()
        _ = factorial(n)
        end_time = time.process_time()
        duration = end_time - start_time
        print(f"Factorial({n}): {duration:.6f} seconds")


if __name__ == "__main__":
    calculate_factorial_in_python()
