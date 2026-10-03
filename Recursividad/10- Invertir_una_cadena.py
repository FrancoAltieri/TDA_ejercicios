#Implementar una función recursiva que devuelva una cadena invertida.

#No utilizar [::-1].

def invertir_rec(cadena,n,cadena_invertida):
    
    if n < 0:
        return cadena_invertida
    
    cadena_invertida.append(cadena[n])
    
    return "".join(invertir_rec(cadena,n-1,cadena_invertida))
    
def invertir(cadena): 
    resultado = []
    return invertir_rec(cadena,len(cadena)- 1,resultado)

if __name__ == "__main__":
    string = "asdasdasd"
    print(invertir(string))