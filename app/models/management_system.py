from models.singleton import Singleton
from models.user import User
from models.vehicle import Vehicle


class ManagementSystem(metaclass=Singleton):
    def __init__(self):
        self.__vehicles = {}
        self.__users = {}
        self.__active_rides = {}
        self.__all_rides = {}
        self.__customer_to_registration_num = {}
        self.__registration_num_to_customers = {}

    def add_user(self, name, gender, age):
        if name in self.__users:
            raise ValueError("User already exists..")
        self.__users.setdefault(name, User(name, gender, age))

    def get_user(self, name):
        if name not in self.__users:
            raise ValueError("User does not exist..")
        return self.__users.get(name).get_user_as_document()

    def add_vehicle(self, owner, company, registration_num, capacity=5):
        if owner not in self.__users:
            raise ValueError("Owner does not exist")
        if registration_num in self.__vehicles:
            raise ValueError("Vehicle with same registration number exists")
        vehicle = Vehicle(owner, company, registration_num, capacity=capacity)
        self.__vehicles.setdefault(registration_num, vehicle)
        owner_obj: User = self.__users.get(owner)
        owner_obj.add_vehicle(vehicle)

    def get_vehicle(self, registration_num):
        if registration_num not in self.__vehicles:
            raise ValueError("Vehicle does not exist..")
        return self.__vehicles.get(registration_num).get_vehicle_as_document()

    def show_all_users(self):
        return list(self.__users.keys())

    def show_all_vehicles(self):
        return list(self.__vehicles.keys())

    def offer_ride(self, origin, destination, registration_number):
        if registration_number not in self.__vehicles:
            raise ValueError("Vehicle does not exist")
        if registration_number in self.__registration_num_to_customers and \
                len(self.__registration_num_to_customers[registration_number]) > 1:
            raise ValueError("Vehicle already on a ride")
        vehicle: Vehicle = self.__vehicles.get(registration_number)
        owner = vehicle.get_owner()
        user: User = self.__users.get(owner)
        user.add_to_times_taken()
        user.add_to_times_offered()
        trip_key = origin + '|' + destination
        self.__active_rides.setdefault(trip_key, set())
        vehicle.set_current_ride(trip_key)
        self.__active_rides.setdefault(trip_key, set()).add(registration_number)

    def show_rides(self, origin, destination, seats_required, preference='vacancy'):
        trip_key = origin + '|' + destination
        vehicles_list = []
        sorted_result = []
        priority_list = []
        leftovers = []
        for reg_num in self.__active_rides.get(trip_key, set()):
            vehicle: Vehicle = self.__vehicles.get(reg_num)
            if vehicle.get_vacant_seats() > seats_required:
                continue
            vehicles_list.append(vehicles_list)

        if preference == 'vacancy':
            priority_list = vehicles_list
        else:
            for vehicle in vehicles_list:
                if vehicle.get_company() == preference:
                    priority_list.append(vehicle)
                else:
                    leftovers.append(vehicle)

        sorted_result.extend(sorted(priority_list, key=lambda x: x.get_vacant_seats(),
                                    reverse=True))
        sorted_result.extend(sorted(leftovers, key=lambda x: x.get_vacant_seats(),
                                    reverse=True))
        return [x.get_vehicle_as_document() for x in sorted_result]

    def select_ride(self, name, registration_number, seats_required):
        if name not in self.__users:
            raise ValueError("Invalid user")
        user: User = self.__users.get(name)
        if registration_number not in self.__vehicles:
            raise ValueError("Invalid registration_number")
        if name in self.__customer_to_registration_num:
            raise ValueError("Ride already booked by user")
        vehicle: Vehicle = self.__vehicles.get(registration_number)
        vehicle.occupy_seats(seats_required)
        user.add_to_times_taken(seats_required)
        self.__customer_to_registration_num.setdefault(name, registration_number)
        self.__registration_num_to_customers.setdefault(registration_number, set()).add(name)
        return

    def end_ride(self, name):
        registration_number = self.__customer_to_registration_num.get(name, None)
        if registration_number not in self.__vehicles:
            raise ValueError("Invalid/expired user")
        vehicle: Vehicle = self.__vehicles.get(registration_number)
        self.__active_rides.get(vehicle.get_current_ride(), set()).discard(registration_number)
        if len(self.__active_rides.get(vehicle.get_current_ride(), set())) == 0:
            self.__active_rides.pop(vehicle.get_current_ride(), None)
        vehicle.reset()
        all_customers = self.__registration_num_to_customers.get(registration_number)
        for customer in all_customers:
            self.__customer_to_registration_num.pop(customer)
        self.__registration_num_to_customers.pop(registration_number)
        return

    def get_user_stats(self, name):
        if name not in self.__users:
            raise ValueError("Invalid user")
        return self.__users.get(name).get_user_stats()

    def get_ride_details_for_user(self, name):
        if name not in self.__customer_to_registration_num:
            raise ValueError("User has no active trips..")
        reg_num = self.__customer_to_registration_num.get(name)
        return self.get_ride_details(reg_num)

    def get_ride_details(self, registration_num):
        if registration_num not in self.__vehicles:
            raise ValueError("Invalid registration number")
        return self.show_current_snapshot(reg_num_filter=registration_num)

    def show_current_snapshot(self, origin_filter=None, destination_filter=None, reg_num_filter=None):
        snapshot = []
        for trip_key, reg_num_list in self.__active_rides.items():
            origin, destination = trip_key.split('|')
            if origin_filter and origin_filter != origin:
                continue
            if destination_filter and destination_filter != destination:
                continue
            for reg_num in reg_num_list:
                if reg_num_filter and reg_num_filter != reg_num:
                    continue
                occupants = list(self.__registration_num_to_customers.get(reg_num, {}))
                vehicle_details = self.__vehicles.get(reg_num).get_vehicle_as_document()
                snapshot.append({'origin': origin, 'destination': destination,
                                 'occupants': occupants, 'vehicle_details': vehicle_details})
        return snapshot
