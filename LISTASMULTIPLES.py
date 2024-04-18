'''
Elaborar un programa en python utilizando multi listas y realiza las siguientes funciones:

1. Registrar candidadtos a una oportunidad de empleo el cual debe cumplir las sig cond
a. Edad 25-35
b. Profesión ING.SISTEMAS - ING INFORMATICO
c. Experiencia: 2 a 4 años

2. Consultar candidatos: Mostrar todos los candidatos

3. Información a capturar:
ls_identificacion, ls_experiencia, ls_profesion, ls_edad, ls_nombres, ls_correo, ls_contacto, ls_ciudad, ls_sexo
'''
ls_identificacion,ls_experiencia,ls_profesion,ls_edad,ls_nombres,ls_correo,ls_contacto,ls_ciudad,ls_sexo = [],[],[],[],[],[],[],[],[]
import os

def fnt_limpiar():
    os.system('cls')
    print('By: Menesex\nVersión 1.0\n')

def fnt_registrar(id,experiencia,profesion,edad,nombres,correo,contacto,ciudad,sexo):
    #a. Edad 25-35
    #b. Profesión ING.SISTEMAS - ING INFORMATICO
    #c. Experiencia: 2 a 4 años
    if id == '' or experiencia == '' or profesion == '' or edad == '' or nombres == '' or correo == '' or contacto == '' or ciudad == '' or sexo == '':
        input('ERROR: Porfavor rellene la totalidad de los datos <ENTER>')
    else:
        ls_identificacion.append(id)
        ls_experiencia.append(experiencia)
        ls_profesion.append(profesion)
        ls_edad.append(edad)
        ls_nombres.append(nombres)
        ls_correo.append(correo)
        ls_contacto.append(contacto)
        ls_ciudad.append(ciudad)
        ls_sexo.append(sexo)
        input('Candidato registrado éxitosamente <ENTER>')

def fnt_consultar():
    fnt_limpiar()
    sw2 = True
    while sw2 == True: #Menú de búsqueda
        fnt_limpiar()
        id = input('<<<MENÚ DE BÚSQUEDA>>>\n[0]Volver al menú principal\n[1]Todos los datos\n[2]Filtrar por id\n--> ')
        
        if id == '0': #salir
            sw2 = False
            
        elif id == '1':#Mostar todos los datos
            for i in range(len(ls_identificacion)):
                print(f'ID: {ls_identificacion[i]} | \tAños de experiencia: {ls_experiencia[i]} | \tProfesión: {ls_profesion[i]} | \tEdad: {ls_edad[i]} | \tNombres: {ls_nombres[i]} | \tCorreo: {ls_correo[i]} | \tContacto: {ls_contacto[i]} | \tCiudad: {ls_ciudad[i]} | \tSexo: {ls_sexo[i]} | \n')
            input('\nFin de la busqueda.. <ENTER>')
                
        elif id == '2': #Mostrar los datos según id
            id = input('ID a buscar: ')
            if id in ls_identificacion:
                indx = ls_identificacion.index(id)
                print(f'ID: {ls_identificacion[indx]} | \tAños de experiencia: {ls_experiencia[indx]} | \tProfesión: {ls_profesion[indx]} | \tEdad: {ls_edad[indx]} | \tNombres: {ls_nombres[indx]} | \tCorreo: {ls_correo[indx]} | \tContacto: {ls_contacto[indx]} | \tCiudad: {ls_ciudad[indx]} | \tSexo: {ls_sexo[indx]} | \n')
                input('<ENTER>')
            else:
                input('Identificación no regitrada.. <ENTER>')
                
        else:#Opción no válida
            input('Porfavor seleccione una opción válida.. <ENTER>')

def fnt_iniciarDatos():
    global ls_identificacion,ls_experiencia,ls_profesion,ls_edad,ls_nombres,ls_correo,ls_contacto,ls_ciudad,ls_sexo
    ls_identificacion = ['01','02','03','04','05']
    ls_experiencia = [2,2,3,4,3]
    ls_profesion = ['1','1','2','2','1']
    ls_edad = [25,32,27,35,30]
    ls_nombres = ['Juanito Perez','Antonio Jaramillo','Guillermo Hernandez','Sebastian Aguirre','Valentina Acevedo']
    ls_correo = ['Juanito@gmail','Antonio@gmail','Guillermo@gmail','Sebastian@gmail','Valentina@gmail',]
    ls_contacto = ['32138721','212321','331239','310342219','3138291287',]
    ls_ciudad = ['Apartadó','Turbo','Carepa','Chigordó','Medellín',]
    ls_sexo = ['Másculino','Másculino','Másculino','Másculino','Femenino']
    input('Lista inicializada correctamente (= ')
def fnt_selector(op):
    global sw
    if op == '0': #salir del programa
        sw = False
        
    elif op == '1': #Registrar candidato - (ENTRADA DE DATOS)
        fnt_limpiar()
        id = input('Identificación: ')
        
        if id in ls_identificacion: #validar id (¿registrada?)
            input('<ERROR> Candidato ya registrado')
            
        else:
            #validar si cumple con los requisitos..
            experiencia = int(input('Años de experiencia: '))
            profesion = input('Profesión\n[1]ING. Sistemas\n[2]ING. Informático\n[3]Otro\n--> ')
            edad = int(input('Edad: '))
            if((experiencia >= 2 and experiencia <= 4) and (profesion == '1' or profesion =='2') and (edad >= 25 and edad <=35)):
                #continuar pidiendo datos para terminar el registro
                nombres = input('Nombres y apellidos completos: ')
                correo = input('Correo: ')
                contacto = input('Contacto: ')
                ciudad = input('Ciudad: ')
                sexo = input('Sexo: ')
                fnt_registrar(id,experiencia,profesion,edad,nombres,correo,contacto,ciudad,sexo)
                
            else:
                input('<ERROR> El candidato no cumple con los requisitos')
            
    elif op == '2':
        fnt_consultar()
    elif op == '3':
        fnt_iniciarDatos()
    else:
        input('Porfavor ingrese una opción correcta.. <ENTER>')
           
sw = True
while sw == True:
    fnt_limpiar()
    op = input('<<MENU PRINCIPAL>>\n[0]Salir\n[1]Regitrar candidatos\n[2]Consultar candidatos\n[3]Rellenar listas con datos de prueba\n--> ')
    fnt_selector(op)
