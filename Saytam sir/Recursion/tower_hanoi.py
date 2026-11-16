def hanoi(n,source,helper,dest):
    if n ==  1:
        print(f"Transfer disk {n} is {source} to {dest}")
        return
    
    hanoi(n-1,source,dest,helper)
    print(f"Transfer dist {n} is {source} to {dest}")
    hanoi(n-1,helper,source,dest)
    
    
n = int(input("Enter a number "))
hanoi(n,"S","H","D")