import time
from itertools import cycle
class TrafficLight:
    __color = [['red', [5]], ['yellow', [2]], ['green', [3]],['yellow', [2]]]

    def running(self):
        print('Включили светофор № 1')
        for light in cycle(self.__color):
            print(f'\r{light[0]}', end='')
            time.sleep(light[1][0])

TrafficLight_1 = TrafficLight()
TrafficLight_1.running()


