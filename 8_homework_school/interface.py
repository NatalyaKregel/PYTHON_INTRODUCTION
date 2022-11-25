from logger import save_database, loading_database, add_student, put_grade, see_grade

def controller():
    loading_database()                                                      # выгружаем данные из БД учеников (students_db.json)
    print('----------------------------------------------------- ')
    print('ДОБРО ПОЖАЛОВАТЬ В ЖУРНАЛ УСПЕВАЕМОСТИ УЧАЩИХСЯ СШ №19!')
    print('----------------------------------------------------- ')
    print('Выберите режим работы:')
    print('Если вы учитель, нажмите 1\nЕсли вы ученик, нажмите 2')
    flag = int(input())
    while flag == 1:
        print('Выберите действие, которое хотите сделать:\n1 - внести ученика в журнал\n2 - поставить оценку ученику\n0 - выйти из приложения')
        flag = int(input())
        if flag == 1:
            add_student()
        elif flag == 2:
            put_grade()
        elif flag == 0:
            flag = 0
    else:
        save_database()  

    while flag == 2:
        surname = input('Для поиска информации введите фамилию ученика или 0 для выхода из приложения\n ')
        if surname == 0:
            flag = 0
        else:
            see_grade(surname)

