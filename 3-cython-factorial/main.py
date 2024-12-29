import time
from factorial import factorial

# Test the factorial function
for n in [20, 200, 2000, 20000, 200000]:
    start_time = time.time()
    result = factorial(n)
    end_time = time.time()
    print(f"Factorial of {n} computed in {end_time - start_time:.6f} seconds")
