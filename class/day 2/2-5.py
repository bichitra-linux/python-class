## for a positive number n, find all it's positive factors

n = int(input("Enter a positive integer: "))
print("The factors of", n, "are:")
for i in range(1, n+1):
    if n % i == 0:
        print(i)
