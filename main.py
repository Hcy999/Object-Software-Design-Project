# main.py
from road import Road, StopSign, Intersection, SpeedLimit, Yield
from dynamic_road_item import Car, Truck, Light
from simulation import Simulation
from GUI import MetricGUI, ImperialGUI  
import time

def main():
    # let the user choose the unit system
    unit = None
    while unit not in ('I', 'M'):
        unit = input('Enter "M" for metric or "I" for Imperial: ').strip().upper()
        if unit not in ('I', 'M'):
            print('Invalid input. Please enter "I" for Imperial or "M" for metric.')

    # let user enter a speed limit based on the user-selected unit system
    speed_unit = 'km/h' if unit == 'M' else 'mph'
    speed_limit = None
    while speed_limit is None:
        try:
            speed_limit = float(input(f"Enter the speed limit in {speed_unit}: "))
        except ValueError:
            print(f"Invalid input. Please enter a number for the speed limit in {speed_unit}.")

    # Initialize vehicles
    car = Car(mile_marker=0, current_speed=0.0)
    truck1 = Truck(mile_marker=0, current_speed=0.0, load_weight=4)
    truck2 = Truck(mile_marker=0, current_speed=0.0, load_weight=8)
    vehicles = [car, truck1, truck2]

    gui = MetricGUI() if unit == 'M' else ImperialGUI()

    for vehicle in vehicles:
        gui.set_speed_limit(vehicle, speed_limit)

    for i in range(11):
        print(f"Time: {i+1} seconds")
        for vehicle in vehicles:
            vehicle.update_speed(1)  
            speed = gui.get_speed(vehicle)
            print(f"{type(vehicle).__name__} speed: {speed:.2f} {speed_unit}")

if __name__ == "__main__":
    main()
