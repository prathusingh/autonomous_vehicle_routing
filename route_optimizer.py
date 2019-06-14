class RouteOptimizer:

    @staticmethod
    def calculate_pickup_combinations(rides, current_pickup_order, curr_pos, pickup_combinations, start=0):
        for ride_index in range(start, len(rides)):
            current_pickup_order.append(rides[ride_index].start)
            pickup_combinations.append(current_pickup_order.copy())
            calculate_pickup_combinations(
                rides, current_pickup_order, rides[ride_index].start, pickup_combinations, ++start)
            current_pickup_order.pop()

    @staticmethod
    def calculate_positions_permutations(pos_list, permutations=list(), start=0):
        for index in range(start, len(pos_list)):
            list_copy = pos_list.copy()
            list_copy[start] = pos_list[index]
            list_copy[index] = pos_list[start]
            permutations.append(list_copy)
            calculate_positions_permutations(pos_list, permutations, ++start)

    @staticmethod
    def calculate_optimized_path(rider_list, curr_pos):
        pickup_combinations = list()
        calculate_pickup_combinations(
            rider_list, list(), curr_pos, pickup_combinations)
        pass

    def get_path(self, curr_pos, rider_list):
        calculate_optimized_path(rider_list, curr_pos)

    @staticmethod
    # memoize already calculte ride time between two coordinates in 2D plane
    def calculate_ride_time(start_coordinate, end_coordinate):
        # TODO
        pass
