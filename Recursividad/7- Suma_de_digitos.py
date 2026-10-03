#Implementar una función recursiva que calcule la suma de los dígitos de un número entero positivo.

#No convertir el número a str.

def suma_digitos(n): 
    if n < 10:
        return n
    
    valor_recursivo = n // 10
    valor_digito = n % 10
    
    return valor_digito + suma_digitos(valor_recursivo)


if __name__ == "__main__":
    
    print(suma_digitos(123456789))