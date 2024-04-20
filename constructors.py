class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def getx(self):
        return self.x
    def draw(self):
        print("draw ")
    def move(self):
        print("move ")
point1=point(10,30)
point1.draw() 
point1.move()
print(point1.getx())
point1.x = 50
print(point1.x)
print(point1.y)
