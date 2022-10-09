# from funcs_for_hw4 import *
#
# arr1 = [6, 5, 4, 3, 2]
# arr2 = [7, 8, 9, 10, 11, 12]
#
# print(sum_arrs(arr1, arr2))
# print(sum_arrs2(arr1=arr2, arr2=arr1))


# 4.1. Напишите функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью кортежа):
#      периметр квадрата, площадь квадрата и диагональ квадрата.
#
# def square(n):
#     return (n * 4, n ** 2, n * (2 ** 0.5))
# print(square(2))
#
# def square(a):
#     p = lambda a: a * 4
#     s = lambda a: a * a
#     d = lambda a: ((a**2 + a**2)**0.5)
#     return p(a), s(a), d(a)
#
# print(square(2))
#
# 4.2. Напишите фукнцию, которая принимает произвольное количество именнованных аргументов и выводит их построчно
#      в формате аргумент: значение. Например:
# 	name: John
# 	last_name: Smith
# 	age: 35
# 	position: web developer
#
# def show_kwargs(**kwargs):
#     for key, value in kwargs.items():
#         print(f'{key}: {value}')
#
# show_kwargs(name = 'John', last_name= 'Smith', age= 35, position= 'web developer')
#
# 4.3. Используя лямбда-выражение, из списка my_list = [20, -3, 15, 2, -1, -21] создайте новый список, содержащий только
#      положительные числа
#
# my_list = [20, -3, 15, 2, -1, -21]
# new_lst = list(filter(lambda x: (x >= 0), my_list))
# print(new_lst)
#
# 4.4. Используя лямбда выражение, получите результат перемножения значений в предыдущем списке
#
# from functools import reduce
# my_list = [20, -3, 15, 2, -1, -21]
# new_lst = list(filter(lambda x: (x >= 0), my_list))
# summmm = reduce((lambda x, y: x * y), new_lst)
# print(summmm)
#
# 4.5. Создайте файл my_calc.py и пропишите в нем минимум 4 функции, выполняющие базовые арифметические вычисления.
#      Примените эти функции в качестве методов в другом файле.
import my_calc
print(my_calc.multi(2, 3))
print(my_calc.sum_args(2, 3, 4, 5, 5, 6))
print(my_calc.multi(5, 6))
print(my_calc.division(99, 0))

