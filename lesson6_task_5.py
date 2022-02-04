class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Start drawing!')


class Pen(Stationery):
    def draw(self):
        print(f'Start drawing with a pen {self.title}!')


class Pencil(Stationery):
    def draw(self):
        print(f'Start drawing with a pencil {self.title}!')


class Handle(Stationery):
    def draw(self):
        print(f'Start drawing with a highlighter {self.title}!')


pen = Pen('Pilot')
pencil = Pencil('Koh-i-Noor')
marker = Handle('ZIG')
list_stationary = [pen, pencil, marker]
for i in list_stationary:
    i.draw()
