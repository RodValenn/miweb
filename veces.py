
def promedio():
    nota=1
    laboratorio=6
    examen=10
    prom=(nota+laboratorio+examen)/3
    return prom
notaF=promedio()
print(notaF)

def fibonacci_sequence(n):
    if n <= 0:
        return "N debe ser un número positivo"
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        while len(fib_sequence) < n:
            next_fib = fib_sequence[-1] + fib_sequence[-2]
            fib_sequence.append(next_fib)
        return fib_sequence


secuencia = fibonacci_sequence(20)
print(f"Los primeros  números de Fibonacci son: {secuencia}")





def dob_Valor(n):
    return n**2
n=10    
dob_Valor(n)
