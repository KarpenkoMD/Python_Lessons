import os
import my_method

str_to_lookup: str = 'Мама сшила м0не штаны и7з бере9зовой кор45ы 893'
file_name_to_operate: str = 'file.txt'

while True:
    os.system('cls||clear')
    print('Выберете номер задачи:\n\
        Задача 1 определит, присутствует ли в заданном списке строк, некоторое число.\n\
        Задача 2 найдет сумму чисел списка стоящих на нечетной позиции.\n\
        Задача 3 найдет расстояние между двумя точками пространства.\n\
        Задача 4 определит позицию второго вхождения строки в списке либо сообщить, что её нет.\n\
        Задача 5 найдет произведение пар чисел в списке..\n\
        Задача 6 выведет список из N членов последовательности. Для N = 5: 1, -3, 9, -27, 81.')
    print('Для выхода нажмите \'q\'')
    input_key = input()
    match input_key:
        case '1':
            accuracy = my_method.input_number('Введите точностью d для вычисления числа π: ','str_float')
            pi = my_method.pi_round(accuracy)
            output_result_string = ('\nЧисло π c заданной точностью\t{0}\n\
                 \rРавно\t\t\t\t{1}'.format(accuracy,pi))
            break
        case '2':
            list_size = my_method.input_number('Введите количество элементов списка: ','natural')
            list_numbers = my_method.list_random_fill(list_size,0,10)
            list_unique_elements = my_method.find_unique_elements(list_numbers)
            output_result_string = (f'\nВ последовательности: {list_numbers}\n\
                \rУникальные элементы: {list_unique_elements}')
            break
        case '3':
            number_N = my_method.input_number('Введите число N для составления списка простых множителей: ','natural')
            list_factors = my_method.get_factors_list(number_N)
            list_unique_factors = my_method.find_unique_elements(list_factors )
            output_result_string = (f'Список простых множителей числа {number_N} равен {list_factors },\n\
                \rа список уникальных множителей выглядит так {list_unique_factors}')
            break
        case '4':
            ctr_sum = my_method.fill_file_with_text(file_name_to_operate, str_to_lookup)
            if ctr_sum != len(str_to_lookup):
                raise Warning(f'Ошибки записи в файл! {ctr_sum}')
            str_from_file = my_method.get_text_from_file(file_name_to_operate)
            str_result = my_method.check_words_in_string(str_from_file)
            output_result_string = (f'Скаченная из файла строка: {str_from_file}\n' +
                f'обработанная строка, которая не содержит слов с цифрами: {str_result}')
            break
        case '5':
            break
        case '6':
            break
        case 'q':
            input_key = None
            break
        case _:
            print('Ошибка ввода! Нажмите любую клавишу.')
            input()

if input_key != None:
    print(f'Результат {input_key} задачи:\
    {output_result_string}\nДо свидания!')