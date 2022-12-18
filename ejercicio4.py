#boletos de la suerte4
while True:
    boleto=input("ingrese el numero del boleto: ")
    if len(boleto)<4:
        print("error, tiene que ser un número de más de 4 dígitos")
        print(input("ingrese el numero del boleto: "))
    else:
        def boletos(boleto):
            if len(boleto)%2==0:
                div1=boleto[:len(boleto)//2]
                div2=boleto[len(boleto)//2:]
                sumapar1=0
                sumapar2=0
                for i in range(len(div1)):
                    int(div1)
                    int(boleto)
                    int(sumapar1)
                    sumapar1+=(div1[i])
                    print(sumapar1)
                for i in range(len(div2)):
                    int(div2)
                    int(boleto)
                    int(sumapar2)
                    sumapar2+=(div2[i])
                    print(sumapar2)
                if sumapar1==sumapar2:
                    print("Traerá buena suerte")
                else:
                    print("No traerá buena suerte")
            else:
                divi1=boleto[:len(boleto)//2]
                divi2=boleto[len(boleto)//2+1:]
                sumaimpar1=[]
                sumaimpar2=[]
                for i in range(len(divi1)):
                    int(divi1)
                    int(boleto)
                    int(sumaimpar1)
                    sumaimpar1+=sum(divi1[i])
                    print(sumaimpar1)
                for i in range(len(divi2)):
                    int(divi2)
                    int(boleto)
                    int(sumaimpar2)
                    sumaimpar2+=sum(divi2[i])
                    print(sumaimpar2)
                if divi1[0]==divi2[1]:
                    print("Traerá buena suerte")
                else:
                    print("No traerá buena suerte")
    break
if __name__=="__main__":
    print(boletos(boleto))


