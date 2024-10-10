# fmt: off
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9] 
]

# fmt: on

print(matrix[0][0])

for row in matrix:
    for item in row:
        print(item)

matrix_2 = []
# 5 x 5 matrix, items: 0..4
for i in range(5):
    row = []
    for j in range(5):
        row.append(j)
    matrix_2.append(row)

print(matrix_2)
# print([list(range(5))] * 5)
