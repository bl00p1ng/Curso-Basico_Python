menu = """
💱 Bienvenido al Conversor de Monedas
:: Elige una opción
1 → Pesos Colombianos
2 → Pesos Argentinos
3 → Pesos Mexicanos

Tu elección → """

option = input(menu)

if option == '1':
    cop = input("¿Cuántos pesos Colombianos tienes?: ")
    cop = float(cop)
    usd_value = 3875

    usd = cop / usd_value
    usd = round(usd, 2)
    usd = str(usd)

    print("Tienes $" + usd + " USD")

elif option == '2':
    ars = input("¿Cuántos pesos Argentinos tienes?: ")
    ars = float(ars)
    usd_value = 65

    usd = ars / usd_value
    usd = round(usd, 2)
    usd = str(usd)

    print("Tienes $" + usd + " USD")

elif option == '3':
    mxn = float(input("¿Cuántos pesos Mexicanos tienes?: "))
    usd_value = 24
    usd = mxn / usd_value
    usd = round(usd, 2)
    usd = str(usd)

    print("Tienes $" + usd + " USD")

else:
    print("⚠ Ingresaste una opción incorrecta")
