""" Задача 5
Напишите программу, которая принимает на вход координаты
двух точек и находит расстояние между ними в 2D пространстве. """

from math import sqrt

def input_number (input_message):
    while True: 
        input_str = input(input_message)
        if is_float(input_str):
            return float(input_str)
        else:
            print('Вы ввели текст, а надо число')
            
def is_float(str):
    try:
        float(str)
        return True
    except ValueError:
        return False

print('Программа находит расстояние между двумя точками по координатам.')

xy_name_1 = ['X1', 'Y1']
xy_name_2 = ['X2', 'Y2']
xy_point_1 = [0,0] # X, Y
xy_point_2 = [0,0] # X, Y

for i in range(2):
    xy_point_1[i] = input_number(f'Введите координату {xy_name_1[i]}:')

for i in range(2):
    xy_point_2[i] = input_number(f'Введите координату {xy_name_2[i]}:')

interval = sqrt((xy_point_1[0]-xy_point_2[0])**2 + (xy_point_1[1]-xy_point_2[1])**2) 
interval = round(interval,3)
print(f'Расстояние между точками {xy_point_1} и {xy_point_2} = {interval}')