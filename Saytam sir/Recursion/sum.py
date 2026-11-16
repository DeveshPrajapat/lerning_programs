def sum(n):

    """Sum of Natural Number """
    if n == 0:
        return 0
    return n+sum(n-1)
  
  
print(f"Sum of Natural number is {sum(10)}")
print(f"Sum of Natural number is {sum(4)}")


