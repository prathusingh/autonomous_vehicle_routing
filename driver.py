from request_handler import RequestHandler
from route_optimizer import RouteOptimizer
from rider import Rider


class Driver:
    def __init__(self):
        self.grid_start_pos = [0, 0]
        self.grid_end_pos = [9, 9]
        self.current_pos = self.grid_start_pos.copy()
        self.current_time = 0
        self.req_handler = RequestHandler()
        self.load_riders()
        self.drive()

    def load_riders(self):
        self.riders = list()
        for req in self.req_handler.request_dict[self.current_time]:
            self.riders.append(Rider(req['start'], req['end'], req['name']))

    def drive(self):
        self.route_optimizer = RouteOptimizer()
        self.route_optimizer.get_optimized_path(
            self.current_pos, self.riders, self.grid_start_pos, self.grid_end_pos)

        # fetch the path queue based on rides

        # while(path queue is not empty) {

        self.log_status()

        # move the vehicle in the direction of position (which is popped from path queue)

        # advance time

        # check new ride
        # if ride:
        # load riders
        # fetch path queue again

        # }

    def is_new_ride_at_current_time_step(self):
        pass

    def log_status(self):
        # log current pos
        # log if pickup is there
        # log if dropoff is there
        # log vehicle passenger names
        pass


driver = Driver()

print(driver.req_handler.rider_pos_mapping)
