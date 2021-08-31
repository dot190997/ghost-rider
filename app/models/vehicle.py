class Vehicle:
    def __init__(self, owner, company, registration_no, capacity=5):
        self.__owner = owner
        self.__company = company
        self.__registration_no = registration_no
        self.__capacity = capacity
        self.__seats_left = self.__capacity - 1
        self.__current_ride = None

    def get_vehicle_as_document(self):
        return {
            'owner': self.__owner,
            'company': self.__company,
            'registration_no': self.__registration_no,
            'capacity': self.__capacity,
            'seats_left': self.__seats_left,
        }

    def get_owner(self):
        return self.__owner

    def set_current_ride(self, current_ride):
        self.__current_ride = current_ride

    def get_current_ride(self):
        return self.__current_ride

    def get_company(self):
        return self.__company

    def get_vacant_seats(self):
        return self.__seats_left

    def occupy_seats(self, seats_required):
        if seats_required > self.__seats_left:
            raise ValueError("Insufficient seats")
        self.__seats_left -= seats_required

    def reset(self):
        self.__seats_left = self.__capacity - 1
        self.__current_ride = None
