def gcd(n1,n2):
    """Greatest common divisor of two numbers using recursion"""
    if n2 == 0:
        return n1
  
    return gcd(n2,n1%n2)

n1 = int(input("Enter the n1 "))
n2 = int(input("Enter the n2 "))

print(gcd(n1,n2))