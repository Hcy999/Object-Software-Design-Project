class Road:
    def __init__(self, name, length):
        self.name = name
        self.length = length
        self.road_items = []  

    def get_length(self):
        return self.length

    def get_road_name(self):
        return self.name

    def add_road_item(self, road_item):
       road_item.set_current_road(self)
       self.road_items.append(road_item)  


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

