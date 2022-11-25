import json
import os
from pprint import pprint

def set_students(data_list):                                                        # записываем данные ученика в словарь
    student_db[data_list[0]] = data_list[1:], {}

def set_grade(surname, lesson, grade):                                              # добавляем оценки    
    if student_db.get(surname) is None:
        print(f'Такой ученик в журнале не найден')
        print(student_db)
    else:
        if lesson in student_db[surname][1]:
            student_db[surname][1][lesson].extend(grade)
        else:
            student_db[surname][1][lesson] = grade


def get_student(surname_student):                                                   # выводим данные ученика 
    if student_db.get(surname_student) is None:
        print(f'Такой ученик в журнале не найден')
    else:
        data = student_db[surname_student]
        print(f'{surname_student}{", ".join(data[0])}:')
        print(*[f'{key}:{", ".join(value)}'for key,  value in data[1].items()], sep='\n') 

def add_student():                                                                  # добавляем ученика в журнал
    data = input('Введите фамилию, имя и класс через пробел): ').split(' ')          
    set_students(data)
    save_database()

def put_grade():                                                                    # добавляем оценки ученику в журнал
    surname = input('Введите фамилию ученика: ')
    lesson = input('Введите название предмета: ')
    grade = input('Введите оценку ученика: ').split()
    set_grade(surname, lesson, grade)

def see_grade(surname):                                                             # добавляем оценки ученику в журнал
    get_student(surname)


                                                                                    # сохраняем данные из словаря student_db в наш файл students_db.json
def save_database():
    json.dump(student_db, open('students_db.json', 'w'))

                                                                                    # загружаем данные из нашего файла students_db.json в словарь student_db
def loading_database():
    global student_db
    if os.stat('students_db.json').st_size == 0:
        student_db = {}
    else:
        student_db = json.load(open('students_db.json'))