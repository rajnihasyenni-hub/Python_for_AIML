n = int(input("Enter a positive integer: "))

total_sum = 0
for i in range(1, n + 1):
    total_sum += i

print("Sum from 1 to", n, "is:", total_sum)
