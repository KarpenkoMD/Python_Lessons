from gc import garbage
import os
from my_method import*

garbage_str = 'абв'

while True:
    os.system('cls||clear')
    print('Выберете номер задачи:\n\
        Задача 1 Удаляющую из текста все слова, содержащие ""абв"".\n\
        Задача 2 - игра с конфетами.\n\
        Задача 3 Создайте два списка — один с названиями языков программирования, другой — с числами от 1 до длины первого.\n\
        Задача 4 Реализуйте RLE алгоритм.')
    print('Для выхода нажмите \'q\'')
    input_key = input()
    match input_key:
        case '1':
            str_form_file = get_text_from_file('Lesson5/test_file_task1.txt')
            # str_form_file  = str_form_file .lower()
            words_list = list(map(str,(str_form_file .lower()).split()))
            words_list = [words_list[i] for i in range(len(words_list)) \
                if words_list[i].find(garbage_str) == -1 ]
            output_result_string = (f'\nРезультат выборки слов без \'{garbage_str}\' и из строки {str_form_file}:\n\
                \b{words_list}')
            break
        case '2':
            words_number = input_number('Введите количество слов в строке: ')

            output_result_string = (f'Выиграл игрок: ')
            break
        case '3':
            result_list = ''
            output_result_string = (f'Список  {result_list}')
            break
        case '4':
            encrypted_str = ''
            decrypted_str = ''

            output_result_string = (f'Зашифрованная строка: {encrypted_str}\n\
                \rРасшифрованная строка: {decrypted_str}')
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
    fill_file_with_text('Lesson5/result_task'+str(input_key),output_result_string)