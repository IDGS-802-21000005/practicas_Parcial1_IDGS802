import os

class Piramide: 
    #Declaracion de propiedades
    niveles =0

#declaracion de constructor
    def __init__(self,n):
        self.niveles = n
        
#declaracion de metodos de clase
    def mostrar_piramide(self):
        for i in range(0,self.niveles):
            niv = ""
            for j in range(0,i+1):
                niv+="*"
            print("{}".format(niv))

def main():
    #La linea para limpiar la terminal
    os.system('cls')
    n = int(input("¿Cuántos niveles quieres?: "))
    obj=Piramide(n)
    obj.mostrar_piramide()

if __name__ == "__main__":
    main()