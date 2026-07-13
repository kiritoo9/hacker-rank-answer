def solve():
    num = 16
   
    result = num ** 0.5 # this operation is equal to math.sqrt(x)
    return result%1 == 0 # check valid integer with digit after comma
            
print(solve())