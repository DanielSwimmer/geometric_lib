def area(a):
    if type(a) != int and type(a) != float:
        raise TypeError
    if a < 0:
        raise ValueError
    else:
    # "Принимает число a, выдает произведение a на a"
        return a * a

def perimeter(a):
    if type(a) != int and type(a) != float:
        raise TypeError
    if a < 0:
        raise ValueError
    else:
    # "Принимает число a, выдает произведение a на 4"
        return 4 * a
