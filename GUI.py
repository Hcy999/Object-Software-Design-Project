# GUI.py



class ISimInput:
    def set_speed_limit(self, vehicle, speed):
        raise NotImplementedError("Subclass must implement abstract method")

class ISimOutput:
    def get_speed(self, vehicle):
        raise NotImplementedError("Subclass must implement abstract method")

class GUI(ISimInput, ISimOutput):
    pass

class MetricGUI(GUI):
    def get_speed(self, vehicle):
        return vehicle.get_current_speed() * MPS_TO_KPH

    def set_speed_limit(self, vehicle, speed):
        vehicle.set_desired_speed(speed / MPS_TO_KPH)  # Convert kph to m/s

class ImperialGUI(GUI):
    def get_speed(self, vehicle):
        return vehicle.get_current_speed() * MPS_TO_MPH

    def set_speed_limit(self, vehicle, speed):
        vehicle.set_desired_speed(speed / MPS_TO_MPH)  # Convert mph to m/s
