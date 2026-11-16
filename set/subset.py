s1 = {1,2,34,5,67,88,9}
s2 = {1}

for i in s1:
    for j in s2:
        if i == j:
            print("S2 is subset of S1 ")
            break

