class Bird:
    
    def __init__(self,name):
        self.name=name
    
    def detail(self):
        print(f"Bird name is {self.name}")
    
    def flight(self):
        print(f"{self.name} can fly")
        

class Sparrow(Bird):
    
    def flight(self):
        print(f"{self.name} can fly")
    
class Ostrich(Bird):
    
    def flight(self):
        print(f"{self.name} can't fly")
    
class Macow(Bird):
   
    def flight(self):
        print(f"{self.name} can fly")
    

print ("#######################")
obj_spr=Sparrow('Sparrow')
obj_spr.detail()
obj_spr.flight()
print ("#######################")

obj_mac=Macow('Macow')
obj_mac.detail()
obj_mac.flight()
print ("#######################")

obj_ocr=Ostrich('Ostrich')
obj_ocr.detail()
obj_ocr.flight()
print ("#######################")
