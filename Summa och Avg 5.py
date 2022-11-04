
avg = int(input("Ange, hur många tal som du ska beräkna summan och medel för:  "))
def calcAvg():
    sum = 0
    counter = avg 
    while counter > 0:
        num = int(input("mata in ett tal:  "))
        sum = sum + num
        
        counter = counter -1
    print(f"summan är:  {sum}, medel är: {sum/avg}")

calcAvg()
       