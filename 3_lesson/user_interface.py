import data_provider as prov
import logger as log

def temperature_view(sensor):
    data = prov.get_temperature(sensor) # получение данных из провайдера
    log.temperature_logger(data)        # записываем в лог информацию, которую получили
    return data


def preassure_view(sensor):
    data = prov.get_preassure(sensor)
    log.preassure_logger(data)          # записываем в лог информацию, которую получили
    return data

def wind_speed_view(sensor):
    data = prov.get_wind_speed(sensor)
    log.wind_speed_logger(data)         # записываем в лог информацию, которую получили
    return data    