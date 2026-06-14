def solve(n):
    # wrong solve
    count = n // 2
    rem = n%2 if count > 0 else 0
    
    print(f"n={n}", count, rem)
    total_step = 1 + count + rem
    return total_step


def brute_solve(n):
    if n <= 2:
        return n
    
    dp = {
        1:1,
        2:2
    }
    for i in range(3, n+1):
        dp[i] = dp[i-1]+dp[i-2]
    
    return dp[n]
    

# entry
cases = [1, 2, 3, 4, 7]
for case in cases:
    print(
        "total step:", brute_solve(case)
    )
    
    
# 1 + 1 + 1 + 1
# 1 + 1 + 2
# 1 + 2 + 1
# 2 + 1 + 1
# 2 + 2