import random


def input_number(input_message, number_type='int'):
    """Функция обеспечивает проверку вводимых данных в зависимости от параметра number_type\n
    При 'int' - проверяет, является ли число целым и возвращает целое число типа int\n
    При 'natural' - проверяет, является ли число целым и больше 0, возвращает целое число типа int\n
    При 'float' - проверяет, введено ли число с плавающей точкой, заменяет ',' на '.'
    и возвращает число типа float\n
    При 'str_float' - аналогично float, но возвращает вещественное число в виде строки"""
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
            case 'float' | 'str_float':
                if input_str.find(',') != -1:
                    input_str = input_str.replace(',', '.')
                if is_float(input_str):
                    if number_type == 'float':
                        return float(input_str)
                    if number_type == 'str_float':
                        return input_str
            case _:
                raise AttributeError('Ошибка параметра функции!')


def is_float(str):
    """Функция возвращает True если строка str является вещественным числом"""
    try:
        float(str)
        return True
    except ValueError:
        return False


def is_int(str):
    """Функция возвращает True если строка str является целым числом"""
    try:
        int(str)
        return True
    except ValueError:
        return False


def list_random_fill(size: int, min_border=0, max_border=10):
    """Функция заполняет список размером size случайными целыми числами от in_border до max_border\n
    Если min_border или max_border  являются вещественными числами, то список будет заполнен вещественными числами\n
    Возвращает функция заполненный список"""
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
    """Записывает в файл с именем file_name сроку str_to_output.\n
    Возвращает количество записанных символов control_sum """
    with open(file_name, 'w') as data:
        control_sum: int = data.write(str_to_output)
        data.write('\n')
    return control_sum


def get_text_from_file(file_name: str) -> str:
    """Считывает строки из файла с именем file_name.\n
    Возвращает считанную строку без литерала '\\n' """
    with open(file_name, 'r') as data:
        download_str = data.readline()
    download_str = download_str.removesuffix('\n')
    #download_str = download_str.replace('\n','')
    return download_str


def check_words_in_string(str_to_lookup: str) -> str:
    """Проверяет слова на наличие цифр, в качестве аргумента передается строка, 
    в которой необходимо найти слова без цифр.\n
    Функция возвращает строку, сформированную из слов без цифр"""
    result_string = ''
    char_count = 0
    digit_flag = 0
    length = len(str_to_lookup)
    for i in range(0, length):
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


def pi_count() -> float:
    """ Вычисляет число Пи по ряду Мадхава"""
    pi_counted: float = 1
    # изначальная формула ряда выглядит так: pi_counted +=((-1)**i)/((2*i+1)*(3**i))
    # для ускорения вычислений вводим два коэффициента k1 и k2, а расчетны начинаем с i=1
    i = 1
    k1, k2 = -1, 3
    while i < 100000:
        pi_counted += k1/((2*i+1)*k2)
        k1 *= -1
        k2 *= 3
        i += 1
    pi_counted *= 12**0.5
    return pi_counted


def pi_round(accuracy_template: str):
    """ Вычисляет число Пи и обрезает его вещественную часть в соответствии с шаблоном accuracy_template\n
    Функция возвращает число Пи с количеством знаков после запятой как в шаблоне"""
    pi_rounded = pi_count()
    count = 0
    acc_float = float(accuracy_template)
    while acc_float != int(acc_float):
        acc_float *= 10
        pi_rounded *= 10
        count += 1
    str_pi = str(int(pi_rounded))
    # пришлось так сделать, чтобы был красивый вывод в строке
    str_pi = str_pi[0]+'.' + str_pi[1:len(str_pi)]
    return str_pi


def find_unique_elements(num_list: list) -> list:
    """Функция в качестве аргумента принимает список числе num_list и выбирает из него 
    уникальные элементы.\n
    Возвращает список уникальных элементов"""
    unique_list = []
    for element in num_list:
        # if unique_list.count(element) == 0:
        #    unique_list.append(element)
        exist_flg = 0
        for k in range(0, len(unique_list)):
            if unique_list[k] == element:
                exist_flg = 1
                break
        if exist_flg == 0:
            unique_list.append(element)
    return unique_list


def get_factors_list(number: int) -> list:
    """Функция находит простые множители числа number.\n
    Возвращает список множителей"""
    lst_factors = []
    factor = 2
    while factor**2 < number:
        if number % factor == 0:
            lst_factors.append(factor)
            number = number // factor
            factor = 2
            continue
        factor += 1
    lst_factors.append(number)
    return lst_factors
