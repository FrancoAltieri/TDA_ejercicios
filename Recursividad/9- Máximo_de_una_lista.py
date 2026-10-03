#Implementar una función recursiva que devuelva el mayor elemento de una lista.

#No utilizar max().

#Suponer que la lista no está vacía.

def maximo_rec(lista,i,candidato):
    
    if i == len(lista):
        return candidato
    
    if lista[i] > candidato:
        candidato = lista[i]
    
    return maximo_rec(lista,i+1,candidato) 
    
def maximo(lista): 
    n = 0
    valor_maximo = maximo_rec(lista,1,lista[0])
    return valor_maximo

if __name__ == "__main__":
    print(maximo([1,3,9]))