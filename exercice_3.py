def pow(x,n):
    return 1 if n<=0 else x*pow(x,n-1)

print(pow(42, 0)) # 1
print(pow(1, 10)) # 1
print(pow(2, 5)) # 32
print(pow(7, 2)) # 49