
class Road:
    NumOfRoads = 0

    def __init__(self, streetName, locX, locY, length, heading):
        self.name = streetName
        self.length = length
        self.heading = heading
        self.xlocation = locX
        self.ylocation = locY
        Road.NumOfRoads += 1
        self.items = []  # Initialize the items list here

    def add_item(self, item):
        self.items.append(item)  # Add the add_item method here

    def print(self, print_driver, o):
        print_driver.print_road(self, o)
        for item in self.items:
            # Assumes each road item has a print_road_item method
            item.print_road_item(o)


class RoadItem:
    def __init__(self, mile_marker, current_road=None):
        self.mile_marker = mile_marker
        self.current_road = current_road
        self.next_item = None
        self.prev_item = None

    def get_mile_marker(self):
        return self.mile_marker

    def get_current_road(self):
        return self.current_road

    def set_current_road(self, road):
        self.current_road = road

    def get_next(self):
        return self.next_item

    def set_next(self, next_item):
        self.next_item = next_item

    def get_previous(self):
        return self.prev_item

    def set_previous(self, prev_item):
        self.prev_item = prev_item

