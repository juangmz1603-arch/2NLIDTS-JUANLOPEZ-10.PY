MAX_TAM = 10

def ingresar_valores(frente, final, cola, contador):
    if (final + 1 ) % MAX_TAM == frente :
        print ( "Desbordamiento de la Cola.")
        return frente, final, cola, contador
    elemento = int (input("Ingrese un elemento para la cola:"))
    final = (final + 1 ) % MAX_TAM
    cola [final]= elemento
    contador += 1
    print ("Elemento", contador, "agregado a la cola:", elemento)
    return frente, final, cola, contador
def eliminar_elemento(frente, final, contador):
    if frente==final:
        print("La Cola esta Vacia. No se puede eliminar.")
        return frente, contador
    frente = (frente + 1) % MAX_TAM
    contador -= 1
    print("Elemento eliminado de la Cola.")
    return frente, contador
def imprimir(frente, final, cola):
    print("Elementos de la cola en el orden de ingreso:")
    i = frente + 1 
    while i != final + 1:
        print(" " + str(cola[i]))
        i = (i + 1) % MAX_TAM
    print ()

def main ():
    cola = [0] * MAX_TAM
    contador = 0
    frente =0
    final =0

    respuesta = input("Desea ingresar elementos a la Cola? (s/n):").upper()
    while respuesta == "S" and contador < 10:
        frente, final, cola, contador, = ingresar_valores(frente, final, cola, contador)
        if contador < 10:
            respuesta = input("Desea agragar mas elementos de la Cola?(s/n):").upper()
    if frente == final:
        print("La cola esta vacia.")
        return
    primer_elemento = cola[(frente + 1)% MAX_TAM]
    print ("El primer Elemento de la Cola es:" + " ", primer_elemento)
    frente, contador = eliminar_elemento(frente, final, contador)
    imprimir(frente, final, cola)
if __name__== "__main__":
    main ()

 
