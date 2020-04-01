def listSum(array):
    return 0 if len(array)==0 else array[0]+listSum(array[1:])

print(listSum([]))  # 0
print(listSum([42]))  # 42
print(listSum([3, 1, 5, 2]))  # 11