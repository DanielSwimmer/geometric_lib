"""
Geometry Functions Module
Lab 4: Unit Testing
"""

import math

def rectangle_area(a: float, b: float) -> float:
    """
    Вычисляет площадь прямоугольника.
    
    Args:
        a (float): Длина первой стороны
        b (float): Длина второй стороны
        
    Returns:
        float: Площадь прямоугольника
        
    Raises:
        ValueError: Если стороны отрицательные
    """
    if a < 0 or b < 0:
        raise ValueError("Стороны прямоугольника не могут быть отрицательными")
    return a * b

def rectangle_perimeter(a: float, b: float) -> float:
    """
    Вычисляет периметр прямоугольника.
    
    Args:
        a (float): Длина первой стороны
        b (float): Длина второй стороны
        
    Returns:
        float: Периметр прямоугольника
        
    Raises:
        ValueError: Если стороны отрицательные
    """
    if a < 0 or b < 0:
        raise ValueError("Стороны прямоугольника не могут быть отрицательными")
    return 2 * (a + b)

def triangle_area(a: float, b: float, c: float) -> float:
    """
    Вычисляет площадь треугольника по формуле Герона.
    
    Args:
        a (float): Длина первой стороны
        b (float): Длина второй стороны
        c (float): Длина третьей стороны
        
    Returns:
        float: Площадь треугольника
        
    Raises:
        ValueError: Если стороны отрицательные или треугольник не существует
    """
    if a < 0 or b < 0 or c < 0:
        raise ValueError("Стороны треугольника не могут быть отрицательными")
    
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Треугольник с такими сторонами не существует")
    
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))

def triangle_perimeter(a: float, b: float, c: float) -> float:
    """
    Вычисляет периметр треугольника.
    
    Args:
        a (float): Длина первой стороны
        b (float): Длина второй стороны
        c (float): Длина третьей стороны
        
    Returns:
        float: Периметр треугольника
        
    Raises:
        ValueError: Если стороны отрицательные или треугольник не существует
    """
    if a < 0 or b < 0 or c < 0:
        raise ValueError("Стороны треугольника не могут быть отрицательными")
    
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Треугольник с такими сторонами не существует")
    
    return a + b + c

def circle_area(r: float) -> float:
    """
    Вычисляет площадь круга.
    
    Args:
        r (float): Радиус круга
        
    Returns:
        float: Площадь круга
        
    Raises:
        ValueError: Если радиус отрицательный
    """
    if r < 0:
        raise ValueError("Радиус не может быть отрицательным")
    return math.pi * r ** 2

def circle_perimeter(r: float) -> float:
    """
    Вычисляет длину окружности (периметр круга).
    
    Args:
        r (float): Радиус круга
        
    Returns:
        float: Длина окружности
        
    Raises:
        ValueError: Если радиус отрицательный
    """
    if r < 0:
        raise ValueError("Радиус не может быть отрицательным")
    return 2 * math.pi * r