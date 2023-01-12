from abc import abstractmethod, ABC
from time import sleep


class Vehicle(ABC):

    speed_of_vehicle = {
        "car": 30,
        "bike": 40,
        "CNG": 25
    }

    def __init__(self, vehicle_type, license_plate, rate, driver) -> None:
        self.vehicle_type = vehicle_type
        self.rate = rate
        self.driver = driver
        self.status = "available"
        self.license_plate = license_plate
        self.speed = self.speed_of_vehicle[vehicle_type]

    @abstractmethod
    def start_driving(self):
        pass

    @abstractmethod
    def trip_finished(self):
        pass


class Bike(Vehicle):

    def __init__(self, vehicle_type, license_plate, rate, driver) -> None:
        super().__init__(vehicle_type, license_plate, rate, driver)

    def start_driving(self, start, destination):
        self.status = "unavailable"
        distance = abs(start - destination)
        print(self.vehicle_type, self.license_plate, " started")
        for i in range(0, distance):
            sleep(1)
            print(
                f"driving {self.license_plate} current position {i} of {distance}")

        self.trip_finished()

    def trip_finished(self):
        self.status = "available"
        print(self.vehicle_type, self.license_plate, " complete trip")


class CNG(Vehicle):

    def __init__(self, vehicle_type, license_plate, rate, driver) -> None:
        super().__init__(vehicle_type, license_plate, rate, driver)

    def start_driving(self, start, destination):
        self.status = "unavailable"
        distance = abs(start - destination)
        print(self.vehicle_type, self.license_plate, " started")
        for i in range(0, distance):
            sleep(1)
            print(
                f"driving {self.license_plate} current position {i} of {distance}")

        self.trip_finished()

    def trip_finished(self):
        self.status = "available"
        print(self.vehicle_type, self.license_plate, " complete trip")


class Car(Vehicle):

    def __init__(self, vehicle_type, license_plate, rate, driver) -> None:
        super().__init__(vehicle_type, license_plate, rate, driver)

    def start_driving(self, start, destination):
        self.status = "unavailable"
        distance = abs(start - destination)
        print(self.vehicle_type, self.license_plate, " started")
        for i in range(0, distance):
            sleep(1)
            print(
                f"driving {self.license_plate} current position {i} of {distance}")

        self.trip_finished()

    def trip_finished(self):
        self.status = "available"
        print(self.vehicle_type, self.license_plate, " complete trip")
