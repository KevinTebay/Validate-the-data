age = input("Enter your age: ")

while not age.isdigit() or int(age) < 1 or int(age) > 120:
    print("Invalid age. Please enter a number between 1 and 120.")
    age = input("Enter your age: ")

print("Age accepted:", age)
