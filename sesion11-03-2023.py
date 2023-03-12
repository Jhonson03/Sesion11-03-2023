'''Crear un programa que solicite 4 notas obtenidas de un curso de
programacion y mediante una condicion simple mostrar si aprobó 
o desaprobó la materia (tener en cuenta que la nota promedio para 
aprobar es 6)'''


not1 = float(input("Ingrese su nota 1 -> "))
not2 = float(input("\nIngrese su nota 2 -> "))
not3 = float(input("\nIngrese su nota 3 -> "))
not4 = float(input("\nIngrese su nota 4 -> "))

promedio = (not1 + not2 + not3 + not4) / 4

#round() sirve para redondear a los decimales que se le declare

if promedio >= 6:
    print(f"\nUsted aprobo la materia con un promedio de {round(promedio, 2)}")
    # print("Usted aprobo la materia con un promedio de {}".format(promedio))
    # print("Usted aprobo la materia con un promedio de ", promedio)
    # print("Usted aprobo la materia con un promedio de "+ promedio)
    
else:
    print("\nNo aprobo el curso, su promedio fue de ", round(promedio, 2))
    
print("\nFin del Programa")

#----------------------------------------------------------------------------------------

#.lower() sirve para convertir toda cadena de caracteres o letras en minisculas
Fruta = input("Ingrese su fruta -> ").lower()

if Fruta == 'sandia':
    print("Usted eligio Sandia")