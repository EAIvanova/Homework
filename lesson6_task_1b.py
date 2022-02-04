from time import sleep


class TrafficLight:

    def running(self):
        while True:
            print(f'\rRED', end='')
            sleep(5)
            print(f'\rYELLOW', end='')
            sleep(3)
            print(f'\rGREEN', end='')
            sleep(6)
            print(f'\rYELLOW', end='')
            sleep(3)


traffic_light = TrafficLight()
traffic_light.running()
