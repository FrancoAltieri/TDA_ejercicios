#Implementar una función recursiva que calcule base^exponente.

#Suponer que el exponente es un entero mayor o igual a 0.

#No utilizar **.
def potencia(base, exponente): 
    if exponente == 0:
        return 1
    
    return base * potencia(base,exponente - 1)



if __name__ == "__main__":
    numero = potencia(3,4)
    print(numero)