import math
'''Ejercicios integradores para revisar en la clase 7'''
# 1. Escribir una función que calcule el máximo común divisor entre dos números.
'''
def MCD():
    a = int(input('Introduce un número: '))
    b = int(input('Introduce otro número: '))
    result = math.gcd(a, b)
    return print('El Maximo Comun Divisor es: ', result)
MCD()
'''

# 2. Escribir una función que calcule el mínimo común múltiplo entre dos números
'''
def MCM():
    a = int(input('Introduce un número: '))
    b = int(input('Introduce otro número: '))
    result = math.lcm(a, b)
    return print('El Minimo Común Múltiplo es: ', result)
MCM()
'''

# 3. Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y la cantidad de veces que aparece (frecuencia).
'''
def frecuenciaPalabra():
    cadena = input('Ingrese una cadena de caracteres: ')
    palabras = cadena.lower().split()
    frec = {}
    for i in palabras:
        frec[i] = frec.get(i, 0) + 1
    return print(frec)
frecuenciaPalabra()
'''

# 4. Escribir una función que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y la cantidad de veces que aparece (frecuencia). Escribir otra función que reciba el diccionario generado con la función anterior y devuelva una tupla con la palabra más repetida y su frecuencia.
'''
def frecuenciaPalabra():
    cadena = input('Ingrese una cadena de caracteres: ')
    palabras = cadena.lower().split()
    frec = {}
    for i in palabras:
        frec[i] = frec.get(i, 0) + 1
    return print(frec)

def tuplaDic(frec):
    palabraMax = None
    frecuenciaMax = 0
    for palabra, frecuencia in frec.items():
        if frecuencia > frecuenciaMax:
            palabraMax = palabra
            frecuenciaMax = frecuencia
    return (palabraMax, frecuenciaMax)

frec = frecuenciaPalabra()
palabraMax, frecuenciaMax = tuplaDic(frec)
'''

# 5. Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una cadena de texto en su valor numérico, escriba una función get_int() que lea un valor entero del usuario y lo devuelva, iterando mientras el valor no sea correcto. Intente resolver el ejercicio tanto de manera iterativa como recursiva.

#Solucion iterativa
'''
def get_int():
    while True:
        try:
            num = int(input('Ingrese un numero entero: '))
            return num
        except ValueError:
            print('Error: el valor ingresado no es un numero entero valido.')
'''      
#Solucion recursiva
'''
def get_int():
    try:
        num = int(input('Ingrese un numero entero: '))            
        return num
    except ValueError:
        print('Error: el valor ingresado no es un numero entero valido.')
        return get_int()
'''

# 6. Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los siguientes métodos para la clase:
# - Un constructor, donde los datos pueden estar vacíos.
# - Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
#  mostrar(): Muestra los datos de la persona.
#  Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad.
'''
class Persona:
    def __init__(self, nombre='', edad=0, dni=0):
        self._nombre = nombre
        self._edad = edad
        self._dni = dni

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        if isinstance(nombre, str):
            self._nombre = nombre
        else:
            print('Error: El nombre tiene que ser una cadena de caracteres.')
    
    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self, edad):
        if isinstance(edad, int) and edad > 0:
            self._edad = edad
        else:
            print('Error: La edad debe ser un numero entero positivo.')
            
    @property
    def dni(self):
        return self._dni
    
    @dni.setter
    def dni(self, dni):
        if isinstance(dni, int) and len(str(dni)) == 8:
            self._dni = dni
        else:
            print('Error: El DNI debe ser una cadena de 8 caracteres numericos.')

    def mostrar(self):
        print(f'Nombre: {self._nombre} \nEdad: {self._edad} \nDNI: {self._dni}')
        
    def es_mayor_de_edad(self):
        if self.edad >= 18:
            return True
        else:
            return False
'''

# 7. Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es opcional. Crear los siguientes métodos para la clase:
# -  Un constructor, donde los datos pueden estar vacíos.
# - Los setters y getters para cada uno de los atributos. El atributo no se puede modificar directamente, sólo ingresando o retirando dinero.
# - mostrar(): Muestra los datos de la cuenta.
# - ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.
# - retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.

'''
class Cuenta:
    def __init__(self, titular, cantidad=0):
        self.__titular = titular
        self.__cantidad = cantidad
        
        @property
        def titular(self):
            return self.__titular
        
        @titular.setter
        def titular(self, titular):
            self.__titular = titular
        
        @property
        def cantidad(self):
            return self.__cantidad
        
        @cantidad.setter
        def cantidad(self, cantidad):
            self.__cantidad = cantidad
        
    def mostrar(self):
        print(f'Nombre: {self.__titular} \nSaldo: {self.__cantidad}')
    
    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__cantidad += cantidad
        
    def retirar(self, cantidad):
        self.__cantidad -= cantidad        
'''

# 8. Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase CuantaJoven que deriva de la clase creada en el punto 7. Cuando se crea esta nueva clase además del titular y la cantidad se debe guardar una bonificación que estará expresada en tanto por ciento. Crear los siguientes métodos para la clase:
# - Un constructor.
# - Los setters y getters para el nuevo atributo.
# - En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular es mayor de edad pero menor de 25 años y falso en caso contrario.
# - Además, la retirada de dinero sólo se podrá hacer si el titular es válido.
# - El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta.
'''
class Persona:
    def __init__(self, nombre='', edad=0, dni=0):
        self._nombre = nombre
        self._edad = edad
        self._dni = dni

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        if isinstance(nombre, str):
            self._nombre = nombre
        else:
            print('Error: El nombre tiene que ser una cadena de caracteres.')
    
    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self, edad):
        if isinstance(edad, int) and edad > 0:
            self._edad = edad
        else:
            print('Error: La edad debe ser un numero entero positivo.')
            
    @property
    def dni(self):
        return self._dni
    
    @dni.setter
    def dni(self, dni):
        if isinstance(dni, int) and len(str(dni)) == 8:
            self._dni = dni
        else:
            print('Error: El DNI debe ser una cadena de 8 caracteres numericos.')
            
            
class Cuenta:
    def __init__(self, titular, cantidad=0):
        self.__titular = titular
        self.__cantidad = cantidad
        
        @property
        def titular(self):
            return self.__titular
        
        @titular.setter
        def titular(self, titular):
            self.__titular = titular
        
        @property
        def cantidad(self):
            return self.__cantidad
        
        @cantidad.setter
        def cantidad(self, cantidad):
            self.__cantidad = cantidad
            
class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad, bonificacion):
        super().__init__(titular, cantidad=0)
        self.__bonificacion = bonificacion
        
        @property
        def bonificacion(self):
            return self.__bonificacion
'''