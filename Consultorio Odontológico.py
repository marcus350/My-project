#Programa - trabajo final de promoción
#Materia:Algoritmos y estructura de datos
#Alumno: Marcos Ariel Argüello
#Sistema de gestión de un consultorio odontológico

#Área de funciones y TAD's
class turno():
    def __init__(self):
        self.turnos = []

    def carga_turnos(self):#carga de datos
            cod = input("Ingrese el código del turno: ")
            while not cod.isdigit():
                cod = input("Código inválido. Ingrese un número entero positívo: ")#validación del código
            cod = int(cod)
            while cod != 0:#variable de control: cod
                apel = input("Ingrese el apellido del paciente: ").capitalize()
                while apel.isdigit():
                    apel = input("Apellido inválido. Ingrese el apellido del paciente: ").capitalize()
                dni = input("Ingrese el DNI del paciente: ")
                while not dni.isdigit() or len(dni)<7 or len(dni)>8:
                    dni = input("DNI inválido. Ingrese un número entero: ")
                dni = int(dni)
                obso = input("Ingrese la obra social del paciente (OSDE/SWISS/PARTICULAR): ").upper()
                while obso not in ["OSDE", "SWISS", "PARTICULAR"]:
                    obso = input("Obra social inválida. Ingrese una obra social válida (OSDE/SWISS/PARTICULAR): ").upper()
                if obso=="OSDE":#el arancel para OSDE es 0
                    arancel=0
                elif obso=="SWISS":#el arancel para SWISS es 1500
                    arancel=1500
                else:#el arancel para PARTICULAR es 5000
                    arancel=5000
                print("Usted ha ingresdo la obra social",obso," entonces el arancel correspondiente es: ",arancel)
                dia = input("Ingrese la fecha del turno (dd/mm/aaaa): ")#validar el formato
                while len(dia) != 10 or dia[2] != "/" or dia[5] != "/" or not dia.replace("/", "").isdigit() or int(dia[0:2]) < 1 or int(dia[0:2]) > 31 or int(dia[3:5]) < 1 or int(dia[3:5]) > 12 or int(dia[6:]) < 2025:
                    dia = input("Formato o fecha inválidos. Ingrese la fecha en formato dd/mm/aaaa: ")
                hora = input("Ingrese la hora del turno (HH:MM): ")
                while len(hora) != 5 or hora[2] != ":" or not hora.replace(":", "").isdigit() or int(hora[0:2])<8 or int(hora[0:2])>17 or int(hora[3:5])<0 or int(hora[3:5])>59:
                    hora = input("Formato u hora inválida. Ingrese la hora en formato HH:MM entre las 08:00 y las 17:59: ")
                motivo = input("Ingrese el motivo del turno(consulta/arreglo/limpieza/extracción): ").capitalize()
                while motivo not in ["Consulta","Arreglo","Limpieza","Extracción","Extraccion"]:
                    motivo = input("Ingrese el motivo del turno(consulta/arreglo/limpieza/extracción): ").capitalize()
                prof = input("Ingrese el odontólogo con el que se va a atender (López/Perez): ").capitalize()
                if prof =="Lopez":
                    prof="López"
                while prof not in ["López","Lopez", "Perez"]:
                    prof = input("Opción no válida. Ingrese el odontólogo con el que se va a atender (López/Perez): ").capitalize()
                while any(t[5] == dia and t[6] == hora and t[8] == prof for t in self.turnos):#evaluar si hay o no un turno cargado previamente
                    print("Ya existe un turno asignado en esa fecha, hora y profesional.")
                    dia = input("Ingrese otra fecha del turno (dd/mm/aaaa): ")
                    while len(dia) != 10 or dia[2] != "/" or dia[5] != "/" or not dia.replace("/", "").isdigit() or int(dia[0:2]) < 1 or int(dia[0:2]) > 31 or int(dia[3:5]) < 1 or int(dia[3:5]) > 12 or int(dia[6:]) < 2025:
                        dia = input("Formato o fecha inválidos. Ingrese la fecha en formato dd/mm/aaaa: ")
                    hora = input("Ingrese una nueva hora del turno (HH:MM): ")
                    while len(hora) != 5 or hora[2] != ":" or not hora.replace(":", "").isdigit() or int(hora[0:2])<8 or int(hora[0:2])>17 or int(hora[3:5])<0 or int(hora[3:5])>59:
                        hora = input("Formato inválido. Ingrese la hora en formato HH:MM: ")
                    prof = input("Ingrese un nuevo profesional (López/Perez): ").capitalize()
                    if prof =="Lopez":
                        prof="López"
                    while prof not in ["Lopez","López", "Perez"]:
                        prof = input("Opción no válida. Ingrese el odontólogo (López/Perez): ").capitalize()
                paciente = [cod, apel, dni, obso, arancel, dia, hora, motivo, prof]
                self.turnos.append(paciente)
                cod = input("Ingrese el código de otro turno (0 para finalizar): ")
                while not cod.isdigit() or any(i[0]==int(cod) for i in self.turnos):
                    cod = input("Código inválido o ya ingresado. Ingrese un código válido: ")
                cod = int(cod)
            return self.turnos

    def mostrar_turnos(self):#Mostrar los turnos en pantalla
            for i in self.turnos:
                print(i)

    def nuevo_turno(self):#Crear un nuevo turno
        cod = input("Ingrese el código del turno: ")
        while not cod.isdigit() or cod=="0" or any(t[0] == int(cod) for t in self.turnos):#validar el código del turno, para que no se repita ni sea un str.
            cod = input("Código inválido o repetido. Ingrese un número positívo único: ")
        cod = int(cod)
        apel = input("Ingrese el apellido del paciente: ").capitalize()
        while apel.isdigit():#validar el apellido, para que no sea otra cosa que un str
            apel = input("Apellido inválido. Ingrese el apellido del paciente: ").capitalize()
        dni = input("Ingrese el DNI del paciente: ")
        while not dni.isdigit() or len(dni)<7 or len(dni)>8:
            dni = input("DNI inválido. Ingrese un número entero: ")
        dni = int(dni)
        obso = input("Ingrese la obra social del paciente(OSDE/SWISS/PARTICULAR): ").upper()
        while obso not in ["OSDE", "SWISS", "PARTICULAR"]:
            obso = input("Obra social inválida. Ingrese una obra social válida (OSDE/SWISS/PARTICULAR): ").upper()
        for i in self.turnos:
            if i[3]==obso:
                arancel=i[4]
        print("Usted ha ingresdo la obra social",obso,"entonces el arancel correspondiente es:",arancel)
        dia = input("Ingrese la fecha del turno (dd/mm/aaaa): ")
        while len(dia) != 10 or dia[2] != "/" or dia[5] != "/" or not dia.replace("/", "").isdigit() or int(dia[0:2]) < 1 or int(dia[0:2]) > 31 or int(dia[3:5]) < 1 or int(dia[3:5]) > 12 or int(dia[6:]) < 2025:
            dia = input("Formato o fecha inválidos. Ingrese la fecha en formato dd/mm/aaaa: ")
        hora = input("Ingrese la hora del turno (HH:MM): ")
        while len(hora) != 5 or hora[2] != ":" or not hora.replace(":", "").isdigit() or int(hora[0:2])<8 or int(hora[0:2])>17 or int(hora[3:5])<0 or int(hora[3:5])>59:
            hora = input("Formato u hora inválida. Ingrese la hora en formato HH:MM entre las 08:00 y las 17:59: ")
        motivo = input("Ingrese el motivo del turno(consulta/arreglo/limpieza/extracción): ").capitalize()
        while motivo not in ["Consulta","Arreglo","Limpieza","Extracción","Extraccion"]:
            motivo = input("Ingrese el motivo del turno(consulta/arreglo/limpieza/extracción): ").capitalize()
        prof = input("Ingrese el odontólogo con el que se va a atender (López/Perez): ").capitalize()
        if prof =="Lopez":
            prof="López"
        while prof not in ["Lopez","López", "Perez"]:
            prof = input("Opción no válida. Ingrese el odontólogo (López/Perez): ").capitalize()
        while any(t[5] == dia and t[6] == hora and t[-1] == prof for t in self.turnos):
            print("Ya existe un turno asignado en esa fecha, hora y profesional.")
            dia = input("Ingrese otra fecha del turno (dd/mm/aaaa): ")
            while len(dia) != 10 or dia[2] != "/" or dia[5] != "/" or not dia.replace("/", "").isdigit() or int(dia[0:2]) < 1 or int(dia[0:2]) > 31 or int(dia[3:5]) < 1 or int(dia[3:5]) > 12 or int(dia[6:]) < 2025:
                dia = input("Formato o fecha inválidos. Ingrese la fecha en formato dd/mm/aaaa: ")
            hora = input("Ingrese una nueva hora del turno (HH:MM): ")
            while len(hora) != 5 or hora[2] != ":" or not hora.replace(":", "").isdigit() or int(hora[0:2])<8 or int(hora[0:2])>17 or int(hora[3:5])<0 or int(hora[3:5])>59:
                hora = input("Formato inválido. Ingrese la hora en formato HH:MM: ")
            prof = input("Ingrese un nuevo profesional (López/Perez): ").capitalize()
            if prof =="Lopez":
                prof="López"
            while prof not in ["López", "Perez"]:
                prof = input("Opción no válida. Ingrese el odontólogo (López/Perez): ").capitalize()
        pacientenuevo = [cod, apel, dni, obso, arancel, dia, hora, motivo, prof]
        self.turnos.append(pacientenuevo)
        return self.turnos

    def cancelar(self):#Cancelar un turno
        cod=input("Ingrese el código del turno: ")
        while not cod.isdigit() or int(cod)==0:
            cod=input("Código inválido. Ingrese el código de un turno: ")
        for i in self.turnos:
            if i[0]==cod:
                self.turnos.remove(i)
        return self.turnos

    def modificar_turno(self):#Modificar día,hora o profesional de un turno
        menu = """
        Ingrese:
        1. para cambiar la fecha
        2. para cambiar la hora
        3. para cambiar al profesional
        """
        cod = input("Ingrese el código del turno: ")
        while not cod.isdigit() or cod == "0" or not any(int(cod) == t[0] for t in self.turnos):
            cod = input("Código inválido o no encontrado. Ingrese un número positivo: ")
        cod = int(cod)
        for i in self.turnos:
            if i[0] == cod:
                print(i)
                print(menu)
                preg = int(input("Opción: "))
                while preg not in [1, 2, 3]:
                    preg = int(input("Opción no válida. Por favor, ingrese una opción válida: "))
                dia = i[5]
                hora = i[6]
                prof = i[8]
                if preg == 1:
                    dia = input("Ingrese la nueva fecha del turno (dd/mm/aaaa): ")
                    while len(dia) != 10 or dia[2] != "/" or dia[5] != "/" or not dia.replace("/", "").isdigit() or int(dia[0:2]) < 1 or int(dia[0:2]) > 31 or int(dia[3:5]) < 1 or int(dia[3:5]) > 12 or int(dia[6:]) < 2025:
                        dia = input("Formato o fecha inválidoss. Ingrese la fecha en formato dd/mm/aaaa: ")
                elif preg == 2:
                    hora = input("Ingrese la nueva hora del turno (HH:MM): ")
                    while len(hora) != 5 or hora[2] != ":" or not hora.replace(":", "").isdigit() or int(hora[0:2])<8 or int(hora[0:2])>17 or int(hora[3:5])<0 or int(hora[3:5])>59:
                        hora = input("Formato u hora inválida. Ingrese la hora en formato HH:MM entre las 08:00 y las 17:59: ")
                elif preg == 3:
                    prof = input("Ingrese un nuevo profesional (López/Perez): ").capitalize()
                    while prof not in ["López", "Perez","Lopez"]:
                        prof = input("Opción no válida. Ingrese el odontólogo (López/Perez): ").capitalize()
                while any(t[0] != cod and t[5] == dia and t[6] == hora and t[8] == prof for t in self.turnos):
                    print("Ya existe un turno asignado en esa fecha, hora y profesional.")
                    dia = input("Ingrese otra fecha del turno (dd/mm/aaaa): ")
                    while len(dia) != 10 or dia[2] != "/" or dia[5] != "/" or int(dia[0:2]) < 1 or int(dia[0:2]) > 31 or int(dia[3:5]) < 1 or int(dia[3:5]) > 12 or int(dia[6:]) < 2025:
                        dia = input("Formato inválido. Ingrese la fecha en formato dd/mm/aaaa: ")
                    hora = input("Ingrese una nueva hora del turno (HH:MM): ")
                    while len(hora) != 5 or hora[2] != ":" or not hora.replace(":", "").isdigit() or int(hora[0:2])<8 or int(hora[0:2])>17 or int(hora[3:5])<0 or int(hora[3:5])>59:
                        hora = input("Formato inválido. Ingrese la hora en formato HH:MM: ")
                    prof = input("Ingrese un nuevo profesional (López/Perez): ").capitalize()
                    if prof =="Lopez":
                        prof="López"
                    while prof not in ["López", "Perez"]:
                        prof = input("Opción no válida. Ingrese el odontólogo (López/Perez): ").capitalize()
                i[5] = dia
                i[6] = hora
                i[8] = prof
        return self.turnos


    def arancel_nuevo(self):#Aumentar el arancel dependiendo de la obra social ingresada
        obso=input("Ingrese la obra social(OSDE/SWISS/PARTICULAR): ").upper()
        while obso not in ["OSDE", "SWISS", "PARTICULAR"]:
                    obso = input("Obra social inválida. Ingrese una obra social válida (OSDE/SWISS/PARTICULAR): ").upper()
        arancel=input("Ingrese el porcentaje de aumento del arancel: ")
        while not arancel.isdigit():
            arancel=input("Inválido. Ingrese el porcentaje de aumento del arancel: ")
        arancel=int(arancel)
        for i in self.turnos:
            if i[3]==obso:
                i[4]=i[4]+(i[4]*arancel)/100
        return self.turnos
    
    def arancel_cero(self):#Mostrar los turnos con aranceles 0
        aranceles0 = []
        for i in self.turnos:
            if i[4] == 0:
                aranceles0.append(i)
        return aranceles0

    def mayor_arancel(self):#Mostrar los turnos con mayores aranceles
        max = -999999
        mayor = []
        for i in self.turnos:
            if i[4] > max:
                max = i[4]
                mayor = [i]  
            elif i[4] == max:
                mayor.append(i)
        return mayor
    
    def perez(self):#Mostrar los turnos de Perez
        turnosperez=[]
        for i in self.turnos:
            if i[-1]=="Perez":
                turnosperez.append(i)
        return turnosperez
    
    def lopez(self):#Mostrar los turnos de López
        turnoslopez=[]
        for i in self.turnos:
            if i[-1]=="López" or i[-1]=="Lopez":
                turnoslopez.append(i)
        return turnoslopez
    
    def mod_datos(self):#Modificar los datos de un paciente
        cod = input("Ingrese el código del turno: ")
        while not cod.isdigit() or cod == "0" or not any(int(cod) == t[0] for t in self.turnos):
            cod = input("Código inválido o no encontrado. Ingrese un número positivo: ")
        cod = int(cod)
        for i in self.turnos:
            if i[0] == cod:
                apel = input("Ingrese el apellido del paciente: ").capitalize()
                while apel.isdigit():
                    apel = input("Apellido inválido. Ingrese el apellido del paciente: ").capitalize()
                dni = input("Ingrese el DNI del paciente: ")
                while not dni.isdigit() or len(dni)<7 or len(dni)>8:
                    dni = input("DNI inválido. Ingrese un número entero: ")
                dni = int(dni)
                obso = input("Ingrese la obra social del paciente (OSDE/SWISS/PARTICULAR): ").upper()
                while obso not in ["OSDE", "SWISS", "PARTICULAR"]:
                    obso = input("Obra social inválida. Ingrese una obra social válida (OSDE/SWISS/PARTICULAR): ").upper()
                arancel = None
                for t in self.turnos:
                    if t[3] == obso:
                        arancel = t[4]
                if arancel is None:
                    arancel = 0  
                i[1] = apel
                i[2] = dni
                i[3] = obso
                i[4] = arancel

        return self.turnos

#Programa principal
print("Bienvenido al Consultorio Odontológico Sonrisas Felices")
print()
turnosasig=turno()
turnosasig.carga_turnos()
print()
turnosasig.mostrar_turnos()
print()
menu="""
1.Asignar nuevo turno
2.Cancelar turno
3.Modificar la fecha, hora o profesional de un turno
4.Aumentar el arancel de un turno por la obra social
5.Mostrar turnos cuyo arancel es 0
6.Mostrar turnos con mayores aranceles
7.Mostrar todos los turnos de Perez
8.Mostrar todos los turnos de Lopez
9.Modificar datos de un paciente
10.Salir
"""
print(menu)
opcion=int(input("Ingrese una opción del menú: "))
while (opcion!=10):
    if opcion==1:
        nuevo=turnosasig.nuevo_turno()
        turnosasig.mostrar_turnos()
        print(menu)
    elif opcion==2:
        turnosasig.mostrar_turnos()
        print(turnosasig.cancelar())
        turnosasig.mostrar_turnos()
        print(menu)
    elif opcion == 3:
        turnosasig.mostrar_turnos()
        turnosasig.modificar_turno()
        turnosasig.mostrar_turnos()
        print(menu)
    elif opcion==4:
        print(turnosasig.arancel_nuevo())
        turnosasig.mostrar_turnos()
        print(menu)
    elif opcion==5:
        turnos_cero = turnosasig.arancel_cero()
        for t in turnos_cero:
            print(t)
        print(menu)
    elif opcion==6:
        print(turnosasig.mayor_arancel())
        print(menu)
    elif opcion==7:
        for i in turnosasig.perez():
            print(i)
        print(menu)
    elif opcion==8:
        for i in turnosasig.lopez():
            print (i)
        print(menu)
    elif opcion==9:
        for i in turnosasig.mod_datos():
            print(i)
        print(menu)
    else:
        print("Usted ha ingresado una opción no válida")
        print(menu)
    opcion=int(input("Ingrese una opción del menú: "))
print("Fin del programa")
print("Gracias por usar el programa")
