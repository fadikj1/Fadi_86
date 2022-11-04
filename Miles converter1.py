""" Skapa en funktion för att Omvandla km till mil, ta in km från användaren och km ska  anges 
med decimaltal, och svaret i mil ska begränsas till 2 decimaler. 1 km är 0.621371 mil
"""
def kmToMil(km):
    milcoverter = 0.62
    mil = km * milcoverter
    print(f"Distance in miles:  {mil:.2f}")

km = float(input("what is the distace in kilometer:  "))

kmToMil()