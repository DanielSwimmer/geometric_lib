def area(a, b):
    if type(a) != int and type(a) != float or type(b) != int and type(b) != float:
        raise TypeError
    if a < 0 or b < 0:
        raise ValueError
    else:
    # "Принимает числа a и b, выдает произведение данных чисел"
        return a * b 

def perimeter(a, b):
    if type(a) != int and type(a) != float or type(b) != int and type(b) != float:
        raise TypeError
    if a < 0 or b < 0:
        raise ValueError
    else:
    # "Принимает числа a и b, выдает произведение суммы данных чисел на 2"
        return 2*(a + b) 