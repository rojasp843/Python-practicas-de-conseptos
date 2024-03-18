# 1) Determinar si un número es par, impar o cero: Este ejercicio te permite
# ingresar un número y determinar si es par, impar o cero utilizando 
# estructuras de control condicionales.--------------------------------
ingrese_numero = 2
if (ingrese_numero==0):
    print ("numero 0 no es impar ni par")
elif (ingrese_numero %2==0):
    print("el numero es par")
else:
    print("el numero es impar")


# 2) Determinar si un número es positivo, negativo o cero: 
# En este ejercicio, podrás ingresar un número y el programa determinará 
# si es positivo, negativo o cero, nuevamente utilizando estructuras 
# condicionales.--------------------------------------------------------------------------
ingrese_numero = 2
if (ingrese_numero==0):
    print("numero es 0, no es ni positivo ni negativo")
elif (ingrese_numero>0):
    print (f"{ingrese_numero}numero es positivo")
else:
    print(f"{ingrese_numero}numero es negativo")  

#3) El programa evalúa el salario anual del usuario y realiza múltiples----------------------
# verificaciones anidadas. 
# Primero, verifica el nivel de ingresos.
# Segundo, Si el salario es alto, se procede a verificar el tiempo de empleo
# y luego el rendimiento laboral. 
# Tercero, Dependiendo de estas condiciones, se imprimen mensajes específicos y, 
# en algunos casos, se calcula un bono basado en el rendimiento.
#Datos de entrada:
#  ¿Cual es tu salario anual?
# "¿Cuántos años has estado empleado en la empresa actual?:
# ¿Cómo calificarías tu rendimiento laboral? (Excelente/Bueno/Regular): """)

# ¿Cual es tu salario anual?
salario_anual = 100
if (salario_anual>=100):
    print ("tienes un buen salario")
#¿Cuántos años has estado empleado en la empresa actual?
años_empleado = 10
if (años_empleado>=10):
    print("llevas mucho tiempo trabajando con nosotros")
elif (años_empleado<10):
    print("Llevas poco tiempo trabajando con nosotros,esperamos que sigas trabajando con nosotros mas años para recibir bebeficios exclusivos")
# ¿Cómo calificarías tu rendimiento laboral? (Excelente/Bueno/Regular)
rendimiento_laboral = "Exelente"
if (rendimiento_laboral=="Exelente"):
    print("Por tu sacrificio te vamos a dar un bono de $500")
elif (rendimiento_laboral=="Bueno"):
    print("Por tu sacrificio te vamos a dar un bono de $400")
elif (rendimiento_laboral=="Regular"):
    print("Esperamos mas de ti, se que puedes! para insentivarte te daremos un bono de $150")

exit()

# 4) Evaluación de nota académica: Este ejercicio evalúa una nota académica 
# y determina si el estudiante aprueba, va a recuperatorio o debe rendir 
# en marzo, utilizando estructuras de control condicionales.--------------------------------------------------------------------------
nota = 8
#-----------------------no es Python
if (nota >= 6):
    print ("nos vemos el año que viene")
else:
    print ("no aprobo")
    if (nota >= 4):
        print ("vas a recuperatorio")
    else: 
        print ("a marzo") 
#---------------------Sobre dimenciona (mal)
if (nota>=6):
    print("nos vemos el año que viene")
elif (nota>=4 and nota <6):
    print("vas a recuperatorio")
elif (nota<4):
    print("a marzo")
#---------------------Es Python ok
if (nota >=6):
    print("nos vemos el año que viene")
elif nota >= 4 :
    print ("vas a recuperatorio")
else:
    print ("a marzo")
#-------------------------------------------------------------------------


