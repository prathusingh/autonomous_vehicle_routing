import sys


class RouteOptimizer:
    minimum_time = sys.maxsize

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

    @staticmethod
    def calculate_optimized_path(rider_list, curr_pos):
        pickup_combinations = list()
        calculate_pickup_combinations(
            rider_list, list(), pickup_combinations)

        for ride_order in pickup_combinations:
            current_time = 0
            current_pos = curr_pos.copy()
            for ride in ride_order:
                current_time += calculate_ride_time(current_pos, ride.start)
                current_pos = ride.start.copy()
            dropoff_permutations = list()
            calculate_permutations(
                ride_order, permutations=dropoff_permutations)
            dropoff_time = sys.maxsize
            for dropoff_order in dropoff_permutations:
                current_dropoff_time = 0
                current_start_pos = current_pos.copy()
                for next_dropoff in dropoff_order:
                    dropoff_time += calculate_ride_time(
                        current_start_pos, next_dropoff.end)
                    current_start_pos = ride.end.copy()
                if current_dropoff_time < dropoff_time:
                    dropoff_time = current_dropoff_time

            current_time += dropoff_time

            for index in range(len(ride_order), len(rider_list)):
                calculate_ride_time()
                current_time += rider_list[index].start
                current_time += rider_list[index].end

    def get_path(self, curr_pos, rider_list):
        calculate_optimized_path(rider_list, curr_pos)

    @staticmethod
    # memoize already calculte ride time between two coordinates in 2D plane
    def calculate_ride_time(start_coordinate, end_coordinate):
        # TODO
        pass
