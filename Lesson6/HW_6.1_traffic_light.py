# Создать класс TrafficLight ( светофор) и определить у него один атрибут color (цвет) и метод
# running (запуск). Атрибут реализовать как приватный. В рамках метода реализовать
# переключение светофора в режимы: красный, желтый, зеленый. Продолжительность первого
# состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый)
# — на ваше усмотрение. Переключение между режимами должно осуществляться только в
# указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр
# и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении
# выводить соответствующее сообщение и завершать скрипт.

from itertools import cycle
import time


class TrafficLight:
    def __init__(self, color):
        self.__color = color

    def trafficlight_running(self):
        if self.__color == "red":
            colors = ["red", "7", "yellow", "2", "green", "2"]
        if self.__color == "yellow":
            colors = ["yellow", "2", "green", "2", "red", "7"]
        if self.__color == "green":
            colors = ["green", "2", "red", "7", "yellow", "2"]
        count = 0
        for el in cycle(colors):
            if count > 5:
                break
            if el.isdigit():
                time.sleep(int(el))
                count += 1
            else:
                print(el)


sample2 = TrafficLight("green")
sample2.trafficlight_running()
