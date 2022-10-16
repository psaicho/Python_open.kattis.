import random


def random_average(n):
    suma = 0
    for i in range(int(n)):
        suma += random.randint(1, 100)
    return suma/n


print(random_average(15))