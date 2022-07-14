""" Задача 4 
Реализуйте выдачу случайного числа (или алгоритм перемешивания списка)
не использовать random.randint и вообще библиотеку random
Можете использовать xor, биты, библиотеку time (миллисекунды или наносекунды) - для задания случайности """

import time 

def my_random(min=0, max=10):
    result = min-1
    digit_num = len(str(max))
    while result < min or result > max:
        string_time = str(time.time_ns()//100)
        result = int(string_time[len(string_time)-digit_num:len(string_time)])
    return result

min_value = 1 
max_value = 100

print(my_random(min_value,max_value))
