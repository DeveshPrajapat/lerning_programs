n = int(input("Enter number of rows: "))

prev_row = []

for i in range(n):
    row = []
    for j in range(i + 1):
        if j == 0 or j == i:
            row.append(1)
        else:
            row.append(prev_row[j - 1] + prev_row[j])
    print(" " * (n - i - 1), end="")  # spacing
    for num in row:
        print("*", end=" ")
    print()
    prev_row = row # save row for next iteration
    
for i in range(n,0,-1):
    row = []
    for j in range(i + 1):
        if j == 0 or j == i:
            row.append(1)
        else:
            row.append(prev_row[j - 1] + prev_row[j])
    print(" " * (n - i - 1), end="")  # spacing
    for num in row:
        print("*", end=" ")
    print()
    prev_row = row 