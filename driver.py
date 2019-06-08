from perceptive_automata.request_handler import RequestHandler

class Driver:
    def __init__(self):
        self.grid_start_pos = [0, 0]
        self.grid_end_pos = [9, 9]
        self.current_pos = self.grid_start_pos.copy()
        self.current_time = 0
        self.req_handler = RequestHandler()
        self.drive()

    def is_new_ride_at_current_time_step(self):
        pass

    def log_status(self):
        # log current pos
        # log if pickup is there
        # log if dropoff is there
        # log vehicle passenger names
        pass

    def drive(self):
        # fetch the path queue based on rides

        # while(path queue is not empty) {

            self.log_status()

            # move the vehicle in the direction of position (which is popped from path queue)

            # advance time

            # check new ride
            # if ride:
              # fetch path queue again





        #}





driver = Driver()

print(driver.req_handler.rider_pos_mapping)



