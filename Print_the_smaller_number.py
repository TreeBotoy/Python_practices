num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if num1 < num2:
    print(f"{num1} is smaller than {num2}.")
elif num1 > num2:
    print(f"{num2} is smaller than {num1}.")
else:
    print(f"Both numbers are equal: {num1} and {num2}.")