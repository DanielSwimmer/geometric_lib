# "Импортируем библиотеку math"
import math

def area(r):
    if type(r) != int and type(r) != float:
        raise TypeError
    if r < 0:
        raise ValueError
    else:
    # "Принимает число r, выводит произведение r на r на π"
        return math.pi * r * r

def perimeter(r):
    if type(r) != int and type(r) != float:
        raise TypeError
    if r < 0:
        raise ValueError
    else:
    # "Принимает число r, выдает произведение r на 2 на π"
        return 2 * math.pi * r
