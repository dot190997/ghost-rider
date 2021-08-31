from models.vehicle import Vehicle


class User:
    def __init__(self, name: str, gender: str, age: int):
        self.__name = name
        self.__gender = gender
        self.__age = age
        self.__vehicles = []
        self.__times_offered = 0
        self.__times_taken = 0

    def add_vehicle(self, vehicle: Vehicle):
        self.__vehicles.append(vehicle)

    def add_to_times_taken(self, num=1):
        self.__times_taken += num

    def add_to_times_offered(self):
        self.__times_offered += 1

    def get_user_as_document(self):
        return {
            "name": self.__name,
            "gender": self.__gender,
            "age": self.__age,
            "vehicles": [x.get_vehicle_as_document() for x in self.__vehicles],
        }

    def get_user_stats(self):
        return {
            'total_ride_seats_taken': self.__times_taken,
            'total_rides_offered': self.__times_offered
        }
