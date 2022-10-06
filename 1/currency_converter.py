eur_rate = input("Enter a EUR/GBP rate (in EUR) ? ")
print("Rate saved!\n")
amount = input("How much do you want to convert (in EUR)? ")
converted_eur = int(amount) / int(eur_rate)
print(f"{amount} EUR is {converted_eur:.2f} GBP")

