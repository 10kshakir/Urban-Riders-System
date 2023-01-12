import hashlib
import threading

from Brta import BRTA
from vehicles import CNG, Bike, Car
from ride_manager import uber
from random import randint

license_authority =BRTA()


class User:
      def __init__(self,name,email,password) -> None:
            self.name=name
            self.email =email
            self.password =hashlib.md5(password.encode()).hexdigest()
            already_exist=False
            with open ("user.txt","r")as file:
                  if email in file.read():
                        already_exist=True
            file.close()
            if already_exist == False:
                  with open("user.txt","a") as file:
                        file.write(f"{email} {self.password} \n")
                  file.close()
           
      
      @staticmethod
      def log_in(email,password):
            stored_pass=""
            d=""
            with open("user.txt","r") as file:
                  lines =file.readlines()
                  for line in lines:
                        if email in line:
                        
                              d,stored_pass,k=line.split(" ")
                              
                              
            file.close()
            hashed_pass=hashlib.md5(password.encode()).hexdigest()
            print(hashed_pass)
            print(stored_pass)
            if (stored_pass == hashed_pass and d==email ):
                  print("Log in succesfully")
            else:
                  print("worng password")


class Rider(User):
      def __init__(self, name, email, password,location,balance) -> None:
            super().__init__(name, email, password)
            self.__trip_history =[]
            self.location = location
            self.balance=balance
      
      def set_location(self,location):
            self.location = location

      def get_location(self):
            return self.location
      
      def request_trip(self,destination):
            pass

      def start_a_trip(self,fare,trip_info):
            self.balance -=fare
            self.__trip_history.append(trip_info)
      
      def get_trip_history(self):
            return self.__trip_history

class Driver(User):
      def __init__(self, name, email, password,location,license) -> None:
            super().__init__(name, email, password)
            self.location =location
            self.__trip_history =[]
            self.license =license
            self.valid_driver =license_authority.validate_license(email,license)
            self.earning =0
      
      def take_driving_test(self):
            result= license_authority.take_driving_test(self.email)
            if (result == False):
                  # print("you failed")
                  self.license= None
            else:
                  
                  self.license= result
                  self.valid_driver =True


      def register_a_vehicle(self,vehicle_type,license_plate,rate):
            if self.valid_driver is True:
                  
                  if vehicle_type =="car":
                        self.vehicle =Car(vehicle_type,license_plate,rate,self)
                        uber.add_a_vehicle(vehicle_type,self.vehicle)
                  elif vehicle_type =="bike":
                        self.vehicle =Bike(vehicle_type,license_plate,rate,self)
                        uber.add_a_vehicle(vehicle_type,self.vehicle)
                  else :
                        self.vehicle =CNG(vehicle_type,license_plate,rate,self)
                        uber.add_a_vehicle(vehicle_type,self.vehicle)
            else:
                  pass


      def start_a_trip(self,start,destination,fare,trip_info):
            self.earning += fare
            self.location =destination
            trip_thread =threading.Thread(target=self.vehicle.start_driving,args=(start,destination,))
            # self.vehicle.start_driving(start,destination)
            trip_thread.start()
            self.__trip_history.append(trip_info)


rider_1 =Rider("rider_1","rider_1@mail.com","rider1",randint(0,100),5000)
rider_2 =Rider("rider_2","rider_2@mail.com","rider2",randint(0,100),6000)

driver_1=Driver("driver_1","driver_1@mail.com","driver1",randint(0,30),5639)
driver_1.take_driving_test()
driver_1.register_a_vehicle("bike",1245,10)

driver_2=Driver("driver_2","driver_2@mail.com","driver2",randint(0,30),5739)
driver_2.take_driving_test()
driver_2.register_a_vehicle("bike",2245,10)

driver_3=Driver("driver_3","driver_3@mail.com","driver3",randint(0,30),5839)
driver_3.take_driving_test()
driver_3.register_a_vehicle("bike",3245,10)


driver_4=Driver("driver_4","driver_4@mail.com","driver4",randint(0,30),5939)
driver_4.take_driving_test()
driver_4.register_a_vehicle("bike",4245,10)

print(uber.get_available_cars())
uber.find_a_vehicle(rider_1,"bike",90)


