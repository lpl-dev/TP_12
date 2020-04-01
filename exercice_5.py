def product(a,b):
    return 0 if a<1 else b+product(a-1,b)

print(product(5,2)) # 10
print(product(9,3)) # 27