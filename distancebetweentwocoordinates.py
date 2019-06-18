class DistanceBetweenTwoCoordinates:
    def __init__(self, start_coordinate, end_coordinate):
        self.start_coordinate = start_coordinate
        self.end_coordinate = end_coordinate

    def __hash__(self):
        return hash((self.start_coordinate, self.end_coordinate))

    def __eq__(self, other):
        return (self.start_coordinate, self.end_coordinate) == (other.start_coordinate, other.end_coordinate)

    def __ne__(self, other):
        return not (self == other)
