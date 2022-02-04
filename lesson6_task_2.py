class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_weight_asf(self, mass_asf, thick):
        result = self._length * self._width * mass_asf * thick / 1000
        return result


road = Road(5000, 20)
print(road.get_weight_asf(25, 5))
