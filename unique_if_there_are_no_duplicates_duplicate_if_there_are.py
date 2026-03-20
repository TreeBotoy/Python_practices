num_set = []
final_number = []
for i in range(0,10):
    numbers = int(input("numbers:"))
    final_number.append(numbers)
if final_number.count(i) == 1:
    print("unique")
elif final_number.count(i) < 1:
    print("duplicate")