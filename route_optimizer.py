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
        min_time_to_complete_rides = sys.maxsize
        optimized_path = list()

        pickup_combinations = list()
        calculate_pickup_combinations(
            rider_list, list(), pickup_combinations)

        for pickup_order in pickup_combinations:
            time_to_complete_rides = 0
            current_pos = curr_pos.copy()
            for ride in pickup_order:
                time_to_complete_rides += calculate_ride_time(
                    current_pos, ride.start)
                current_pos = ride.start.copy()
            dropoff_permutations = list()
            calculate_permutations(
                pickup_order, permutations=dropoff_permutations)

            max_dropoff_time = sys.maxsize
            next_pos = current_pos.copy()

            for dropoff_order in dropoff_permutations:
                total_dropoff_time = 0
                current_start_pos = current_pos.copy()
                for next_dropoff in dropoff_order:
                    total_dropoff_time += calculate_ride_time(
                        current_start_pos, next_dropoff.end)
                    current_start_pos = next_dropoff.end.copy()
                if total_dropoff_time < max_dropoff_time:
                    max_dropoff_time = total_dropoff_time
                    next_pos = current_start_pos.copy()

            time_to_complete_rides += max_dropoff_time

            for index in range(len(pickup_order), len(rider_list)):
                time_to_complete_rides += calculate_ride_time(
                    next_pos, rider_list[index].start)
                time_to_complete_rides += calculate_ride_time(
                    rider_list[index].start, rider_list[index].end)

            if min_time_to_complete_rides < time_to_complete_rides:
                min_time_to_complete_rides = time_to_complete_rides

    def get_path(self, curr_pos, rider_list):
        calculate_optimized_path(rider_list, curr_pos)

    @staticmethod
    # memoize already calculte ride time between two coordinates in 2D plane
    def calculate_ride_time(start_coordinate, end_coordinate):
        # TODO
        pass
