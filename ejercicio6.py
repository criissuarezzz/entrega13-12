import random

#Escriba una rotate que gire una matriz bidimensional (una matriz) ya sea en sentido horario o antihorario 90 grados y devuelva la matriz rotada.
sentido = input("Ingrese el sentido de la rotación (horario o antihorario): ")
n= int(input("Ingrese el tamaño de la matriz: "))
matriz = [[random.randint(0, 9) for i in range(n)] for j in range(n)]
print("Matriz original:", matriz, sep="\n")

def rotar_matriz(matriz, sentido):
    if sentido == "antihorario":
        return [[matriz[i][j] for i in range(len(matriz))] for j in range(len(matriz[0])-1, -1, -1)]
    elif sentido == "horario":
        return [[matriz[i][j] for i in range(len(matriz)-1, -1, -1)] for j in range(len(matriz[0]))]
    else:
        raise ValueError("Sentido no válido")

if __name__=="__main__":
    print("Matriz rotada:", rotar_matriz(matriz, sentido), sep="\n")