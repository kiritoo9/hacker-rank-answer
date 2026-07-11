def guess(n):
    pick = 1702766719
    # pick = 8
    
    if n == pick:
        return 0
    elif n > pick:
        return -1
    else:
        return 1

def solve():
    n = 2126753390
    # n = 10
    
    # binary search
    # split to two side
    left = 0
    right = n
    while left <= right:
        mid = left + (right-left) // 2
        p = guess(mid)
        if p == 0:
            return mid
        elif p == -1:
            right = mid-1
        elif p == 1:
            left = mid+1
            
print(solve())