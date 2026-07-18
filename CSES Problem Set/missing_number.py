def solve(n, nums):
    hm = set([int(s) for s in nums.split(" ")])
    for i in range(1, n+1):
        if i not in hm:
            print(i)
            break

if __name__ == "__main__":
    lines = []
    for i in range(2):
        n = input()
        lines.append(n)
        
    solve(int(lines[0]), lines[1])