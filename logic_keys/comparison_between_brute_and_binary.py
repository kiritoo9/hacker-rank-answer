# Sqrt(x)

import time

def binary_solve(x):
    left = 0
    right = x
    
    while left <= right:
        mid = (left + right) // 2
        if mid * mid == x:
            return mid
        elif mid * mid > x:
            right = mid - 1
        else:
            left = mid + 1
            
    return right


def brute_solve(x):
    i = 0
    while i*i <= x:
        i += 1
    return i-1
        
start = time.perf_counter()

# case = 4
# case = 8
case = 100_000_000_000_000_000
o = binary_solve(case)


# o = brute_solve(case)
print(o)

elapsed = time.perf_counter() - start
print(f"total: {elapsed:.6f}s")