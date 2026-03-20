lowest = None
while True:
    try:
        num = float(input("Enter a number (then enter a letter to stop): "))
        if lowest is None or num < lowest:
            lowest = num
    except ValueError:
        print("Invalid input. Please enter a valid number or a letter t3o stop.")
        break
print("The lowest number entered is:", lowest)
