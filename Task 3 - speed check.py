speed = input("Enter the speed of the vehicle in km/h: ")

while not speed.isdigit() or int(speed) <= 0 or int(speed) > 200:
    print("Invalid speed. Please enter a value greater than 0 and less than or equal to 200.")
    speed = input("Enter the speed of the vehicle in km/h: ")

print("Speed accepted:", speed)
