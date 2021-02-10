usd = input("¿Cuántos dólares tienes?: ")
usd = float(usd)

cop_value = 3585

cop = usd * cop_value
cop = round(cop, 2)
cop = str(cop)

print("Tienes $" + cop + " COP")
