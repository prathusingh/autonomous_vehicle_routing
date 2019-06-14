class RouteOptimizer:
    minimum_time = 0

    @staticmethod
    def calculate_pickup_combinations(rides, pickup_order, curr_pos, ride_time, start=0):
        for ride_index in range(start, len(rides)):

            ride_time += calculate_ride_time(curr_pos, rides[ride_index].start)
            pickup_order.append(rides[ride_index].start)
            calculate_dropoff_combinations(pickup_order)
            calculate_pickup_combinations(
                rides, pickup_order, rides[ride_index].start, ++start)
            pickup_order.pop()

    @staticmethod
    def calculate_positions_combinations(list_positions):

        pass

    @staticmethod
    def total_ride_time():
        pass

    def get_path(self, curr_pos, rider_list):
        pickup_order = []
        possible_ride_time = 0
        calculate_pickup_combinations(
            rider_list, pickup_order, curr_pos, possible_ride_time)

    @staticmethod
    # memoize already calculte ride time between two coordinates in 2D plane
    def calculate_ride_time(start_coordinate, end_coordinate):
        pass

    def optimize_routes(time_step):
        pass
