cpdef factorial(int n):
    cdef long result = 1
    cdef int i
    for i in range(1, n + 1):
        result *= i
    return result
