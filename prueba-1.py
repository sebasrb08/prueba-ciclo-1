import io
import json
def cargarClientes():
    try:
        dicClientes={}
        with open("clientes.json","r+")as archivo:            
            dicClientes = json.load(archivo)
            return dicClientes
    except:
        dicClientes={}
        return dicClientes


def cargarTarjeta():
    try:
        dicTarjetas={}
        with open("tarjetas.json","r+")as archivo:            
            dicTarjetas = json.load(archivo)
            return dicTarjetas
    except:
        dicTarjetas={}
        return dicTarjetas

def menu():
    while True:
        try:
            print("-"*50)
            
            print("""
\tMenu:
1.Clientes
2.Tarjeta Credito
3.Informe
4.salir 
                """)
            print("-"*50)
            opcion=int(input("Ingrese su opcion: "))
            print("-"*50)
            if opcion <1 or opcion >4:
                print("!Error¡,digite una opcion valida")
                continue
            return opcion
        except ValueError:
            print("Error,digite un numero")

def clientes(dicClientes):
    while True:
        try:
            print("-"*50)
            print("""
\tClientes:
1.Agregar
2.Modificar
3.Eliminar
4.Salir
                """)
            print("-"*50)
            opcion=int(input("Ingrese su opcion: "))
            print("-"*50)
            if opcion <1 or opcion >5:
                print("!Error¡,digite una opcion valida")
                continue
            
        except ValueError:
            print("Error,digite un numero")
        
        if opcion==1:
            dicClientes=agregarClientes(dicClientes)
        elif opcion == 2:
            dicClientes=modificarClientes(dicClientes)
        elif opcion== 3:
            dicClientes=eliminarClientes(dicClientes)
        elif opcion ==4:
            return dicClientes
            break
        
        


def agregarClientes(dicClientes):
    
    nom=nombre()
    cedu=cedula(dicClientes)
    num=numeroT()
    sx=sexo()
    
    dicClientes[cedu]={}
    dicClientes[cedu]["nombre"]=nom
    dicClientes[cedu]["numeroTelefono"]=num
    dicClientes[cedu]["sexo"]=sx
    
    enviarClientes(dicClientes)
    return dicClientes
    
def enviarClientes(dicClientes):
    with open("clientes.json","w+")as archivo:
        json.dump(dicClientes,archivo)

def nombre():
    while True:
        try:
            print("-"*50)
            nom=input("Ingrese nombre: ")
            print("-"*50)
            if not nom.isalpha():
                print("Error,Ingrese un nombre de tipo (string)")
                continue
            return nom
        except:
            print("Error,Ingrese un nombre")    
            
def cedula(dicClientes):
    while True:
        flat=False
        try:
            print("-"*50)
            cedu=input("Ingrese Cedula: ")
            print("-"*50)
            if not cedu.isdigit():
                print("Error,Ingrese una cedula de tipo (entero)")
                continue
            for i in dicClientes.keys():
                    if i == cedu:
                        print("cedula ya registrada,registre una cedula diferente")
                        flat=True
            if flat==True:
                continue
            
            return cedu 
        except:
            print("Error,Ingrese un numero de cedula ")    

def numeroT():
    while True:
        try:
            print("-"*50)
            numero=input("Ingrese numero de telefono: ")
            print("-"*50)
            if not numero.isdigit():
                print("Error,Ingrese un numero de telefono de tipo (string) ")
                continue
            return numero
        except:
            print("Error,Ingrese un numero de telefono")    
            
def sexo():
    while True:
        try:
            print("-"*50)
            sx=input("Ingrese su tipo de genero (Masculino/Femenino): ")
            print("-"*50)
            if sx.upper() == "MASCULINO" or sx.upper() == "FEMENINO":
                return sx
            else:
                print("Error,Digite un tipo de genero valido")
                continue
            
        except:
            print("Error,Ingrese un tipo de genero valido")   

def modificarClientes(dicClientes):
    if dicClientes=={} :
        ag=input("No se ha agregado ningun cliente, Desea agregarlo (Si/No) ?")
        if ag.upper() == "SI":
            dicClientes=agregarClientes(dicClientes)
            return dicClientes
        elif ag.upper() =="NO":
            return
        
    while True:
        flat=False
        try:
            print("-"*50)
            cedula=input("Ingrese numero de cedula: ")
            print("-"*50)
            for i in dicClientes.keys():
                if i == cedula:
                    flat=True
            if flat == False:
                print("Digite un numero de cedula valido")
                continue
            else:
                break
        except:
            print("Error,digite un numero de cedula valido")
    
    while True:
        try:
            print("""
\tModificar:
1.Nombre
2.Numero de Telefono
3.Sexo
                """)
            
            opcion=int(input("Ingrese su opcion a modificar: "))
            if opcion <1 or opcion >3:
                print("!Error¡,digite una opcion valida")
                continue
                        
            if opcion==1:
                name=nombre()
                dicClientes[cedula]["nombre"]=name
            elif opcion == 2:
                numeroTelef=numeroT()
                dicClientes[cedula]["numeroTelefono"]=numeroTelef
            elif opcion== 3:
                sx=sexo()
                dicClientes[cedula]["sexo"]=sx
            
            enviarClientes(dicClientes)
    
            return dicClientes
                      
        except ValueError:
            print("Error,digite un numero")

def eliminarClientes(dicClientes):
    if dicClientes=={} :
        ag=input("No se ha agregado ningun cliente, Desea agregarlo (Si/No) ?")
        if ag.upper() == "SI":
            dicClientes=agregarClientes(dicClientes)
            return dicClientes
        elif ag.upper() =="NO":
            return
    while True:
        flat=False
        try:
            print("-"*50)
            cedula=input("Ingrese numero de cedula: ")
            print("-"*50)
            for i in dicClientes.keys():
                if i == cedula:
                    flat=True
            if flat == False:
                print("Digite un numero de cedula valido")
                continue
            else:
                break
        except:
            print("Error,digite un numero de cedula valido")
    dicClientes.pop(cedula)
    enviarClientes(dicClientes)
    return dicClientes


def tarjetasCredito(dicTarjetas,dicClientes):
    
    if dicClientes=={}:
        ag=input("No se ha agregado ningun cliente, Desea agregarlo (Si/No) ?")
        if ag.upper() == "SI":
            agregarClientes(dicClientes)
            return
        elif ag.upper() =="NO":
            return

    while True:
        try:
            print("""
\tTarjetas de Credito:
1.Agregar
2.Modificar
3.Eliminar
4.Salir
                """)
            
            opcion=int(input("Ingrese su opcion: "))
            if opcion <1 or opcion >5:
                print("!Error¡,digite una opcion valida")
                continue
            
        except ValueError:
            print("Error,digite un numero")
        
        if opcion==1:
            dicTarjetas= agregarCredito(dicTarjetas,dicClientes)
        elif opcion == 2:
            dicTarjetas=modificarCredito(dicTarjetas)
        elif opcion== 3:
            dicTarjetas = eliminarCredito(dicTarjetas)
        elif opcion ==4:
            return dicTarjetas
        

def agregarCredito(dicTarjetas,dicClientes):
    tipoTarjeta=tipo()
    numCredito=numeroCredito(dicTarjetas)
    validez=validezMA()
    codiVeri=codigoVerificacion()
    idClient=idCliente(dicClientes)
    
    tipos=["Master Card","Visa","American Express"]
    
    dicTarjetas[numCredito]={}
    dicTarjetas[numCredito]["tipoTarjeta"]=tipos[tipoTarjeta-1]
    dicTarjetas[numCredito]["validez"]=validez
    dicTarjetas[numCredito]["codiVeri"]=codiVeri
    dicTarjetas[numCredito]["idCliente"]=idClient
    
    enviarTarjeta(dicTarjetas)
    
    return dicTarjetas   
    

def enviarTarjeta(dicTarjetas):
    with open("tarjetas.json","w+")as archivo:
        json.dump(dicTarjetas,archivo)

def tipo():
    while True:
        try:
            print("""
\t Tipo Tarjetas Credito
1.Masterd Card
2.Visa
3.American Express
                """)
            
            tipoTarjeta=int(input("Ingrese Tipo de Tarjeta de Credito: "))
            if tipoTarjeta <1 or tipoTarjeta >3:
                print("!Error¡,digite una opcion valida")
                continue
            return tipoTarjeta
        except ValueError:
            print("Error,digite un numero")
            
def numeroCredito(dicTarjetas):
    while True:
        flat=False
        try:
            print("-"*50)
            numCredito=input("Ingrese el numero tarjeta de credito: ")
            print("-"*50)
            if not numCredito.isdigit():
                print("Error,Ingrese un numero de tarjeta de tipo (entero)")
                continue
            for i in dicTarjetas.keys():
                    if i == numCredito:
                        print("numero de tarjeta ya registrada,registre una tarjeta diferente")
                        flat=True
            if flat==True:
                continue
            return numCredito
        except:
            print("Error,Ingrese un numero de tarjeta valido ")    

def validezMA():
    while True:
        cont=0
        flat=False
        res="no"
        try:
            print("-"*50)
            validez=input("Ingrese fecha de validez (mm/yyyy): ")
            print("-"*50)
            for i in validez:
                if i.isdigit():
                    cont+=1
                if cont ==2:
                    if i =="/":
                        res="si"
                if cont==6:
                    flat=True
                
            if flat== False or res=="no":
                print("Error,Digite este formato (mm/yyyy)")
            else:                
                return validez
        except:
            print("Error,ingrese una fecha valida")    

def codigoVerificacion():
    while True:
        try:
            print("-"*50)
            codiVeri=int(input("Ingrese codigo de verificacion (100/999): "))
            print("-"*50)
            if codiVeri < 100 or codiVeri > 999:
                print("Error,digite codigo de verificacion valido")
                continue
            return codiVeri
        except ValueError:
            print("Error,Digite un un numero de tres digitos para codigo de verificacion")    

def idCliente(dicClientes):
    while True:
        flat=False
        try:
            print("-"*50)
            idClien=input("Ingrese la cedula del cliente: ")
            print("-"*50)
            if not idClien.isdigit():
                print("Error,digite un numero de cedula")
                continue
            for i in dicClientes.keys():
                if i == idClien:
                    flat = True
            if flat== False:
                print("Digite un numero de cedula valido")
            else:
                return idClien
        except:
            print("Error,digite un numero de cedula") 

def modificarCredito(dicTarjetas):
    if dicTarjetas=={} :
        ag2=input("No se ha agregado ninguna tarjeta, Desea ingresarlo (Si/No) ?")
        if ag2.upper() == "SI":
            dicTarjetas=agregarCredito(dicTarjetas)
            return dicTarjetas
        elif ag2.upper() =="NO":
            return
        
    while True:
        flat=False
        try:
            numeroT=input("Ingrese numero de tarjeta: ")
            for i in dicTarjetas.keys():
                if i == numeroT:
                    flat=True
            if flat == False:
                print("Digite un numero de tarjeta valido")
                continue
            else:
                break
        except:
            print("Error,digite un numero de tarjeta valido")
    
    while True:
        try:
            print("""
\tModificar:
1.Tipo De Tarjeta De Credito
2.Mes Y Año De Validez
3.Codigo De Verificacion
                """)
            
            opcion=int(input("Ingrese su opcion a modificar: "))
            if opcion <1 or opcion >3:
                print("!Error¡,digite una opcion valida")
                continue
            
            tipos=["Master Card","Visa","American Express"]
            
            if opcion==1:
                tipoT=tipo()
                dicTarjetas[numeroT]["tipoTarjeta"]=tipos[tipoT-1]
            elif opcion == 2:
                validez=validezMA()
                dicTarjetas[numeroT]["validez"]=validez
            elif opcion== 3:
                codiV=codigoVerificacion()
                dicTarjetas[numeroT]["codiVeri"]=codiV
            
            enviarTarjeta(dicTarjetas)
            
            return dicTarjetas                
        except ValueError:
            print("Error,digite un numero")
        
        
            
def eliminarCredito(dicTarjetas):
    if dicTarjetas=={} :
        ag2=input("No se ha agregado ninguna tarjeta, Desea ingresarlo (Si/No) ?")
        if ag2.upper() == "SI":
            dicTarjetas=agregarCredito(dicTarjetas)
            return dicTarjetas
        elif ag2.upper() =="NO":
            return
        
    while True:
        flat=False
        try:
            numeroT=input("Ingrese numero de tarjeta: ")
            for i in dicTarjetas.keys():
                if i == numeroT:
                    flat=True
            if flat == False:
                print("Digite un numero de tarjeta valido")
                continue
            else:
                break
        except:
            print("Error,digite un numero de tarjeta valido")
    dicTarjetas.pop(numeroT)
    enviarTarjeta(dicTarjetas)
    return dicTarjetas



def informe(dicTarjetas,dicClientes):
    if dicClientes=={} :
        ag=input("No se ha agregado ningun cliente, Desea agregarlo (Si/No) ?")
        if ag.upper() == "SI":
            agregarClientes(dicClientes)
            return
        elif ag.upper() =="NO":
            return
    
    if dicTarjetas=={} :
        ag2=input("No se ha agregado ninguna tarjeta, Desea ingresarlo (Si/No) ?")
        if ag2.upper() == "SI":
            agregarCredito(dicTarjetas)
            return
        elif ag2.upper() =="NO":
            return
        
    while True:
        try:
            print("""
\tInforme::
1.Tarjetas de credito de un cliente
2.Informacion de una Tarjeta de credito
3.Listado de Tarjetas de Credito
4.Listado Clientes con Tarjetas de Credito
5.Cantidad de Tarjetas de cierto Tipo
                """)
            
            opcion=int(input("Ingrese su opcion: "))
            if opcion <1 or opcion >5:
                print("!Error¡,digite una opcion valida")
                continue
            break
        except ValueError:
            print("Error,digite un numero")
    if opcion==1:
        clienteTarjetas(dicTarjetas,dicClientes)
    elif opcion == 2:
        informacionTarjeta(dicTarjetas,dicClientes)
    elif opcion== 3:
        ListadoTarjetas(dicTarjetas,dicClientes)
    elif opcion==4:
        ListadoClientes(dicClientes,dicTarjetas)
    elif opcion == 5:
        cantidadTipo(dicTarjetas)


def clienteTarjetas(dicTarjetas,dicClientes):
    while True:
        flat=False
        try:
            cedula=input("Ingrese Cedula: ")
            for i in dicClientes.keys():
                if i == cedula:
                    flat=True
            if flat == False:
                print("Digite una cedula registrada en el sistema")
                continue
            else:
                break
        except:
            print("Error,digite un numero de tarjeta valido")
    print("-"*50)
    print("Nombre: ",dicClientes[cedula]["nombre"])
    print()
    cont=0
    for i in dicTarjetas.keys():
        if dicTarjetas[i]["idCliente"] == cedula:
            cont+=1
            print("\t",cont)
            print()
            print("Numero de Tarjeta Credito",i)
            print("Tipo de Tarjeta de Credito: ",dicTarjetas[i]["tipoTarjeta"])
            print("Año y Mes de Validez: ",dicTarjetas[i]["validez"])
            print("Codigo de Verificacion: ",dicTarjetas[i]["codiVeri"])
            print("ID Cliente:",dicTarjetas[i]["idCliente"])
            print("-"*80)


def informacionTarjeta(dicTarjetas,dicClientes):
    while True:
        flat=False
        try:
            numeroT=input("Ingrese numero de tarjeta de credito: ")
            for i in dicTarjetas.keys():
                if i == numeroT:
                    flat=True
            if flat == False:
                print("Digite un numero de tarjeta valido")
                continue
            else:
                break
        except:
            print("Error,digite un numero de tarjeta valido")
    print("-"*80)
    print("Numero de Tarjeta Credito",numeroT)
    print("Tipo de Tarjeta de Credito: ",dicTarjetas[numeroT]["tipoTarjeta"])
    print("Año y Mes de Validez: ",dicTarjetas[numeroT]["validez"])
    print("Codigo de Verificacion: ",dicTarjetas[numeroT]["codiVeri"])
    for i in dicClientes.keys():
        if i == dicTarjetas[numeroT]["idCliente"]:
            print("Cedula:",i)           
            print("Nombre:",dicClientes[i]["nombre"])
            print("numero de Telefono:",dicClientes[i]["numeroTelefono"])           
            print("sexo:",dicClientes[i]["sexo"])           
            print("-"*80)
   
def ListadoTarjetas(dicTarjetas,dicClientes):
    for i in dicTarjetas.keys():
        print("-"*80)
        print("Numero de Tarjeta Credito",i)
        print("Tipo de Tarjeta de Credito: ",dicTarjetas[i]["tipoTarjeta"])
        print("Año y Mes de Validez: ",dicTarjetas[i]["validez"])
        print("Codigo de Verificacion: ",dicTarjetas[i]["codiVeri"])
        print("Cedula del Cliente:",dicTarjetas[i]["idCliente"])
        for l in dicClientes.keys():
            if dicTarjetas[i]["idCliente"] == l:
                print("Nombre de Propietario:",dicClientes[l]["nombre"])
                print("-"*80)

def ListadoClientes(dicClientes,dicTarjetas):
        flat=True
        for i in dicClientes.keys():
            for l in dicTarjetas.keys():
                if i==dicTarjetas[l]["idCliente"]:
                    print("-"*80)
                    print("Cedula:",i)           
                    print("Nombre:",dicClientes[i]["nombre"])
                    print("numero de Telefono:",dicClientes[i]["numeroTelefono"])           
                    print("sexo:",dicClientes[i]["sexo"])           
                    print("-"*80)
                    flat= False
    
        if flat==True:
            print("Ningun cliente tiene tarjeta de credito")

def cantidadTipo(dicTarjetas):
    tipos=["Master Card","Visa","American Express"]
    master=0
    visa=0
    american=0
    for i in dicTarjetas.keys():
        if dicTarjetas[i]["tipoTarjeta"] == tipos[0]:
            master+=1
        elif dicTarjetas[i]["tipoTarjeta"] == tipos[1]:
            visa+=1
        elif dicTarjetas[i]["tipoTarjeta"] == tipos[2]:
            american+=1
    print("-"*80)
    print(f"Tarjetas Master Card: {master}")
    print(f"Tarjetas Visa: {visa}")
    print(f"Tarjetas American Express: {american}")
    print("-"*80)
    
            
def salir():
    flat=False
    return flat

dicClientes=cargarClientes()
dicTarjetas=cargarTarjeta()


flat=True

while flat==True:
    opcion=menu()
    
    if opcion==1:
        dicClientes=clientes(dicClientes)
    elif opcion == 2:
        dicTarjetas=tarjetasCredito(dicTarjetas,dicClientes)
    elif opcion== 3:
        informe(dicTarjetas,dicClientes)
    elif opcion==4:
        flat=salir()