import random


def input_number(input_message, number_type = 'int'):
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
                if is_int(input_str):
                    return float(input_str)
            case _:
                raise AttributeError('Ошибка параметра функции!')

def list_random_fill(size: int, min_border=0, max_border=10):
    new_list = []
    if size <= 0:
        raise AttributeError('Ошибка параметра функции!')
    if type(max_border)==int and type(min_border)==int:
        for i in range(0,size):
            new_list.append(random.randint(min_border, max_border))
    elif type(max_border)==float or type(min_border)==float:
        for i in range(0,size):
            new_list.append(round(random.random()*\
                random.randint(int(min_border), int(max_border)),3))
    else:
        raise AttributeError('Ошибка параметра функции!')
    return new_list
def dec_to_bin(dec_num:int):
    bin_num = '000'
    return bin_num
def get_sum_odd_elements(num_list:list):
    sum = 0
    for num in num_list:
        if num_list.index(num) % 2 !=0:
            sum += num
    return sum
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
