li = [
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20]
    
]

for i in range(4):
    row_sum = 0
    for j in range(5):
        row_sum = row_sum+li[i][j]
    print(f"Sum of {i+1} rows {row_sum}")

print("-------------------------------------")

for j in range(5):
    col_sum = 0
    for i in range(4):
        col_sum = col_sum+li[i][j]
    print(f"Sum of {j+1} cols {col_sum}")