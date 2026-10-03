#Implementar una función recursiva que multiplique dos números enteros positivos utilizando únicamente sumas.

#No utilizar *.

def multiplicar(a, b): 
    if b < 1:
        return 0
    
    return a + multiplicar(a,b-1)


if __name__ == "__main__":
    print(multiplicar(2,32))