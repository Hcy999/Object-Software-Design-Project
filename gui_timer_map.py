import time

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
        self.elapsed_time = 0
        self.start_time = None

     def start(self):
        """Start Timer"""
        if self.start_time is None:
            self.start_time = time.time()

     def stop(self):
        """Stop Timer"""
        if self.start_time is not None:
            self.elapsed_time += time.time() - self.start_time
            self.start_time = None
