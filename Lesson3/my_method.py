import random

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
                if is_int(input_str):
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


def get_sum_odd_elements(num_list: list):
    sum = 0
    for num in num_list:
        if num_list.index(num) % 2 != 0:
            sum += num
    return sum


def mult_pair_elements(num_list: list):
    num_list_size = len(num_list)
    mult_pair_list = []
    for i in range(0, num_list_size//2):
        mult_pair_list.append(num_list[i]*num_list[num_list_size-1-i])
    if num_list_size % 2 != 0:
        mult_pair_list.append(num_list[num_list_size//2]**2)
    return mult_pair_list


def min_max_fraction_difference(num_list: list):
    if len(num_list) < 2:
        raise AttributeError('Ошибка параметра функции!')
    max = round(num_list[0] - int(num_list[0]), 3)
    min = round(num_list[1] - int(num_list[1]), 3)
    if max < min:
        max, min = min, max
    for i in range(2, len(num_list)):
        temp = round(num_list[i] - int(num_list[i]), 3)
        if temp > max:
            max = temp
        elif temp < min:
            min = temp
    temp_str = str(round(max-min, 3)).split('.')
    return int(temp_str[1])


def dec_to_bin(dec_num: int):
    bin_num_list = []
    if dec_num < 0:
        bin_num_list.append('-')
        dec_num *= -1
    while dec_num > 0:
        bin_num_list.insert(0, str(dec_num % 2))
        dec_num = dec_num // 2
    if bin_num_list.count('-') != 0:
        bin_num_list.pop()
        bin_num_list.insert(0, '-')
    return ("".join(bin_num_list))


def count_fibonacci(fib_num, is_negative: int = 0):
    fib_list = [0]
    if fib_num < 1:
        return fib_list
    fib_list.append(1)
    for i in range(2, fib_num+1):
        fib_list.append(fib_list[i-1] + fib_list[i-2])
    if is_negative !=0:
        neg_fib_list=[1,0]
        for i in range(2, fib_num+1):
            neg_fib_list.insert(0,fib_list[i]*(-1)**(i+1))
        neg_fib_list.pop()
        neg_fib_list.extend(fib_list)
        fib_list = neg_fib_list
    return fib_list
