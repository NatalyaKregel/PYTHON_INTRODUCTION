id_user = None
input_data = None
result = None

def get_id_user(num_id):                        # получаем id пользователя
    global id_user
    id_user = num_id

def get_input_data(data):                       # пользователь вводит пример
    global input_data
    input_data = data

def get_result(res):                            # получаем результата 
    global result
    result = res

def save_log():                                 #  записываем данные в log
    with open('file10.txt', 'a', encoding="utf-8") as f:
        f.writelines(f'ID user: {id_user}, Input: {input_data}, Result: {result}\n')