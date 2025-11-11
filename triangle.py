def area(a, h):
    if type(a) != int and type(a) != float or type(h) != int and type(h) != float:
        raise TypeError()
    if a < 0 or h < 0:
        raise ValueError()
    else:
    # "Принимает числа a и h, выдает произведение a на h, деленное на 2"
        return a * h / 2 

def perimeter(a, b, c):
    if (type(a) != int and type(a) != float) or (type(b) != int and type(b) != float) or (type(c) != int and type(c) != float):
        raise TypeError()
    if a < 0 or b < 0 or c < 0:
        raise ValueError()
    elif (a + b <= c) or (a + c <= b) or (b + c <= a):
        raise ValueError()
    else:
    # "Принимает числа a, b, c, выдает сумму этих чисел"
        return a + b + c 