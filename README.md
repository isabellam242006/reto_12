# reto_12
1. Consulte que hacen los siguientes métodos de strings en python: endswith, startswith, isalpha, isalnum, isdigit, isspace, istitle, islower, isupper.


**endswith:** Devuelve ```True``` si la cadena principal termina con una cadena como argumento.

**startswith**: 	Devuelve ```True``` si la cadena principal comienza con la que se pasa como argumento.

**isalpha:** Devuelve si la cadena es alfa.

**isalnum:** Devuelve si la cadena es alfanumérica.

**isdigit:**	Devuelve ```True``` si todos los caracteres son dígitos.

**isspace**: Devuelve ```True``` si todos los caracteres de la cadena son espacios.

**istitle**: Devuelve ```True``` si la cadena está en formato de título.

 **islower**: Devuelve ```True``` si todos los caracteres de la cadena estén en su forma minúscula.
 
 **isupper**: Devuelve  ```True ``` si todos los caracteres de la cadena estén en su forma mayúscula.

 Referencia: https://elpythonista.com/string-en-python

 2. Procesar el archivo y extraer:

- Cantidad de vocales

- Cantidad de consonantes

- Listado de las 50 palabras que más se repiten
  
  *Para este punto extraje un poema y lo guardé como un archivo json con el fin de analizarlo más a fondo*
```python
file = open("poema.txt", "w") #Con este código podremos crear el archivo
#El poema con tres comillas para que no hayan problemas con el salto de línea
poema = '''Mi táctica es  
Mirarte
Aprender como sos
Quererte como sos

Mi táctica es
Hablarte
Y escucharte
Construir con palabras
Un puente indestructible

Mi táctica es
Quedarme en tu recuerdo
No sé cómo ni sé
Con qué pretexto
Pero quedarme en vos

Mi táctica es
Ser franco
Y saber que sos franca
Y que no nos vendamos
Simulacros
Para que entre los dos
No haya telón
Ni abismos

Mi estrategia es
En cambio
Más profunda y más
Simple
Mi estrategia es
Que un día cualquiera
No sé cómo ni sé
Con qué pretexto
Por fin me necesite'''

file.write(poema)    #write para pasar el poema al archivo
file.close()         #Cierra el archivo
```
```python
#Código para contar la cantidad de vocales
def contar_vocales(poema):
    contador_vocales = 0
    for line in poema:
        for vocales in line:
            if vocales in "aeiouAEIOUáéíóúÁÉÍÓÚ":
                contador_vocales += 1
    return contador_vocales



if __name__ == "__main__":
    with open("poema.txt") as poema:
        poema = poema.read()
    total_vocales = contar_vocales(poema)
    print(f"El número de vocales en total es  {total_vocales}")
```
```python
#Código para contar la cantida de consonantes
def contar_consonantes(poema):
    contador_consonantes = 0
    for lineas in poema:
        for consonantes in lineas:
            if consonantes in "bcdfghjklmnñpqrstvwxyzBCDFGHJKLMNÑPQRSTVWXYZ":
                contador_consonantes+=1
    return contador_consonantes

if __name__ == "__main__":
    with open ("poema.txt") as poema:
        poema = poema.read()
    total_consonantes = contar_consonantes(poema)
    print(f"La cantidad de consonantes es {total_consonantes}")
```
