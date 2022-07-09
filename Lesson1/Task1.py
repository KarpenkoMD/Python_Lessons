
""" # Задача 1 
Напишите программу, которая принимает на вход цифру, 
обозначающую день недели, и проверяет, является ли этот день выходным.
 """

input_number = ''
day_number = 0
while True: 
    input_number = input('Введите день недели:')
    if input_number.isdigit():
       day_number = int(input_number)
       if day_number >= 1 and day_number <=7:
         break
    print('Ошибка! Введите число от 1 до 7!')
    
if day_number >= 1 and day_number <=5:
    print('Сегодня рабочий день! Иди пахать!')
elif day_number >= 6 and day_number <=7:
    print('Сегодня выходной!')
