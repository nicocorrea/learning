l1 = [1, 2, 3, 4]
l2 = [2, 3]
l3 = {1, 2, 3, 4}
l4 = {3, 5}
l5 = {1, 2, 3}
l6 = frozenset([1, 2, 3, 4])  # For a set that I don't want to make mutable

print(l3 & l4)
print(l3 | l4)

print(l5 ^ l3)
print(l5 < l3)


def test(arg, result=[]):
    result.append(arg)
    return result


print(test('a'))
print(test('b'))


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


#  Ejemplo de Generator, which doesn't consume memory as lists since it only stores the last value

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


""" Page 217. """
