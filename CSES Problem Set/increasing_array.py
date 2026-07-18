def solve(nums):
    nums = [int(n) for n in nums.split(" ")]
    
    c = 0
    for i in range(1, len(nums)):
        p = nums[i-1]
        n = nums[i]
        
        if p-n > 0:
            c += p-n
            nums[i] = p
            
    print(c)

lines = []
for i in range(2):
    lines.append(input())
    
solve(lines[1])