"""
NOTE: This file assumes the data we will be getting from API
That's why there is hard coded data in the file
"""

requests_time_0 = [
    {
        "name": "Elon",
        "start": [3, 5],
        "end": [8, 7]
    },
    {
        "name": "George",
        "start": [1, 2],
        "end": [4, 3]
    }
]

requests_time_1 = []

requests_time_2 = [
    {
        "name": "Nancy",
        "start": [8, 7],
        "end": [1, 3]
    },
    {
        "name": "Prathu",
        "start": [1, 2],
        "end": [8, 7]
    }
]


class RequestHandler:
    def __init__(self):
        self.request_dict = dict()
        self.rider_pos_mapping = dict()
        self.get_new_request()
        self.update_request_dict()
        self.update_rider_pos_mapping()

    def get_new_request(self):
        # get new request from API
        # if new request
            # self.process_request()
            # self.update_rider_pos_mapping()
        pass

    def update_request_dict(self):
        # assume we have request lists as defined at the top
        self.request_dict[int("requests_time_0".split("_")[2])] = requests_time_0
        self.request_dict[int("requests_time_1".split("_")[2])] = requests_time_1
        self.request_dict[int("requests_time_2".split("_")[2])] = requests_time_2

    def update_rider_pos_mapping(self):
        for ride in requests_time_0:

            if tuple(ride["start"]) in self.rider_pos_mapping:
                # Here P stands for pickup
                self.rider_pos_mapping[tuple(ride["start"])].append([ride["name"], "P"])
            else:
                self.rider_pos_mapping[tuple(ride["start"])] = [[ride["name"], "P"]]

            if tuple(ride["end"]) in self.rider_pos_mapping:
                # Here D stands for drop off
                self.rider_pos_mapping[tuple(ride["end"])].append([ride["name"], "D"])

            else:
                self.rider_pos_mapping[tuple(ride["end"])] = [[ride["name"], "D"]]

        for ride in requests_time_1:

            if tuple(ride["start"]) in self.rider_pos_mapping:
                # Here P stands for pickup
                self.rider_pos_mapping[tuple(ride["start"])].append([ride["name"], "P"])
            else:
                self.rider_pos_mapping[tuple(ride["start"])] = [[ride["name"], "P"]]

            if tuple(ride["end"]) in self.rider_pos_mapping:
                # Here D stands for drop off
                self.rider_pos_mapping[tuple(ride["end"])].append([ride["name"], "D"])

            else:
                self.rider_pos_mapping[tuple(ride["end"])] = [[ride["name"], "D"]]

        for ride in requests_time_2:

            if tuple(ride["start"]) in self.rider_pos_mapping:
                # Here P stands for pickup
                self.rider_pos_mapping[tuple(ride["start"])].append([ride["name"], "P"])
            else:
                self.rider_pos_mapping[tuple(ride["start"])] = [[ride["name"], "P"]]

            if tuple(ride["end"]) in self.rider_pos_mapping:
                # Here D stands for drop off
                self.rider_pos_mapping[tuple(ride["end"])].append([ride["name"], "D"])

            else:
                self.rider_pos_mapping[tuple(ride["end"])] = [[ride["name"], "D"]]
