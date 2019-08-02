'''
Definition of Trip:
class Trip:
    self.id; # trip's id, primary key
    self.driver_id, self.rider_id; # foreign key
    self.lat, self.lng; # pick up location
    def __init__(self, rider_id, lat, lng):

Definition of Helper
class Helper:
    @classmethod
    def get_distance(cls, lat1, lng1, lat2, lng2):
        # return calculate the distance between (lat1, lng1) and (lat2, lng2)
'''
from Trip import Trip, Helper


class MiniUber:

    def __init__(self):
        self.drivers = {} # id: lat, lng, trip


    # @param {int} driver_id an integer
    # @param {double} lat, lng driver's location
    # return {trip} matched trip information if there have matched rider or null
    def report(self, driver_id, lat, lng):
        if driver_id not in self.drivers:
            self.drivers[driver_id] = [lat, lng, None]
        else:
            self.drivers[driver_id][0] = lat
            self.drivers[driver_id][1] = lng

        return self.drivers[driver_id][2]


    # @param rider_id an integer
    # @param lat, lng rider's location
    # return a trip
    def request(self, rider_id, lat, lng):
        the_dvr_id = None
        min_distance = float("inf")
        for dvr_id, dvr in self.drivers.items():
            if dvr[2]:
                continue

            distance = Helper.get_distance(lat, lng, dvr[0], dvr[1])
            if distance < min_distance:
                min_distance = distance
                the_dvr_id = dvr_id

        if not the_dvr_id:
            return None

        trip = Trip(rider_id, lat, lng)
        trip.driver_id = the_dvr_id
        self.drivers[the_dvr_id][2] = trip
        return trip