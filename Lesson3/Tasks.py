import os
import my_method


while True:
    os.system('cls||clear')
    print('Выберете номер задачи.\n\
        Задача 1 найдёт сумму элементов списка, стоящих на нечётной позиции.\n\
        Задача 2 найдёт произведение пар чисел списка.\n\
        Задача 3 найдёт разницу между максимальным и минимальным значением дробной части элементов списка.\n\
        Задача 4 будет преобразовывать десятичное число в двоичное.\n\
        Задача 5 составит список чисел Фибоначчи, в том числе для отрицательных индексов.\n')
    print('Для выхода нажмите \'q\'')
    input_key = input()
    match input_key:
        case '1':
            n = my_method.input_number('Введите число')
            result_string = 'Задача 1'
            break
        case '2':
            result_string = 'Задача 2'
            break
        case '3':
            result_string = 'Задача 3'
            break
        case '4':
            result_string = 'Задача 4'
            break
        case '5':
            result_string = 'Задача 4'
            break
        case 'q':
            input_key = None
            break
        case _:
            print('Ошибка ввода! Нажмите любую клавишу.')
            input()

if input_key != None:
    print(f'Результат {input_key} задачи:\
    {result_string}.\nДо свидания!')