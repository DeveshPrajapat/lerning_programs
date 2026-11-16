# 1.Find the first non-repeating character in a string.
st ="aaddfffc"
list = []
for i in st:
    for j in st:
        if i  == j :
            
            print(i)