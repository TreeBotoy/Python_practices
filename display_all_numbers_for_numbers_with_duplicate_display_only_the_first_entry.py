nums = []
for i in range(10):
    n = int(input("Enter a number: "))
    nums.append(n)
seen = []
for x in nums:
    if x not in seen:
        print(x)
        seen.append(x)