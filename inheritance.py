class Mammal:
    def ocean(self):
        print("it lives in ocean")
class Fish(Mammal):
    def breadth(self):
        print("it can breath underwater")
class Shark(Mammal):              
    def eat(self):
        print("it eats other mammals for food") 
        
         
ocean1=Fish()
ocean1.ocean()
ocean1.breadth()  

ocean2=Shark()
ocean2.eat()