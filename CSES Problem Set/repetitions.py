def solve(s):
    s = list(s)
    i, j, l = 0, 1, 1
    store = []
    
    while i < len(s) and j < len(s):
        if s[i] == s[j]:
            l += 1
            if j+1 >= len(s):
                store.append(l)
            j += 1
        else:
            store.append(l)
            l = 1
            i = j
            j += 1
            
    print(max(store) if len(store) > 0 else 1)

solve(input())