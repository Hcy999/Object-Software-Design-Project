from abc import ABC, abstractmethod
from road import RoadItem

class Constants:
    ACC_RATE = 3.5          # Acceleration rate for cars in m/s
    ACC_RATE_EMPTY = 2.5    # Acceleration rate for light trucks in m/s
    ACC_RATE_FULL = 1.0     # Acceleration rate for heavy trucks in m/s
    DEC_RATE = 7.0          # Braking rate for cars in m/s
    DEC_RATE_EMPTY = 5.0    # Braking rate for light trucks in m/s
    DEC_RATE_FULL = 2.0     # Braking rate for heavy trucks in m/s
    MPS_TO_MPH = 2.237

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
        self.set_current_speed(self.get_current_speed() + Constants.ACC_RATE * seconds_delta * Constants.MPS_TO_MPH)

    def decelerate(self, seconds_delta):
        self.set_current_speed(self.get_current_speed() - Constants.DEC_RATE * seconds_delta * Constants.MPS_TO_MPH)

class Truck(Vehicle):
    def __init__(self, mile_marker, current_road=None, current_speed=0.0, desired_speed=0.0, load_weight=0):
        super().__init__(mile_marker, current_road, current_speed, desired_speed)
        self.load_weight = load_weight

    def accelerate(self, seconds_delta):
        if self.load_weight <= 5:
            self.set_current_speed(self.get_current_speed() + Constants.ACC_RATE_EMPTY * seconds_delta * Constants.MPS_TO_MPH)
        else:
            self.set_current_speed(self.get_current_speed() + Constants.ACC_RATE_FULL * seconds_delta * Constants.MPS_TO_MPH)

    def decelerate(self, seconds_delta):
        if self.load_weight <= 5:
            self.set_current_speed(self.get_current_speed() - Constants.DEC_RATE_EMPTY * seconds_delta * Constants.MPS_TO_MPH)
        else:
            self.set_current_speed(self.get_current_speed() - Constants.DEC_RATE_FULL * seconds_delta * Constants.MPS_TO_MPH)

    

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
