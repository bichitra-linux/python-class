# Take input from the user
seconds = int(input("Enter the number of seconds: "))

# Calculate hours, minutes, and remaining seconds
hours = seconds // 3600
seconds %= 3600

minutes = seconds // 60
seconds %= 60

# Calculate days, months, and years
days = hours // 24
hours %= 24

months = days // 30
days %= 30

years = months // 12
months %= 12

# Print the result
print(f"It is equal to {years} years, {months} months, {days} days, {hours} hours, {minutes} minutes, and {seconds} seconds.")
