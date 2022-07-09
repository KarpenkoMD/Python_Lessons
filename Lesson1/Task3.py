""" Задача 3
Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 
и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится). """


def input_number (input_message):
    while True: 
        input_str = input(input_message)
        if is_int(input_str):
            return int(input_str)
        elif is_float(input_str):
            return float(input_str)
        else:
            print('Вы ввели текст, а надо число')
            
def is_float(str):
    try:
        float(str)
        return True
    except ValueError:
        return False

def is_int(str):
    try:
        int(str)
        return True
    except ValueError:
        return False

xy_name = ['X', 'Y']
xy_point = [0,0] # X, Y

print('Программа по координатам точки (X и Y) выдаёт номер четверти плоскости.')
for i in range(2):
    xy_point[i] = input_number(f'Введите координату {xy_name[i]}:')

if xy_point[0] == 0 and xy_point[1] == 0:
    print(f'Точка с координатами {xy_point} находится в нулевой точке координатной плоскости.')
elif xy_point[1] == 0:
    if xy_point[0] > 0:
        print(f'Точка с координатами {xy_point} находится на оси абсцисс правее оси ординат.')
    elif xy_point[0] < 0:
        print(f'Точка с координатами {xy_point} находится на оси абсцисс левее оси ординат.')
elif xy_point[0] == 0:
    if xy_point[1] > 0:
        print(f'Точка с координатами {xy_point} находится на оси ординат выше оси абсцисс.')
    elif xy_point[1] < 0:
        print(f'Точка с координатами {xy_point} находится на оси ординат ниже оси абсцисс.')
elif xy_point[0] > 0:
    if xy_point[1] > 0:
        print(f'Точка с координатами {xy_point} находится в 1й четверти.')
    elif xy_point[1] < 0:
        print(f'Точка с координатами {xy_point} находится в 4й четверти.')
elif xy_point[0] < 0:
    if xy_point[1] > 0:
        print(f'Точка с координатами {xy_point} находится в 2й четверти.')
    elif xy_point[1] < 0:
        print(f'Точка с координатами {xy_point} находится в 3й четверти.')