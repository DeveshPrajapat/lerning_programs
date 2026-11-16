# n = 10
# binar = ""
# while n>0:
#     remainder = n%2
#     binar = str(remainder)+binar
#     n//=2

# print(binar)

def binary(n):
    """Decimal to Binary"""
    if n == 0:
        return ""
    return binary(n//2)+str(n%2)

n = 10
bin = binary(n)
print(bin if bin != "" else "0")