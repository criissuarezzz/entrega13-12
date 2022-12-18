from ast import main
from string import ascii_letters


string=input("Introduzca una cadena:")
def cadena(string):
    if string == "#":
        return []
    if string[0]=="#" or string[-1]!="#":
        palabra= string.split("#")[-1]
        if palabra[1] in ascii_letters:
            return(palabra)
        else:
            print("error")
            print(input("Introduzca una cadena:"))
    else:
        if "#" in string:
            print("No se puede dividir")
            print(input("Introduzca una cadena:"))
        else:
            return(string)

print(cadena(string))


if __name__=='__main__':
    main()



