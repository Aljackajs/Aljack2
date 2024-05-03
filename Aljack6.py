.import random


names = ["PRIYA", "VIJAY", "RAKHESH", "DAVID", "KAVYA"]
roll_numbers = [random.randint(1000, 9999) for _ in range(len(names))]
marks = [random.randint(0, 100) for _ in range(len(names))]


data = list(zip(names, roll_numbers, marks))


names_list = [item[0] for item in data]
roll_numbers_list = [item[1] for item in data]
marks_list = [item[2] for item in data]


all_names = tuple(names_list)
all_roll_numbers = tuple(roll_numbers_list)
all_marks = tuple(marks_list)


print("List of tuples containing name, roll number, and marks:")
print(data)

print("\nTuple containing all names:", all_names)
print("Tuple containing all roll numbers:", all_roll_numbers)
print("Tuple containing all marks:", all_marks)
