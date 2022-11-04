

from optparse import Values
from typing import Counter


shoppingvegn = {}

def card():
    active = True
    counter = 0
    while active:
        
        item = input("ange vara: ")
        cost = int(input(f"vad kostar varan  {item}? skriva priset: in Sek:  "))
        shoppingvegn[item] = cost
        counter =  counter + 1

        repeat = input(" Vill du lägga till fler varor?  (Jag/Nej)?")
        if repeat == "nej":
            active = False

    print("\n")
    print(f" Din kundvagn innehåller {counter} varor:")
    print(f"___________________________________________________")
    for item, cost in shoppingvegn.items():
        print(f"items: {item} , {cost} Kronor")

    cost = shoppingvegn.values()
    total = sum(cost)

    print(f"-------------------summan{total}kronor -----------------------")



card()
