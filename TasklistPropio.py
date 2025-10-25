'''
TaskList propio de Natalia Osorio Oliveros para tareas diarias, con funciones como:
mostrar un menú 
mostrar lista de tareas
agregar tareas
editar tareas
marcar tareas
eliminar tareas
Salir del programa

'''

##importar el modulo locale para obtener el nombre de las fechas en español
import locale
locale.setlocale(locale.LC_TIME, "es_ES.UTF-8")

##Importar el módulo que trae la fecha y hora actual
from datetime import datetime


## Crear la lista de tareas
tareas = []

## Contandor incrementable para los ids, empezando con el número 1
nextId = 1 

## Función para mostrar el menú de las acciones que se pueden realizar dentro del programa
def menu():
    print("\n---- TaskList ヾ(≧▽≦*)o ----\n")
    print("1. Agregar Tarea")
    print("2. Editar Tarea")
    print("3. Lista de Tareas")
    print("4. Marcar Tareas Realizadas (cambiar estado de NOT a OK)")
    print("5. Eliminar Tarea")
    print("6. Salir del programa")
    
##Función para mostrar la lista de Tareas
def lista():
    # Si aún no hay tareas
    if not tareas:
       print("-------------------------") 
       print("No hay tareas (～￣▽￣)～")
       print("-------------------------") 
       return
    
    ## Si hay tareas
    print( "\n   ID   | ESTADO | TÍTULO | PRIORIDAD   | FECHA DE REALIZACIÓN   | FECHA LÍMITE   ")
    
    ##Contador para tareas realizadas y tareas que no
    tareasRealizadas = 0
    tareasNoRealizadas = 0
    ## Recorrer cada campo de una tarea
    for t in tareas:
        estado = "OK " if t[2] else "NOT"      
        ## Imprimir tarea en el orden ID ESTADO TÍTULO PRIORIDAD FECHA DE REALIZACIÓN  FECHA LÍMITE
        print(f"  {t[0]:<6}| {estado} | {t[1]} | {t[3]}  | {t[4]} | {t[5]}   ")

        ## Contabilizar cuántas tareas se han realizado y cuántas faltan por realizar
        if estado == "OK ":
            tareasRealizadas +=1 
        else:
            tareasNoRealizadas += 1
    
    ## Mostrar cuántas tareas se encuentran realizadas y cuántas no
    print(f"\n Tareas realizadas: {tareasRealizadas}")
    print(f" Tareas no realizadas: {tareasNoRealizadas}")
    print(f"\n ¡ÁNIMO, TÚ PUEDES! o(〃＾▽＾〃)o")
            
        
## Función para agregar una tarea
def agregar():
    ## Determinar nextId como variable global
    global nextId
    
    ## Colocar el título a la tarea
    ## función strip() para quitar los espacios que se añadan al título
    titulo = input("\nTítulo: ").strip()
    
    ## No se ingresa ningún título
    if not titulo:
        print("---------------------")
        print("\n Título vacío →_→ ")
        print("---------------------")
        return
    
    while True:
        ## Colocar la prioridad de la tarea
        print("\nIngrese el tipo de PRIORIDAD para la tarea: ")
        ## Función capitalize() para poner en mayúscula la primera letra de una cadena de texto y convertir todas las demás en minúsculas
        prioridad = input(" Alta \n Media \n Baja \n-->  ") .strip().capitalize()
        
        ## No se ingresa ninguna prioridad
        if not prioridad:
            print("\n Sin prioridad →_→ ")
            continue
        ## Si el usuario escribe una prioridad diferente
        elif prioridad not in ["Alta", "Media", "Baja"]:
            print("\nPrioridad no válida ┗|｀O′|┛")
            continue
        else:     
            break
    
    while True:
        ##Solicitar la fecha límite para realizar la tarea
        print("\n Por favor ingrese la FECHA LÍMITE para realizar la tarea:")
        fechaLimite = input(" Utilice el siguiente formato: Día(2 dígitos) de mes(escrito en letras) del año(4 digitos)  \n--> ").strip()
        
        ##Validar el formato de la fecha
        try:
            datetime.strptime(fechaLimite, "%d de %B del %Y")
            break
        
        except ValueError:
            print("\nFecha no válida ┗|｀O′|┛. Use Día(2 dígitos) de mes(escrito en letras) del año(4 digitos)  ")
            continue
    
    
    ## Agregar la tarea
    tareas.append([nextId, titulo, False, prioridad, None, fechaLimite ])    
    ## Incrementar Id
    nextId += 1
    print("\n¡Tarea agregada con éxito! \\(@^0^@)/")
    
## Función para validar si hay tareas y si se encuentra el ID de las tareas
def validarTareas():
    
     # Si aún no hay tareas
    if not tareas:
       print("-------------------------") 
       print("No hay tareas (～￣▽￣)～")
       print("-------------------------") 
       ## Retornar nada
       return None
   
    while True: 
        ## Función lista()
        lista()
    ## Verificar que la tarea a marcar tenga un ID Válido
        try:
            tId = int(input("\nIngrese el id: \n--> ").strip())   
            return tId
        except ValueError:
            print("\nId inválido ┗|｀O′|┛")
            print("Por favor digíte valores numéricos...")
            continue
    
## Función para editar una tarea
def editar():
     
    print("\n EDITAR TAREA o(*￣▽￣*)ブ")
    ## Validar Tareas y obtener el id
    tId = validarTareas()
    ## Si la función no retornó nada
    if tId is None:
        return 
    ## Recorrer cada tarea y cada campo de la tarea
    for i, t in enumerate(tareas):
         ## Comparar si el id de la tarea es igual al id ingresado
        if t[0] == tId:
            ## Mostrar la tarea correspondiente al ID
            print( "\n   ID   | ESTADO | TÍTULO | PRIORIDAD   | FECHA DE REALIZACIÓN   | FECHA LÍMITE   ")
            estado = "OK " if t[2] else "NOT" 
            print(f"  {t[0]:<6}| {estado} | {t[1]} | {t[3]}  | {t[4]} | {t[5]}   ")
            
            while True:
                ## Preguntar que se desea modificar de la tarea
                opcion = input("\nIngrese alguna de las siguientes opciones: \n 1. Editar Título \n 2. Editar Fecha Límite \n 3. Editar Prioridad \n--> ").strip()
                
                ## El usuario no ingresa ninguna opción
                if not opcion:
                    print("---------------------")
                    print("\nNo se ingresó ninguna opción →_→")
                    print("---------------------")
                    continue
                
                if opcion not in ("1", "2", "3"):
                    print("Por favor solo ingrese opciones validas ┗|｀O′|┛")
                    continue
                    
                ## Editar Título
                if opcion == "1":
                    nuevoTitulo = input("\nIngrese el título editado: \n--> ").strip()
                    ## Condicional por si el usuario ingresa o no título
                    if nuevoTitulo:
                        t[1] = nuevoTitulo
                        print("\n ¡Título editado con éxito! \\(@^0^@)/")
                        return
                    else:
                        print("---------------------")
                        print("\nTítulo vacío, no se realizaron cambios →_→")
                        print("---------------------")
                        break
                
                ## Editar fecha Límite
                elif opcion == "2":
                    ## Bucle para la fecha límite
                    while True:
                        ##Solicitar la fecha límite para realizar la tarea
                        print("\n Por favor ingrese la FECHA LÍMITE editada para realizar la tarea:")
                        nuevaFechaLimite = input(" Utilice el siguiente formato: Día(2 dígitos) de mes(escrito en letras) del año(4 digitos)  \n--> ").strip()
                        
                        ##Validar el formato de la fecha
                        try:
                            datetime.strptime(nuevaFechaLimite, "%d de %B del %Y")
                            if nuevaFechaLimite:
                                t[5] = nuevaFechaLimite
                                print("\n ¡Fecha Límite editada con éxito! \\(@^0^@)/")
                                return
                            else:
                                print("---------------------")
                                print("\nFecha límite vacía, no se realizaron cambios →_→")
                                print("---------------------")
                                return
                                 
                        except ValueError:
                            print("\nFecha no válida ┗|｀O′|┛. Use Día(2 dígitos) de mes(escrito en letras) del año(4 digitos)  ")
                            continue
                    
                
                ## Editar prioridad
                elif opcion == "3":
                    ## Bucle para validar la prioridad
                     while True:
                        ## Colocar la prioridad de la tarea
                        print("\nIngrese el nuevo tipo de PRIORIDAD para la tarea: ")
                        ## Función capitalize() para poner en mayúscula la primera letra de una cadena de texto y convertir todas las demás en minúsculas
                        nuevaPrioridad = input(" Alta \n Media \n Baja \n-->  ") .strip().capitalize()
                        
                        ## No se ingresa ninguna prioridad
                        if not nuevaPrioridad:
                            print("---------------------")
                            print("\n Prioridad vacía, no se realizaron cambios →_→ ")
                            print("---------------------")
                            continue
                        ## Si el usuario escribe una prioridad diferente
                        elif nuevaPrioridad not in ["Alta", "Media", "Baja"]:
                            print("\nPrioridad no válida ┗|｀O′|┛")
                            continue
                        else:
                            t[3] = nuevaPrioridad
                            print("\n ¡Prioridad editada con éxito! \\(@^0^@)/")  
                            return
            
                  
    ## si no existe el id que se ingresó
    print("\nNo existe el id a editar ＞︿＜")

## Función para marcar una tarea
def marcarTarea():
     
    print("\n MARCAR TAREA o(*￣▽￣*)ブ")
    ## Validar Tareas y obtener el id
    tId = validarTareas()
    ## Si la función no retornó nada
    if tId is None:
        return
    
    ## Recorrer cada campo de la tarea
    for t in tareas:
        ## Comparar si el id de la tarea es igual al id ingresado
        if t[0] == tId:
        ## Si la tarea ya está marcada como realizada
            if t[2]:
               print("\n¡Esta tarea ya está marcada como realizada! ✪ ω ✪")
               return 
            
            ## Cambiar el estado de la tarea
            t[2] = True
            print("\n¡Tarea realizada!  (●'◡'●)")
            
            ##Convertir las fechas de strings a objetos tipo datetime
            ## Agregar la fecha en que se realizó la tarea
            fechaRealizacion = datetime.now()
            ## Guardar la versión en texto
            t[4] = fechaRealizacion.strftime("%d de %B del %Y")
            
            fechaLimite_dt = datetime.strptime(t[5], "%d de %B del %Y")
            
            ## Comparación de fechas para mostrar un mensaje función .date() para comparar solo las fechas sin la hora
            if fechaRealizacion.date() <=  fechaLimite_dt.date():
                print("\n¡La tarea fue realizada a tiempo! \\(@^0^@)/")
                
            else:
                print("\nLa tarea fue realizada fuera de la fecha límite （︶^︶）")    
            return
        
    ## si no existe el id que se ingresó
    print("\nNo existe el id ＞︿＜")    
    

## Función para eliminar una tarea
def eliminar():
    
    print("\n ELIMINAR TAREA o(*￣▽￣*)ブ")
    ## Validar Tareas y obtener el id
    tId = validarTareas()
    ## Si la función no retornó nada
    if tId is None:
        return
    ## Recorrer cada tarea y cada campo de la tarea
    for i, t in enumerate(tareas):
        ## Comparar si el id de la tarea es igual al id ingresado
        if t[0] == tId:
            ## eliminar
            del tareas[i]
            print("\n¡Tarea eliminada con éxito! \\(@^0^@)/")
            return
    ## si no existe el id que se ingresó
    print("\nNo existe el id a eliminar ＞︿＜")   
        

## Bucle para mostrar el menú al usuario
while (True):
    ## llamar la función menu
    menu()
    
    ## Pedir al usuario que digite una opción
    opcion = input("\nDigite una opción:  \n--> ").strip()
    
    ## Condicional dependiendo de la opción digitada
    if opcion == "1":
        ## llamar la función agregar
        agregar()
    
    elif opcion == "2":
        ## llamar la función editar
        editar()
    
    elif opcion == "3":
        ## llamar la función lista
        lista()
    elif opcion == "3":
        ## llamar la función lista
        lista()
        
    elif opcion == "4":
        ## llamar la función marcarTarea
        marcarTarea()
    
    elif opcion == "5":
        ## llamar la función eliminar
        eliminar()
    
    elif opcion == "6":
        print("\nHasta la próxima o(≧∀≦)o")
        ## Salir de bucle
        break
    ## Opción inválida
    else:
        print("\nLa opción ingresada no es válida ┗|｀O′|┛ ")
    
        
    
    
        
    
        