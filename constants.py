from enum import Enum

class Heading(Enum):
    North = 1
    South = 2
    East = 3
    West = 4

class Constants:
    CharMapSize = 40
    WorldSize = 200.0
    MpsToMph = 2.237
    MpsToKph = 3.6
    MetersToMiles = 0.000621371
    MetersToKm = 0.001

class Conversions:
    @staticmethod
    def WCpointToCCpoint(val):
        return int(val * (Constants.CharMapSize / Constants.WorldSize) + (Constants.CharMapSize / 2))

    @staticmethod
    def WClengthToCClength(val):
        return int(val * (Constants.CharMapSize / Constants.WorldSize))
