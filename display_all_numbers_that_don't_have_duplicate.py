nums = []
for i in range(10):
    n = int(input("Enter a number: "))
    nums.append(n)
print("Numbers without duplicates:")
for x in nums:
    if nums.count(x) == 1:
        print(x)