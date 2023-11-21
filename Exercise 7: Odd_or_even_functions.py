user_input = input("Enter a number: ")

try:
    number = int(user_input)
    # Check if the number is odd or even
    if number % 2 == 0:
        print(f"{number} is an even number.")
    else:
        print(f"{number} is an odd number.")
except ValueError:
    print("Please enter a valid integer.")
