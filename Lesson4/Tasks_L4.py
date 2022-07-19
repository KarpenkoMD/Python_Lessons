import os
import my_method

str_to_lookup: str = 'Мама сши8ла мне штаны и7з бере9зовой кор45ы 893.'
file_name_to_operate: str = 'file.txt'

while True:
    os.system('cls||clear')
    print('Выберете номер задачи:\n\
        Задача 1 Вычислить число π c заданной точностью d.\n\
        Задача 2 выведет список неповторяющихся элементов исходной последовательности.\n\
        Задача 3 составит список простых множителей числа N.\n\
        Задача 4 текстовом файле удалить все слова, которые содержат хотя бы одну цифру.')
    print('Для выхода нажмите \'q\'')
    input_key = input()
    match input_key:
        case '1':
            accuracy = my_method.input_number('Введите точностью d для вычисления числа π: ','float')
            # list_numbers = my_method.list_random_fill(list_size,0,50)
            # sum_odd_elements = my_method.get_sum_odd_elements(list_numbers)
            output_result_string = (f'число π c заданной точностью {accuracy}')
            # + str(list_numbers)\  + ' равна ' + str(sum_odd_elements))
            break
        case '2':
            list_size = my_method.input_number('Введите количество элементов списка: ','natural')
            list_numbers = my_method.list_random_fill(list_size,0,10)
            # list_mult_pairs = my_method.mult_pair_elements(list_numbers)
            output_result_string = (f'В последовательности {list_numbers}\n')
            break
        case '3':
            number_N = my_method.input_number('Введите количество элементов списка: ','natural')
            # list_numbers = my_method.list_random_fill(list_size,1,10.0)
            # difference = my_method.min_max_fraction_difference(list_numbers)
            output_result_string = (f'Список простых множителей числа {number_N}\n')
            break
        case '4':
            ctr_sum = my_method.fill_file_with_text(file_name_to_operate, str_to_lookup)
            if ctr_sum != len(str_to_lookup):
                raise Warning(f'Ошибки записи в файл! {ctr_sum}')
            str_from_file = my_method.get_text_from_file(file_name_to_operate)
            str_result = my_method.check_words_in_string(str_from_file)
            # decimal_number = my_method.input_number(\
            #     'Введите десятичное число для перевода в двоичное: ','int')
            # str_binary_number = my_method.dec_to_bin(decimal_number)
            output_result_string = (f'Скаченная из файла строка: {str_from_file}\n' +
                f'обработанная строка, которая не содержит слов с цифрами: {str_result}')
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