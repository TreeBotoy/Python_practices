num_1 = float(input("Enter the first number: "))
num_2 = float(input("Enter the second number: "))
num_3 = float(input("Enter the third number: "))
num_4 = float(input("Enter the fourth number: "))
num_5 = float(input("Enter the fifth number: "))
num_6 = float(input("Enter the sixth number: "))
num_7 = float(input("Enter the seventh number: "))
num_8 = float(input("Enter the eighth number: "))
num_9 = float(input("Enter the ninth number: "))
num_10 = float(input("Enter the tenth number: "))
odd_count = 0
for num in [num_1, num_2, num_3, num_4, num_5, num_6, num_7, num_8, num_9, num_10]:
    if int(num) % 2 != 0:
        odd_count += 1
print("The number of odd numbers is:", odd_count)