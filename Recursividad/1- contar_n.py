#Implementar una función recursiva que muestre por pantalla todos los números desde 1 hasta n.
def contar_rec(n,i):
    if i > n:
        return
    print(i)
    contar_rec(n,i+1)
    
def contar(n):
    contador = 1
    contar_rec(n,contador)
    
    
    

if __name__ == "__main__":
    numero = 5
    contar(numero)