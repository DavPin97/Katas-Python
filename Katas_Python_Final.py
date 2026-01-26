#1 Escribe una funcion que reciba una cadena de texto como parametro y devuelva un diccionario con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados.

texto = 'Cadena de prueba'

def frecuencia_letras(texto):

    diccionario_frecuencias = {}

    texto_sin_espacios = texto.replace(' ','').lower()

    for letra in texto_sin_espacios:

        if letra in diccionario_frecuencias:
            diccionario_frecuencias[letra] += 1
        else:
            diccionario_frecuencias[letra] =1

    return diccionario_frecuencias

conteo_letras = frecuencia_letras(texto)

print(conteo_letras)

#2 Dada una lista de numeros, obten una nueva lista con el doble del valor. Usa la funcion map()

lista_numeros = [1,2,3,4]

def doble(x):
    return x * 2

resultado = map(doble, lista_numeros)

print(list(resultado))

#3 Escribe una funcion que tome una lista de palabras y una palabra objetivo como parametros. 
# La funcion debe devolver una lista con todas las palabras de la lista original que contengan
# la palabra objetivo

lista_palabras = ['oscar','david','samuel','juan']

def buscar_palabra (palabra_objetivo, lista_palabras):

    lista_nueva =[]

    for palabra in lista_palabras:

        if palabra_objetivo in palabra:

            lista_nueva.append(palabra)

    return lista_nueva

listado_nuevo = buscar_palabra('david',lista_palabras)

print(listado_nuevo)

#4 Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()

lista1 = [2,4,6,8]

lista2 = [0,1,2,3]


def resta_lista(x, y):
    return x - y # Funcion para restar dos parametros

diferencia = map(resta_lista,lista1,lista2)

print(list(diferencia))

#5 Ecribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por defecto 
# es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual que nota aprobado. 
# Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver una tupla que contenga la media 
# y el estado.

lista_notas = [6,4,7,2,8]


def media(lista_notas, aprobado=5):

    
    media = sum(lista_notas) / len(lista_notas)

    if media < aprobado:
        estado = 'Suspenso'
    
    else:
        estado = 'Aprobado'
    
    return (media, estado)

media_notas = media(lista_notas)

print(media_notas)

#6 Escribe una función que calcule el factorial de un número de manera recursiva.

def factorial(n):

    if n == 0 or n == 1:
        return 1
    
    else:
        return n * factorial(n-1)

factorial2 = factorial(5)
print(factorial2) 

#7 Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()

lista_tuplas = [('rojo','azul'),('coche','casa')]

lista_string = list(map(lambda x:' '.join(x),lista_tuplas)) # Uso lambda para definir una funcion anonima para transformar de lista de tuplas a lista de strings

print(lista_string)

#8 Escribe un programa que pida al usuario dos números e intente dividirlos. 
# Si el usuario ingresa un valor no numérico o intenta dividir por cero, 
# maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje 
# indicando si la división fue exitosa o no.

try:
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))

    resultado = num1 / num2

except ValueError:
    print(" Error: Debes ingresar valores numéricos.")

except ZeroDivisionError:
    print(" Error: No se puede dividir por cero.")

else:
    print(f"División exitosa. El resultado es: {resultado}")

finally:
    print("Programa finalizado.")

#9 Escribe una función que tome una lista de nombres de mascotas como parámetro y 
# devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España. 
# La lista de mascotas a excluir es ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"].
# Usa la función filter()

mascotas = ['Gatos','Oso','Lagartos','Tigre','Hamsters','Cocodrilo','Loros']

mascotas_prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]

resultado = list(filter(lambda mascotas:mascotas not in mascotas_prohibidas, mascotas))

print(resultado)

#10 Escribe una función que reciba una lista de números y calcule su promedio. 
# Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente.

lista_numeros = [5,10,29,5]

def promedio (x):

    if len(x) == 0:
        return 'La lista esta vacia'
    else:
        media = sum(x)/len(x)

    return media

resultado = promedio(lista_numeros)

print(resultado)


#11 Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor
# no numerico o un valor fuera del rango esperado (menor que 0 o mayor que 120), maneja las excepciones adecuadamente

try:
    edad = float(input('Introduce tu edad'))

    if edad < 0 or edad > 120:
        print('Por favor inserte un numero entre 0 y 120')
    else:
        print('Su edad ha sido introducida correctamente')

except ValueError:
    print('Por favor inserte un valor numerico valido')

#12 Genera una funcion que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la funcion map()

frase = 'Me voy de vacaciones'

def longitud_palabras(palabra):
    return len(palabra)

lista_longitudes = list(map(longitud_palabras, frase.split()))
print(lista_longitudes)

#13 Genera una funcion la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra
#   en mayusculas y minusculas. Las letras no pueden estar repetidas. Usa la funcion map()

caracteres = 'Elefante'

def transformar(letra):
    return letra.upper(),letra.lower()

lista_tuplas = list(map(transformar,caracteres))
print(lista_tuplas)

#14 Crea una funcion que retorne las palabras de una lista de palabras que comience con una letra en especifico.
# Usa la funcion filter ()

lista_palabras = ['mantequilla','avion','esperpento','iglu','iglesia', 'amigo']

letra = 'a'

def primera_letra(palabra):
    return palabra[0] == letra.lower()

palabras_filtradas = list(filter(primera_letra,lista_palabras))

print(palabras_filtradas)

#15 Crea una funcion lambda que sume 3 a cada numero de una lista dada

numeros = [20,30,40,50,60]

suma = lambda x:x+3

print(list(map(suma,numeros)))

#16 Escribe una funcion que tome una cadena de texto y un numero entero n como parametro y devuelva una lista de 
# todas las palabras que sean mas largas que n. Usa la funcion filter()

texto = 'la semana que viene me voy de vacaciones'

n = 4

def longitud(palabra):
    return len(palabra) > n 

lista_filtrada = list(filter(longitud,texto.split()))
print(lista_filtrada)

#17 Crea una funcion que tome una lista de digitos y devuelva el numero correspondiente. Por ejemplo, [5,7,2] correspondiente
# al numero quinientos setenta y dos (572). Usa la funion reduce

from functools import reduce

lista = [ 5,7,2]

def concatenar_digitos(lista):
    return int(reduce(lambda x,y: str(x)+ str(y),lista))

print(concatenar_digitos(lista))

#18 Escribe un programa en Pyhton que cree una lista de diccionarios que contenga informacion de estudiantes
# (nombre,edad,calificacion) y use la funcion filter para extraer a los estudiantes con una calificacion mayor o igual a 90
# Usa la funcion filter()

estudiantes = [
    {'nombre':'Oscar','edad':30,'calificacion':91},
    {'nombre':'David','edad':28,'calificacion':99},
    {'nombre':'Samuel','edad':27,'calificacion':56},
    {'nombre':'Juan','edad':29,'calificacion':12}
]

estudiantes_aprobados = list(filter(lambda x:x['calificacion'] >= 90,estudiantes))

for estudiante in estudiantes_aprobados:
    print(f"El estudiante {estudiante['nombre']} ha obtenido una calificacion de {estudiante['calificacion']}")

#19 Crea una funcion lambda que filtre los numeros impares de una lista dada

lista = [2,3,4,5,6,7,8,9]

lista_impares = list(filter(lambda x: x % 2 != 0, lista))
print(lista_impares)

#20 Para una lista con elementos tipo integer y string obten una nueva lista solo con los valores int.
# usa la funcion filter()

lista = [3,'hola',6,'adios']

lista_int = list(filter(lambda x:isinstance(x,int),lista))
print(lista_int)

#21 Crea una funcion que calcule el cubo de un numero dado mediante una funcion lambda

numero_cubo = lambda x:x ** 3
print(numero_cubo(3))

## 22 Dada una lista numerica, obten el producto total de los valores de dicha lista. Usa la funcion reduce()

numeros = [2,4,6,8,10,12]

producto_numeros = reduce(lambda x,y:x * y,numeros)
print(producto_numeros)

#23 Concatena una lista de palabras. Usa la funcion reduce()

lista_palabras = ['quiero','aprobar','python']

concat = reduce(lambda x,y:x + ' ' + y, lista_palabras)
print(concat)

#24 Calcula la diferencia total en los valores de una lista. Usa la funcion reduce()

lista_numeros = [10,2,4,5]

diferencia_total = reduce(lambda x,y:x-y,lista_numeros)
print(diferencia_total)

#25 Crea una funcion que cuente el numero de caracteres en una cadena de texto dada

frase = 'Hola buenos dias'

def contar(caracteres):
    return len(caracteres.replace(' ','')) #se añade replace para no contar los espacios de la cadena de texto.

total_caracteres = contar(frase)
print(total_caracteres)

#26 Crea una funcion lambda que calcule el resto de la division entre dos numeros dados

resto = lambda x, y:x % y
print(resto(9,2))

#27 Crea una funcion que calcule el promedio de una lista de numeros

lista_numeros = [2,4,6,8,10,20,1,4]

def media(x):
    return sum(x) / len(x)

promedio = media(lista_numeros)
print(promedio)

#28 Crea una funcion que busque y devuelva el primer elemento duplicado en una lista dada

numeros = [1,2,3,4,5,6,6,7,8,9,9]

def duplicado(x):

    numeros_duplicados = []

    for numero in x:
        if numero in numeros_duplicados:
            return numero
        else:
            numeros_duplicados.append(numero)

primer_duplicado = duplicado(numeros)
print(primer_duplicado)

#29 Crea una funcion que convierta una variable en una cadena de texto y enmascare todos los caracteres
# con el caracter '#', excepto los ultimos cuatro

contraseña = '45337687'

def enmascarar(contraseña):
    longitud_contraseña = len(contraseña)
    ultimos_digitos = contraseña[-4:]  
    mascara = '#' * (longitud_contraseña - 4) 
    return mascara + ultimos_digitos  # Concatena la máscara y los últimos 4 caracteres

contraseña_enmascarada = enmascarar(contraseña)
print(contraseña_enmascarada)

#30 Crea una funcion que determine si dos palabras son anagramas, es decir, si estan formadas por las mismas letras en diferente orden

def anagrama (x,y):

    letras_x = sorted(x.lower())
    letras_y = sorted(y.lower())

    if letras_x != letras_y:
        return 'Las palabras no son anagramas'
    else:
        return 'Las palabras si son anagramas'

palabra1 = 'lobo'
palabra2 = 'bolo'
resultado = anagrama(palabra1,palabra2)
print(resultado)

#31 Crea una funcion  que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en esa lista. Si el nombre esta
# en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se lanza una excepcion.

def buscar_nombre():
    try:
        entrada_nombres = input('Introduce los nombres para el listado: ')
        listado_nombres = [nombre.strip() for nombre in entrada_nombres.split(',')]

        if not listado_nombres or listado_nombres == [""]:
            raise ValueError('El listado no puede estar vacío')

        nombre_buscado = input('Introduce el nombre que deseas buscar de la lista introducida: ').strip()

        if nombre_buscado in listado_nombres:
            print(f'El nombre {nombre_buscado} se ha encontrado en el listado introducido.')
        else:
            raise ValueError(f'El nombre {nombre_buscado} no se encuentra en el listado introducido.')

    except ValueError as e:
        print(f'Error: {e}')

buscar_nombre()

#32 Crea una funcino que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y devuelva
# el puesto del empleado si esta en la lista, de lo contrario, devuelve un mensaje indicando que la persona no trabaja aqui

empleados = [
    {'nombre': 'Alejandro', 'Puesto': 'RRHH'},
    {'nombre': 'David', 'Puesto': 'Manager'},
    {'nombre': 'Miguel', 'Puesto': 'Customer Service'},
    {'nombre': 'Jose', 'Puesto': 'CEO'}   
]

def buscador(empleado, listado):
    for nombre in listado:
        if nombre['nombre'] == empleado:
            return nombre['Puesto']
    
    return 'Este empleado no forma parte de la empresa'

print(buscador('David',empleados))

#33 Crea una funcion lambda que sume elementos correspondientes de dos listas dadas

lista1 = [2,4,6,8,10]
lista2 = [1,2,3,4,5]

suma_listas = list(map(lambda x,y: x + y,lista1,lista2))
print(suma_listas)

"""34 Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. 
Los métodos disponibles son: crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e info_arbol . 
El objetivo es implementar estos métodos para manipular la estructura del árbol.
 Código a seguir:
 1. Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
 2. Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad.
 3. Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
 4. Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.
 5. Implementar el método quitar_rama para eliminar una rama en una posición específica.
 6. Implementar el método info_arbol para devolver información sobre la longitud del tronco, el número de ramas y las longitudes de las mismas
Caso de uso:
 1. Crear un árbol.
 2. Hacer crecer el tronco del árbol una unidad.
 3. Añadir una nueva rama al árbol.
 4. Hacer crecer todas las ramas del árbol una unidad.
 5. Añadir dos nuevas ramas al árbol.
 6. Retirar la rama situada en la posición 2.
 7. Obtener información sobre el árbol.
"""
class Arbol():
    def __init__(self):
        self.tronco = 1
        self.ramas = []
    
    def crecer_tronco(self):
        self.tronco += 1
    
    def nueva_rama(self):
        self.ramas.append(1)

    def crecer_ramas(self):
        self.ramas = [rama + 1 for rama in self.ramas]

    def quitar_rama(self,indice):
        if 0 <= indice < len(self.ramas):
            del self.ramas[indice]
        else:
            return 'El índice no es válido'

    def info_arbol(self):  # Función para devolver información sobre el árbol
        return {
            'longitud_tronco': self.tronco,
            'numero_ramas': len(self.ramas),
            'longitud_ramas': self.ramas
        }


manzano = Arbol()
print('Árbol creado:', manzano.info_arbol())

manzano.crecer_tronco()
print('El tronco del árbol ha crecido:', manzano.info_arbol())

manzano.nueva_rama()
print('Ha crecido una nueva rama en tu árbol:', manzano.info_arbol())

manzano.crecer_ramas()
print('Las ramas de tu árbol han crecido:', manzano.info_arbol())

manzano.nueva_rama()
manzano.nueva_rama()
print('Han crecido 2 ramas nuevas en tu árbol:', manzano.info_arbol())

manzano.quitar_rama(1)  
print('Ha caído una rama de tu árbol:', manzano.info_arbol())

print('Tu árbol tiene las siguientes características:', manzano.info_arbol())



"""36 Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente. 
Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y agregar dinero al saldo.
 Código a seguir:
1 Inicializar un usuario con su nombre, saldo y si tiene o no cuenta corriente mediante True y False.
2 Implementar el método retirar_dinero para retirar dinero del saldo del usuario. Lanzará un error en caso de no poder hacerse.
3 Implementar el método transferir_dinero para realizar una transferencia desde otro usuario al usuario actual. Lanzará un error en caso de no poder hacerse.
4 Implementar el método agregar_dinero para agregar dinero al saldo del usuario.
 
 Caso de uso:
 1 Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
 2 Agregar 20 unidades de saldo de "Bob".
 3 Hacer una transferencia de 80 unidades desde "Bob" a "Alicia".
 4 Retirar 50 unidades de saldo a "Alicia"."""

class UsuarioBanco():
    def __init__(self, nombre, saldo, cuenta_corriente):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def retirar_dinero(self, cantidad_retirada):
        if not self.cuenta_corriente:
            return f'Error: {self.nombre} no tiene cuenta corriente y no puede retirar dinero.'
        
        if cantidad_retirada > self.saldo:
            return 'No hay saldo suficiente para realizar el retiro.'
        
        self.saldo -= cantidad_retirada
        return f'{self.nombre} ha retirado {cantidad_retirada}. Saldo actual: {self.saldo}'

    def transferir_dinero(self, usuario_transferir, cantidad_transferir):
        if not self.cuenta_corriente:
            return f'Error: {self.nombre} no tiene cuenta corriente y no puede transferir dinero.'
        
        if self.saldo < cantidad_transferir:
            return 'No se puede realizar la transferencia por saldo insuficiente.'

        self.saldo -= cantidad_transferir
        usuario_transferir.saldo += cantidad_transferir
        return (f'Se ha realizado una transferencia de {cantidad_transferir} de {self.nombre} a {usuario_transferir.nombre}. '
                f'Saldo actual de {self.nombre}: {self.saldo}. Saldo actual de {usuario_transferir.nombre}: {usuario_transferir.saldo}')

    def agregar_dinero(self, cantidad_ingreso):
        if cantidad_ingreso <= 0:
            return 'La cantidad a ingresar debe ser mayor a 0.'

        self.saldo += cantidad_ingreso
        return f'{self.nombre} ha ingresado {cantidad_ingreso}. Saldo actual: {self.saldo}'

#usuarios
usuario1 = UsuarioBanco('Alicia', 100, True)
usuario2 = UsuarioBanco('Bob', 50, True)


print(usuario2.agregar_dinero(20))       # Bob agrega 20 unidades
print(usuario2.transferir_dinero(usuario1, 80))  # Bob transfiere 80 unidades a Alicia
print(usuario1.retirar_dinero(50))       # Alicia retira 50 unidades

"""37. Crea una función llamada procesar_texto que procesa un texto según la opción especificada: reemplazar_palabras , contar_palabras , eliminar_palabra . 
Estas opciones son otras funciones que tenemos que definir primero y llamar dentro de la función procesar_texto. 
Código a seguir:
1 Crear una función contar_palabras para contar el número de veces que aparece cada palabra en el texto. Tiene que devolver un diccionario.
2 Crear una función reemplazar_palabras para reemplazar una palabra_original del texto por una palabra_nueva. Tiene que devolver el texto con el remplazo de palabras.
3 Crear una función eliminar_palabra para eliminar una palabra del texto.Tiene que devolver el texto con la palabra eliminada.
4 Crear la función procesar_texto que tome un texto, una opción(entre "contar", "reemplazar", "eliminar") y un número de argumentos variable según la opción indicada.
Caso de uso:
Comprueba el funcionamiento completo de la función procesar_texto"""

def contar_palabras(texto):
    palabras = texto.split()
    conteo = {}
    for palabra in palabras:
        if palabra in conteo:
            conteo[palabra] += 1
        else:
            conteo[palabra] = 1
    return conteo

def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    return texto.replace(palabra_original, palabra_nueva)

def eliminar_palabra(texto, palabra_eliminar):
    palabras = texto.split()
    texto_modificado = ' '.join([palabra for palabra in palabras if palabra != palabra_eliminar])
    return texto_modificado

def procesar_texto(texto,opcion, *args):
    if opcion == 'contar':
        return contar_palabras(texto)
    elif opcion == 'reemplazar' and len(args) == 2:
        palabra_original, palabra_nueva = args
        return reemplazar_palabras(texto, palabra_original, palabra_nueva)
    elif opcion == 'eliminar' and len(args) == 1:
        palabra_eliminar = args[0]
        return eliminar_palabra(texto, palabra_eliminar)
    else:
        return 'Error: No has ingresado los parámetros válidos para la función deseada.'
    
texto = 'Las tortugas van despacio y comen rapido'
print(procesar_texto(texto, 'contar'))
print(procesar_texto('reemplazar', texto, 'tortugas','vacas'))
print(procesar_texto('eliminar', texto, 'rapido'))






#38 Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.

hora_usuario = input("Introduce la hora actual en formato HH:MM:")


hora = int(hora_usuario[:2])

if 6 <= hora < 12:
    print(f'Es por la mañana, son las {hora_usuario}')
elif 12 <= hora < 19:
    print(f'Es por la tarde, son las {hora_usuario}')
else:
    print(f'Es por la noche, son las {hora_usuario}')







"""39  Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica. Las reglas de calificación son:
0 - 69 insuficiente
70 - 79 bien
80 - 89 muy bien
90 - 100 excelente"""

try:
    nota_examen = int(input('Por favor introduzca la nota obtenida en el examen: '))

    if 0 <= nota_examen <= 69:
        print(f'La nota obtenida en el examen es de {nota_examen} - Insuficiente')
    elif 70 < nota_examen <= 79:
        print(f'La nota obtenida en el examen es de {nota_examen} - Bien')
    elif 80 < nota_examen <= 89:
        print(f'La nota obtenida en el examen es de {nota_examen} - Muy bien')
    elif 90 < nota_examen <= 100:
        print(f'La nota obtenida en el examen es de {nota_examen} - Excelente')
    else:
        raise ValueError('El valor introducido no es valido como nota de examen')
    
except ValueError:
    print('Error; Introduzca un valor valido entre 0-100')

 




"""40 Escribe una función que tome dos parámetros: figura una cadena que puede ser "rectangulo" , "circulo" o "triangulo") y datos (una tupla con los datos necesarios para 
calcular el área de la figura)"""
import math

def calculo_area(figura, datos):
    if figura == 'rectangulo':
        if len(datos) != 2:
            return 'Para calcular el área de un rectángulo necesitas introducir la base y altura'
        base, altura = datos
        return base * altura

    elif figura == 'circulo':
        if len(datos) != 1:
            return 'Para calcular el área de un círculo necesitas introducir el valor del radio'
        radio = datos[0]
        return math.pi * (radio ** 2)
    
    elif figura == 'triangulo':
        if len(datos) != 2:
            return 'Para calcular el área de un triángulo necesitas introducir la base y altura'
        base, altura = datos
        return (base * altura) / 2
    else:
        return 'La figura indicada no se puede calcular'


print('El área del rectángulo es', calculo_area('rectangulo', (2, 5)))
print('El área del círculo es', calculo_area('circulo', (2,)))
print('El área del triángulo es', calculo_area('triangulo', (2, 5)))
  





"""41 En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el 
monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe hacer lo siguiente:
1. Solicita al usuario que ingrese el precio original de un artículo.
2. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no).
3. Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento.
4. Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido (es decir, mayor 
a cero). Por ejemplo, descuento de 15€. 
5. Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él. 
6. Recuerda utilizar estructuras de control de flujo como if, elif y else para llevar a cabo estas acciones en tu 
programa de Python"""

precio_articulo = float(input('Por favor ingresa el valor del artículo que deseas comprar: '))
activar_descuento = input('¿Tienes un cupón de descuento? (si/no): ').lower()

if activar_descuento == 'si':
    descuento_aplicable = float(input('Ingrese el valor del cupón que desea aplicar a su compra: '))
    
    if descuento_aplicable <= 0:
        print('El valor del cupón debe ser mayor que cero.')
    elif descuento_aplicable > precio_articulo:
        print('El descuento no puede ser mayor que el valor del artículo.')
    else:
        valor_articulo = round(precio_articulo - descuento_aplicable, 2)
        print(f'El valor final del artículo, después del descuento, es de {valor_articulo} €.')

elif activar_descuento == 'no':
    print(f'El valor del artículo es de {precio_articulo} €.')

else:
    print('Respuesta no válida. Por favor, ingrese "si" o "no".')