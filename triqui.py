"""Script para simular el juego triqui"""


#   1|2|3  O|X|X
#   4|5|6  X| |O
#   7|8|9  X|O|
#
#  1- lista de listas
#  2- Lista grande de 9
#  3- Diccionario + listas
#  

lista_usuario=[" "]*9
diccionario_triqui = { 0:[1,2,3],
                       1:[4,5,6],
                       2:[7,8,9],
                       3:[1,4,7],
                       4:[2,5,8],
                       5:[3,6,9],
                       6:[1,5,9],
                       7:[3,5,7]}

def pintar_cuadro():
    print(lista_usuario[:3])
    print(lista_usuario[3:6])
    print(lista_usuario[6:9])
        
        

def pedir_jugada():
    numero , letra = input("Numero-Letra < - ").split()
    numero = int(numero)-1
    if lista_usuario[numero]!=" ":
        print("El numero ya esta ocupado ")
        pedir_jugada()
    else:
        lista_usuario[numero]=letra

def verificar_jugada():
    es_triqui= False
    for jugada  in diccionario_triqui.values():
        # jugada = [1,2,3]
        palabra =""
        for cuadro in jugada:
            palabra+=lista_usuario[cuadro-1]

        # palabra  len = 3 , ' ','X','O' 
        primera_letra = palabra[0]
        if primera_letra!=" " and palabra.count(primera_letra)==3:
            es_triqui=True
            print("Es triqui de ",primera_letra)
            break

    return es_triqui



def run():    
    pintar_cuadro()
    es_triqui=False
    contador_turnos=0
    while not es_triqui and contador_turnos<9:
        pedir_jugada()
        pintar_cuadro()
        es_triqui=verificar_jugada()
        contador_turnos+=1

    
    
if __name__ == "__main__":
    run()