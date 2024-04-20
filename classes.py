class point:
    def draw(self):
        print("draw ")
    def move(self):
        print("move ")
point1=point()
point1.draw() 
point1.move() 
point1.x=10
point1.y=20
print(point1.x)
print(point1.y)         