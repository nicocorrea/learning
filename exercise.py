import itertools
from collections import deque
from collections import Counter
from collections import defaultdict
from dataclasses import dataclass
from collections import namedtuple
l1 = [1, 2, 3, 4]
l2 = [2, 3]
l3 = {1, 2, 3, 4}
l4 = {3, 5}
l5 = {1, 2, 3}
l6 = frozenset([1, 2, 3, 4])  # For a set that I don't want to make mutable

print(l3 & l4)  # 3
print(l3 | l4)  # {1, 2, 3, 4, 5}

print(l5 ^ l3)  # {4}
print(l5 < l3)  # True


def test(arg, result=[]):
    result.append(arg)
    return result


print(test('a'))  # ['a']
print(test('b'))  # Prints both 'a' and 'b'. List does not empty.


def test_dic(**kwargs):
    # Inside the signature of a function it packs the elements
    for key, value in kwargs.items():
        print(key, value)


test = dict(nombre='nico', apellido="correa")
# Using the ** outside the signature of a funtion is unpacking the elements
test_dic(**test)


def test_asterix(data: list, *, start=0, end=100):
    """This is a test docstring

    We just replace an element in a list

    Args:
        data: a list
        *: Good practice to state that if you don't define the next parameters
        you get the default
        start: (default: {0})
        end: (default: {100})
    """
    print(data[start:end])


lista = [1, 2, 3, 4, 5, 6, 7]

help(test_asterix)  # Outputs the docstring of the function


def knights(saying):
    def inner(quote):
        return f'We are the knights who say: {quote}'
    return inner(saying)


print(knights('Nil'))

#  Ejemplo de Closure


def multiplier_custom(multiplier):
    multiplier = multiplier

    def inner(arg1):
        return arg1 * multiplier
    return inner


por_tres = multiplier_custom(3)
print(por_tres(3))

#  Ejemplo de Lambda function


def a(x): return x + 3


print(a(4))


#  Ejemplo de Generator, which do not consume memory like lists

def my_range(first=0, last=10, step=1):
    number = first
    while number < last:
        yield number
        number += step


for x in my_range():
    print(x)

genobj = (alumno for alumno in zip(
    ['nicolas', 'fernando'], ['correa', 'alvarez izquierdo']))
for x in genobj:
    print(x)


#  Ejemplo de Decorators

def document_it(func):
    def new_function(*args, **kwargs):
        print('Running function: ', func.__name__)
        print('Positional arguments: ', args)
        print('Keyword arguments: ', kwargs)
        result = func(*args, **kwargs)
        print('Result: ', result)
        return result
    return new_function


def square_it(func):
    def new_function(*args, **kwargs):
        return func(*args) ** 2
    return new_function


@document_it
@square_it  # The decorator closest to the function runs first
def add_ints(a, b):
    return (a + b)


add_ints(3, 5, nombre='Nicolas')


#  Uso de global variables, hay que declararlas

animal = 'gato'


def change_gato():
    global animal
    animal += 'pepito'


print(animal)  # 'gato'
change_gato()
print(animal)  # 'gatopepito'


#  Usando Recursion para aplastart una lista

def flatten(lol):
    for item in lol:
        if isinstance(item, list):
            for subitem in flatten(item):
                yield subitem
        else:
            yield item


lol = [1, 2, [3, 4, 5], [6, [7, 8, 9], []]]
print(list(flatten(lol)))  # 1, 2, 3, 4, 5, 6, 7, 8, 9


#  Ejercicio para imprimir 'start' y 'end' con decorator
def decorator(func):
    def inner_function(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return inner_function


@decorator
def test():
    print('nicolas')


test()


# Ejercicio de crear tu propia exception, BASICO

class OopsException(Exception):
    pass


def test_exception():
    try:
        raise OopsException('Caught an oops')
    except OopsException as exp:
        print(exp)


test_exception()


class A():

    count = 0

    def __init__(self):
        A.count += 1

    def exclaim(self):
        print("I am A.")

    @classmethod
    def kids(cls):
        print("A has", cls.count, "little objects.")

    @staticmethod
    def type_of_class():
        print("My name is an alphabet letter.")

    def __str__(self):
        return 'I am __str__'

    def __repr__(self):
        return 'I am __repr__'


easy_a = A()
breezy_a = A()
wheezy_a = A()
A.kids()  # 'A has 3 little objects.'
A.type_of_class()

print(breezy_a)  # 'I am __str__'


#  Ejemplo de namedtuples


Pepe = namedtuple('Pepe', 'bill tail')
duck = Pepe('wide orange', 'long')
duck2 = Pepe(tail='short', bill='ioio')
print(duck)  # Pepe(bill='wide orange', tail='long')
print(duck2)  # Pepe(bill='ioio', tail='short')


#  Ejemplo de dataclasses, used to store data and not much behavior (method)


@dataclass
class AnimalClass:
    name: str
    habitat: str
    teeth: int = 0


snowman = AnimalClass('yeti', 'Himalayas', 46)
duck = AnimalClass(habitat='lake', name='duck')
print(snowman)  # AnimalClass(name='yeti', habitat='Himalayas', teeth=46)
print(duck)  # AnimalClass(name='duck', habitat='lake', teeth=0)


#  Ejercicio de capitulo 10

class Element():

    def __init__(self, name, symbol, number):
        self.__name = name
        self.__symbol = symbol
        self.__number = number

    def __str__(self):
        return self.name + self.symbol + str(self.number)

    @property
    def name(self):
        return self.__name

    @property
    def symbol(self):
        return self.__symbol

    @property
    def number(self):
        return self.__number


test = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}

example = Element(**test)
print(example)


class Laser():

    def does(self):
        return 'disintegrate'


class Claw():

    def does(self):
        return 'crush'


class Smartphone():

    def does(self):
        return 'ring'


class Robot():

    def __init__(self, laser, claw, smartphone):
        self.laser = laser
        self.claw = claw
        self.smartphone = smartphone

    def does(self):
        print(self.laser.does(), self.claw.does(), self.smartphone.does())


r = Robot(Laser(), Claw(), Smartphone())
r.does()


# Ejemplo de setdeafult() y defaultdict()

periodic_table = {'hydrogen': 1, 'helium': 2}
periodic_table.setdefault('carbon', 12)  # Agrega esta key-value

periodic_table.setdefault('helium', 450)
# Me devuelve el id de 'helium' que ya esta


periodic_table = defaultdict(int)
# int es una function que asigna 0 por default
periodic_table['helim'] = 1
periodic_table['prueba']
print(periodic_table)  # {'helim': 1, 'prueba': 0}

periodic_table = defaultdict(lambda: 'que?')
periodic_table['primero']
print(periodic_table)  # {'primero': 'que?'}

food_counter = defaultdict(int)
for food in ['papa', 'carne', 'carne']:
    food_counter[food] += 1

print(food_counter)
""" Si usabamos el diccionario normal Python hubiera levantado una exception en el primer food_counter[food] que no existe"""


# Ejemplo de Counter()


breakfast = ['spam', 'spam', 'eggs', 'spam']
breakfast_counter = Counter(breakfast)
print(breakfast_counter)
print(Counter('pepe'))

""" Similar a 'sets', puedo usar intersection (&) y union (|) entre Counters. """

# 's', porque me devuelta una lista con cada letra
print(deque('nicolas').pop())

for item in itertools.chain([1, 2], [5, 5]):
    print(item)
# 1, 2, 5, 5

# for item in itertools.cycle([1, 2, 3, 4]):
#    pass
    # print(item)
# 1, 2, 3, 4, 1, 2, 3, 4 ..... forever

for item in itertools.accumulate([1, 2, 3, 4]):
    print(item)
# 1, 2, 6, 10


def multiply(a: int, b: int) -> int:
    return a * b


for item in itertools.accumulate([1, 2, 2, 2], multiply):
    print(item)
#1, 2, 4, 8


# Ejemplo de random
from random import choice, sample, randint, random

ejemplo = ['pepe', 'nico', 1, 5, 20]
print(choice(ejemplo)) # Returns one element random
print(sample(ejemplo, 3))  # Returns 3 random elements from the list
print(randint(1, 5)) # Returns a number between 1 and 5
print(random()) # Returns a number from 0 to 1, in float


# Unicode

import unicodedata

def unicode_test(value):
    name = unicodedata.name(value)
    value2 = unicodedata.lookup(name)
    print(f'value={value}, name={name}, value2={value2}')

unicode_test('A')
# value=A, name=LATIN CAPITAL LETTER A, value2=A

unicode_test('\u00f2')
# value=ò, name=LATIN SMALL LETTER O WITH GRAVE, value2=ò

print(len('$'), len('\u00f3'))
# 1 1 because it counts UNICODE characters, not bytes


snowman = '\u2603'
print(len(snowman)) # 1
print(len(snowman.encode('utf-8'))) # 3, porque son bytes
print(type(snowman)) # 'str'
print(type(snowman.encode('utf8'))) # 'bytes'

""" Continue from page 306
"""