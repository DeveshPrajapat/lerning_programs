text = input("Enter your String ")

start = 0
end = len(text) -1 
c = 1

while start < end:
    if text[start] != text[end]:
        
        c = 0
        break
    start +=1
    end -=1
    
if c:
    print("Palindorme")
else:
    print("Not Palindorme")

