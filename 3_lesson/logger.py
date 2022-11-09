from datetime import datetime as dt    # как только данные получаем должны залогировать (записать)

def temperature_logger(data):           # логирование времени
    time=dt.now().strftime('%H:%M')
    with open('log.csv','a') as file:
        file.write('{};temperature;{}\n'
                    .format(time,data))

def preassure_logger(data):             # логирование давления
    time=dt.now().strftime('%H:%M')
    with open('log.csv','a') as file:
        file.write('{};preassure;{}\n'
                    .format(time,data))


def wind_speed_logger(data):            # логирование скорость ветра
    time=dt.now().strftime('%H:%M')
    with open('log.csv','a') as file:
        file.write('{};wind_speed;{}\n'
                    .format(time,data))     

                