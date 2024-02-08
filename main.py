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

    car = Car(mile_marker=0, current_speed=0.0, desired_speed=65.0)  
    truck1 = Truck(mile_marker=0, current_speed=0.0, desired_speed=55.0, load_weight=4)  
    truck2 = Truck(mile_marker=0, current_speed=0.0, desired_speed=50.0, load_weight=8)  

    vehicles = [car, truck1, truck2]

    
    sim_output = MetricOutput()  # Or ImperialOutput()

    for i in range(11):
        print(f"Time: {i+1} seconds")
        for v in vehicles:
            v.update_speed(1)  
            print(f"{type(v).__name__} speed: {sim_output.get_speed(v):.2f} {'km/h' if isinstance(sim_output, MetricOutput) else 'mph'}")

if __name__ == "__main__":
    main()
