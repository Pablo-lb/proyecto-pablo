def suma(a, b, c=0, d=0):
    if c != 0 and d != 0:
        return a + b + c + d
    elif c != 0:
        a + b + c
    else:
        return a + b
    
print(suma(2,5,2,1))
