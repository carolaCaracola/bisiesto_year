year = 2020

print("Es bisiesto" if not year % 4 and (year % 100 or  not year % 400) else "No es bisiesto")