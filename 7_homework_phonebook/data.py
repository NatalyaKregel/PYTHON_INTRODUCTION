def get_data ():
    data = []
    surname = input('Введите фамилию: ')
    data.append(surname)
    name = input('Введите имя: ')
    data.append(name)
    mob_phone = input('Введите мобильный телефона: ')     
    data.append(mob_phone)
    dom_phone = input('Введите домашний телефон: ')
    data.append(dom_phone)
    return data