import sys
from distancebetweentwocoordinates import DistanceBetweenTwoCoordinates


class RouteOptimizer:
    def __init__(self):
        self.distance_map_between_two_coordinates = dict()

    @staticmethod
    def calculate_pickup_combinations(rides, current_pickup_order, pickup_combinations, start=0):
        for ride_index in range(start, len(rides)):
            current_pickup_order.append(rides[ride_index])
            pickup_combinations.append(current_pickup_order.copy())
            start += 1
            calculate_pickup_combinations(
                rides, current_pickup_order, pickup_combinations, start)
            current_pickup_order.pop()

    @staticmethod
    def calculate_permutations(list_to_permute, permutations=list(), start=0):
        for index in range(start, len(list_to_permute)):
            list_copy = list_to_permute.copy()
            list_copy[start] = list_to_permute[index]
            list_copy[index] = list_to_permute[start]
            permutations.append(list_copy)
            start += 1
            calculate_permutations(list_to_permute, permutations, start)

    def get_distance_between_two_coordinates(self, start_coordinate, end_coordinate, grid_start_coordinate, grid_end_coordinate):
        hashed_key = DistanceBetweenTwoCoordinates(
            tuple(start_coordinate), tuple(end_coordinate))
        return self.distance_map_between_two_coordinates[hashed_key] if hashed_key in self.distance_map_between_two_coordinates else calculate_ride_time(
            start_coordinate, end_coordinate, grid_start_coordinate, grid_end_coordinate)

    def get_optimized_path(self, curr_pos, rider_list, grid_start_pos, grid_end_pos):
        min_time_to_complete_rides = sys.maxsize
        optimized_path = list()

        pickup_combinations = list()
        calculate_pickup_combinations(
            rider_list, list(), pickup_combinations)

        for pickup_order in pickup_combinations:
            path = list()
            path.extend(pickup_order)
            time_to_complete_rides = 0
            current_pos = curr_pos.copy()
            for ride in pickup_order:
                time_to_complete_rides += self.get_distance_between_two_coordinates(
                    current_pos, ride.start, grid_start_pos, grid_end_pos)
                current_pos = ride.start.copy()
            dropoff_permutations = list()
            calculate_permutations(
                pickup_order, permutations=dropoff_permutations)

            max_dropoff_time = sys.maxsize
            next_pos = current_pos.copy()
            optimized_dropoff_path = list()

            for dropoff_order in dropoff_permutations:
                total_dropoff_time = 0
                dropoff_path = list()
                dropoff_path.extend(dropoff_order)
                current_start_pos = current_pos.copy()
                for next_dropoff in dropoff_order:
                    total_dropoff_time += self.get_distance_between_two_coordinates(
                        current_start_pos, next_dropoff.end, grid_start_pos, grid_end_pos)
                    current_start_pos = next_dropoff.end.copy()
                if total_dropoff_time < max_dropoff_time:
                    max_dropoff_time = total_dropoff_time
                    next_pos = current_start_pos.copy()
                    optimized_dropoff_path = dropoff_path.copy()

            time_to_complete_rides += max_dropoff_time
            path.extend(optimized_dropoff_path)

            for index in range(len(pickup_order), len(rider_list)):
                time_to_complete_rides += self.get_distance_between_two_coordinates(
                    next_pos, rider_list[index].start, grid_start_pos, grid_end_pos)
                path.append(rider_list[index].start)
                time_to_complete_rides += self.get_distance_between_two_coordinates(
                    rider_list[index].start, rider_list[index].end, grid_start_pos, grid_end_pos)
                path.append(rider_list[index].end)

            if min_time_to_complete_rides < time_to_complete_rides:
                min_time_to_complete_rides = time_to_complete_rides
                optimized_path = path.copy()

        return optimized_path

    @staticmethod
    # memoize already calculte ride time between two coordinates in 2D plane
    def calculate_ride_time(current_coordinate, end_coordinate, grid_start_coordinate, grid_end_coordinate):
        calculate_ride_time(
            current_coordinate.start[0] + 1, end_coordinate, grid_start_coordinate, grid_end_coordinate)
        calculate_ride_time(
            current_coordinate.start[1] + 1, end_coordinate, grid_start_coordinate, grid_end_coordinate)
        calculate_ride_time(
            current_coordinate.start[0] - 1, end_coordinate, grid_start_coordinate, grid_end_coordinate)
        calculate_ride_time(
            current_coordinate.start[1] - 1, end_coordinate, grid_start_coordinate, grid_end_coordinate)
