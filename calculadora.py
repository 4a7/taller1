# problemas con negativos en otras bases , agregar try excepts, cambios de base en memoria
from tkinter import *
def Calculadora():#muestra el frame de calculadora y esconde el resto
    calculadora.pack()
    acercade.pack_forget()
    ayuda.pack_forget()
    
    
def Acercade():#muestra el frame de acerca de y esconde el resto
    calculadora.pack_forget()
    ayuda.pack_forget()
    acercade.pack()
def Ayuda():#muestra el frame de ayuda y esconde el resto
    calculadora.pack_forget()
    ayuda.pack()
    acercade.pack_forget()
    f=open("a.pdf","r")
    texto=f.read()
    ayuda.config(text=texto)
def Salir():
    principal.quit()# se sale del mainloop
basetrabaja={0:10}
indices={"A":10,"B":11,"C":12,"D":13,"E":14,"F":15}
indices2={10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
texto={"txt":"0","mem":"0","res":""}#el texto tiene que salir de la funcion texto,
########principal##############

principal=Tk()
principal.config(bg="#f03d3f")
principal.title("Calculadora")
principal.resizable(0,0)#no permite modificar el tamano de la ventana
principal.geometry("464x262+0+0")
calculadora=Label(principal,width=400,height=300,bg="#f03d3f")##f03d3f#094448#102537#848b9f
calculadora.pack()
ayuda=Label(principal,width=405,height=300,bg="#f03d3f")
ayuda.pack()
acercade=Label(principal,width=400,height=300,bg="#f03d3f",text="Calculadora\nVersion 1.0\nCreada por Juan F.Villacis")
acercade.pack()

##########################FUNCIONES CONVERTIDORAS
def de10aotro(num,destino):#convierte de 10 a otras bases
    num=str(num)
    try:
        print("entro",num)
        if num[0]=="-":
            print("lo es")
            num=num[1:]
            negativo=1
        else:
            negativo=0
    
        num2=float(num)
        num2=int(num2)
        destino=int(destino)
        print(num2,destino)
        
        digitos=[]
        division=0
        a=1
        while num2>0 or a==1:
            a=2
            division=num2%destino
            division=str(division)
            
            digitos.append(division)
            num2=num2//destino
        digitos.reverse()
        retorno=""
        print(digitos)
        
        for i in digitos:#une los valores de la lista, si el valor >9 entonces lo reemplaza por su letra
            
            if int(i)>9:
                
                retorno=retorno+indices2[int(i)]
                

                
            else:

                retorno=retorno+i
        num=str(num)
        
        if "." in num:
            
            flotante=""
            num2=(float(num)-int(float(num)))
            cont=0
            a=1
            while (cont==0 or cont<8) and (num2!=0 or a==1):
                a=2
                temporal=(num2*destino)
                num2=temporal-int(temporal)
                if int(temporal)>9:
                    temporal=indices2[int(temporal)]
                else:
                    temporal=str(int(temporal))
                flotante=flotante+temporal
                cont+=1
            
            retorno=retorno+"."+flotante
        if negativo ==1:
            retorno="-"+retorno
        
        
        return retorno
    except:
        pass








def deotraa10(num,fuente):
    num=str(num)
    try:
        if "-" in num:
            num=num[1:]
            negativo=1
        else:
            negativo=0
        copia=str(num)
        num=str(num)
        
        retorno=0
        if "." in num:
            copia2=""
            flotante=0
            check=0
            cont=-1
            for i in num:
                if check==1:
                    if i in "ABCDEF":
                        i=indices[i]
                    flotante=flotante+(int(i)*(fuente**cont))
                    
                    cont-=1
                if i==".":
                    check=1
                if check==0:
                    copia2=copia2+i
                
            flotante=str(flotante)
            flotante=flotante[2:]
            
            copia=copia2
        cont=len(copia)-1
        for i in range(len(copia)):
            if copia[i].isdigit():
                a=((int(copia[i])*(int(fuente)**cont)))
                retorno=retorno+a
                        
                        
            elif copia[i].isalpha():
                retorno=retorno+int((indices[copia[i]]*(int(fuente)**cont)))
            cont-=1
            retorno=int(retorno)
            
        retorno=str(retorno)
        if "." in num:
            retorno=retorno+"."+flotante
        if negativo ==1:
            retorno="-"+retorno
        
            
        return retorno
    except:
        pass

#convierte los numeros cuando se apreta un boton de cambio de base
def conviertelosnumeros1():
    try:
        tira=texto["txt"]
        tira=tira.replace("//","&")
        tira2=""
        temporal=""
        numeros="ABCDEF012345678.9"
        simbolos="+-*/%&="

        for i in tira:
            if i in numeros:
                temporal=temporal+i
                
            if i in simbolos:
                temporal=deotraa10(temporal,basetrabaja[0])
                tira2=tira2+temporal
                tira2=tira2+i
                temporal=""
        tira2=tira2+deotraa10(temporal,basetrabaja[0])
        tira2=tira2.replace("&","//")
        texto["txt"]=tira2
    except:
        pass

def conviertelosnumeros2():
    try:
        tira=texto["txt"]
        tira=tira.replace("//","&")
        tira2=""
        temporal=""
        numeros="ABCDEF012345678.9"
        simbolos="+-*/=%&"

        for i in tira:
            if i in numeros:
                temporal=temporal+i
                
            if i in simbolos:
                temporal=de10aotro(temporal,basetrabaja[0])
                tira2=tira2+temporal
                tira2=tira2+i
                temporal=""
        tira2=tira2+de10aotro(temporal,basetrabaja[0])
        tira2=tira2.replace("&","//")
        texto["txt"]=tira2
    except:
        pass

##################colores###########

color="#f03d3f"#color de teclas normales
colores={"hex":color,"dec":"#ffffff","oct":color,"bin":color,"memoria":color}

def arreglaigual():
    try:
    
        if "=" in texto["txt"] and texto["txt"][-1]!="=":
            
            if texto["txt"][-1] in ("1234567890ABCDEF"):
                texto["txt"]=""
    except:
        pass
def sincroniza(texto):#formato de los numeros
    try:
        texto["txt"]=texto["txt"].replace("//","&")
        ops="/*+%&"       
        if texto["txt"]=="":
            texto["txt"]="0"
        elif len(texto["txt"])>1 and texto["txt"][0]=="0" and texto["txt"][1] not in ops and texto["txt"][1]!=".":
            texto["txt"]=texto["txt"][1:]
        
        texto["txt"]=texto["txt"].replace("&","//")
    except:
        pass
    

#############menu#################
        
barramenu=Menu(principal)
mnuMenu=Menu(barramenu)
barramenu.add_command(label="Calculadora",command=Calculadora)
barramenu.add_command(label="Acerca de",command=Acercade)
barramenu.add_command(label="Ayuda",command=Ayuda)
barramenu.add_command(label="Salir",command=principal.destroy)#destruye principal
principal.config(menu=barramenu)#se pone para agregarlo a principalS
#################resultado label########################
resultado=Label(calculadora,text=texto["txt"],anchor=E,bd=0,bg="white",font=("Calibri",12),width=57,height=3)
resultado.place(x=3,y=3.5)
####################################funciones que activan y desactivan numeros
def activa(n):
    if n==10:
        btnA.config(state="disabled")
        btnB.config(state="disabled")
        btnC.config(state="disabled")
        btnD.config(state="disabled")
        btnE.config(state="disabled")
        btnF.config(state="disabled")
        btn0.config(state="normal")
        btn1.config(state="normal")
        btn2.config(state="normal")
        btn3.config(state="normal")
        btn4.config(state="normal")
        btn5.config(state="normal")
        btn6.config(state="normal")
        btn7.config(state="normal")
        btn8.config(state="normal")
        btn9.config(state="normal")

    if n==2:
        btnA.config(state="disabled")
        btnB.config(state="disabled")
        btnC.config(state="disabled")
        btnD.config(state="disabled")
        btnE.config(state="disabled")
        btnF.config(state="disabled")
        btn0.config(state="normal")
        btn1.config(state="normal")
        btn2.config(state="disabled")
        btn3.config(state="disabled")
        btn4.config(state="disabled")
        btn5.config(state="disabled")
        btn6.config(state="disabled")
        btn7.config(state="disabled")
        btn8.config(state="disabled")
        btn9.config(state="disabled")
    
    if n==8:
        btnA.config(state="disabled")
        btnB.config(state="disabled")
        btnC.config(state="disabled")
        btnD.config(state="disabled")
        btnE.config(state="disabled")
        btnF.config(state="disabled")
        btn0.config(state="normal")
        btn1.config(state="normal")
        btn2.config(state="normal")
        btn3.config(state="normal")
        btn4.config(state="normal")
        btn5.config(state="normal")
        btn6.config(state="normal")
        btn7.config(state="normal")
        btn8.config(state="disabled")
        btn9.config(state="disabled")
    
    if n==16:
        btnA.config(state="normal")
        btnB.config(state="normal")
        btnC.config(state="normal")
        btnD.config(state="normal")
        btnE.config(state="normal")
        btnF.config(state="normal")
        btn0.config(state="normal")
        btn1.config(state="normal")
        btn2.config(state="normal")
        btn3.config(state="normal")
        btn4.config(state="normal")
        btn5.config(state="normal")
        btn6.config(state="normal")
        btn7.config(state="normal")
        btn8.config(state="normal")
        btn9.config(state="normal")

    
#el anchor pone el texto en E(p12 manual)
#funciones imprimir en el label#########################################
############################################################
###############################################################abcdef
def PrintF(texto):
    try:
        arreglaigual()
        texto["txt"]=texto["txt"]+"F"
        sincroniza(texto)
        resultado.config(text=texto["txt"])
    except:
        pass
    
    
    
def PrintA(texto):
    try:
        arreglaigual()
        texto["txt"]=texto["txt"]+"A"
        sincroniza(texto)
        resultado.config(text=texto["txt"])
    except:
        pass
    
    
    
def PrintB(texto):
    try:
        arreglaigual()
        texto["txt"]=texto["txt"]+"B"
        sincroniza(texto)
        resultado.config(text=texto["txt"])
    except:
        pass
    
    
def PrintC(texto):
    try:
        arreglaigual()
        texto["txt"]=texto["txt"]+"C"
        sincroniza(texto)
        resultado.config(text=texto["txt"])
    except:
        pass
    
    
def PrintD(texto):
    try:
        arreglaigual()
        texto["txt"]=texto["txt"]+"D"
        sincroniza(texto)
        resultado.config(text=texto["txt"])
    except:
        pass
    
    
def PrintE(texto):
    try:
        arreglaigual()
        texto["txt"]=texto["txt"]+"E"
        sincroniza(texto)
        resultado.config(text=texto["txt"])
    except:
        pass
##################################################################operaciones
##################################################################operaciones
##################################################################operaciones
##################################################################operaciones
##################################################################operaciones
##################################################################operaciones
##################################################################operaciones
##################################################################operaciones
##################################################################operaciones
def operacion(k,num1,num2):
    try:
        if basetrabaja[0]!=10:
            if "." in (deotraa10(num1,basetrabaja[0])) or "." in (deotraa10(num2,basetrabaja[0])):
                num1=float(deotraa10(num1,basetrabaja[0]))
                num2=float(deotraa10(num2,basetrabaja[0]))
            else:
                num1=int(deotraa10(num1,basetrabaja[0]))
                num2=int(deotraa10(num2,basetrabaja[0]))
        else:
            if "." in num1 or "." in num2:
                num1=float(num1)
                num2=float(num2)
            else:
                num1=int(num1)
                num2=int(num2)
        
        if k=="&":
            
            resultado= num1//num2
        elif k=="/":
            resultado= num1/num2
        elif k=="*":
            resultado= num1*num2
        elif k=="-":
            resultado= num1-num2
        elif k=="+":
            resultado= num1+num2
            
        elif k=="%":
            resultado= num1%num2
        print(basetrabaja[0],num1,num2,resultado)
        
        if basetrabaja[0]!=10:
            resultado=de10aotro(resultado,basetrabaja[0])
        
        return resultado
    except:
        return ""
        ######################convierte el valor respuesta a la base en la que se esta trtabajando
def devuelta(num):
    try:
        retorno=retorno2=""
        if "." in num:
            num=float(num)
        else:
            num=int(num)
        while num>0:
            retorno=retorno+str(num%basetrabaja[0])
            num=num//basetrabaja[0]
        for i in range(len(retorno)-1,-1,-1):
            retorno2=retorno2+retorno[i]
        return retorno2
    except:
        return ""
###################################
def analiza(string):#retorna el valor de unaoperacion contando la prioridad
    try:
        ops=["&%","/*","+-"]
        ops2="&%,/*,+-"
        numeros="01234567.89ABCDEF"
        string=string.replace("//","&")
        
        for i in range(3):
            for k in string:
                numero1=""
                numero2=""
                nuevostring=""
                
                
                
                    
                if k in ops[i] and string.index(k)!=0:
                    for h in string[:(string.index(k))]:
                        
                        if h in numeros:
                            numero1=numero1+h
                        else:
                            if (string.index(h)==0 and h=="-"):
                                numero1=numero1+h
                            elif h in ops2:
                                numero1=""
                            
                                
                    for h in string[(string.index(k))+1:]:
                        if h in numeros:
                            numero2=numero2+h
                        else:
                            if  (string[string.index(h)-1]in ops[i] and h=="-"):
                                numero2=numero2+h
                            else:
                                break
                    
                    num1=numero1
                    num2=numero2
              
                    reemplazador=numero1+k+numero2
                    nuevostring=operacion(k,num1,num2)
                   
                    string=string.replace(reemplazador,str(nuevostring),1)
            
        return((string))#string tiene el resultado#estaba devuelta(string)
    except:
        return ""
############################################convierte decbinocthex


def encuentranum():
    try:
        a=texto["txt"]
        for i in a:
            if i =="b" or i =="d" or i =="h" or i =="o":
                numero=""
                if i =="b":
                    k=2
                elif i=="d":
                    k=10
                elif i=="h":
                    k=16
                elif i=="o":
                    k=8
                    
                    
                
               
                
                for j in range(a.index(i)+1,len(a)):
     
                    if a[j] in "0123456789ABCDE.F":
                        numero=numero+a[j]
                        
                    else:
                        break
                re=i+numero
                numero=deotraa10(numero,k)
                numero=de10aotro(numero,basetrabaja[0])
                a=a.replace(re,numero)
        texto["txt"]=a
    except:
        pass
            
    
        
################################################################################bases temporales
def PrintDec(texto):
    try:
        arreglaigual()
        texto["txt"]=texto["txt"]+"d"
        sincroniza(texto)
        activa(10)
        resultado.config(text=texto["txt"])
    except:
        pass
    
def PrintBin(texto):
    try:
        arreglaigual()
        texto["txt"]=texto["txt"]+"b"
        sincroniza(texto)
        resultado.config(text=texto["txt"])
        activa(2)
    except:
        pass
    
    
def PrintOct(texto):
    try:
        arreglaigual()
        texto["txt"]=texto["txt"]+"o"
        sincroniza(texto)
        resultado.config(text=texto["txt"])
        activa(8)
    except:
        pass
    
def PrintHex(texto):
    try:
        arreglaigual()
        texto["txt"]=texto["txt"]+"h"
        sincroniza(texto)
        resultado.config(text=texto["txt"])
        activa(16)
    except:
        pass
    
#########################################################################numeros
def Print9(texto):
    try:
        arreglaigual()
        texto["txt"]=texto["txt"]+"9"
        sincroniza(texto)
        resultado.config(text=texto["txt"])
    except:
        pass
    
def Print8(texto):
    try:
        arreglaigual()
        texto["txt"]=texto["txt"]+"8"
        sincroniza(texto)
        resultado.config(text=texto["txt"])
    except:
        pass
    
def Print7(texto):
    arreglaigual()
    texto["txt"]=texto["txt"]+"7"
    sincroniza(texto)
    resultado.config(text=texto["txt"])
    
def Print6(texto):
    try:
        arreglaigual()
        texto["txt"]=texto["txt"]+"6"
        sincroniza(texto)
        resultado.config(text=texto["txt"])
    except:
        pass
    
def Print5(texto):
    try:
        arreglaigual()
        texto["txt"]=texto["txt"]+"5"
        sincroniza(texto)
        resultado.config(text=texto["txt"])
    except:
        pass
    
def Print4(texto):
    try:
        arreglaigual()
        texto["txt"]=texto["txt"]+"4"
        sincroniza(texto)
        resultado.config(text=texto["txt"])
    except:
        pass
    
def Print3(texto):
    try:
        arreglaigual()
        texto["txt"]=texto["txt"]+"3"
        sincroniza(texto)
        resultado.config(text=texto["txt"])
    except:
        pass
    
def Print2(texto):
    try:
        arreglaigual()
        texto["txt"]=texto["txt"]+"2"
        sincroniza(texto)
        resultado.config(text=texto["txt"])
    except:
        pass
       
def Print1(texto):
    try:
        texto["txt"]=texto["txt"]+"1"
        sincroniza(texto)
        resultado.config(text=texto["txt"])
    except:
        pass
    
def Print0(texto):
    try:
        arreglaigual()
        texto["txt"]=texto["txt"]+"0"
        sincroniza(texto)
        resultado.config(text=texto["txt"])
    except:
        pass
    
def PrintPoint(texto):
    try:
        arreglaigual()
        
        
        if texto["txt"][-1] == ".":
            texto["txt"]=texto["txt"]
        else:
            texto["txt"]=texto["txt"]+"."
        
            

        resultado.config(text=texto["txt"])
    except:
        pass
    

    

############################################################operaciones
def PrintMult(texto):
    try:
        if "=" in texto["txt"]:
            texto["txt"]=str(texto["res"])
            
            texto["txt"]=texto["txt"]+"*"
        else:
       
            texto["txt"]=texto["txt"].replace("//","&")
            if texto["txt"][-1] in "+-%&/*":
                texto["txt"]=texto["txt"][:len(texto["txt"])-1]+"*"
            else:
                texto["txt"]=texto["txt"]+"*"
            texto["txt"]=texto["txt"].replace("&","//")
        
        activa(basetrabaja[0])
        resultado.config(text=texto["txt"])
    except:
        pass
        
        
    
    
    
def PrintSub(texto):
    try:
        if "=" in texto["txt"]:
            texto["txt"]=str(texto["res"])
            
            texto["txt"]=texto["txt"]+"-"
        else:
            texto["txt"]=texto["txt"].replace("//","&")
        
            if texto["txt"][-1] in "-%&/+":
                print(texto["txt"][-1])
                texto["txt"]=texto["txt"][:len(texto["txt"])-1]+"-"
                
            else:
                texto["txt"]=texto["txt"]+"-"
            texto["txt"]=texto["txt"].replace("&","//")
            
        sincroniza(texto)
        resultado.config(text=texto["txt"])
    except:
        pass
    
def PrintPlus(texto):
    try:
        print(texto["txt"])
        if "=" in texto["txt"]:
            texto["txt"]=str(texto["res"])
            
            texto["txt"]=texto["txt"]+"+"
        else:
            texto["txt"]=texto["txt"].replace("//","&")
            if texto["txt"][-1] in "*/%&+-":
                texto["txt"]=texto["txt"][:len(texto["txt"])-1]+"+"
            else:
                texto["txt"]=texto["txt"]+"+"
            texto["txt"]=texto["txt"].replace("&","//")
        resultado.config(text=texto["txt"])
        activa(basetrabaja[0])
    except:
        pass
    
def PrintDiv(texto):
    try:
        if "=" in texto["txt"]:
            texto["txt"]=str(texto["res"])
            
            texto["txt"]=texto["txt"]+"/"
        else:
            texto["txt"]=texto["txt"].replace("//","&")
            if texto["txt"][-1] in "+%&*-/":
                texto["txt"]=texto["txt"][:len(texto["txt"])-1]+"/"
            else:
                texto["txt"]=texto["txt"]+"/"
            texto["txt"]=texto["txt"].replace("&","//")
        resultado.config(text=texto["txt"])
        activa(basetrabaja[0])
    except:
        pass
    
def PrintDI(texto):
    try:
        if "=" in texto["txt"]:
            texto["txt"]=str(texto["res"])
            
            texto["txt"]=texto["txt"]+"//"
        else:
            texto["txt"]=texto["txt"].replace("//","&")
            if texto["txt"][-1] in "+%&*/":
                texto["txt"]=texto["txt"][:len(texto["txt"])-1]+"//"
            else:
                texto["txt"]=texto["txt"]+"&"
            texto["txt"]=texto["txt"].replace("&","//")
        resultado.config(text=texto["txt"])
        activa(basetrabaja[0])
    except:
        pass
    
def PrintMod(texto):
    try:
        if "=" in texto["txt"]:
            texto["txt"]=str(texto["res"])
            
            texto["txt"]=texto["txt"]+"%"
        else:
            texto["txt"]=texto["txt"].replace("//","&")
            if texto["txt"][-1] in "+*/-%&":
                texto["txt"]=texto["txt"][:len(texto["txt"])-1]+"%"
            else:
                texto["txt"]=texto["txt"]+"%"
            texto["txt"]=texto["txt"].replace("&","//")
        
        resultado.config(text=texto["txt"])
        activa(basetrabaja[0])
    except:
        pass
    
def PrintDlt(texto):
    try:
        texto["txt"]=texto["txt"].replace("//","&")
        texto["txt"]=texto["txt"][:len(texto["txt"])-1]
        sincroniza(texto)
        texto["txt"]=texto["txt"].replace("//","&")
        resultado.config(text=texto["txt"])
        activa(basetrabaja[0])
    except:
        pass
    
def PrintIgual(texto):
    try:
        if "=" not in texto["txt"]:
            encuentranum()
            texto["res"]=analiza(texto["txt"])
            texto["res"]=(analiza(texto["txt"]))
            
            texto["txt"]=texto["txt"]+"="+analiza(texto["txt"])
            print(texto["res"])
            resultado.config(text=texto["txt"])
        activa(basetrabaja[0])
    except:
        pass
def Clear(texto):
    try:
        texto["txt"]="0"
        resultado.config(text=texto["txt"])
        activa(basetrabaja[0])
    except:
        pass
def MasMenos(texto):#optimizar para que funcione con operaciones, para que sea haga el ifual sin ponerlo
    
    encuentranum()
    try:
        print("+/-",texto["txt"])
        texto["txt"]=analiza(texto["txt"])
        if "." in texto["txt"]:
            texto["txt"]=str(float(texto["txt"])*-1)
        else:
            texto["txt"]=str(int(texto["txt"])*-1)
        print(texto["txt"])
        resultado.config(text=texto["txt"])
        activa(basetrabaja[0])
    except:
        pass
    
####################################
    ####################################
    ####################################
    ####################################
    ####################################
    ####################################
    ####################################

def colordebase(base):
    color="#f03d3f"
    if base=="dec":
        colores["dec"]="#ffffff"
        colores["bin"]=color
        colores["oct"]=color
        colores["hex"]=color
        encuentranum()
        conviertelosnumeros1()
        basetrabaja[0]=10
        activa(basetrabaja[0])
        resultado.config(text=texto["txt"])
        
       
    elif base=="hex":
        colores["dec"]=color
        colores["bin"]=color
        colores["oct"]=color
        colores["hex"]="#ffffff"
        conviertelosnumeros1()
        basetrabaja[0]=16
        encuentranum()
        conviertelosnumeros2()
        activa(basetrabaja[0])
        resultado.config(text=texto["txt"])
    elif base=="oct":
        colores["dec"]=color
        colores["bin"]=color
        colores["oct"]="#ffffff"
        colores["hex"]=color
        encuentranum()
        conviertelosnumeros1()
        basetrabaja[0]=8
        conviertelosnumeros2()
        activa(basetrabaja[0])
        resultado.config(text=texto["txt"])
    elif base=="bin":
        colores["dec"]=color
        colores["bin"]="#ffffff"
        colores["oct"]=color
        colores["hex"]=color
        conviertelosnumeros1()
        basetrabaja[0]=2
        encuentranum()
        conviertelosnumeros2()
        activa(basetrabaja[0])
        resultado.config(text=texto["txt"])
    btndec.config(bg=colores["dec"])
    btnoct.config(bg=colores["oct"])
    btnbin.config(bg=colores["bin"])
    btnhex.config(bg=colores["hex"])
    

    #################### ########3
    #################### ########3
def formageneral(n):
    indice1=0
    indice2=0
    numero=""
    if n=="b":
        indice1=texto["txt"].index(n)
        for i in texto["txt":]:
            while i in "01":
                numero=numero+""
        
                
    #recibe la letra i que esta en texto, tienen que convertirlo a la base 10
    #analiza texto para asi reconocer cuales son los umeros que estan despues de la leetra ej b####,los ####estan despues de la b, estan en bin
    pass


       

############operaciones de memoria################
def Mplus(texto):
    try:
        sumar=""
        if "=" in texto["txt"]:
            check=0
            for i in texto["txt"]:
                if check==1:
                    sumar=sumar+i
                if i=="=":
                    check=1
        else:
            sumar=analiza(texto["txt"])
        
        texto["mem"]=str(int(texto["mem"])+int(sumar))
    except:
        pass
    if texto["mem"]=="0":
        colores["memoria"]="#f03d3f"
    else:
        colores["memoria"]="#ffffff"
    
    btnMR.config(bg=colores["memoria"])


def Msub(texto):
    try:
        texto["mem"]=str(int(texto["mem"])-int(texto["txt"]))
    except:
        pass
    if texto["mem"]==0:
        colores["memoria"]="#f03d3f"
    else:
        colores["memoria"]="#ffffff"
    print(texto["mem"])
    btnMR.config(bg=colores["memoria"])
    print(texto["mem"])
def Mclear(texto):
    texto["mem"]="0"
    colores["memoria"]="#f03d3f"
    print(texto["mem"])
    btnMR.config(bg=colores["memoria"])
    print(texto["mem"])
def Mload(texto):
    texto["txt"]=str(texto["mem"])
    btnMR.config(bg=colores["memoria"])
    resultado.config(text=texto["txt"])
    print(texto["mem"])

#################
#botones bases

btndec=Button(calculadora,text="Dec",bd=0,bg=colores["dec"],font=("Calibri",12),width=5,height=2,command=lambda: colordebase("dec"))
btndec.place(x=0,y=67)
btnbin=Button(calculadora,text="Bin",bd=0,bg=colores["bin"],font=("Calibri",12),width=5,height=2,command=lambda: colordebase("bin"))
btnbin.place(x=0,y=115.5)
btnoct=Button(calculadora,text="Oct",bd=0,bg=colores["oct"],font=("Calibri",12),width=5,height=2,command=lambda: colordebase("oct"))
btnoct.place(x=0,y=164.6)
btnhex=Button(calculadora,text="Hex",bd=0,bg=colores["hex"],font=("Calibri",12),width=5,height=2,command=lambda: colordebase("hex"))
btnhex.place(x=0,y=214.3)


    


    
#botones abcdef
btnA=Button(calculadora,text="A",bd=0,bg=color,font=("Calibri",12),width=4,state="disabled",height=1,command=lambda: PrintA(texto))
btnA.place(x=47,y=67.4)
btnB=Button(calculadora,text="B",bd=0,bg=color,font=("Calibri",12),width=4,state="disabled",height=1,command=lambda: PrintB(texto))
btnB.place(x=47,y=99.5)
btnC=Button(calculadora,text="C",bd=0,bg=color,font=("Calibri",12),width=4,state="disabled",height=1,command=lambda: PrintC(texto))
btnC.place(x=47,y=132.5)
btnD=Button(calculadora,text="D",bd=0,bg=color,font=("Calibri",12),width=4,state="disabled",height=1,command=lambda: PrintD(texto))
btnD.place(x=47,y=166)
btnE=Button(calculadora,text="E",bd=0,bg=color,font=("Calibri",12),width=4,state="disabled",height=1,command=lambda: PrintE(texto))
btnE.place(x=47,y=198.8)
btnF=Button(calculadora,text="F",bd=0,bg=color,font=("Calibri",12),width=4,state="disabled",height=1,command=lambda: PrintF(texto))
btnF.place(x=47,y=232)

#botones memoria
btnMR=Button(calculadora,text="MR",bd=0,bg=colores["memoria"],font=("Calibri",12),width=5,height=2,command=lambda: Mload(texto))
btnMR.place(x=89,y=164.6)
btnMsub=Button(calculadora,text="M-",bd=0,bg=color,font=("Calibri",12),width=5,height=2,command=lambda: Msub(texto))
btnMsub.place(x=89,y=115.5)
btnMplus=Button(calculadora,text="M+",bd=0,bg=color,font=("Calibri",12),width=5,height=2,command=lambda: Mplus(texto))
btnMplus.place(x=89,y=67.4)
btnMC=Button(calculadora,text="MC",bd=0,bg=color,font=("Calibri",12),width=5,height=2,command=lambda: Mclear(texto))
btnMC.place(x=89,y=214.3)
#botones base temporal
btnd=Button(calculadora,text="d",bd=0,bg=color,font=("Calibri",12),width=5,height=2,command=lambda: PrintDec(texto))
btnd.place(x=136,y=67.4)
btnb=Button(calculadora,text="b",bd=0,bg=color,font=("Calibri",12),width=5,height=2,command=lambda: PrintBin(texto))
btnb.place(x=136,y=115.5)
btno=Button(calculadora,text="o",bd=0,bg=color,font=("Calibri",12),width=5,height=2,command=lambda: PrintOct(texto))
btno.place(x=136,y=164.6)
btnh=Button(calculadora,text="h",bd=0,bg=color,font=("Calibri",12),width=5,height=2,command=lambda: PrintHex(texto))
btnh.place(x=136,y=214.3)
#botones 0147
btn7=Button(calculadora,text="7",bd=0,bg=color,font=("Calibri",12),width=5,height=2,command=lambda: Print7(texto))
btn7.place(x=183,y=67.4)
btn4=Button(calculadora,text="4",bd=0,bg=color,font=("Calibri",12),width=5,height=2,command=lambda: Print4(texto))
btn4.place(x=183,y=115.5)
btn1=Button(calculadora,text="1",bd=0,bg=color,font=("Calibri",12),width=5,height=2,command=lambda: Print1(texto))
btn1.place(x=183,y=164.6)
btn0=Button(calculadora,text="0",bd=0,bg=color,font=("Calibri",12),width=5,height=2,command=lambda: Print0(texto))
btn0.place(x=183,y=214.3)
#botones 852.
btn8=Button(calculadora,text="8",bd=0,bg=color,font=("Calibri",12),width=5,height=2,command=lambda: Print8(texto))
btn8.place(x=230,y=67.4)
btn5=Button(calculadora,text="5",bd=0,bg=color,font=("Calibri",12),width=5,height=2,command=lambda: Print5(texto))
btn5.place(x=230,y=115.5)
btn2=Button(calculadora,text="2",bd=0,bg=color,font=("Calibri",12),width=5,height=2,command=lambda: Print2(texto))
btn2.place(x=230,y=164.6)
btnpunto=Button(calculadora,text=".",bd=0,bg=color,font=("Calibri",12),width=5,height=2,command=lambda: PrintPoint(texto))
btnpunto.place(x=230,y=214.3)
#botones 963,+/-
btn9=Button(calculadora,text="9",bd=0,bg=color,font=("Calibri",12),width=5,height=2,command=lambda: Print9(texto))
btn9.place(x=277,y=67.4)
btn6=Button(calculadora,text="6",bd=0,bg=color,font=("Calibri",12),width=5,height=2,command=lambda: Print6(texto))
btn6.place(x=277,y=115.5)
btn3=Button(calculadora,text="3",bd=0,bg=color,font=("Calibri",12),width=5,height=2,command=lambda: Print3(texto))
btn3.place(x=277,y=164.6)
btnPlusub=Button(calculadora,text="+/-",bd=0,bg=color,font=("Calibri",12),width=5,height=2,command=lambda: MasMenos(texto))
btnPlusub.place(x=277,y=214.3)
#botones /+*-
btnDiv=Button(calculadora,text="/",bd=0,bg=color,font=("Calibri",12),command=lambda: PrintDiv(texto),width=5,height=2)
btnDiv.place(x=324,y=67.4)
btnMult=Button(calculadora,text="*",bd=0,bg=color,font=("Calibri",12),width=5,height=2,command=lambda: PrintMult(texto))
btnMult.place(x=324,y=115.5)
btnPlus=Button(calculadora,text="+",bd=0,bg=color,font=("Calibri",12),width=5,height=2,command=lambda: PrintPlus(texto))
btnPlus.place(x=324,y=164.6)
btnSub=Button(calculadora,text="-",bd=0,bg=color,font=("Calibri",12),width=5,height=2,command=lambda: PrintSub(texto))
btnSub.place(x=324,y=214.3)


#boton =
btnIgual=Button(calculadora,text="=",bd=0,bg=color,font=("Calibri",12),width=5,height=10,command=lambda: PrintIgual(texto))
btnIgual.place(x=371,y=67.4)
#botones C,<-,//,%
btnClear=Button(calculadora,text="C",bd=0,bg=color,font=("Calibri",12),width=5,height=2,command=lambda: Clear(texto))
btnClear.place(x=418,y=67.4)
btnDlt=Button(calculadora,text="<-",bd=0,bg=color,font=("Calibri",12),width=5,height=2,command=lambda: PrintDlt(texto))
btnDlt.place(x=418,y=115.5)
btnDI=Button(calculadora,text="//",bd=0,bg=color,font=("Calibri",12),width=5,height=2,command=lambda: PrintDI(texto))
btnDI.place(x=418,y=164.6)
btnMod=Button(calculadora,text="%",bd=0,bg=color,font=("Calibri",12),width=5,height=2,command=lambda: PrintMod(texto))
btnMod.place(x=418,y=214.3)

principal.mainloop()

        








    
        



