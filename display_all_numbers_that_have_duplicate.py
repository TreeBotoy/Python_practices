nums = []
for i in range(10):
    n = int(input(f"Enter number {i+1}: "))
    nums.append(n)

duplicates_found = []

print("Numbers that have duplicates:")
for x in nums:
    if nums.count(x) > 1 and x not in duplicates_found:
        print(x)
        duplicates_found.append(x)