class RouteOptimizer:
    minimum_time = 0

    @staticmethod
    def calculate_pickup_combinations(rides, pickup_order, curr_pos, ride_time):
        for ride in rides:
            ride_time += recursively_calculate_ride_time()
            pickup_order.append(ride.start)

            # return path queue

    @staticmethod
    def calculate_dropoff_combinations(dropoff_list):
        pass

    def get_path(self, curr_pos, rider_list):
        pickup_order = []
        possible_ride_time = 0
        calculate_pickup_combinations(
            rider_list, pickup_order, curr_pos, possible_ride_time)

    @staticmethod
    # memoize already calculte ride time between two coordinates in 2D plane
    def recursively_calculate_ride_time(start_coordinate, end_coordinate):
        pass

    def optimize_routes(time_step):
        pass
