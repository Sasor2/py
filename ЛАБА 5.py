class Person:
 
    def __init__(self, name, age):
        self.name = name  
        self.age = age    
          
 
 
class Tom(Person):

    def say_hello(self):
            print("Hello")      
    
 
people = Tom("Tom", 22)
 
people.say_hello()
print(people.name)    
print(people.age)      


people.age = 37
print(people.age)