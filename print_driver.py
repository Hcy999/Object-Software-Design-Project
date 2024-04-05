from constants import Constants, Conversions, Heading

class IPrintDriver:
    def print_road(self, road, char_matrix):
        pass

class ConsolePrint(IPrintDriver):
    def print_road(self, road, char_matrix):
        CCx = Conversions.WCpointToCCpoint(road.xlocation)
        CCy = Conversions.WCpointToCCpoint(-road.ylocation)
        distance = 0
        CCRoadLength = Conversions.WClengthToCClength(road.length)
        
        
        if road.heading == Heading.North or road.heading == Heading.South:
            x = CCx
            while distance < CCRoadLength:
                if 0 <= CCy - distance < Constants.CharMapSize:
                    char_matrix.map[CCy - distance][x] = '|'
                    char_matrix.map[CCy - distance][x + 2] = '|'
                    char_matrix.map[CCy - distance][x + 4] = '|'
                distance += 1
        elif road.heading == Heading.East or road.heading == Heading.West:
            y = CCy
            while distance < CCRoadLength:
                if 0 <= CCx + distance < Constants.CharMapSize:
                    char_matrix.map[y][CCx + distance] = '-'
                    char_matrix.map[y + 2][CCx + distance] = '-'
                    char_matrix.map[y + 4][CCx + distance] = '-'
                distance += 1
