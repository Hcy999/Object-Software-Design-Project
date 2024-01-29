from abc import ABC, abstractmethod

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


# Dynamic abstractmethod
class DynamicRoadItem(RoadItem, ABC):
    def __init__(self, mile_marker, current_road=None):
        super().__init__(mile_marker, current_road)

    @abstractmethod
    def update(self, seconds: int):
        pass


class Vehicle(DynamicRoadItem):
    def __init__(self, mile_marker, current_road=None, current_speed=0.0, desired_speed=0.0, speed_limit=0.0, color=""):
        super().__init__(mile_marker, current_road)
        self.current_speed = current_speed
        self.desired_speed = desired_speed
        self.speed_limit = speed_limit
        self.color = color

    def get_current_speed(self):
        return self.current_speed

    def set_desired_speed(self, speed):
        self.desired_speed = speed

    def get_speed_limit(self):
        return self.speed_limit

    def update(self, seconds):
        # linearly approaches the desired speed
        speed_difference = self.desired_speed - self.current_speed
        # Assume the vehicle can accelerate or decelerate 1 unit per second
        acceleration = min(abs(speed_difference), 1) * (1 if speed_difference > 0 else -1)
        self.current_speed += acceleration * seconds
        # Make sure not over speed limit
        self.current_speed = min(self.current_speed, self.speed_limit)
        distance_traveled = (self.current_speed / 3600) * seconds
        self.mile_marker += distance_traveled

class Car(Vehicle):
    def __init__(self, mile_marker, current_road=None, current_speed=0.0, desired_speed=0.0, speed_limit=0.0, color=""):
        
        super().__init__(mile_marker, current_road, current_speed, desired_speed, speed_limit, color)
     
class Truck(Vehicle):
    def __init__(self, mile_marker, current_road=None, current_speed=0.0, desired_speed=0.0, speed_limit=0.0, color="", load_weight=0.0):
        super().__init__(mile_marker, current_road, current_speed, desired_speed, speed_limit, color)
        self.load_weight = load_weight  

    def set_load_weight(self, weight):
        self.load_weight = weight

    def get_load_weight(self):
        return self.load_weight
    

class Light(DynamicRoadItem):
    def __init__(self, mile_marker, current_road=None, red_time=0, yellow_time=0, green_time=0):
        super().__init__(mile_marker, current_road)
        self.red_time = red_time
        self.yellow_time = yellow_time
        self.green_time = green_time
        # Assuming the light starts at red
        self.color = 'red'
        # Time for which the light has been on
        self.time_on = 0

    def update(self, seconds):
        # Increment the time the light has been on
        self.time_on += seconds
        
        # Determine the current color based on the time the light has been on
        cycle_time = self.red_time + self.yellow_time + self.green_time
        time_in_current_cycle = self.time_on % cycle_time
        
        if time_in_current_cycle <= self.red_time:
            self.color = 'red'
        elif time_in_current_cycle <= self.red_time + self.yellow_time:
            self.color = 'yellow'
        else:
            self.color = 'green'

    def get_light_color(self):
        return self.color


class Simulation:
    def __init__(self):
        self.dynamic_road_items = []  # Save all dynamic roaditem
        self.gui = GUI()
    def update(self, seconds: int):
        # Update status of all dynamic pavement items
        for item in self.dynamic_road_items:
            item.update(seconds)

    def add_dynamic_road_item(self, item):
        # Only Dynamic Items of type should be added
        if isinstance(item, DynamicRoadItem):
            self.dynamic_road_items.append(item)
        else:
            raise ValueError("Only dynamic road items can be added.")


class Map:
    def __init__(self):
        self.roads = []  # Association to Roads

    def add_road(self, road):
        self.roads.append(road)


class GUI:
    def __init__(self):
        self.simulation = None  # Reference to the Simulation 
        self.map = None  # Reference to the Map 
        self.timer = None  # Reference to the Timer 

    def link_simulation(self, simulation):
        self.simulation = simulation

    def link_map(self, map_):
        self.map = map_

    def link_timer(self, timer):
        self.timer = timer


class Timer:
     def __init__(self):
        self.gui = None  # GUI
