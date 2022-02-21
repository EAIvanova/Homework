from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, v):
        self.v = v

    @property
    def consumption(self):
        return self.v / 6.5 + 0.5

    def sum_consumption(self, list_cts):
        s = 0
        for coat in list_cts:
            s += coat.consumption
        return s


class Suit(Clothes):
    def __init__(self, h):
        self.h = h

    @property
    def consumption(self):
        return 2 * self.h + 0.3

    def sum_consumption(self, list_suits):
        s = 0
        for suit in list_suits:
            s += suit.consumption
        return s


coat_1 = Coat(48)
coat_2 = Coat(50)
suit_1 = Suit(1.72)
suit_2 = Suit(1.84)
suit_3 = Suit(1.76)
suit_4 = Suit(1.90)

list_costumes = [suit_1, suit_2, suit_3, suit_4]
list_coats = [coat_1, coat_2]

print(f'{coat_1.consumption:2f}')
print(f'{suit_1.consumption:2f}')
print(f'{suit_1.sum_consumption(list_costumes):2f}')
print(f'{coat_1.sum_consumption(list_coats):2f}')
print(f'{(suit_1.sum_consumption(list_costumes) + coat_1.sum_consumption(list_coats)):2f}')
