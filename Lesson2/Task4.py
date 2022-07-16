""" Задача 4 
Реализуйте выдачу случайного числа (или алгоритм перемешивания списка)
не использовать random.randint и вообще библиотеку random
Можете использовать xor, биты, библиотеку time (миллисекунды или наносекунды) - для задания случайности """

import time 
import random

def my_random(min=0, max=10):
    result = min-1
    digit_num = len(str(max))
    while result < min or result > max:
        string_time = str(time.time_ns()//100)
        ##print(string_time)
        result = int(string_time[-digit_num: len(string_time)])
        result = result >> 2
        time.sleep(0.01)

    return result

min_value = 1 
max_value = 10
##start = time.time_ns()
for i in range(0,20):
    start = time.time_ns()  
    print(my_random(min_value,max_value), end =' ')
    finish = time.time_ns()
print('\n', finish-start)

""" for i in range(0,20):
    start = time.time_ns()  
    print(random.randint(min_value,max_value), end =' ')
    finish = time.time_ns()
print('\n', finish-start)  """