year = int(input("Enter a year: "))

if year % 4 == 0:   # if year is divisible by 4
    if year % 100 == 0:   # if year is divisible by 100
        if year % 400 == 0:  # if year is divisible by 400
            print(year, "is a leap year")
        else:
            print(year, "is not a leap year")
    else:
        print(year, "is a leap year")
else:
    print(year, "is not a leap year")
