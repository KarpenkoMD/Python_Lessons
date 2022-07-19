import random
from unittest import result

def input_number(input_message, number_type='int'):
    while True:
        input_str = input(input_message)
        match number_type:
            case 'int':
                if is_int(input_str):
                    return int(input_str)
                else:
                    print('Ошибка ввода!')
            case 'natural':
                if is_int(input_str) and int(input_str) > 0:
                    return int(input_str)
                else:
                    print('Ошибка ввода!')
            case 'float':
                if input_str.find(',') != -1:
                    input_str = input_str.replace(',','.')
                if is_float(input_str):
                    return float(input_str)
            case _:
                raise AttributeError('Ошибка параметра функции!')


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


def list_random_fill(size: int, min_border=0, max_border=10):
    new_list = []
    if size <= 0:
        raise AttributeError('Ошибка параметра функции!')
    if type(max_border) == int and type(min_border) == int:
        for i in range(0, size):
            new_list.append(random.randint(min_border, max_border))
    elif type(max_border) == float or type(min_border) == float:
        for i in range(0, size):
            new_list.append(round(random.random() *
                                  random.randint(int(min_border), int(max_border)), 3))
    else:
        raise AttributeError('Ошибка параметра функции!')
    return new_list

def fill_file_with_text(file_name: str, str_to_output: str) -> int:
    """ записывает в файл с именем file_name сроку str_to_output, возвращает количество записанных символов control_sum """
    with open(file_name, 'w') as data:
        control_sum: int = data.write(str_to_output)
        data.write('\n')
    return control_sum

def get_text_from_file(file_name: str) -> str:
    """ считывает строки из файла с именем file_name, возвращает считанную строку без литерала '\\n' """
    with open(file_name, 'r') as data:
        download_str = data.readline()
    download_str = download_str.removesuffix('\n')
    #download_str = download_str.replace('\n','')
    return download_str

def check_words_in_string(str_to_lookup: str) -> str:
    result_string = ''
    char_count = 0
    digit_flag = 0
    length = len(str_to_lookup)
    for i in range(0,length):
        cur_char = str_to_lookup[i]
        if cur_char == ' ':
            if digit_flag == 0:
                if len(result_string) != 0:
                    result_string += ' '
                result_string += str_to_lookup[i-char_count:i]
            char_count = 0
            digit_flag = 0
        elif is_int(str_to_lookup[i]): 
            digit_flag = 1
        else:
            char_count += 1
    return result_string