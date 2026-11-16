def sum_list(li):
    """Sum of Even Number in list """
    
    if li == []:
        return 0
    if li[0]%2 == 0:
        return li[0] + sum_list(li[1:])
    else:
        return sum_list(li[1:])
        

li = [2,3,45,6,7]

print(sum_list(li))