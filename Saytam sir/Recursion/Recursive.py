def string(str):
    if str ==  "":
        return str
    
    return string(str[1:]) + str[0]

s=string("Devesh")
print(s)