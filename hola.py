def Factorial(num):
    resultado = 1  
    for i in range(1, num + 1):
        resultado *= i
    return resultado  

num = int(input("Introduzca el número del que desea conocer el factorial: "))
print("El factorial de", num, "es", Factorial(num))
