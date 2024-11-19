score = input("Enter the exam score: ")

while not score.isdigit() or int(score) < 0 or int(score) > 100:
    print("Invalid score. Please enter a value between 0 and 100.")
    score = input("Enter the exam score: ")

print("Score accepted:", score)
