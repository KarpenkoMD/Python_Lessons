""" Задача 4 
Напишите программу, которая по заданному номеру четверти,
показывает диапазон возможных координат точек в этой четверти (x и y). """

def InputNumber (input_message):
    while True: 
        input_str = input(input_message)
        if input_str.isdigit():
            return int(input_str)
        else:
            print('Ошибка! Введите число!')
    
input_quarter = 0
print('Программа показывает диапазон возможных координат точек в четверти (x и y).')
while True: 
    input_quarter = InputNumber('Введите номер четверти:')
    if input_quarter >= 1 and input_quarter <= 4:
        break
    else:
        print('Ошибка! Четверть может быть 1, 2, 3 или 4!')

match input_quarter:
    case 1:
        print(f'В {input_quarter} четверти возможны значения координаты Х > 0 и Y > 0.')
    case 2:
        print(f'В {input_quarter} четверти возможны значения координаты Х < 0 и Y > 0.')
    case 3:
        print(f'В {input_quarter} четверти возможны значения координаты Х < 0 и Y < 0.')
    case 4:
        print(f'В {input_quarter} четверти возможны значения координаты Х > 0 и Y < 0.')
