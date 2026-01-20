numero = int(input("Insira um valor: "))

if numero < 0 :
    print("Você digitou um número negativo.")

elif numero > 0 : 
    if numero % 2 == 0:

        print("Você digitou um número positivo e par.")
    else :
        print("Você digitou um número positivo e ímpar.")

else :
    print("Você digitou zero.")

