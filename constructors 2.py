class person:
    def __init__(self,name):
        self.name=name
    def greet(self):
        print("Hi")
        print("I am "+self.name)
john=person("smith ")
john.greet()            