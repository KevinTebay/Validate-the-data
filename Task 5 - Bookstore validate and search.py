# 2D array (list of lists) containing book titles and their prices as integers
Books = [
    ["The Great Gatsby", 35],
    ["To Kill a Mockingbird", 25],
    ["1984", 18],
    ["Pride and Prejudice", 40],
    ["The Catcher in the Rye", 20]
]

# Get and validate the maximum price
max_price = input("Enter the maximum price you are willing to pay: ")

while not max_price.isdigit() or int(max_price) <= 0:
    print("Invalid price. Please enter a positive whole number.")
    max_price = input("Enter the maximum price you are willing to pay: ")

max_price = int(max_price)

# Get the book title to search for
book_title = input("Enter the title of the book you are looking for: ")

# Perform a linear search in the Books 2D array
found = False
for book in Books:
    if book[0].lower() == book_title.lower():  # Case-insensitive match
        found = True
        if book[1] <= max_price:
            print("Book found: " + book[0] + " - Price: $" + str(book[1]))
        else:
            print("Book found, but the price ($" + str(book[1]) + ") exceeds your budget.")
        break

if not found:
    print("Book not found in inventory.")

