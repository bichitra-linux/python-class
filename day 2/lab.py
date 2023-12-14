numbers = []
for _ in range(5):
    number = int(input("Enter a number: "))
    numbers.append(number)

smallest = numbers[0]
count = 1

for i in range(1, len(numbers)):
    if numbers[i] < smallest:
        smallest = numbers[i]
        count = 1
    elif numbers[i] == smallest:
        count += 1

print("The smallest number is:", smallest)
print("It occurs", count, "time(s).")
