fibonacci = [0, 1] + [fibonacci[i-1] + fibonacci[i-2] for i in range(2, 20)]
print(fibonacci)
