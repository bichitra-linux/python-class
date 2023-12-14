## for a positive number n, claculate 1+2+...+n

n = int(input("Enter a positive integer: "))
total = 0
for i in range(1, n+1):
    total = total + i
print("The sum of the first", n, "positive integers is", total)

