def solve(nums):
    for n in nums:
        y = n[0]
        x = n[1]
        
        box = 1
        counter = [0, 1]
        
        values = []
        for l in range(1, max(y, x)+1):
            if l%2 != 0:
                values.append([i for i in range(counter[0], counter[-1]+1) if i > 0])
            else:
                values.append([i for i in range(counter[-1], counter[0]-1, -1)])
                
            box += 2 # increase two for each layers
            counter = [counter[-1]+1, counter[-1]+box]
        
        print(values[y][x])
        

n = int(input())
lines = []
for i in range(n):
    s = input()
    lines.append([int(i) for i in s.split(" ")])
    
solve(lines)
    
    
'''
1
2 3
'''
