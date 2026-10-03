#Implementar una función recursiva que devuelva la suma de todos los números enteros desde 1 hasta n.
def suma_hasta(n): 
    if n < 1:
        return 0
    return n + suma_hasta(n-1)


if __name__ == "__main__":
    numero = suma_hasta(5)
    print(numero)