""" Задача 3
Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму. """

def input_number (input_message):
    while True: 
        input_str = input(input_message)
        if is_int(input_str) and int(input_str) > 0:
            return int(input_str)
        else:
            print('Ошибка ввода!')
            
def is_int(str):
    try:
        int(str)
        return True
    except ValueError:
        return False

def calculate(n):
    if n != 0:
        return (1+1/n)**n
    else:
        return False
def get_dictionary_sum(dict_num):
    sum = 0
    for i in range (1,len(dict_num)):
        sum += dict_num[i]
    return sum

number_N = input_number ("Введите натуральное число N:")
dictionary_numbers = {}
for i in range (1,number_N+1):
    dictionary_numbers[i]=round(calculate(i),3)
output_str = 'Сумма элементов словаря ' + str(dictionary_numbers) + ' равна ' + str(get_dictionary_sum(dictionary_numbers))
print(output_str)
