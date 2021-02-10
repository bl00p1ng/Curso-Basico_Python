def conversor(currency, usd_value):
    cop = input("¿Cuántos pesos " + currency + " tienes?: ")
    cop = float(cop)

    usd = cop / usd_value
    usd = round(usd, 2)
    usd = str(usd)

    print("Tienes $" + usd + " USD")


menu = """
💱 Bienvenido al Conversor de Monedas
:: Elige una opción
1 → Pesos Colombianos
2 → Pesos Argentinos
3 → Pesos Mexicanos

Tu elección → """

option = input(menu)

if option == '1':
    conversor("Colombianos", 3875)

elif option == '2':
    conversor("Argentinos", 65)

elif option == '3':
    conversor("Mexicanos", 24)

else:
    print("⚠ Ingresaste una opción incorrecta")
