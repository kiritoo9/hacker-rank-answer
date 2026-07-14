def solve():
    num1 = "1"
    num2 = "9" # 533
    
    numbers = [str(n) for n in range(0, 10)]
    max_length = max(len(num1), len(num2))
    multiple = {n:0 for n in range(1, max_length+1)}
    
    arr_str = []
    narr1 = list(num1)
    narr2 = list(num2)
    
    i = len(narr1)-1
    j = len(narr2)-1
    p = max_length
    
    while p > 0:
        if i < 0 or j < 0:
            arr_str.append(None)
            p -= 1
            continue
        
        v1 = narr1[i:i+1]
        v2 = narr2[j:j+1]
        
        n1 = numbers.index(v1[-1])
        n2 = numbers.index(v2[-1])
        n3 = n1+n2+1
        tens = n3//10
        print(n3, tens, i, j, p)
        
        if tens > 0:
            multiple[p-1] = tens
            n3 -= tens*10
            
        arr_str.append(int(numbers[n3-1]))
        
        i -= 1
        j -= 1
        p -= 1
    
    arr_str = list(reversed(arr_str))
    
    o_str = ""
    for i in range(1, max_length+1):
        if arr_str[i-1] is not None:
            o_str += numbers[arr_str[i-1]+multiple[i]]
        else:
            k = narr1 if len(narr1) > len(narr2) else narr2
            o_str += str(int(k[i-1])+multiple[i])
            
    return o_str

print(solve())