import random
# slump tal 1-10
nummer = random.randint(1, 10)
playername = input(f"vad heter du:  ")
print(f"Hej, {playername} gissa tal mellan 1 - 10")

def guessnr():
    for i in range(0,5):
        counter = 0
        guess = int(input(f"gissa en siffra: "))
        counter = counter + 1
        if   guess < nummer:
            print(f"din gissningsnummer: {counter} på siffran {guess} är för lågt")
        if   guess > nummer :
            print(f"din gissningsnummer: {counter} på siffran {guess} är för högt")
        if  guess == nummer :
            break
    if guess == nummer:
        print(f"din gissningsnummer: nummer {counter} på siffran {guess} är rätt efrter {counter}")
    else:
        print(f"Gissningar var fel.Det rätta numret var:{str(nummer)}")

guessnr()

        
