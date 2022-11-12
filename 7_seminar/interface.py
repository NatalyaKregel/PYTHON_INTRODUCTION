import digit
import in_num                                    # импорт всего файла
import log

def button_click():
    print('Введите "0" если хотите продолжать')
    print('Введите "1" если хотите закончить')
    flag = int(input())
    while flag == 0:
        primer = digit.parse()
        result = digit.calculate(primer)
        in_num.view_data(result)                         # вывод
        log.loger(primer, result)
        print('Введите "0" если хотите продолжать')
        print('Введите "1" если хотите закончить')
        flag = int(input())
    print('Программа завершилась!')





