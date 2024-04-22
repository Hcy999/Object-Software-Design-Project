from road import Road
from Droad import Car, Truck, TrafficLight
from GUI import MetricGUI, ImperialGUI  
from print_driver import ConsolePrint
from map import Map, CharMatrix
from constants import Constants, Heading
import time
import os
import platform



@staticmethod
def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def main():
    sim_input = MetricGUI()
    map_obj = Map()
    cp = ConsolePrint()

    uptown = sim_input.create_road("Uptown", 0, -0.09, 0.180, Heading.North)
    map_obj.add_road(uptown)

    traffic_light1 = TrafficLight(mile_marker=26, red_duration=5, yellow_duration=1, green_duration=3)
    traffic_light2 = TrafficLight(mile_marker=26, green_duration=5, yellow_duration=2, red_duration=3)
    traffic_light2.current_color = 'green'
    traffic_lights = [traffic_light1, traffic_light2]

    for time_step in range(30):
        for tl in traffic_lights:
            tl.update()

        cm = CharMatrix()

        TrafficLight.print_traffic_lights(traffic_lights, cm)  

        map_obj.print(cp, cm)

        for row in cm.map:
            print(''.join(row))

        time.sleep(1)
        clear_screen()

if __name__ == "__main__":
    main()
