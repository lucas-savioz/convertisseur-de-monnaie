from forex_python.converter import CurrencyRates

currency = CurrencyRates()
devises_valides = ["USD", "EUR", "GBP", "JPY", "AUD", "CAD", "CZK" "CHF", "CNY", "SEK", "NZD", "NOK", "SGD", "MXN", "INR", "BRL", "ZAR", "RUB", "HKD", "TRY", "KRW", "AED"]
file_name = "./backup.txt"

# Saisir la devise de départ
while True:
    devise_depart = input("Saisir votre devise de départ : ").upper()
    if devise_depart in devises_valides:
        break
    else:
        print("Devise invalide, réessayer")

# Saisir la devise d'arrivée
while True:
    devise_arrivee = input("Saisir votre devise d'arrivée : ").upper()
    if devise_arrivee in devises_valides:
        break
    else:
        print("Devise invalide, réessayer")

# Saisir le montant
while True:
    try:
        amount = float(input("Saisir un montant : "))
        break
    except ValueError:
        print("Erreur, veuillez entrer un montant valide")

# Effectue la conversion des devises
converted_amount = currency.convert(devise_depart, devise_arrivee, amount)

# Affiche le résultat
print(f"{amount} {devise_depart} équivaut à {converted_amount} {devise_arrivee}")

# Sauvegarde le le résultat dans le fichier bachup.txt
with open(file_name, "w") as file:
    file.write(f"{amount} {devise_depart} équivaut à {converted_amount} {devise_arrivee}")