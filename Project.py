from abc import ABC, abstractmethod

class Road:
    def __init__(self, name, length):
        self.name = name
        self.length = length
        self.head = None  

    def get_length(self):
        return self.length

    def get_road_name(self):
        return self.name

    def add_road_item(self, road_item):
        road_item.set_current_road(self)
        
        if not self.head:
            self.head = road_item
        else:
            current_item = self.head
            while current_item.get_next():
                current_item = current_item.get_next()
            current_item.set_next(road_item)
            road_item.set_previous(current_item)


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


class Static(RoadItem):
    def __init__(self, mile_marker, current_road=None):
        super().__init__(mile_marker, current_road)
        

class StopSign(Static):
    def __init__(self, mile_marker, current_road=None):
        super().__init__(mile_marker, current_road)
       
class Intersection(Static):
    def __init__(self, mile_marker, current_road=None, turns=None):
        super().__init__(mile_marker, current_road)
        self.turns = turns if turns is not None else []  

    def add_turn(self, turn):
        self.turns.append(turn)

    def get_turn(self, index):
        return self.turns[index] if index < len(self.turns) else None
    
class SpeedLimit(Static):
    def __init__(self, mile_marker, current_road=None, speed_limit=None):
        super().__init__(mile_marker, current_road)
        self.speed_limit = speed_limit

    def get_speed_limit(self):
        return self.speed_limit

class Yield(Static):
    def __init__(self, mile_marker, current_road=None):
        super().__init__(mile_marker, current_road)


# Dynamic abstractmethod
class Dynamic(RoadItem, ABC):
    def __init__(self, mile_marker, current_road=None):
        super().__init__(mile_marker, current_road)

    @abstractmethod
    def update(self, seconds: int):
        pass


class Vehicle(Dynamic):
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
    

class Light(Dynamic):
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
        self.road_items = []  # Save all dynamic roaditem

    def update(self, seconds: int):
        # Update status of all dynamic pavement items
        for item in self.road_items:
            item.update(seconds)

    def add_dynamic_road_item(self, item):
        # Only Dynamic Items of type should be added
        if isinstance(item, Dynamic):
            self.road_items.append(item)
        else:
            raise ValueError("Only dynamic road items can be added.")

# Creating Road
main_road = Road("Main Street", 5.0)

# Creating stop signs and speed limit signs
stop_sign = StopSign(mile_marker=1.0, current_road=main_road)
speed_limit_sign = SpeedLimit(mile_marker=2.0, current_road=main_road, speed_limit=35)

# Add static items to the road
main_road.add_road_item(stop_sign)
main_road.add_road_item(speed_limit_sign)

# Creating Car and Truck
my_car = Car(mile_marker=0, current_road=main_road, current_speed=0, desired_speed=35, speed_limit=35, color="red")
my_truck = Truck(mile_marker=0, current_road=main_road, current_speed=0, desired_speed=30, speed_limit=35, color="blue", load_weight=5000)

# Creating traffic lighT
traffic_light = Light(mile_marker=2.5, current_road=main_road, red_time=30, yellow_time=5, green_time=60)

# Creating simulation
simulation = Simulation()

# Add dynamic items to the simulation
simulation.add_dynamic_road_item(my_car)
simulation.add_dynamic_road_item(my_truck)
simulation.add_dynamic_road_item(traffic_light)

# simulation 60 seconds
simulation.update(60)


print(f"Road Name: {main_road.get_road_name()}, Length: {main_road.get_length()} miles")
print(f"Stop Sign at mile marker {stop_sign.get_mile_marker()}")
print(f"Speed Limit Sign at mile marker {speed_limit_sign.get_mile_marker()} with limit {speed_limit_sign.get_speed_limit()} mph")
print(f"Car at mile marker {my_car.get_mile_marker()} with a speed of {my_car.get_current_speed()} mph and color {my_car.color}")
print(f"Truck at mile marker {my_truck.get_mile_marker()} with a speed of {my_truck.get_current_speed()} mph, color {my_truck.color}, and load weight {my_truck.get_load_weight()} units")
print(f"Traffic Light at mile marker {traffic_light.get_mile_marker()} is {traffic_light.get_light_color()}")
