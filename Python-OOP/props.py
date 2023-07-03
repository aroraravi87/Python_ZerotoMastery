class Celsius:
    def __init__(self,temperature=0):
        self.set_temperature(temperature)
        
        #getter method
    def get_temperature(self):
         return self._temperature   
        
        #setter method
    def set_temperature(self,value):
        if value<-273.15:
            raise ValueError("Temp below -273.15 is not possible.")
        self._temperature=value        
     
     # get props used   
    def to_fahrenheit(self):
        return (self.get_temperature()*1.8)+32
    
    
temp=Celsius(10)
print(f"Fahrenheit temp is {temp.to_fahrenheit()}",)    

# setter temp value
temp.set_temperature(100)
print(f"Fahrenheit temp is {temp.to_fahrenheit()}",)    
