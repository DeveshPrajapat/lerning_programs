def staircase(n):
    if n <= 1:
        return 1
    else:
        return staircase(n-1)+staircase(n-2)

print(staircase(5))
    