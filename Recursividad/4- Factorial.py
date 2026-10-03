#Implementar una función recursiva que calcule el factorial de n.
def factorial(n): 
    
    if n == 0:
        return 1
    valor = n * factorial(n-1)
    return valor



if __name__ == "__main__":
    numero = factorial(5)
    print(numero)
    