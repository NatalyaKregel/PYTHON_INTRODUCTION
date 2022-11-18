from data import get_data as contact

# чтение файла с контактами
def import_contact():
    with open('Contacts.csv', 'r', encoding='utf=8') as f:
        return f.read()

# запись контактов в справочник в разных форматах
def export_csv (data):
    file = 'Contacts.csv'
    with open (file, 'a', encoding = 'utf-8') as d:
        d.write(f'Фамилия: {data[0]}; Имя: {data[1]}; Мобильный телефон: {data[2]}; Домашний телефон: {data[3]}\n' + '----------------------------------------------------------------------------------------' + '\n')
        

def export_txt (data):
    file = 'contact.txt'
    with open (file, 'a', encoding = 'utf-8') as d:
        d.write(f'Фамилия: {data[0]}\nИмя: {data[1]}\nМобильный телефон: {data[2]}\nДомашний телефон: {data[3]}\n' + '\n')
        