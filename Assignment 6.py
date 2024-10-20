


#Challenge:Allow the user to choose from multiple currency pairs and implement appropriate error handling for invalid currency inputs.
#Input:Ask the user to enter an amount in one currency (e.g., USD).
#Processing:Convert the amount to another currency (e.g., EUR) using a fixed exchange rate.
#Output:Display the converted amount in the target currency.



#Define fixed exchange rates for currency pairs
exchange_rates = {
    "USD to EUR": 0.85,
    "EUR to USD": 1.18,
    "USD to GBP": 0.75,
    "GBP to USD": 1.33,
    "EUR to GBP": 0.88,
    "GBP to EUR": 1.14
}

#Input: Ask the user to select a currency pair
print("Available currency pairs: ")
for pair in exchange_rates:
    print(pair)

currency_pair = input("\nEnter the currency pair (e.g., 'USD to EUR'): ")

#Error handling for invalid currency pair input
if currency_pair not in exchange_rates:
    print("Invalid currency pair, Please choose a valid pair from the list.")
else:
    #Input: Ask the user to enter an amount in the source currency
    try:
        amount = float(input(f"Enter the amount in {currency_pair.split(' ')[0]}: "))
        if amount < 0:
            print("Amount must be a non-negative number.")
        else:
            #Processing: Convert the amount to the target currency
            converted_amount = amount * exchange_rates[currency_pair]

            #Output: Display the converted amount in the target currency
            print(f"{amount:.2f} {currency_pair.split(' ')[0]} is equal to {converted_amount:.2f} {currency_pair.split(' ')[2]}.")
    except ValueError:
        print("Invalid input. Please enter a numeric value for the amount.")
