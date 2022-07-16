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
            list_size = my_method.input_number('Введите количество элементов списка: ','natural')
            list_numbers = my_method.list_random_fill(list_size,0,50)
            sum_odd_elements = my_method.get_sum_odd_elements(list_numbers)
            output_result_string = 'Сумма нечетных элементов списка ' + str(list_numbers)\
                 + ' равна ' + str(sum_odd_elements)
            break
        case '2':
            list_size = my_method.input_number('Введите количество элементов списка: ','natural')
            list_numbers = my_method.list_random_fill(list_size,0,10)
            list_mult_pairs = my_method.mult_pair_elements(list_numbers)
            output_result_string = 'Произведение пар чисел списка ' + str(list_numbers)\
                 + ' равно ' + str(list_mult_pairs)
            break
        case '3':
            list_size = my_method.input_number('Введите количество элементов списка: ','natural')
            list_numbers = my_method.list_random_fill(list_size,1,10.0)
            difference = my_method.min_max_fraction_difference(list_numbers)
            output_result_string = '\nРазница между максимальным и минимальным значением дробной части элементов списка\n'\
                + str(list_numbers) + '\nравна ' + str(difference)
            break
        case '4':
            decimal_number = my_method.input_number(\
                'Введите десятичное число для перевода в двоичное: ','int')
            binary_number = my_method.dec_to_bin(decimal_number)
            output_result_string = 'Десятичное число ' + str(decimal_number) +\
                 ' = ' + binary_number + ' в двоичном виде'
            break
        case '5':
            number = my_method.input_number(\
                'Введите число для ряда Фибоначчи: ','natural')
            output_result_string = 'Задача 5'
            break
        case 'q':
            input_key = None
            break
        case _:
            print('Ошибка ввода! Нажмите любую клавишу.')
            input()

if input_key != None:
    print(f'Результат {input_key} задачи:\
    {output_result_string}.\nДо свидания!')