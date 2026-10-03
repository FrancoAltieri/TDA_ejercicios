#Implementar una función recursiva que muestre por pantalla todos los números desde n hasta 1.

def contar_hacia_atras(n):
    if n < 1:
        return
    print(n)
    contar_hacia_atras(n-1)
    

if __name__ == "__main__":
    numero = 5
    contar_hacia_atras(numero)
    