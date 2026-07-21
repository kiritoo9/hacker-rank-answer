def solve(n):
    if n == 1:
       print(1) 
    elif n == 2 or n == 3:
        print("NO SOLUTION")
    else:
        data = [i for i in range(1, n+1) if i%2 == 0]
        data += [i for i in range(1, n+1) if i%2 != 0]
        
        print(" ".join(str(s) for s in data))
    
solve(int(input()))