import random


class Car:

    direction = ['north', 'northeast', 'east', 'west', 'northwest',
                 'south', 'southeast', 'southwest']

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        print(f'{name} has a color {color}.')

    def go(self):
        print(f'{self.name}: GO!')

    def stop(self):
        print(f'{self.name}: STOP!')

    def turn(self):
        print(f'{self.name}: car turned {random.choice(self.direction)}')

    def show_speed(self):
        print(f'{self.name}: car speed is {self.speed}')


class TownCar(Car):

    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print(f'{self.name}: speed exceeded!')


class WorkCar(Car):

    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print(f'{self.name}: speed exceeded!')


class SportCar(Car):
    pass


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


town = TownCar(90, 'white', 'BMW')
sport = SportCar(120, 'red', 'Ferrari')
work = WorkCar(50, 'yellow', 'MAN')
police = PoliceCar(100, 'blue', 'Ford')

list_of_cars = [town, sport, work, police]

for i in list_of_cars:
    i.go()
    i.turn()
    i.stop()
    print(i.show_speed())
