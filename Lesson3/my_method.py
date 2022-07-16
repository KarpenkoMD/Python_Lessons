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