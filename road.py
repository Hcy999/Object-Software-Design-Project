class Road:
    NumOfRoads = 0

    def __init__(self, streetName, locX, locY, length, heading):
        self.name = streetName
        self.length = length
        self.heading = heading
        self.xlocation = locX
        self.ylocation = locY
        Road.NumOfRoads += 1

    def print(self, print_driver, o):
        print_driver.print_road(self, o)



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


class StaticRoadItem(RoadItem):
    def __init__(self, mile_marker, current_road=None):
        super().__init__(mile_marker, current_road)
        

class StopSign(StaticRoadItem):
    def __init__(self, mile_marker, current_road=None):
        super().__init__(mile_marker, current_road)
       
class Intersection(StaticRoadItem):
    def __init__(self, mile_marker, current_road=None, turns=None):
        super().__init__(mile_marker, current_road)
        self.turns = turns if turns is not None else []  

    def add_turn(self, turn):
        self.turns.append(turn)

    def get_turn(self, index):
        return self.turns[index] if index < len(self.turns) else None
    
class SpeedLimit(StaticRoadItem):
    def __init__(self, mile_marker, current_road=None, speed_limit=None):
        super().__init__(mile_marker, current_road)
        self.speed_limit = speed_limit

    def get_speed_limit(self):
        return self.speed_limit

class Yield(StaticRoadItem):
    def __init__(self, mile_marker, current_road=None):
        super().__init__(mile_marker, current_road)

