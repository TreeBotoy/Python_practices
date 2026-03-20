numbers = []
while True:
    val = input("Enter a number (or a letter to stop): ")
    try:
        num = int(val)
        numbers.append(num)
    except:
        break
if len(numbers) > 0:
    most_frequent = numbers[0]
    max_count = 0
    for x in numbers:
        current_count = numbers.count(x)
        if current_count > max_count:
            max_count = current_count
            most_frequent = x
    print("The number with the most duplicates is:", most_frequent)
    print("It appeared", max_count, "times.")
else:
    print("No numbers were entered.")