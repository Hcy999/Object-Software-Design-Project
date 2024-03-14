from constants import Constants

class Map:
    def __init__(self):
        self.roads = []

    def add_road(self, road):
        self.roads.append(road)

    def print(self, print_driver, o):
        for road in self.roads:
            road.print(print_driver, o)

class CharMatrix:
    def __init__(self, size=Constants.CharMapSize):
        self.map = [[' ' for _ in range(size)] for _ in range(size)]