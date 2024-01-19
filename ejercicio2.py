import os

class ListaNumeros: 
    #Declaracion de propiedades

    # longitud = 0
    lista = []
    lista_completa=[]
    repetidos ={}
    pares=[]
    impares=[]

#declaracion de constructor
    # def __init__(self,n):
    #     self.longitud = n
        
#declaracion de metodos de clase
    def agregar(self,n):
        self.lista_completa.append(n)
        self.lista_completa.sort()
        if n in self.lista:
            if n in self.repetidos:
                self.repetidos[n] += 1
            else:
                self.repetidos[n] = 2 
        else:
            self.lista.append(n)
            
            if n%2 == 0:
                self.pares.append(n)
            else:
                self.impares.append(n)
            self.lista.sort()
    def mostrar(self):
        print("Esta es la lista de números ordenada")
        print(self.lista_completa)
        print("Esta es la lista de números sin repeticiones")
        print(self.lista)
        print("Esta es la lista de números repetidos")
        print(self.repetidos)
        print("Esta es la lista de números pares")
        print(self.pares)
        print("Esta es la lista de números impares")
        print(self.impares)

def main():
    #La linea para limpiar la terminal
    os.system('cls')
    n = int(input("¿Cuántos números quieres en la lista?: "))
    obj = ListaNumeros()
    
    for i in range(1,n+1):
        nn = int(input('Ingresa el número {}'.format(i)+": "))
        obj.agregar(nn)
    
    
    obj.mostrar()

if __name__ == "__main__":
    main()