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
    print("4. Marcar Tareas Realizadas")
    print("5. Eliminar Tarea")
    print("6. Salir del programa")
    
##Función para mostrar la lista de Tareas
def lista():
    # Si aún no hay tareas
    if not tareas:
       print("No hay tareas (～￣▽￣)～")
       return
    
    ## Si hay tareas
    print( "\n   ID   |   ESTADO   |   TÍTULO   |   PRIORIDAD   |   FECHA DE REALIZACIÓN   |   FECHA LÍMITE   ")
    
    ## Recorrer cada campo de una tarea
    for t in tareas:
        estado = "OK " if t[2] else "NOT"
        ## Imprimir tarea en el orden ID ESTADO TÍTULO PRIORIDAD FECHA DE REALIZACIÓN Y FECHA LÍMITE
        print(f" {t[0]:>7}    |    {estado}     |    {t[1]}   |   {t[2]}   |   {t[3]}   |   {t[4]}   |   {t[5]}   |")
        

## Función para agregar una tarea
def agregar():
    ## Determinar nextId como variable global
    global nextId
    
    ## Colocar el título a la tarea
    ## función strip() para quitar los espacios que se añadan al título
    titulo = input("\nTítulo: ".strip())
    
    ## No se ingresa ningún título
    if not titulo:
        print("\n Título vacío →_→ ")
        return
    
    ## Colocar la prioridad de la tarea
    print("Ingrese la prioridad para la tarea")
    
    ## Agregar la tarea
    tareas.append([nextId, titulo, False])    
    ## Incrementar Id
    nextId += 1
    print("\n¡Tarea agregada con éxito! \(@^0^@)/")
    
    

## Función para marcar una tarea
def marcarTarea():
    # Si aún no hay tareas
    if not tareas:
       print("No hay tareas (～￣▽￣)～")
       return
   
   ## Verificar que la tarea a marcar tenga un ID Válido
    try:
       tId = int(input("\nIngrese el id de la tarea a marcar como realizada （*＾-＾*）").strip())    
    except ValueError:
        print("\nId inválido ┗|｀O′|┛")
        print("Por favor digíte valores numéricos...")
        return
    
    ## Recorrer cada campo de la tarea
    for t in tareas:
        ## Comparar si el id de la tarea es igual al id ingresado
        if t[0] == tId:
            ## Cambiar el estado de la tarea
            t[2] = True
            print("\n¡Tarea realizada!  (●'◡'●)")
            return
    ## si no existe el id que se ingresó
    print("\nNo existe el id ＞︿＜")    


## Función para eliminar una tarea
def eliminar():
    
    # Si aún no hay tareas
    if not tareas:
       print("No hay tareas (～￣▽￣)～")
       return
   
   ## Verificar que la tarea a marcar tenga un ID Válido
    try:
       tId = int(input("\nIngrese el id de la tarea que desea eliminar （*＾-＾*）\n-->").strip())    
    except ValueError:
        print("\nId inválido ┗|｀O′|┛")
        print("Por favor digíte valores numéricos...")
        return
    
    ## Recorrer cada tarea y cada campo de la tarea
    for i, t in enumerate(tareas):
         ## Comparar si el id de la tarea es igual al id ingresado
        if t[0] == tId:
            ## eliminar
            del tareas[i]
            print("\n¡Tarea eliminada con éxito! \(@^0^@)/")
            return
    ## si no existe el id que se ingresó
    print("\nNo existe el id a eliminar ＞︿＜")   
        

## Bucle para mostrar el menú al usuario
while (True):
    ## llamar la función menu
    menu()
    
    ## Pedir al usuario que digite una opción
    opcion = input("Digite una opción:  \n--> ").strip()
    
    ## Condicional dependiendo de la opción digitada
    if opcion == "1":
        ## llamar la función agregar
        agregar()
    
    elif opcion == "2":
        ## llamar la función lista
        lista()
        
    elif opcion == "3":
        ## llamar la función marcarTarea
        marcarTarea()
    
    elif opcion == "4":
        ## llamar la función eliminar
        eliminar()
    
    elif opcion == "5":
        print("\nHasta la próxima o(≧∀≦)o")
        ## Salir de bucle
        break
    ## Opción inválida
    else:
        print("\nLa opción ingresada no es válida ┗|｀O′|┛ ")
    
        
    
    
        
    
        