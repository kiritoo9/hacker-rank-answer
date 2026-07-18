def solve(n):
    nums = [n]
    while n > 1:
        if n%2 == 0:
            n = n//2
        else:
            n = (n*3)+1
        nums.append(n)
            
    return " ".join(str(s) for s in nums)

if __name__ == "__main__":
    n = input()
    print(solve(int(n)))