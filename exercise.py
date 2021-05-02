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


easy_a = A()
breezy_a = A()
wheezy_a = A()
A.kids()  # 'A has 3 little objects.'
A.type_of_class()

""" I left at page 258. """
