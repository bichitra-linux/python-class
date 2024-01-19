import requests
from tkinter import Tk, Label, Entry, Button, messagebox
import matplotlib.pyplot as plt

# Function to fetch the latest exchange rate
def get_exchange_rate(base_currency, target_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = requests.get(url)
    data = response.json()
    exchange_rate = data['rates'][target_currency]
    return exchange_rate

# Function to convert the amount
def convert_currency():
    base_currency = base_entry.get()
    target_currency = target_entry.get()
    amount = float(amount_entry.get())

    if base_currency == "" or target_currency == "" or amount == "":
        messagebox.showerror("Error", "Please fill in all the fields.")
        return

    try:
        exchange_rate = get_exchange_rate(base_currency, target_currency)
        converted_amount = amount * exchange_rate
        result_label.config(text=f"{amount} {base_currency} = {converted_amount} {target_currency}")

        # Plotting the price changes
        prices = [1, exchange_rate]  # Assuming initial price is 1
        currencies = [base_currency, target_currency]
        plt.plot(currencies, prices)
        plt.xlabel('Currency')
        plt.ylabel('Price')
        plt.title('Price Changes')
        plt.show()

    except KeyError:
        messagebox.showerror("Error", "Invalid currency code.")

# Create the GUI
root = Tk()
root.title("Currency Converter")
root.configure(bg="white")

base_label = Label(root, text="Base Currency:", bg="white")
base_label.pack()

base_entry = Entry(root)
base_entry.pack()

target_label = Label(root, text="Target Currency:", bg="white")
target_label.pack()

target_entry = Entry(root)
target_entry.pack()

amount_label = Label(root, text="Amount:", bg="white")
amount_label.pack()

amount_entry = Entry(root)
amount_entry.pack()

convert_button = Button(root, text="Convert", command=convert_currency)
convert_button.pack()

result_label = Label(root, text="", bg="white")
result_label.pack()

root.mainloop()
