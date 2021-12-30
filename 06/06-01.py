from time import sleep
from itertools import cycle

class TrafficLight:
    __color = [
      { 'color': '██', 'delay': 7, 'code': 31 },
      { 'color': '██',  'delay': 2, 'code': 33 },
      { 'color': '██', 'delay': 5, 'code': 32 }
    ]

    def running(self):
        while True:
          for light in cycle(self.__color):
            print(f'\r\033[{light["code"]}m\033[1m{light["color"]}\033[0m ', end='')
            sleep(light['delay'])

TrafficLight = TrafficLight()
TrafficLight.running()
