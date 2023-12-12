## Exercise 1.2
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
num4 = int(input("Enter the fourth number: "))

smallest = num1
position = 1

if num2 < smallest:
    smallest = num2
    position = 2

if num3 < smallest:
    smallest = num3
    position = 3

if num4 < smallest:
    smallest = num4
    position = 4

print("Smallest number:", smallest)
print("Position of first occurrence:", position)


