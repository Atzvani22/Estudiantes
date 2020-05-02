def ordenar_edades():
  lista.sort()
  print (lista)

def Menu():

    print ("----------Bienvenido a Hogwarts-------------")
    print ("Escoge tus opciones")
    print ("1. Agregar alumnos")
    print ("2. Ordenar alumnos por genero")
    print ("3. Ordenar alumnos por edades")
    print ("4. Salir")

    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Escribe la opción que deseas: "))
            correcto=True
        except ValueError:
            print('Error, introduce otro numero')

    return num
salir = False
opcion = 0
nombre = 0
cont = 0
n = 0
borrar = 0

lista =[]
while not salir:

    opcion = Menu()

    if opcion == 1:
        print ("------Agregar alumnos----------")
        i = int(input("Cuantos alumnos quieres cargar:"))
        while nombre < i:
         edad = str(input("Dame la edad del alumno:"))
         genero = str(input("Dame el genero del alumno:"))
         Alumno= (edad + " " + genero);
         lista.append(Alumno)
         nombre=nombre + 1

        input("Los inquilinos cargados son:")
        print(lista)


    elif opcion == 3:
        print("---Alumnos ordenados por edades---")
        ordenar_edades()

    elif opcion == 4:
        salir = True


print ("Fin")
