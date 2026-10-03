#Implementar una función recursiva que determine cuántos dígitos tiene un número entero positivo.

#No convertir el número a str.

def cantidad_digitos(n): 
    if n < 10:
        return 1
    
    valor = n // 10
    
    return 1 + cantidad_digitos(valor)

if __name__ == "__main__":
    digitos = cantidad_digitos(12345678910)
    print(digitos)