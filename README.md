# Crear un programa que calcule el digito verificador del RUT Chileno:

## - Con lo aprendido hasta el momento, realiza un programa que de manera totalmente matemática (ocupando solo lo visto hasta el momento), muestre el digito verificador de un programa. El Rut ingresado debe ser un input que sea de largo 8 (sobre 10 millones) y una vez ingresado este número el programa deberá retornar un número del 1 al 11 (siendo simbólicamente el 10 la letra K y el 11 el número 0, pero esto no es importante que se muestren así).

***
## A continuacion dejare ejemplo del calculo:
***
- **Pasos a seguir para validar un Rut:**\
Se lee el número de derecha a izquierda y este se multiplica con números secuencias desde 2 a 7 y después se vuelven a repetir.

**Rut: 12140884-8**\
4 * 2 = 8\
8 * 3 = 24\
8 * 4 = 32\
0 * 5 = 0\
4 * 6 = 24\
1 * 7 = 7\
2 * 2 = 4\
1 * 3 = 3
- Posterior a obtener la multiplicación se suman los resultados de la multiplicación y se obtiene el resto de 11.

La suma seria 102, entonces calculamos el resto.\
102/11 = 9,272727272727
- Ocupamos el número natural.

11*9 = 99\
102 – 99 = 3\
**Entonces el resto es 3.**
**O calcular el resto en Python seria.**\
102%11 = 3
- Ahora una vez obtenido el resto, se toma 11 – el resto, y ese número es el digito verificador.

seria: 11-3 = 8\
Los resultados posibles son del **1 al 11**,\
si nos da el número **10 = k**,\
si nos da el número **11 = 0**.
***