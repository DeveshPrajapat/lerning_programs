def product(li):
    """Product of List"""
    if li == []:
        return 1
    return li[0]*product(li[1:])
li = [1,2,3,4]
print(product(li))