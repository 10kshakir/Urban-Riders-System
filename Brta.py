import random

class BRTA:
      def __init__(self) -> None:
            self.__license={}
      
      def take_driving_test(self,email):
            score =random.randint(0,100)

            if (score>=33):
                  license_plate = random.randint(3000,9999)
                  self.__license[email]=license_plate
                  return license_plate
            else:
                  return False

      def validate_license(self,email,license):
            for key,val in self.__license.items():
                  
                  if(key == email and val == license ):
                        return True
            
            return False