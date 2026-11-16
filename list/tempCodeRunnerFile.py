li = ["abc","xyz","aba","1221"]
c=0
for i in li:
    if len(i)>1 and i[0] == i[-1]:
        print(i)
        c+=1
print(c)