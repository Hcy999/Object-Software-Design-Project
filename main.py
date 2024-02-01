# main.py
from road import Road, StopSign, Intersection, SpeedLimit, Yield
from dynamic_road_item import Car, Truck, Light
from simulation import Simulation
from gui_timer_map import GUI, Timer, Map
import time

def main():
    
    car = Car(mile_marker=0, current_speed=0.0, desired_speed=65.0)  
    truck1 = Truck(mile_marker=0, current_speed=0.0, desired_speed=55.0, load_weight=4)  
    truck2 = Truck(mile_marker=0, current_speed=0.0, desired_speed=50.0, load_weight=8)  

    vehicles = [car, truck1, truck2]

    
    for i in range(11):
        print(f"Time: {i+1} seconds")
        for v in vehicles:
            v.update_speed(1)  
            print(f"{type(v).__name__} speed: {v.get_current_speed():.2f} mph")

if __name__ == "__main__":
    main()