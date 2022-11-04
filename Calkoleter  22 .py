import math

def add(num1, num2 ):
    return num1 + num2

def subtact(num1, num2 ):
    return num1 - num2
    
def div(num1, num2 ):
    return num1/num2

def multi(num1, num2 ):
    return num1 * num2

def main():
    Operation = Input(" What do you want to do?  (+, -, /, *):  " )
    if (Operation != "+" and Operation != "-"  and Operation != "*"  and Operation != "/"):
        print(" Your input is invalid. Please enter a valid input")
    else:
        num1 =float(input("Enter value for nummber 1:  " ))

        num2 =float(input("Enter value for nummber 2:   "))
        if (Operation == "+"):
            print(add(num1, num2))
        
        elif (Operation == "-"):
            print(subtact(num1, num2))
        elif (Operation == "/"):
            print(dir(num1, num2))
        elif (Operation == "*"):
            print(multi(num1, num2))

    main()








