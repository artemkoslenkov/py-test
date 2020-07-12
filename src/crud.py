import numpy


def pick_rand():
    chars = ['a', 'b', 'c', 'd', 'e']

    items = [
        {
            'id': numpy.random.randint(1, 99),
            'offering': numpy.random.choice(chars),
            'seeking': numpy.random.choice(chars)
        },
    ]

    return numpy.random.choice(items)
