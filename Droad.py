from abc import ABC, abstractmethod
from road import RoadItem
from constants import Constants  # 这将从constants.py文件导入Constants



class DynamicRoadItem(RoadItem, ABC):
    def __init__(self, mile_marker, current_road=None):
        super().__init__(mile_marker, current_road)

    @abstractmethod
    def update(self, seconds: int):
        pass

class Vehicle(DynamicRoadItem, ABC):
    def __init__(self, mile_marker, current_road=None, current_speed=0.0, desired_speed=0.0):
        super().__init__(mile_marker, current_road)
        self.current_speed = current_speed
        self.desired_speed = desired_speed

    def update(self, seconds: int):
        self.update_speed(seconds)

    @abstractmethod
    def accelerate(self, seconds_delta):
        pass

    @abstractmethod
    def decelerate(self, seconds_delta):
        pass

    def get_current_speed(self):
        return self.current_speed

    def set_desired_speed(self, mph):
        self.desired_speed = mph

    def set_current_speed(self, speed):
        if self.current_speed <= speed:  # accelerating
            self.current_speed = min(speed, self.desired_speed)
        else:  # braking
            self.current_speed = max(speed, self.desired_speed)

    def update_speed(self, seconds):
        if self.current_speed > self.desired_speed:
            self.decelerate(seconds)
        elif self.current_speed < self.desired_speed:
            self.accelerate(seconds)

class Car(Vehicle):
    def __init__(self, mile_marker, current_road=None, current_speed=0.0, desired_speed=0.0):
        super().__init__(mile_marker, current_road, current_speed, desired_speed)

    def accelerate(self, seconds_delta):
        self.set_current_speed(self.get_current_speed() + Constants.ACC_RATE * seconds_delta)

    def decelerate(self, seconds_delta):
        self.set_current_speed(self.get_current_speed() - Constants.DEC_RATE * seconds_delta)

class Truck(Vehicle):
    def __init__(self, mile_marker, current_road=None, current_speed=0.0, desired_speed=0.0, load_weight=0):
        super().__init__(mile_marker, current_road, current_speed, desired_speed)
        self.load_weight = load_weight

    def accelerate(self, seconds_delta):
        if self.load_weight <= 5:
            self.set_current_speed(self.get_current_speed() + Constants.ACC_RATE_EMPTY * seconds_delta)
        else:
            self.set_current_speed(self.get_current_speed() + Constants.ACC_RATE_FULL * seconds_delta)

    def decelerate(self, seconds_delta):
        if self.load_weight <= 5:
            self.set_current_speed(self.get_current_speed() - Constants.DEC_RATE_EMPTY * seconds_delta)
        else:
            self.set_current_speed(self.get_current_speed() - Constants.DEC_RATE_FULL * seconds_delta)



class TrafficLight(DynamicRoadItem):
    def __init__(self, mile_marker, red_duration, yellow_duration, green_duration, start_color='red'):
        super().__init__(mile_marker)
        self.red_duration = red_duration
        self.yellow_duration = yellow_duration
        self.green_duration = green_duration
        self.current_color = start_color
        self.timer = 0  
        
    def update(self, seconds=1):
        self.timer += seconds
        cycle_duration = self.red_duration + self.yellow_duration + self.green_duration
        self.timer %= cycle_duration
        if self.timer <= self.red_duration:
            self.current_color = 'red'
        elif self.timer <= self.red_duration + self.yellow_duration:
            self.current_color = 'yellow'
        else:
            self.current_color = 'green'

    @staticmethod
    def print_traffic_lights(traffic_lights, char_matrix):
        first_tl_row_index = len(char_matrix.map) - 13
        second_tl_row_index = first_tl_row_index - 13
        symbol = {'red': 'X', 'yellow': '-', 'green': 'O'}[traffic_lights[0].current_color]
        char_matrix.map[first_tl_row_index][traffic_lights[0].mile_marker] = symbol
        symbol = {'green': 'O', 'red': 'X', 'yellow': '-'}[traffic_lights[1].current_color]
        char_matrix.map[second_tl_row_index][traffic_lights[1].mile_marker] = symbol