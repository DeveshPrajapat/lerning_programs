def gp(a,r,n):
    """GP"""
    if n == 1:
        return a
    return gp(a,r,n-1)*r


a = int(input("Enter the First Term "))
r = int(input("Enter the Common Ratio "))
n = int(input("Enter the Term Number "))

print(gp(a,r,n))
