class Ride_Manager:

      def __init__(self) -> None:
            self.__income =0
            self.__trip_history=[]
            self.__available_cars=[] 
            self.__available_bikes=[] 
            self.__available_cngs=[] 
      
      def add_a_vehicle(self,vehicle_type,vehicle):
            if vehicle_type == "car":
                  self.__available_cars.append(vehicle)
            elif vehicle_type == "bike":
                  self.__available_bikes.append(vehicle)
            else:
                  self.__available_cngs.append(vehicle)
      
      def get_available_cars(self):
            return self.__available_cars

      def total_income(self):
            return self.__income
      def get_trip_history(self):
            return self.__trip_history
      def find_a_vehicle(self,rider,vehicle_type,destination):
            if vehicle_type =="car":
                  vehicles=self.__available_cars
            elif vehicle_type =="bike":
                  vehicles=self.__available_bikes
            else:
                  vehicles=self.__available_cngs

            if len(vehicles) == 0:
                  print(f"no {vehicle_type} available")
                  return False
            
            for vehicle in vehicles:
                  if (rider.location - vehicle.driver.location) <10:
                        distance=abs(rider.location -destination)
                        fare = vehicle.rate * distance
                        if rider.balance <fare:
                                    print("you don't have enough money for the ride")
                                    return False
                        if (vehicle.status =="available"):
                              
                              
                              vehicle.status ="unavailable"
                              vehicles.remove(vehicle)
                              
                              trip_info=f"Found {vehicle_type} match for {rider.name} for fare {fare} from {rider.location} to {destination}\n"
                              vehicle.driver.start_a_trip(rider.location, destination,fare*0.8,trip_info)
                              self.__income += fare*0.2
                              rider.start_a_trip(fare,trip_info)
                              print(trip_info)
                              self.__trip_history.append(trip_info)
                              return True
                  


uber =Ride_Manager()