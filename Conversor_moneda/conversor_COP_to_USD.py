cop = input("¿Cuántos pesos Colombianos tienes?: ")
cop = float(cop)
usd_value = 3875

usd = cop / usd_value
usd = round(usd, 2)
usd = str(usd)

print("Tienes $" + usd + " USD")