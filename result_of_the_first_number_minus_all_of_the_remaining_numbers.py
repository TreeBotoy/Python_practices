result = int(input("Enter the first number: "))
for i in range(2, 11):
    num = int(input(f"Enter number {i}: "))
    result -= num
print("The result of the first number minus all of the remaining numbers is:", result)