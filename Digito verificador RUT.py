"""
Programa de calculo del digito verificador de un RUT
"""

# Impresión por pantalla del mensaje de bienvenida.
print ("\n  ****************************************************")
print (" *                                                    *")
print ("* Bienvenido al calculo del digito verificador del RUT *")
print (" *                                                    *")
print ("  ****************************************************")

# Impresión por pantalla de las instrucciones como el usuario debe ingresar el RUT.
print ("\nIngresa el RUT sin puntos, guion y digito verificador:\n")
print ("Nota: Para que funccione con RUT de formato menor a 10.000.000 anteponer un 0\n")

# Con el (imput) recibimos los datos que fueron ingresados por el usuario y los
# guardamos en la variable (rut).
rut = input ("")

# Crearemos dos variables:
# 1) Variable (suma) y le asignamos el valor 0.
suma = 0
# 2) Variable (i) que vendría ser el coeficiente de multiplicación en el
#    proceso para los cálculos de validación. 
i = 2

# Mediante un ciclo (para o "for en Python") vamos a indicar que: para cada caracter en rango
# de 8 caracteres que contiene el RUT empezando por el ultimo (la función len) en la cadena (rut)
# moviéndonos de uno en uno haremos los siguiente:
for caracter in range(len(rut) - 1, - 1, - 1):
    # 1) Convertiremos cada carácter din cadena rut en un numero entero y lo guardaremos en la
    #    variable numero (como indicamos anteriormente se empezará por el ultimo digito hace al
    #    premier digito).
    numero = int(rut[caracter])
    # 2) Luego el numero entero guardado en variable (numero) lo multiplicaremos por la variable (i)
    #    que está guardando el coeficiente de validación y el resultado lo almacenamos en la
    #    variable (multiplicacion).
    multiplicacion = numero * i
    # 3) También en ciclo para, pondremos un si (if) con la condición mientras el valor que esta
    #    almacenado en la variable (i) sella distinto de 7 la cada pasada por la instrucción lo vamos
    #    a incrementar en 1.
    if i != 7:
        i = i + 1
    # 4) En caso contrario (else), si la variable (i) guarda el valor igual a 7 se asignara el
    #    valor de 2 nuevamente.
    else:
        i = 2
    # 5) Siguiendo dentro del ciclo para (for) realizaremos la operación matemática donde sumaremos
    #    a la variable suma con el valor de inicio 0 cada valor posterior que se formara en la variable
    #    (multiplicacion) y el resultado lo guardaremos en misma variable (suma). Propósito es que en cada
    #    iteración se venga acumulando para recibir la suma total de todas las multiplicaciones.
    suma = suma + multiplicacion

# Y por último cuando no tendremos más caracteres restantes en el ciclo para se sale din el ciclo
# calculando el residuo del valor almacenado en la variable suma dividido a 11.
residuo = suma % 11

# Posterior a esto procedemos con cálculo del digito verificador que es: 11 menos el residuo de la división
# almacenado en la variable (residuo) el resultado.
digi_verif = 11 - residuo

# Las dos condicionales a continuación se encargaran de intercambiar el valor ya que sabemos que si
# digito verificador es 10 se sustituirá con una "K" y si es 11 por un "0".
if digi_verif == 10:
    digi_verif = "K"
elif digi_verif == 11:
    digi_verif = 0

# Impresión por pantalla de los resultados obtenidos y agradecimientos.
print ("\n-----------------------------------------------------")
print ("|                                                   |")
print (f"|    Digito verificador del RUT: {rut} es: {digi_verif}     |")
print ("|                                                   |")
print ("-----------------------------------------------------\n")
print ("Gracias por validar el digito verificador con nosotros\n")
