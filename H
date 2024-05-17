import random
matrix = [[random.randint(10, 40) * 4 for _ in range(5)] for _ in range(4)]
print("Generated Matrix:")
for row in matrix:
    print(row)
