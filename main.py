MPS_TO_KPH = 3.6

# main.py
from road import Road, StopSign, Intersection, SpeedLimit, Yield
from dynamic_road_item import Car, Truck, Light
from simulation import Simulation
from gui_timer_map import GUI, Timer, Map
import time

class ISimOutput:
    def get_speed(self, vehicle):
        raise NotImplementedError("Subclass must implement abstract method")

class ImperialOutput(ISimOutput):
    def get_speed(self, vehicle):
        return vehicle.get_current_speed()

class MetricOutput(ISimOutput):
    def get_speed(self, vehicle):
        return vehicle.get_current_speed() * 1.6

def main():
    # let the user choose the unit 
    unit = None
    while unit not in ('I', 'M'):
        unit = input('Enter "M" for metric or "I" for Imperial: ').strip().upper()
        if unit not in ('I', 'M'):
            print('Please enter "I" for Imperial or "M" for metric.')

    # let user enter a speed limit based on the user-selected unit system
    speed_unit = 'km/h' if unit == 'M' else 'mph'
    speed_limit = None
    while speed_limit is None:
        try:
            speed_limit = float(input(f"Enter the speed limit in {speed_unit}: "))
        except ValueError:
            print(f"Invalid input. Please enter a number for the speed limit in {speed_unit}.")

    car = Car(mile_marker=0, current_speed=0.0, desired_speed=speed_limit)
    truck1 = Truck(mile_marker=0, current_speed=0.0, desired_speed=speed_limit, load_weight=4)
    truck2 = Truck(mile_marker=0, current_speed=0.0, desired_speed=speed_limit, load_weight=8)
    vehicles = [car, truck1, truck2]

    # Initialize output format
    sim_output = MetricOutput() if unit == 'M' else ImperialOutput()

    for i in range(11):
        print(f"Time: {i+1} seconds")
        for v in vehicles:
            v.update_speed(1)
            print(f"{type(v).__name__} speed: {sim_output.get_speed(v):.2f} {speed_unit}")

if __name__ == "__main__":
    main()
