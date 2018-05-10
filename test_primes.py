import itertools


def primes():

    """Реализуйте функцию-генератор primes, которая будет генерировать простые числа в порядке возрастания, 
    начиная с числа 2. """

    d = 2
    while 1:
        isSimple = True
        for i in range(2, d):
            if d % i == 0 and d != 2:
                isSimple = False
                break
        if isSimple:
            yield d
        d += 1


print(list(itertools.takewhile(lambda x : x <= 31, primes())))
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
